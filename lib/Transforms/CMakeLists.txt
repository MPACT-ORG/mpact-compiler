add_subdirectory(Sparsity)

set(linked_libs MPACTSparsityPropagation)

add_mlir_library(MPACTTransformPasses
  Passes.cpp

  DEPENDS
  MPACTTransformsPassIncGen

  LINK_LIBS PUBLIC
  ${linked_libs}
)
