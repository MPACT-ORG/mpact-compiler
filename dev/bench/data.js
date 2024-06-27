window.BENCHMARK_DATA = {
  "lastUpdate": 1719528536364,
  "repoUrl": "https://github.com/MPACT-ORG/mpact-compiler",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "name": "MPACT-ORG",
            "username": "MPACT-ORG"
          },
          "committer": {
            "name": "MPACT-ORG",
            "username": "MPACT-ORG"
          },
          "id": "86dff1a36cbd620f2d73af763e949ec00d777239",
          "message": "[mpact][benchmark] add regression benchmark to gh page",
          "timestamp": "2024-06-27T22:22:10Z",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/pull/52/commits/86dff1a36cbd620f2d73af763e949ec00d777239"
        },
        "date": 1719528535086,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 6669.427405418031,
            "unit": "iter/sec",
            "range": "stddev: 0.000005968668091106435",
            "extra": "mean: 149.93790909061124 usec\nrounds: 2057"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 34.302140003556715,
            "unit": "iter/sec",
            "range": "stddev: 0.0003297513733362601",
            "extra": "mean: 29.15270009090722 msec\nrounds: 33"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5915.897194757258,
            "unit": "iter/sec",
            "range": "stddev: 0.00003919411579877867",
            "extra": "mean: 169.03606791649665 usec\nrounds: 1973"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 6002.4939914783945,
            "unit": "iter/sec",
            "range": "stddev: 0.000027105251732015887",
            "extra": "mean: 166.59741790990168 usec\nrounds: 3551"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 948864.5687594158,
            "unit": "iter/sec",
            "range": "stddev: 1.8437976818208762e-7",
            "extra": "mean: 1.0538911799683288 usec\nrounds: 144238"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 32.142115430220215,
            "unit": "iter/sec",
            "range": "stddev: 0.000630869582999464",
            "extra": "mean: 31.111829032254484 msec\nrounds: 31"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12377.336292065489,
            "unit": "iter/sec",
            "range": "stddev: 0.000005090184458909657",
            "extra": "mean: 80.79282782686057 usec\nrounds: 3299"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 20.396281430385955,
            "unit": "iter/sec",
            "range": "stddev: 0.0003606405379378096",
            "extra": "mean: 49.02854490476979 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 210.87200147418721,
            "unit": "iter/sec",
            "range": "stddev: 0.0005598196294447149",
            "extra": "mean: 4.742213252632355 msec\nrounds: 285"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 189.26652258818748,
            "unit": "iter/sec",
            "range": "stddev: 0.00010650763765171751",
            "extra": "mean: 5.2835545680512865 msec\nrounds: 169"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 1093738.9035266023,
            "unit": "iter/sec",
            "range": "stddev: 8.140592632863567e-8",
            "extra": "mean: 914.2949901257589 nsec\nrounds: 177589"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 21.33905041385192,
            "unit": "iter/sec",
            "range": "stddev: 0.002583893132946909",
            "extra": "mean: 46.862441421051486 msec\nrounds: 19"
          }
        ]
      }
    ]
  }
}