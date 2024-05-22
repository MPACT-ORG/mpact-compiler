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

add_subdirectory(benchmark)
add_subdirectory(python)
add_subdirectory(test)
