# The MPACT Project

## Introduction

The MPACT project's main objective is to dramatically reduce the effort
required to create highly optimizing HPC and ML compilers for a large
class of architectures using LLVM and MLIR. We do this by providing
a declarative language-based mechanism for collecting and expressing
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

To always get updated submodules through `git pull`, set the following flag:

```shell
git config --global submodule.recurse true
```

NOTE: All following commands assume you remain in the `mpact-compiler` directory.

### Setup Python virtual environment

The following commands initialize a virtual environment under bash/sh/etc. For other shells, see Note 1, [below](README.md#notes).

```shell
python3.11 -m venv mpact_venv   # one time set up
source mpact_venv/bin/activate  # MUST BE REPEATED FOR EVERY SESSION
```

Next, set the Python paths as follows; for shells not in the bash/sh family, see Note 2, [below](README.md#notes).
```shell
export PYTHONPATH=`pwd`/build/tools/mpact/python_packages/mpact
```

### Install build requirements

Note that currently we rely on `torch-mlir` requirements defined in that
submodule to ensure all the build requirements are consistent.

```shell
python -m pip install --upgrade pip
python -m pip install -r externals/torch-mlir/requirements.txt
python -m pip install -r externals/torch-mlir/torchvision-requirements.txt
```
For shells not in the bash/sh family, see Note 3, [below](README.md#notes).

### Building the MPACT compiler in-tree

The following command generates configuration files to build the MPACT compiler
project completely *in-tree*, which means that both LLVM as well as torch-mlir
are built from source.

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

And the following to run all benchmarks
(see [Benchmarks](benchmark/README.md) for more details).

```shell
cmake --build build --target benchmark-mpact
```

## Notes

1. Shells other than bash/sh/etc. require a different `activate` script, as shown. Because the python environment has to be set up for every session, we recommend putting it in your .*sh startup file.
   - For csh/tcsh/etc.:
     ```shell
         source `pwd`/mpact_venv/bin/activate.csh
     ```
   - For fish/etc.:
     ```shell
         source <path_to_mpact_compiler>/mpact_venv/bin/activate.fish
     ```
2. Shells other than bash/sh/etc. set their environment variables differently:
   - For csh/tcsh/etc.:
   ```shell
       setenv PYTHONPATH `pwd`/build/tools/torch-mlir/python_packages/torch_mlir:`pwd`/build/tools/mpact/python_packages/mpact
   ```
3. If using csh/tcsh/etc., run the following command before trying to build the compiler:
```shell
rehash
```
