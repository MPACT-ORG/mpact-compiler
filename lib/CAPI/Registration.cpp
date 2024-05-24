//===- Registration.cpp - C Interface for MLIR Registration ---------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
// Also available under a BSD-style license. See LICENSE.
//
//===----------------------------------------------------------------------===//

#include "mpact-c/Registration.h"

#include "mlir/CAPI/IR.h"
#include "mlir/Conversion/Passes.h"
#include "mlir/Dialect/Linalg/Passes.h"
#include "mlir/Transforms/Passes.h"
#include "mpact/Transforms/Passes.h"

MLIR_CAPI_EXPORTED void mpactRegisterAllPasses() {
  mlir::mpact::registerTransformPasses();
}
