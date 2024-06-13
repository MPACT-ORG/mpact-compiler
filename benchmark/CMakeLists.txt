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

add_mlir_python_modules(MPACTBenchmarkPythonModules
  ROOT_PREFIX "${MPACT_PYTHON_PACKAGES_DIR}/mpact/mpact_benchmark"
  INSTALL_PREFIX "python_packages/mpact/mpact_benchmark"
  DECLARED_SOURCES MPACTBenchmarkPythonSources
)

add_custom_target(build-benchmark-mpact)
add_dependencies(build-benchmark-mpact MPACTPythonModules MPACTBenchmarkPythonModules)

add_custom_target(benchmark-mpact)
add_dependencies(benchmark-mpact build-benchmark-mpact)
file(GLOB PYTHON_FILES "${CMAKE_CURRENT_SOURCE_DIR}/python/benchmarks/*.py")

# Loop over each matched .py file and create a custom command to run it.
foreach(PY_FILE IN LISTS PYTHON_FILES)
    add_custom_command(
        TARGET benchmark-mpact
        COMMAND cmake -E echo "Running ${PY_FILE}"
        COMMAND python ${PY_FILE}
        DEPENDS ${PY_FILE}
        USES_TERMINAL
    )
endforeach()
