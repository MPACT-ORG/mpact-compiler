add_llvm_executable(mpact-opt mpact_opt.cpp)

set(dependency_libraries)
if(TORCH_MLIR_ENABLE_STABLEHLO)
  list(APPEND dependency_libraries StablehloRegister)
endif()

target_link_libraries(mpact-opt PRIVATE
  MLIROptLib
  MLIRTransforms
  TorchMLIRInitAll
  TorchMLIRTorchDialect
  TorchMLIRTorchPasses
  ${dependency_libraries}
)
