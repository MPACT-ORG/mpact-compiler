### Run benchmarks

To run all benchmarks:

```shell
cmake --build build --target benchmark-mpact
```

To run selected benchmarks, build the benchmark modules first:

```shell
cmake --build build --target build-benchmark-mpact
```

And then run the benchmark file:

```shell
python path/to/the/_benchmark.py
```

If you would like to run selected kernels in kernels_benchmark.py,
you can use `--benchmark-filter` flag like the following example:

```shell
python path/to/the/kernels_benchmark.py --benchmark-filter=add
```

### Profiler

Utils for profiling python scripts and pytorch models could be found in
benchmark/python/utils/profiler.py.
