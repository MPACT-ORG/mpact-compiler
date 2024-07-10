import torch
import cProfile
from pstats import Stats


def profile_torch(func, args, row_limit=10,
                  save_output=False, func_name=None,
                  file_name="trace"):
    """Use PyTorch's profiler to profile torch ops.

    To see the graph: upload trace.json to chrome://tracing

    More details about PyTorch profiler:
    https://pytorch.org/tutorials/recipes/recipes/profiler_recipe.html
    """
    func_name = func_name if func_name else func.__name__
    with torch.profiler.profile() as prof:
        with torch.profiler.record_function(func_name):
            func(*args)
    print(prof.key_averages().table(sort_by="cpu_time_total",
                                    row_limit=row_limit))
    if save_output:
        prof.export_chrome_trace(f"{file_name}.json")


def profile_python(func, args, row_limit=10, save_output=False,
                   file_name="stats"):
    """Use cProfile to profile python function calls.

    To see the graph, run the following commands:
    1. python -m pip install snakeviz
    2. snakeviz stats.prof
    """
    pr = cProfile.Profile()
    pr.enable()
    func(*args)
    pr.disable()
    stats = Stats(pr)
    stats.sort_stats('tottime').print_stats(row_limit)
    if save_output:
        pr.dump_stats(f"{file_name}.prof")


if __name__ == "__main__":
    # Example usage of the profiler.
    from mpact.models.kernels import MMNet
    from mpact_benchmark.utils.tensor_generator import generate_tensor
    from mpact.mpactbackend import mpact_jit


    # Generate input tensors.
    dense_tensor1 = generate_tensor(seed=0, shape=(32, 32),
                                    sparsity=0.8)
    dense_tensor2 = generate_tensor(seed=1, shape=(32, 32),
                                    sparsity=0.8)
    sparse_tensor1 = dense_tensor1.to_sparse_csr()
    sparse_tensor2 = dense_tensor2.to_sparse_csr()

    # Profile with PyTorch profiler for torch operators.
    # MPACT sparse.
    profile_torch(mpact_jit, (MMNet(), sparse_tensor1, sparse_tensor2))
    # Torch sparse.
    profile_torch(MMNet(), (sparse_tensor1, sparse_tensor2),
                  func_name="sparsexsparse matmul")

    # Profile with cProfile for Python function calls.
    # MPACT sparse.
    profile_python(mpact_jit, (MMNet(), sparse_tensor1, sparse_tensor2))
    # Torch sparse.
    profile_python(MMNet(), (sparse_tensor1, sparse_tensor2))
