#-------------------------------------------------------------------------------
# The MPACT Compiler
#-------------------------------------------------------------------------------

cmake_minimum_required(VERSION 3.12)

project(mpact VERSION 1.0 LANGUAGES CXX C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

set(MPACT_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}")
set(MPACT_BINARY_DIR "${CMAKE_CURRENT_BINARY_DIR}")
message(STATUS "Building the MPACT compiler at ${MPACT_SOURCE_DIR} (into ${MPACT_BINARY_DIR})")

set(MPACT_PYTHON_PACKAGES_DIR "${MPACT_BINARY_DIR}/python_packages")

#-------------------------------------------------------------------------------
# Configure out-of-tree vs in-tree build
#-------------------------------------------------------------------------------

if(CMAKE_SOURCE_DIR STREQUAL CMAKE_CURRENT_SOURCE_DIR)
  message(STATUS "MPACT out-of-tree build.")
  message(FATAL_ERROR "TODO")
else()
  message(STATUS "MPACT in-tree build.")
  # In-tree build with LLVM_EXTERNAL_PROJECTS=mpact

  option(MLIR_ENABLE_BINDINGS_PYTHON "Enables MLIR Python Bindings" OFF)

  # TODO: Fix this upstream so that global include directories are not needed.
  set(MLIR_MAIN_SRC_DIR ${LLVM_MAIN_SRC_DIR}/../mlir)
  set(MLIR_INCLUDE_DIR ${LLVM_MAIN_SRC_DIR}/../mlir/include)
  set(MLIR_GENERATED_INCLUDE_DIR ${LLVM_BINARY_DIR}/tools/mlir/include)
  set(MLIR_INCLUDE_DIRS "${MLIR_INCLUDE_DIR};${MLIR_GENERATED_INCLUDE_DIR}")
endif()

include_directories(${LLVM_INCLUDE_DIRS})
include_directories(${MLIR_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
include_directories(${CMAKE_CURRENT_BINARY_DIR}/include)

add_subdirectory(include)
add_subdirectory(lib)
add_subdirectory(tools)

add_subdirectory(benchmark)
add_subdirectory(python)
add_subdirectory(test)
