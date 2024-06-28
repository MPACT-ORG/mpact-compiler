window.BENCHMARK_DATA = {
  "lastUpdate": 1719612312735,
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
      },
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
          "id": "4b3c2668ba82622c4923d8c4c9c1baa69c7ddacf",
          "message": "[mpact][benchmark] add regression benchmark to gh page",
          "timestamp": "2024-06-28T20:55:50Z",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/pull/52/commits/4b3c2668ba82622c4923d8c4c9c1baa69c7ddacf"
        },
        "date": 1719612311853,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 6751.379871492692,
            "unit": "iter/sec",
            "range": "stddev: 0.000009833798979422932",
            "extra": "mean: 148.11786909257495 usec\nrounds: 1841"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 33.86474121597165,
            "unit": "iter/sec",
            "range": "stddev: 0.00026651849392417",
            "extra": "mean: 29.529237906249506 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5758.930502711753,
            "unit": "iter/sec",
            "range": "stddev: 0.000044023333220703534",
            "extra": "mean: 173.6433526206163 usec\nrounds: 1469"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5777.4834942014395,
            "unit": "iter/sec",
            "range": "stddev: 0.000028187257621068578",
            "extra": "mean: 173.0857389733174 usec\nrounds: 3582"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 953214.3513921018,
            "unit": "iter/sec",
            "range": "stddev: 1.9841163030042895e-7",
            "extra": "mean: 1.0490819809202108 usec\nrounds: 136166"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 5.013373288554875,
            "unit": "iter/sec",
            "range": "stddev: 0.0011602113209591113",
            "extra": "mean: 199.46649539999726 msec\nrounds: 5"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12428.940664347065,
            "unit": "iter/sec",
            "range": "stddev: 0.000004762825437678532",
            "extra": "mean: 80.45737983676612 usec\nrounds: 3075"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 21.516560306190904,
            "unit": "iter/sec",
            "range": "stddev: 0.0009302272687718569",
            "extra": "mean: 46.47583004762488 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 211.12310940718018,
            "unit": "iter/sec",
            "range": "stddev: 0.0009240317536763013",
            "extra": "mean: 4.73657290671748 msec\nrounds: 268"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 186.48264407731656,
            "unit": "iter/sec",
            "range": "stddev: 0.00008089085350596589",
            "extra": "mean: 5.362429329269888 msec\nrounds: 164"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 960641.0805626576,
            "unit": "iter/sec",
            "range": "stddev: 2.0111703200201038e-7",
            "extra": "mean: 1.0409715139542954 usec\nrounds: 112020"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 23.421250169062198,
            "unit": "iter/sec",
            "range": "stddev: 0.0006716290731200427",
            "extra": "mean: 42.69626910526444 msec\nrounds: 19"
          }
        ]
      }
    ]
  }
}