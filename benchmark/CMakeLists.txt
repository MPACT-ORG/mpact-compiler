#-------------------------------------------------------------------------------
# The MPACT Compiler Benchmarks
#-------------------------------------------------------------------------------

declare_mlir_python_sources(MPACTBenchmarkPythonSources)

declare_mlir_python_sources(MPACTBenchmarkPythonSources.BenchmarkSuite
  ROOT_DIR "${CMAKE_CURRENT_SOURCE_DIR}/python"
  ADD_TO_PARENT MPACTBenchmarkPythonSources
  SOURCES_GLOB
    benchmarks/*.py
)

declare_mlir_python_sources(MPACTBenchmarkPythonSources.BenchmarkUtils
  ROOT_DIR "${CMAKE_CURRENT_SOURCE_DIR}/python"
  ADD_TO_PARENT MPACTBenchmarkPythonSources
  SOURCES_GLOB
    utils/*.py
)

add_mlir_python_modules(MPACTBenchmarkPythonPythonModules
  ROOT_PREFIX "${MPACT_PYTHON_PACKAGES_DIR}/mpact/mpact_benchmark"
  INSTALL_PREFIX "python_packages/mpact/mpact_benchmark"
  DECLARED_SOURCES MPACTBenchmarkPythonSources
)
