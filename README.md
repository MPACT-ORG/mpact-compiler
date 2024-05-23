# The MPACT Project

## Introduction

The MPACT project's main objective is to dramatically reduce the effort
required to create highly optimizing HPC and ML compilers for a large class
of architectures using LLVM and MLIR.  We will do this by providing a
declarative language-based mechanism for collecting and expressing
critical aspects of a target architecture in a way that can be reasoned
about and leveraged by all passes in both MLIR and LLVM.

## Building the MPACT compiler

To build and run the MPACT compiler from source (for developers),
please follow the steps below.

### Check out code and sync submodules

Use the following commands to clone the MPACT compiler repository.

```shell
git clone https://github.com/MPACT-ORG/mpact-compiler.git
cd mpact-compiler
git submodule update --init --recursive --progress
```

All of the following commands assume you remain in the `mpact-compiler` directory.

### Setup Python virtual environment

The following commands initialize a virtual environment.

```shell
python3.11 -m venv mpact_venv  # one time set up
```

NOTE: every session you have in this repo requires one of the following
three commands (maybe add it to your .*sh file?).  (Remember to replace
"<path_to_mpact_compiler>" with your specific path.)
```shell
source <path_to_mpact_compiler>/mpact_venv/bin/activate # for bash/sh/etc.

source <path_to_mpact_compiler>/mpact_venv/bin/activate.csh # for csh/tcsh/etc.

source <path_to_mpact_compiler>/mpact_venv/bin/activate.fish # for fish/etc.
```

Also make sure to set the Python paths as follows -- note that shell
syntax depends on the shell you're running, and you need to replace
"<path_to_mpact_compiler>" with your specific path.

```shell
# FOR bash/sh/etc.
export PYTHONPATH=<path_to_mpact_compiler>/build/tools/torch-mlir/python_packages/torch_mlir: \\
        <path_to_mpact_compiler>/build/tools/mpact/python_packages/mpact

# FOR csh/tcsh/etc.
setenv PYTHONPATH <path_to_mpact_compiler>/build/tools/torch-mlir/python_packages/torch_mlir:<path_to_mpact_compiler>/build/tools/mpact/python_packages/mpact
```

### Install build requirements

Note that currently we rely on `torch-mlir` requirements defined in the
submodule to ensure all the build requirements are consistent.

```shell
python -m pip install --upgrade pip
python -m pip install -r externals/torch-mlir/requirements.txt
python -m pip install -r externals/torch-mlir/torchvision-requirements.txt
```

### Building the MPACT compiler in-tree

The following command generates configuration files to build the MPACT compiler
project completely *in-tree*, which means that both LLVM as well as torch-mlir
are built from source.

NOTE: if using csh/tcsh/etc., run the following command:

```shell
rehash
```

```shell
cmake -GNinja -Bbuild \
  -DCMAKE_BUILD_TYPE=Release \
  -DPython3_FIND_VIRTUALENV=ONLY \
  -DLLVM_ENABLE_PROJECTS=mlir \
  -DLLVM_EXTERNAL_PROJECTS="torch-mlir;mpact" \
  -DLLVM_EXTERNAL_TORCH_MLIR_SOURCE_DIR="${PWD}/externals/torch-mlir" \
  -DLLVM_EXTERNAL_MPACT_SOURCE_DIR="${PWD}" \
  -DLLVM_TARGETS_TO_BUILD=host \
  -DMLIR_ENABLE_BINDINGS_PYTHON=ON \
  externals/torch-mlir/externals/llvm-project/llvm
```

Run the following to ensure the MPACT compiler builds and runs correctly.

```shell
cmake --build build --target check-mpact
```
