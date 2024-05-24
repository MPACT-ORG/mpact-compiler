#-------------------------------------------------------------------------------
# The MPACT Compiler Python Modules
#-------------------------------------------------------------------------------

# Disables generation of "version soname" (i.e. libFoo.so.<version>), which
# causes pure duplication as part of Python wheels.
set(CMAKE_PLATFORM_NO_VERSIONED_SONAME ON)


# The directory at which the Python import tree begins.
set(MPACT_PYTHON_ROOT_DIR "${CMAKE_CURRENT_SOURCE_DIR}/mpact")

# We vendor our own MLIR instance in the `mpact` namespace.
add_compile_definitions("MLIR_PYTHON_PACKAGE_PREFIX=mpact.")

declare_mlir_python_sources(MPACTPythonSources)
declare_mlir_python_sources(MPACTPythonExtensions)

declare_mlir_python_sources(MPACTPythonSources.PublicAPI
  ROOT_DIR "${MPACT_PYTHON_ROOT_DIR}"
  ADD_TO_PARENT MPACTPythonSources
  SOURCES
    mpactbackend.py
  )

#-------------------------------------------------------------------------------
# Extensions
#-------------------------------------------------------------------------------

declare_mlir_python_extension(MPACTPythonExtensions.Main
  MODULE_NAME _mpact
  ADD_TO_PARENT MPACTPythonExtensions
  SOURCES
    MPACTModule.cpp
  EMBED_CAPI_LINK_LIBS
    MPACTCAPI
  PRIVATE_LINK_LIBS
    LLVMSupport
)

declare_mlir_python_sources(MPACTPythonSources.SampleModels
  ROOT_DIR "${MPACT_PYTHON_ROOT_DIR}"
  ADD_TO_PARENT MPACTPythonSources
  SOURCES
    models/resnet.py
)

#-------------------------------------------------------------------------------
# Python Modules
#-------------------------------------------------------------------------------

# To compiler TorchMLIRPythonExtension (which registers torch dialect and
# related passes).
# TODO: is there a cleaner way?
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../externals/torch-mlir/include)

set(_source_components
  MLIRPythonSources
  MLIRPythonExtension.Core
  MLIRPythonExtension.RegisterEverything

  # We need the FxImporter from torch-mlir
  TorchMLIRPythonSources.Importers
  TorchMLIRPythonExtensions

  MPACTPythonSources
  MPACTPythonExtensions
)

add_mlir_python_common_capi_library(MPACTAggregateCAPI
  INSTALL_COMPONENT MPACTPythonModules
  INSTALL_DESTINATION python_packages/mpact/mpact/_mlir_libs
  OUTPUT_DIRECTORY "${MPACT_PYTHON_PACKAGES_DIR}/mpact/mpact/_mlir_libs"
  RELATIVE_INSTALL_ROOT ".."
  DECLARED_SOURCES ${_source_components}
)

add_mlir_python_modules(MPACTPythonModules
  ROOT_PREFIX "${MPACT_PYTHON_PACKAGES_DIR}/mpact/mpact"
  INSTALL_PREFIX "python_packages/mpact/mpact"
  DECLARED_SOURCES ${_source_components}
  COMMON_CAPI_LINK_LIBS
    MPACTAggregateCAPI
)
