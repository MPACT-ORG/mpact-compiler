//===----------------------------------------------------------------------===//
//
// Part of the MPACT Project, under the Apache License v2.0 with LLVM
// Exceptions. See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
// Also available under a BSD-style license. See LICENSE.
//
//===----------------------------------------------------------------------===//

#include "mpact/Transforms/Passes.h"
#include "mpact/Transforms/Sparsity/SparseEncodingPropagate.h"

//===----------------------------------------------------------------------===//
// Pass registration
//===----------------------------------------------------------------------===//

namespace {
#define GEN_PASS_REGISTRATION
#include "mpact/Transforms/Passes.h.inc"
} // end namespace

void mlir::mpact::registerTransformPasses() { ::registerPasses(); }
