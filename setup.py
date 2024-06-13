# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
# Also available under a BSD-style license. See LICENSE.

# Script for generating the mpact wheel.
# ```
# $ python setup.py bdist_wheel
# ```
# Environment variables you are probably interested in:
#
#   CMAKE_BUILD_TYPE:
#       specify the build type: DEBUG/RelWithDebInfo/Release
#
#   MPACT_CMAKE_ALREADY_BUILT:
#       the `MPACT_CMAKE_BUILD_DIR` directory has already been compiled,
#       and the CMake compilation process will not be executed again.
#       On CIs, it is often advantageous to re-use/control the CMake build directory.
#
# It is recommended to build with Ninja and ccache. To do so, set environment
# variables by prefixing to above invocations:
# ```
# CMAKE_GENERATOR=Ninja CMAKE_C_COMPILER_LAUNCHER=ccache CMAKE_CXX_COMPILER_LAUNCHER=ccache
# ```
#
# Implementation notes:
# The contents of the wheel is just the contents of the `python_packages`
# directory that our CMake build produces. We go through quite a bit of effort
# on the CMake side to organize that directory already, so we avoid duplicating
# that here, and just package up its contents.
import os
import pathlib
import shutil
import subprocess
import sys

from datetime import date
from distutils.command.build import build as _build
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from setuptools.command.build_py import build_py


def _check_env_flag(name: str, default=None) -> bool:
    return str(os.getenv(name, default)).upper() in ["ON", "1", "YES", "TRUE", "Y"]


PACKAGE_VERSION = "".join(str(date.today()).split("-"))
SRC_DIR = pathlib.Path(__file__).parent.absolute()
CMAKE_BUILD_TYPE = os.getenv("CMAKE_BUILD_TYPE", "Release")
MPACT_CMAKE_ALREADY_BUILT = _check_env_flag("MPACT_CMAKE_ALREADY_BUILT", False)
MPACT_CMAKE_BUILD_DIR = os.path.join(SRC_DIR, "build")


# Build phase discovery is unreliable. Just tell it what phases to run.
class CustomBuild(_build):
    def initialize_options(self):
        _build.initialize_options(self)
        # Make setuptools not steal the build directory name,
        # because the mlir c++ developers are quite
        # used to having build/ be for cmake
        self.build_base = "setup_build"

    def run(self):
        self.run_command("build_py")
        self.run_command("build_ext")
        self.run_command("build_scripts")


class CMakeBuild(build_py):
    def cmake_build(self, cmake_build_dir):
        llvm_dir = str(
            SRC_DIR / "externals" / "torch-mlir" / "externals" / "llvm-project" / "llvm"
        )
        cmake_config_args = [
            f"cmake",
            f"-GNinja",
            f"-DCMAKE_BUILD_TYPE=Release",
            f"-DPython3_FIND_VIRTUALENV=ONLY",
            f"-DLLVM_ENABLE_PROJECTS=mlir",
            f"-DLLVM_EXTERNAL_PROJECTS='torch-mlir;mpact'",
            f"-DLLVM_EXTERNAL_TORCH_MLIR_SOURCE_DIR='{SRC_DIR}/externals/torch-mlir'",
            f"-DLLVM_EXTERNAL_MPACT_SOURCE_DIR='{SRC_DIR}'",
            f"-DLLVM_TARGETS_TO_BUILD=host",
            f"-DMLIR_ENABLE_BINDINGS_PYTHON=ON",
            # Optimization options for building wheels.
            f"-DCMAKE_VISIBILITY_INLINES_HIDDEN=ON",
            f"-DCMAKE_C_VISIBILITY_PRESET=hidden",
            f"-DCMAKE_CXX_VISIBILITY_PRESET=hidden",
            f"{llvm_dir}",
        ]

        cmake_build_args = [
            f"cmake",
            f"--build",
            f".",
            f"--target",
            f"MPACTPythonModules",
            f"MPACTBenchmarkPythonModules",
        ]

        try:
            subprocess.check_call(cmake_config_args, cwd=cmake_build_dir)
            subprocess.check_call(cmake_build_args, cwd=cmake_build_dir)
        except subprocess.CalledProcessError as e:
            print("cmake build failed with\n", e)
            print("debug by follow cmake command:")
            sys.exit(e.returncode)
        finally:
            print(f"cmake config: {' '.join(cmake_config_args)}")
            print(f"cmake build: {' '.join(cmake_build_args)}")
            print(f"cmake workspace: {cmake_build_dir}")
            print(SRC_DIR)

    def run(self):
        target_dir = self.build_lib
        cmake_build_dir = MPACT_CMAKE_BUILD_DIR
        if not cmake_build_dir:
            cmake_build_dir = os.path.abspath(os.path.join(target_dir, "..", "build"))

        python_package_dir = os.path.join(
            cmake_build_dir, "tools", "mpact", "python_packages", "mpact"
        )
        if not MPACT_CMAKE_ALREADY_BUILT:
            os.makedirs(cmake_build_dir, exist_ok=True)
            cmake_cache_file = os.path.join(cmake_build_dir, "CMakeCache.txt")
            if os.path.exists(cmake_cache_file):
                os.remove(cmake_cache_file)
            # NOTE: With repeated builds for different Python versions, the
            # prior version binaries will continue to accumulate. Here we just
            # delete the directory where we build native extensions to keep
            # this from happening but still take advantage of most of the
            # build cache.
            mlir_libs_dir = os.path.join(python_package_dir, "mpact", "_mlir_libs")
            if os.path.exists(mlir_libs_dir):
                print(f"Removing _mlir_mlibs dir to force rebuild: {mlir_libs_dir}")
                shutil.rmtree(mlir_libs_dir)
            else:
                print(f"Not removing _mlir_libs dir (does not exist): {mlir_libs_dir}")
            self.cmake_build(cmake_build_dir)

        if os.path.exists(target_dir):
            shutil.rmtree(target_dir, ignore_errors=False, onerror=None)

        shutil.copytree(python_package_dir, target_dir, symlinks=False)


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class NoopBuildExtension(build_ext):
    def build_extension(self, ext):
        pass


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# Requires and extension modules depend on whether building PyTorch
# extensions.
INSTALL_REQUIRES = [
    "numpy",
    "packaging",
]
EXT_MODULES = [
    CMakeExtension("mpact._mlir_libs._mpact"),
]

setup(
    name="mpact",
    version=f"{PACKAGE_VERSION}",
    author="Reid Tatge",
    author_email="tatge@google.com",
    description="MPACT retargetable ML compiler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    cmdclass={
        "build": CustomBuild,
        "built_ext": NoopBuildExtension,
        "build_py": CMakeBuild,
    },
    ext_modules=EXT_MODULES,
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
)
