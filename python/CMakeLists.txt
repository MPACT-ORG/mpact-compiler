#-------------------------------------------------------------------------------
# The MPACT Compiler Python Modules
#-------------------------------------------------------------------------------

# Disables generation of versioning (i.e. libFoo.so.<version>).
set(CMAKE_PLATFORM_NO_VERSIONED_SONAME ON)

# The directory at which the Python import tree begins.
set(MPACT_PYTHON_ROOT_DIR "${CMAKE_CURRENT_SOURCE_DIR}/mpact")

declare_mlir_python_sources(MPACTPythonSources)

declare_mlir_python_sources(MPACTPythonSources.PublicAPI
  ROOT_DIR "${MPACT_PYTHON_ROOT_DIR}"
  ADD_TO_PARENT MPACTPythonSources
  SOURCES
    mpactbackend.py
)

#-------------------------------------------------------------------------------
# Packages and shared library
#-------------------------------------------------------------------------------

set(_source_components
  MPACTPythonSources
)

add_mlir_python_modules(MPACTPythonModules
  ROOT_PREFIX "${MPACT_PYTHON_PACKAGES_DIR}/mpact/mpact"
  INSTALL_PREFIX "python_packages/mpact/mpact"
  DECLARED_SOURCES ${_source_components}
)
