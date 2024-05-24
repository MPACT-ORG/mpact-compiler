add_mlir_public_c_api_library(MPACTCAPI
  Registration.cpp

  ENABLE_AGGREGATION

  LINK_LIBS PUBLIC
  MLIRIR
  MLIRSupport
  MPACTTransformPasses
)

mpact_target_includes(MPACTCAPI)
