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
  set(MLIR_MAIN_SRC_DIR ${LLVM_MAIN_SRC_DIR}/../mlir)
  set(MLIR_INCLUDE_DIR ${LLVM_MAIN_SRC_DIR}/../mlir/include)
  set(MLIR_GENERATED_INCLUDE_DIR ${LLVM_BINARY_DIR}/tools/mlir/include)
  set(MLIR_INCLUDE_DIRS "${MLIR_INCLUDE_DIR};${MLIR_GENERATED_INCLUDE_DIR}")
endif()

include_directories(${LLVM_INCLUDE_DIRS})
include_directories(${MLIR_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
include_directories(${CMAKE_CURRENT_BINARY_DIR}/include)

# Needed to build TorchMLIRExtensions.
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/externals/torch-mlir/include)

function(mpact_target_includes target)
  set(_dirs
    $<BUILD_INTERFACE:${MLIR_INCLUDE_DIRS}>
    $<BUILD_INTERFACE:${MPACT_SOURCE_DIR}/include>
    $<BUILD_INTERFACE:${MPACT_BINARY_DIR}/include>
  )
  target_include_directories(${target} PUBLIC ${_dirs})
  if(TARGET obj.${target})
    target_include_directories(obj.${target} PRIVATE ${_dirs})
  endif()
endfunction()

list(APPEND CMAKE_MODULE_PATH ${MLIR_MAIN_SRC_DIR}/cmake/modules)
list(APPEND CMAKE_MODULE_PATH ${LLVM_MAIN_SRC_DIR}/cmake)
list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/build_tools/cmake)

include(TableGen)
include(AddLLVM)
include(AddMLIR)
include(AddMLIRPython)

include(MLIRDetectPythonEnv)
mlir_configure_python_dev_packages()

add_subdirectory(include)
add_subdirectory(lib)
add_subdirectory(tools)

add_subdirectory(benchmark)
add_subdirectory(python)
add_subdirectory(test)
