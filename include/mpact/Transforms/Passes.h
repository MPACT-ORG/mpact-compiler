//===------------------------------------------------------------*- C++ -*-===//
//
// Part of the MPACT Project, under the Apache License v2.0 with LLVM
// Exceptions. See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
// Also available under a BSD-style license. See LICENSE.
//
//===----------------------------------------------------------------------===//

#ifndef MPACT_TRANSFORMS_PASSES_H
#define MPACT_TRANSFORMS_PASSES_H

namespace mlir {
namespace mpact {

/// Registers all mpact transform passes.
void registerTransformPasses();

} // namespace mpact
} // namespace mlir

#endif // MPACT_TRANSFORMS_PASSES_H
