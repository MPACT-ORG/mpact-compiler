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
git submodule update --init --progress
```

All following commands assume you remain in the `mpact-compiler` directory.

### Setup Python virtual environment

The following commands initialize a virtual environment.

```shell
python3.11 -m venv mpact_venv  # one time set up
source mpact_venv/bin/activate # for each session
```

### Install build requirements

Note that currently we rely on `torch-mlir` requirements defined in the
submodule to ensure all the build requirements are consistent.

```shell
python -m pip install --upgrade pip
python -m pip install -r externals/torch-mlir/requirements.txt
python -m pip install -r externals/torch-mlir/torchvision-requirements.txt
```
