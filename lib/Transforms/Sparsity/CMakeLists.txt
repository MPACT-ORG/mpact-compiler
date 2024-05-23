add_mlir_conversion_library(MPACTSparsityPropagation
  SparseEncodingPropagate.cpp

  ADDITIONAL_HEADER_DIRS
  ${PROJECT_SOURCE_DIR}/include/mpact/Transforms/Sparsity

  DEPENDS
  MPACTTransformsPassIncGen

  LINK_LIBS PUBLIC
  MLIRIR
  MLIRPass
)

mpact_target_includes(MPACTSparsityPropagation)
