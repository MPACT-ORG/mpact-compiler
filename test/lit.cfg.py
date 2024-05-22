#-------------------------------------------------------------------------------
# The MPACT Compiler LIT Configuration
#-------------------------------------------------------------------------------

import os
import platform
import re
import subprocess
import tempfile

import lit.formats
import lit.util

from lit.llvm import llvm_config
from lit.llvm.subst import ToolSubst
from lit.llvm.subst import FindTool

# The name of this test suite.
config.name = "MPACT"

# The test format.
config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)

# A list of file extensions to treat as test files.
config.suffixes = [".py"]

# A list of files to exclude from the test suite.
config.excludes = [
    "CMakeLists.txt",
    "README.txt",
    "LICENSE.txt",
    "lit.cfg.py",
    "lit.site.cfg.py",
]

# The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# The root path where tests should be run.
config.test_exec_root = os.path.join(config.mpact_obj_root, "test")
config.standalone_tools_dir = os.path.join(config.mpact_obj_root, "bin")

# Substitutions.
config.substitutions.append(("%PATH%", config.environment["PATH"]))
config.substitutions.append(("%shlibext", config.llvm_shlib_ext))

# Tweak the PATH to include the tools dir.
llvm_config.with_environment("PATH", config.llvm_tools_dir, append_path=True)
llvm_config.with_environment(
    "PATH", os.path.join(config.llvm_build_dir, "bin"), append_path=True
)
llvm_config.with_system_environment(["HOME", "INCLUDE", "LIB", "TMP", "TEMP"])

# On Windows the path to python could contain spaces in which case it needs to
# be provided in quotes. This is the equivalent of how %python is setup in
# llvm/utils/lit/lit/llvm/config.py.
if "Windows" in config.host_os:
    config.python_executable = '"%s"' % (config.python_executable)

# Tools.
tool_dirs = [
    config.standalone_tools_dir,
    config.llvm_tools_dir,
    config.mpact_obj_root,
]
tools = [
    "torch-mlir-opt",
    ToolSubst("%PYTHON", config.python_executable, unresolved="ignore"),
]

llvm_config.add_tool_substitutions(tools, tool_dirs)

llvm_config.with_environment(
    "PYTHONPATH",
    [
        os.path.join(config.mpact_src_root, "python"),
        os.path.join(config.torch_mlir_obj_root, "python_packages/torch_mlir"),
    ],
    append_path=True,
)
