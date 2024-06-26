//===------------------------------------------------------------*- C++ -*-===//
//
// Part of the MPACT Project, under the Apache License v2.0 with LLVM
// Exceptions. See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
// Also available under a BSD-style license. See LICENSE.
//
//===----------------------------------------------------------------------===//

#ifndef MPACT_TRANSFORMS_SPARSITY_SPARSEENCODINGPROPAGATE_H
#define MPACT_TRANSFORMS_SPARSITY_SPARSEENCODINGPROPAGATE_H

#include "mlir/Dialect/Func/IR/FuncOps.h"
#include "mlir/IR/BuiltinOps.h"
#include "mlir/Pass/Pass.h"

namespace mlir {
namespace mpact {
std::unique_ptr<OperationPass<func::FuncOp>>
createSparseEncodingPropagationPass();
}
} // namespace mlir

#endif // MPACT_TRANSFORMS_SPARSITY_SPARSEENCODINGPROPAGATE_H
