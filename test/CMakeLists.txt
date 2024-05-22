#-------------------------------------------------------------------------------
# The MPACT Compiler Tests
#-------------------------------------------------------------------------------

configure_lit_site_cfg(
        ${CMAKE_CURRENT_SOURCE_DIR}/lit.site.cfg.py.in
        ${CMAKE_CURRENT_BINARY_DIR}/lit.site.cfg.py
        MAIN_CONFIG
        ${CMAKE_CURRENT_SOURCE_DIR}/lit.cfg.py
)

set(MPACT_TEST_DEPENDS
        FileCheck count not
	MPACTPythonModules
        TorchMLIRPythonModules
        torch-mlir-opt
        )

add_lit_testsuite(check-mpact "Running the MPACT regression tests"
        ${CMAKE_CURRENT_BINARY_DIR}
	DEPENDS ${MPACT_TEST_DEPENDS}
        )
set_target_properties(check-mpact PROPERTIES FOLDER "Tests")

add_lit_testsuites(MPACT ${CMAKE_CURRENT_SOURCE_DIR} DEPENDS ${TORCH_MLIR_TEST_DEPENDS})
