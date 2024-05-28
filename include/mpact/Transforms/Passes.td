//===-- Passes.td - Transforms pass definition file --------*- tablegen -*-===//
//
// Part of the MPACT Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//
//
// This file contains definitions for passes within the Transforms/ directory.
//
//===----------------------------------------------------------------------===//

#ifndef MPACT_TRANSFORMS_PASSES
#define MPACT_TRANSFORMS_PASSES

include "mlir/Pass/PassBase.td"

def SparseEncodingPropagation : Pass<"sparse-encoding-propagation", "func::FuncOp"> {
  let summary = "Propagate sparse tensor encodings";
  let description = [{
    A pass that propagates sparse tensor encodings.

    Background: To avoid introducing repetitive operations, sparse tensors
    in MLIR try to reuse tensor operations whenever available. However, most
    tensor operations are canonicalized/transformed without the knowledge
    of sparsity. The pass tries to propagate missing sparse encodings.

    For example:
    ```mlir
    %s = tensor.extract_slice %input[0, 0,] [2, 1] [1, 1]
       : tensor<2x3xf32, #sparse> to tensor<2x1xf32, #sparse>

    // After rank reducing (by tensor dialect transformation)
    %t = tensor.extract_slice %input[0, 0,] [2, 1] [1, 1]
       : tensor<2x3xf32, #sparse> to tensor<2xf32>
    %s = tensor.expand_shape [[0, 1]] %t
       : tensor<2xf32> to tensor<2x1xf32, #sparse>

    // After sparsity propagation
    %t = tensor.extract_slice %input[0, 0,] [2, 1] [1, 1]
       : tensor<2x3xf32, #sparse> to tensor<2xf32, #sparse1>
    %s = tensor.expand_shape [[0, 1]] %t
       : tensor<2xf32, #sparse1> to tensor<2x1xf32, #sparse>
    ```
  }];

  let constructor = "mlir::mpact::createSparseEncodingPropagationPass()";
  let dependentDialects = [];
}

#endif // MPACT_TRANSFORMS_PASSES
