//===-- MPACTModule.cpp ------------------------------------*- cpp -*-===//
//
// Part of the MPACT Project, under the Apache License v2.0 with LLVM
// Exceptions. See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
// Also available under a BSD-style license. See LICENSE.
//
//===----------------------------------------------------------------------===//

#include "mlir/Bindings/Python/PybindAdaptors.h"
#include "mpact-c/Registration.h"

PYBIND11_MODULE(_mpact, m) {
  mpactRegisterAllPasses();

  m.doc() = "mpact main python extension";
}
