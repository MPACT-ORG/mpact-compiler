/*===-- mpact-c/Registration.h - Registration functions  -----*- C -*-===*\
|*                                                                            *|
|* Part of the MPACT Project, under the Apache License v2.0 with LLVM         *|
|* Exceptions.                                                                *|
|* See https://llvm.org/LICENSE.txt for license information.                  *|
|* SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception                    *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifndef MPACT_C_REGISTRATION_H
#define MPACT_C_REGISTRATION_H

#include "mlir-c/IR.h"
#include "mlir-c/Support.h"

#ifdef __cplusplus
extern "C" {
#endif

/** Registers all passes for symbolic access with the global registry. */
MLIR_CAPI_EXPORTED void mpactRegisterAllPasses(void);

#ifdef __cplusplus
}
#endif

#endif // MPACT_C_REGISTRATION_H
