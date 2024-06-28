window.BENCHMARK_DATA = {
  "lastUpdate": 1719613792010,
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
          "id": "59fc5a073bebb037b2051bbe7c8a63dcf2ad82dc",
          "message": "[mpact][benchmark] add regression benchmark to gh page",
          "timestamp": "2024-06-28T20:55:50Z",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/pull/52/commits/59fc5a073bebb037b2051bbe7c8a63dcf2ad82dc"
        },
        "date": 1719612806541,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5909.837407029962,
            "unit": "iter/sec",
            "range": "stddev: 0.000008143470165037013",
            "extra": "mean: 169.2093929370145 usec\nrounds: 1784"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 34.25301200542631,
            "unit": "iter/sec",
            "range": "stddev: 0.0003366944250263363",
            "extra": "mean: 29.19451287500152 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5882.077387952132,
            "unit": "iter/sec",
            "range": "stddev: 0.00003686250866771616",
            "extra": "mean: 170.0079638612429 usec\nrounds: 2352"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5877.128788845766,
            "unit": "iter/sec",
            "range": "stddev: 0.000029053414735450336",
            "extra": "mean: 170.1511122059985 usec\nrounds: 3654"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 954326.869162598,
            "unit": "iter/sec",
            "range": "stddev: 2.122459628214424e-7",
            "extra": "mean: 1.0478590012638742 usec\nrounds: 122760"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 4.968651510614152,
            "unit": "iter/sec",
            "range": "stddev: 0.0006829851952923742",
            "extra": "mean: 201.26185099996974 msec\nrounds: 5"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12373.282557341212,
            "unit": "iter/sec",
            "range": "stddev: 0.0000045490635324041385",
            "extra": "mean: 80.81929717241351 usec\nrounds: 2830"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 21.285310885533054,
            "unit": "iter/sec",
            "range": "stddev: 0.0015616750096097195",
            "extra": "mean: 46.980756136367646 msec\nrounds: 22"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 203.30817935712298,
            "unit": "iter/sec",
            "range": "stddev: 0.0007360380529483004",
            "extra": "mean: 4.9186412625506835 msec\nrounds: 259"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 188.23867331086552,
            "unit": "iter/sec",
            "range": "stddev: 0.00010421745534155547",
            "extra": "mean: 5.312404631903438 msec\nrounds: 163"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 949008.389438308,
            "unit": "iter/sec",
            "range": "stddev: 1.9566124260579267e-7",
            "extra": "mean: 1.053731464473009 usec\nrounds: 181786"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 22.958249302316247,
            "unit": "iter/sec",
            "range": "stddev: 0.0018635426701932051",
            "extra": "mean: 43.55732821052303 msec\nrounds: 19"
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
          "id": "74f6291a82632c69528c283f0ad04fb7d5d65e63",
          "message": "[mpact][benchmark] add regression benchmark to gh page",
          "timestamp": "2024-06-28T20:55:50Z",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/pull/52/commits/74f6291a82632c69528c283f0ad04fb7d5d65e63"
        },
        "date": 1719613791056,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5930.6630942960965,
            "unit": "iter/sec",
            "range": "stddev: 0.0000069901342084117",
            "extra": "mean: 168.61520947999307 usec\nrounds: 1962"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 33.423283640985495,
            "unit": "iter/sec",
            "range": "stddev: 0.00028784114480996003",
            "extra": "mean: 29.919262593748996 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5977.873004640322,
            "unit": "iter/sec",
            "range": "stddev: 0.00003787120701808724",
            "extra": "mean: 167.28358050158485 usec\nrounds: 2031"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5940.8924212876955,
            "unit": "iter/sec",
            "range": "stddev: 0.00002705331572346874",
            "extra": "mean: 168.32487934249596 usec\nrounds: 3713"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 949863.7726585709,
            "unit": "iter/sec",
            "range": "stddev: 1.791786568219964e-7",
            "extra": "mean: 1.0527825450181165 usec\nrounds: 148302"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 5.032923153686416,
            "unit": "iter/sec",
            "range": "stddev: 0.0007107591068022317",
            "extra": "mean: 198.69168860000173 msec\nrounds: 5"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12511.47988615229,
            "unit": "iter/sec",
            "range": "stddev: 0.0000035197064279101048",
            "extra": "mean: 79.92659614205992 usec\nrounds: 3162"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 21.745137400062706,
            "unit": "iter/sec",
            "range": "stddev: 0.0007012204676885401",
            "extra": "mean: 45.987292772733475 msec\nrounds: 22"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 211.26695216957415,
            "unit": "iter/sec",
            "range": "stddev: 0.0006688596361050787",
            "extra": "mean: 4.733347973881625 msec\nrounds: 268"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 189.42893402892727,
            "unit": "iter/sec",
            "range": "stddev: 0.00008632489640648543",
            "extra": "mean: 5.279024585796868 msec\nrounds: 169"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 952227.2227348501,
            "unit": "iter/sec",
            "range": "stddev: 1.9643415939790627e-7",
            "extra": "mean: 1.0501695142971692 usec\nrounds: 198060"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 5.006633223271329,
            "unit": "iter/sec",
            "range": "stddev: 0.0015691836550795323",
            "extra": "mean: 199.73502259999805 msec\nrounds: 5"
          }
        ]
      }
    ]
  }
}