//===- SparseEncodingPropagate.cpp ---------------------------------------===//
//
// Part of the MPACT Project, under the Apache License v2.0 with LLVM
// Exceptions. See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

#include "mpact/Transforms/Sparsity/SparseEncodingPropagate.h"

namespace mlir {
#define GEN_PASS_DEF_SPARSEENCODINGPROPAGATION
#include "mpact/Transforms/Passes.h.inc"
} // namespace mlir

using namespace mlir;

// -----------------------------------------------------------------------------
// The pass
// -----------------------------------------------------------------------------

namespace {
struct SparseEncodingPropagation
    : public impl::SparseEncodingPropagationBase<SparseEncodingPropagation> {
  SparseEncodingPropagation() = default;
  SparseEncodingPropagation(const SparseEncodingPropagation &pass) = default;

  void runOnOperation() override {}
};
} // namespace

std::unique_ptr<OperationPass<func::FuncOp>>
mlir::mpact::createSparseEncodingPropagationPass() {
  return std::make_unique<SparseEncodingPropagation>();
}
