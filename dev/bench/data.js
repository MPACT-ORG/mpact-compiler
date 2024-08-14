window.BENCHMARK_DATA = {
  "lastUpdate": 1723660633491,
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
      },
      {
        "commit": {
          "author": {
            "email": "yinyingli@google.com",
            "name": "Yinying Li",
            "username": "yinying-lisa-li"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "aa8d896a77995ddf35fc50d9e06e5e121d047610",
          "message": "[mpact][benchmark] set up regression benchmark for each commit with graphs (#58)",
          "timestamp": "2024-07-02T15:28:13-04:00",
          "tree_id": "c9c7befb6fd06fbbcd1209bda7e13fcb6950ed34",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/aa8d896a77995ddf35fc50d9e06e5e121d047610"
        },
        "date": 1719948752248,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5852.580803673562,
            "unit": "iter/sec",
            "range": "stddev: 0.000008098366418064155",
            "extra": "mean: 170.86479171245574 usec\nrounds: 1834"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 34.43076839022791,
            "unit": "iter/sec",
            "range": "stddev: 0.0006086274806415394",
            "extra": "mean: 29.043789806440056 msec\nrounds: 31"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5802.733470460277,
            "unit": "iter/sec",
            "range": "stddev: 0.00004454435239320872",
            "extra": "mean: 172.33257482713216 usec\nrounds: 2018"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5671.297426386338,
            "unit": "iter/sec",
            "range": "stddev: 0.00003430388155974315",
            "extra": "mean: 176.32649547657113 usec\nrounds: 3316"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 986318.2783261854,
            "unit": "iter/sec",
            "range": "stddev: 1.8088304088312995e-7",
            "extra": "mean: 1.0138715077824907 usec\nrounds: 128140"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 31.24834710280663,
            "unit": "iter/sec",
            "range": "stddev: 0.00043359108481316527",
            "extra": "mean: 32.00169265625519 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12359.856575331278,
            "unit": "iter/sec",
            "range": "stddev: 0.000004186711076895069",
            "extra": "mean: 80.90708770811099 usec\nrounds: 3352"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 19.952093711859064,
            "unit": "iter/sec",
            "range": "stddev: 0.0009396451401827426",
            "extra": "mean: 50.12005328571723 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 214.1812644000171,
            "unit": "iter/sec",
            "range": "stddev: 0.0005696395902098518",
            "extra": "mean: 4.668942462363763 msec\nrounds: 279"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 187.5572338761418,
            "unit": "iter/sec",
            "range": "stddev: 0.00010297395640425473",
            "extra": "mean: 5.331705844309772 msec\nrounds: 167"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 976700.9973067238,
            "unit": "iter/sec",
            "range": "stddev: 1.9521875916230403e-7",
            "extra": "mean: 1.0238547956411674 usec\nrounds: 174795"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 21.71808296320426,
            "unit": "iter/sec",
            "range": "stddev: 0.00019562198685462142",
            "extra": "mean: 46.04457961111229 msec\nrounds: 18"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ajcbik@google.com",
            "name": "Aart Bik",
            "username": "aartbik"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "6dbb592d6176f77c3267b33c55ee6a611b191454",
          "message": "[mpact][compiler] add training loop to models with simple test (#60)\n\n* [mpact][compiler] add training loop to models with simple test\r\n\r\nNote that although MPACT currently does not support autograd yet,\r\neventually we need to support this too. The current PR adds a very\r\nsimple training loop to the models, together with a simple neural\r\nnetwork that uses the training loop to learn classification of\r\nsimple sparse/dense tensors in a toy training set.\r\n\r\n* linter for darker (I tested with black?!)",
          "timestamp": "2024-07-10T12:39:05-07:00",
          "tree_id": "4d9b1fd9d8433e1ff5a993d2d4c7f06bf2a23e4a",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/6dbb592d6176f77c3267b33c55ee6a611b191454"
        },
        "date": 1720640716175,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 6667.307948970807,
            "unit": "iter/sec",
            "range": "stddev: 0.000009798278337849673",
            "extra": "mean: 149.98557253596846 usec\nrounds: 1806"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 32.68306054747386,
            "unit": "iter/sec",
            "range": "stddev: 0.0002796872576339917",
            "extra": "mean: 30.596889741933673 msec\nrounds: 31"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5081.997194601598,
            "unit": "iter/sec",
            "range": "stddev: 0.00005778801050901175",
            "extra": "mean: 196.77303266956937 usec\nrounds: 1255"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5379.457621769102,
            "unit": "iter/sec",
            "range": "stddev: 0.00004383342499593898",
            "extra": "mean: 185.89234646134037 usec\nrounds: 1752"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 958591.6369178214,
            "unit": "iter/sec",
            "range": "stddev: 2.287062410905891e-7",
            "extra": "mean: 1.0431970836041504 usec\nrounds: 108969"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 31.187072550165258,
            "unit": "iter/sec",
            "range": "stddev: 0.00040573286387233435",
            "extra": "mean: 32.06456772726817 msec\nrounds: 33"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12337.291032437339,
            "unit": "iter/sec",
            "range": "stddev: 0.000004143615251923706",
            "extra": "mean: 81.05507095283635 usec\nrounds: 3002"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 19.884055989984745,
            "unit": "iter/sec",
            "range": "stddev: 0.003329928946623915",
            "extra": "mean: 50.2915502000036 msec\nrounds: 20"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 211.98538008269045,
            "unit": "iter/sec",
            "range": "stddev: 0.0005443079330878848",
            "extra": "mean: 4.717306446368725 msec\nrounds: 289"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 186.18716697079282,
            "unit": "iter/sec",
            "range": "stddev: 0.00009675966320232993",
            "extra": "mean: 5.37093944910215 msec\nrounds: 167"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 975658.2476396016,
            "unit": "iter/sec",
            "range": "stddev: 2.2318166872127397e-7",
            "extra": "mean: 1.0249490561057504 usec\nrounds: 104625"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 20.124128779092676,
            "unit": "iter/sec",
            "range": "stddev: 0.001882759082698598",
            "extra": "mean: 49.69159216665907 msec\nrounds: 18"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "yinyingli@google.com",
            "name": "Yinying Li",
            "username": "yinying-lisa-li"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "13c317b1f47932db8043fc742e4d6d785af90796",
          "message": "[mpact][profiler] Add utils for profiling Python programs and torch ops (#59)",
          "timestamp": "2024-07-10T16:27:00-04:00",
          "tree_id": "f410eefea9c1a0c21f9fccca8d9f75cc3859c921",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/13c317b1f47932db8043fc742e4d6d785af90796"
        },
        "date": 1720643491530,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5882.730909058561,
            "unit": "iter/sec",
            "range": "stddev: 0.000007809343889197068",
            "extra": "mean: 169.9890774300323 usec\nrounds: 1821"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 35.8260453730093,
            "unit": "iter/sec",
            "range": "stddev: 0.0004098903292627477",
            "extra": "mean: 27.912653757575548 msec\nrounds: 33"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5973.903357378356,
            "unit": "iter/sec",
            "range": "stddev: 0.000029854003888673223",
            "extra": "mean: 167.39474011826823 usec\nrounds: 2378"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5999.677258304794,
            "unit": "iter/sec",
            "range": "stddev: 0.00002214935446779071",
            "extra": "mean: 166.67563219601408 usec\nrounds: 3839"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 950491.2651393854,
            "unit": "iter/sec",
            "range": "stddev: 2.0270360800891412e-7",
            "extra": "mean: 1.0520875221860713 usec\nrounds: 138639"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 33.43772340642905,
            "unit": "iter/sec",
            "range": "stddev: 0.00032030927763137976",
            "extra": "mean: 29.90634224241865 msec\nrounds: 33"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12432.257811160736,
            "unit": "iter/sec",
            "range": "stddev: 0.000004436719488251673",
            "extra": "mean: 80.43591238127928 usec\nrounds: 3150"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 20.156932740504175,
            "unit": "iter/sec",
            "range": "stddev: 0.0007951352667646836",
            "extra": "mean: 49.610722666676295 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 206.25422280035204,
            "unit": "iter/sec",
            "range": "stddev: 0.0005294618156626811",
            "extra": "mean: 4.848385581748648 msec\nrounds: 263"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 186.95337637042098,
            "unit": "iter/sec",
            "range": "stddev: 0.00022424510447555433",
            "extra": "mean: 5.348927200002235 msec\nrounds: 170"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 960457.8018581292,
            "unit": "iter/sec",
            "range": "stddev: 2.443018316368644e-7",
            "extra": "mean: 1.041170156632984 usec\nrounds: 120395"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 21.143431877300007,
            "unit": "iter/sec",
            "range": "stddev: 0.0023997890490843788",
            "extra": "mean: 47.29601163156578 msec\nrounds: 19"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ajcbik@google.com",
            "name": "Aart Bik",
            "username": "aartbik"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "466aed65269e4d9d17a4f4e5b737d3184d60e679",
          "message": "[mpact][compiler] only import what you need in tests (#61)",
          "timestamp": "2024-07-10T13:42:27-07:00",
          "tree_id": "a96ce0dcd9a60503583756c90cf7c618d31f2fdf",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/466aed65269e4d9d17a4f4e5b737d3184d60e679"
        },
        "date": 1720644423077,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5892.849972887261,
            "unit": "iter/sec",
            "range": "stddev: 0.000004959268193198534",
            "extra": "mean: 169.69717617128472 usec\nrounds: 1771"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 34.68541262005039,
            "unit": "iter/sec",
            "range": "stddev: 0.00044738449261459793",
            "extra": "mean: 28.830563757570403 msec\nrounds: 33"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5806.271338374302,
            "unit": "iter/sec",
            "range": "stddev: 0.00004927253595346353",
            "extra": "mean: 172.2275694197905 usec\nrounds: 2204"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5826.095561160015,
            "unit": "iter/sec",
            "range": "stddev: 0.00003290846321017504",
            "extra": "mean: 171.6415375447246 usec\nrounds: 3609"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 966125.627784602,
            "unit": "iter/sec",
            "range": "stddev: 1.838781261933848e-7",
            "extra": "mean: 1.035062078099589 usec\nrounds: 144447"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 31.13639062389227,
            "unit": "iter/sec",
            "range": "stddev: 0.00043796326986517375",
            "extra": "mean: 32.11676048387759 msec\nrounds: 31"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12356.607210939963,
            "unit": "iter/sec",
            "range": "stddev: 0.000003996111306778252",
            "extra": "mean: 80.92836350051223 usec\nrounds: 3326"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 19.92411439930273,
            "unit": "iter/sec",
            "range": "stddev: 0.001130257434495826",
            "extra": "mean: 50.19043657142404 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 204.3538353123811,
            "unit": "iter/sec",
            "range": "stddev: 0.0006957100557737918",
            "extra": "mean: 4.893473119657243 msec\nrounds: 234"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 188.81403914912207,
            "unit": "iter/sec",
            "range": "stddev: 0.00020072138852544395",
            "extra": "mean: 5.296216343373795 msec\nrounds: 166"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 971022.1186577489,
            "unit": "iter/sec",
            "range": "stddev: 1.9237787835734797e-7",
            "extra": "mean: 1.0298426583549996 usec\nrounds: 196890"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 19.598736962010374,
            "unit": "iter/sec",
            "range": "stddev: 0.0033167102573383195",
            "extra": "mean: 51.02369616666477 msec\nrounds: 18"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "yinyingli@google.com",
            "name": "Yinying Li",
            "username": "yinying-lisa-li"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "2f8cf9d04b426ca4895c17f39dd1a1df4632af9a",
          "message": "Update README.md (#62)\n\nadd info for pip install and performance tracking.",
          "timestamp": "2024-07-10T17:11:30-04:00",
          "tree_id": "673633ab88ea05b611089784a38edb7cb96d6f04",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/2f8cf9d04b426ca4895c17f39dd1a1df4632af9a"
        },
        "date": 1720646184454,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5567.115407135617,
            "unit": "iter/sec",
            "range": "stddev: 0.000007841718427423878",
            "extra": "mean: 179.6262385217048 usec\nrounds: 1786"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 33.309292420925736,
            "unit": "iter/sec",
            "range": "stddev: 0.00028773048371934126",
            "extra": "mean: 30.021652437497437 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5617.572222361392,
            "unit": "iter/sec",
            "range": "stddev: 0.000046885770008036976",
            "extra": "mean: 178.012842633226 usec\nrounds: 1595"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5605.020685394918,
            "unit": "iter/sec",
            "range": "stddev: 0.00003302817260819787",
            "extra": "mean: 178.41147359290113 usec\nrounds: 2897"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 990990.6666835662,
            "unit": "iter/sec",
            "range": "stddev: 1.7844414339485182e-7",
            "extra": "mean: 1.0090912393217428 usec\nrounds: 131840"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 31.53526822110171,
            "unit": "iter/sec",
            "range": "stddev: 0.0015008376083111511",
            "extra": "mean: 31.710527812503386 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12410.86842730023,
            "unit": "iter/sec",
            "range": "stddev: 0.0000048379110808968955",
            "extra": "mean: 80.57453882923265 usec\nrounds: 3348"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 20.01479085419484,
            "unit": "iter/sec",
            "range": "stddev: 0.0006618735765434783",
            "extra": "mean: 49.963050190475165 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 197.71393986199735,
            "unit": "iter/sec",
            "range": "stddev: 0.0007309446772089394",
            "extra": "mean: 5.057812315600971 msec\nrounds: 282"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 183.32305573422838,
            "unit": "iter/sec",
            "range": "stddev: 0.00023267992206215093",
            "extra": "mean: 5.4548512514964 msec\nrounds: 167"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 986761.515348736,
            "unit": "iter/sec",
            "range": "stddev: 2.1567528682233168e-7",
            "extra": "mean: 1.0134160933977905 usec\nrounds: 137099"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 19.455210605295285,
            "unit": "iter/sec",
            "range": "stddev: 0.0022573877507840855",
            "extra": "mean: 51.4001117894772 msec\nrounds: 19"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ajcbik@google.com",
            "name": "Aart Bik",
            "username": "aartbik"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "7a3453a08b73ca33da9e9fa8fad7681ad3c976b0",
          "message": "[mpact][compiler] add number of model parameters utility (#63)\n\nAlso addressed recent change in softmax that now\r\nrequires an explicit dimension.",
          "timestamp": "2024-07-29T11:36:51-07:00",
          "tree_id": "366c91d2b4fadbc4ee3433c3a90a5c8d9c8db6c2",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/7a3453a08b73ca33da9e9fa8fad7681ad3c976b0"
        },
        "date": 1722284275381,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5931.531796377585,
            "unit": "iter/sec",
            "range": "stddev: 0.000005071652574157599",
            "extra": "mean: 168.59051495107974 usec\nrounds: 1841"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 33.17216628975288,
            "unit": "iter/sec",
            "range": "stddev: 0.0003879271410842336",
            "extra": "mean: 30.145755066617614 msec\nrounds: 30"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5993.630576633229,
            "unit": "iter/sec",
            "range": "stddev: 0.00005130980458592646",
            "extra": "mean: 166.84378311512899 usec\nrounds: 2001"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 6026.845263496956,
            "unit": "iter/sec",
            "range": "stddev: 0.00003853748350657001",
            "extra": "mean: 165.92428646820278 usec\nrounds: 3236"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 930182.4358174265,
            "unit": "iter/sec",
            "range": "stddev: 1.9286678694588592e-7",
            "extra": "mean: 1.0750579257296116 usec\nrounds: 151241"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 30.6254668808703,
            "unit": "iter/sec",
            "range": "stddev: 0.0004432793010911175",
            "extra": "mean: 32.652563433233205 msec\nrounds: 30"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12610.369889780228,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037063043510125626",
            "extra": "mean: 79.29981505224728 usec\nrounds: 3309"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 19.823408433315738,
            "unit": "iter/sec",
            "range": "stddev: 0.0016338304580261606",
            "extra": "mean: 50.44541171433333 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 211.21185128256394,
            "unit": "iter/sec",
            "range": "stddev: 0.0005156879693893586",
            "extra": "mean: 4.734582808339564 msec\nrounds: 313"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 188.4251600153681,
            "unit": "iter/sec",
            "range": "stddev: 0.00009347137844844848",
            "extra": "mean: 5.3071468795273375 msec\nrounds: 166"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 934284.923747403,
            "unit": "iter/sec",
            "range": "stddev: 1.6748386044850867e-7",
            "extra": "mean: 1.0703372970945682 usec\nrounds: 183790"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 21.37777709213178,
            "unit": "iter/sec",
            "range": "stddev: 0.0014637046687307853",
            "extra": "mean: 46.7775482778355 msec\nrounds: 18"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ajcbik@google.com",
            "name": "Aart Bik",
            "username": "aartbik"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "77bb923bc7cfbf89efae4ac29bf0ff19b55abc6f",
          "message": "[mpact][benchmark] add sparsity safety to tensor generator (#64)",
          "timestamp": "2024-07-30T10:47:15-07:00",
          "tree_id": "101c3e1737a0696e2cfd8f8907314c5d97efd7d5",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/77bb923bc7cfbf89efae4ac29bf0ff19b55abc6f"
        },
        "date": 1722361981743,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5795.275013415691,
            "unit": "iter/sec",
            "range": "stddev: 0.000006064806960702917",
            "extra": "mean: 172.5543650102996 usec\nrounds: 1852"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 35.863891577762125,
            "unit": "iter/sec",
            "range": "stddev: 0.0004447298007974386",
            "extra": "mean: 27.883198281250188 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 6047.643787788464,
            "unit": "iter/sec",
            "range": "stddev: 0.00003405649333583595",
            "extra": "mean: 165.3536542643636 usec\nrounds: 2392"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5744.125294869495,
            "unit": "iter/sec",
            "range": "stddev: 0.00002674640128152646",
            "extra": "mean: 174.09091004563817 usec\nrounds: 3713"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 948162.1425501032,
            "unit": "iter/sec",
            "range": "stddev: 1.8300474994805548e-7",
            "extra": "mean: 1.0546719333367156 usec\nrounds: 151012"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 32.277523192943505,
            "unit": "iter/sec",
            "range": "stddev: 0.0006679373626811565",
            "extra": "mean: 30.981311484848362 msec\nrounds: 33"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12509.23792235964,
            "unit": "iter/sec",
            "range": "stddev: 0.0000037535042530120306",
            "extra": "mean: 79.94092095830632 usec\nrounds: 3340"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 19.832590534506693,
            "unit": "iter/sec",
            "range": "stddev: 0.0038166136959731593",
            "extra": "mean: 50.4220564761876 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 201.70070695431244,
            "unit": "iter/sec",
            "range": "stddev: 0.0007768376000905954",
            "extra": "mean: 4.957840828126159 msec\nrounds: 320"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 189.87909027344634,
            "unit": "iter/sec",
            "range": "stddev: 0.000064124520738428",
            "extra": "mean: 5.266509327382453 msec\nrounds: 168"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 950653.7871268686,
            "unit": "iter/sec",
            "range": "stddev: 1.7578892974751308e-7",
            "extra": "mean: 1.0519076592775893 usec\nrounds: 198060"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 20.29335487555175,
            "unit": "iter/sec",
            "range": "stddev: 0.004256158745070551",
            "extra": "mean: 49.277214444455495 msec\nrounds: 18"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ajcbik@google.com",
            "name": "Aart Bik",
            "username": "aartbik"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "f37a36c213c593245e7da4c1c1e085986e993556",
          "message": "[mpact][benchmark] manual sum of squares benchmark (#65)\n\n* [mpact][benchmark] manual sum of squares benchmark\r\n\r\nThis introduces a \"manual\" benchmark where we can put\r\nsome benchmarking code but without negatively adding\r\nmore load on the regular benchmark suite times.\r\n\r\n* use 4K instead of 1K\r\n\r\n* lint\r\n\r\n* undo edits",
          "timestamp": "2024-07-30T15:14:56-07:00",
          "tree_id": "39168f032bdcc8a083c5f708173a6e9aec58cac4",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/f37a36c213c593245e7da4c1c1e085986e993556"
        },
        "date": 1722377987492,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5891.215859330467,
            "unit": "iter/sec",
            "range": "stddev: 0.000009263101696785644",
            "extra": "mean: 169.74424700738254 usec\nrounds: 1838"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 34.831555094827095,
            "unit": "iter/sec",
            "range": "stddev: 0.000355854570805469",
            "extra": "mean: 28.709599593746304 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5445.977050205876,
            "unit": "iter/sec",
            "range": "stddev: 0.00003580323977868441",
            "extra": "mean: 183.62178003710034 usec\nrounds: 2164"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5625.905057197205,
            "unit": "iter/sec",
            "range": "stddev: 0.000028657618654726816",
            "extra": "mean: 177.74917810258864 usec\nrounds: 3425"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 979858.7836545728,
            "unit": "iter/sec",
            "range": "stddev: 1.9583009278486146e-7",
            "extra": "mean: 1.020555223549976 usec\nrounds: 145943"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 31.717768854035093,
            "unit": "iter/sec",
            "range": "stddev: 0.00037133612139495745",
            "extra": "mean: 31.528068843744705 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12508.816594272885,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036073931774760563",
            "extra": "mean: 79.94361356755734 usec\nrounds: 3302"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 20.10344503346346,
            "unit": "iter/sec",
            "range": "stddev: 0.0005382919104048668",
            "extra": "mean: 49.74271814285744 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 212.68125149753777,
            "unit": "iter/sec",
            "range": "stddev: 0.0005056017753375226",
            "extra": "mean: 4.701871899656266 msec\nrounds: 289"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 188.3627523972336,
            "unit": "iter/sec",
            "range": "stddev: 0.00007639564544060225",
            "extra": "mean: 5.308905222892074 msec\nrounds: 166"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 968079.2484267106,
            "unit": "iter/sec",
            "range": "stddev: 2.8657478729273046e-7",
            "extra": "mean: 1.0329732835665737 usec\nrounds: 166639"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 21.591512367849305,
            "unit": "iter/sec",
            "range": "stddev: 0.0023095925263329473",
            "extra": "mean: 46.314495388893796 msec\nrounds: 18"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "ajcbik@google.com",
            "name": "Aart Bik",
            "username": "aartbik"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "eca7917e14dd523e7f048d9e53bd35a55bbf5283",
          "message": "[mpact][file-formats] add matrix market and extended frostt utils (#66)\n\n* [mpact][file-formats] add matrix market and extended frostt utils\r\n\r\n* add mm back\r\n\r\n* add benchmark util dep to test",
          "timestamp": "2024-07-30T16:32:45-07:00",
          "tree_id": "6a52876d649b94ee6fc8a87d896059570a3171c6",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/eca7917e14dd523e7f048d9e53bd35a55bbf5283"
        },
        "date": 1722382755308,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 5914.089269005995,
            "unit": "iter/sec",
            "range": "stddev: 0.000006207544946596451",
            "extra": "mean: 169.08774191838907 usec\nrounds: 1918"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 34.47596113511465,
            "unit": "iter/sec",
            "range": "stddev: 0.0003280315876168108",
            "extra": "mean: 29.005717812504273 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5671.871754573004,
            "unit": "iter/sec",
            "range": "stddev: 0.00005037490581542402",
            "extra": "mean: 176.30864082808995 usec\nrounds: 2464"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5713.32031009563,
            "unit": "iter/sec",
            "range": "stddev: 0.00008044588444592375",
            "extra": "mean: 175.02957049913098 usec\nrounds: 2766"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 943332.1798233077,
            "unit": "iter/sec",
            "range": "stddev: 2.0259622974613897e-7",
            "extra": "mean: 1.0600719676363701 usec\nrounds: 146135"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 31.176506743812425,
            "unit": "iter/sec",
            "range": "stddev: 0.0004640359792791233",
            "extra": "mean: 32.075434500001165 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12152.82118101611,
            "unit": "iter/sec",
            "range": "stddev: 0.000004941333927079426",
            "extra": "mean: 82.28542040609446 usec\nrounds: 2852"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 19.841889368834504,
            "unit": "iter/sec",
            "range": "stddev: 0.0009961412782114644",
            "extra": "mean: 50.398426349997294 msec\nrounds: 20"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 208.30234475482368,
            "unit": "iter/sec",
            "range": "stddev: 0.0006701236520992671",
            "extra": "mean: 4.800714083065275 msec\nrounds: 313"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 186.8760133680631,
            "unit": "iter/sec",
            "range": "stddev: 0.00022784912720946965",
            "extra": "mean: 5.351141550897933 msec\nrounds: 167"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 955837.5424754084,
            "unit": "iter/sec",
            "range": "stddev: 1.7599020963282733e-7",
            "extra": "mean: 1.0462028907236898 usec\nrounds: 128966"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 19.17946487939754,
            "unit": "iter/sec",
            "range": "stddev: 0.003315302338347528",
            "extra": "mean: 52.139098055555955 msec\nrounds: 18"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "yinyingli@google.com",
            "name": "Yinying Li",
            "username": "yinying-lisa-li"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "6e2dc79d62c9ddaf18754c0b31ba1330855e627e",
          "message": "Update regression-benchmark.yml (#67)\n\nNotify Reid for regression in PR comment.",
          "timestamp": "2024-08-14T09:56:54-07:00",
          "tree_id": "127b62a4602ee9b789c45299d6ed3ab208f85b61",
          "url": "https://github.com/MPACT-ORG/mpact-compiler/commit/6e2dc79d62c9ddaf18754c0b31ba1330855e627e"
        },
        "date": 1723660632659,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_dense",
            "value": 6730.209940234418,
            "unit": "iter/sec",
            "range": "stddev: 0.000007993033069341407",
            "extra": "mean: 148.5837750798557 usec\nrounds: 1894"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_dense",
            "value": 35.74876160326441,
            "unit": "iter/sec",
            "range": "stddev: 0.00038259681939269765",
            "extra": "mean: 27.972996969737956 msec\nrounds: 33"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_dense",
            "value": 5894.952119312239,
            "unit": "iter/sec",
            "range": "stddev: 0.00003545673412430758",
            "extra": "mean: 169.6366619711696 usec\nrounds: 2482"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_dense",
            "value": 5914.356700759963,
            "unit": "iter/sec",
            "range": "stddev: 0.00003549143614847271",
            "extra": "mean: 169.08009621257798 usec\nrounds: 3014"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_dense",
            "value": 977801.5550972892,
            "unit": "iter/sec",
            "range": "stddev: 1.8820227749783258e-7",
            "extra": "mean: 1.0227024029436138 usec\nrounds: 147646"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_dense",
            "value": 32.68183908452969,
            "unit": "iter/sec",
            "range": "stddev: 0.0004854319782700403",
            "extra": "mean: 30.59803328122257 msec\nrounds: 32"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mv_sparse",
            "value": 12367.043881966343,
            "unit": "iter/sec",
            "range": "stddev: 0.000019841026616584518",
            "extra": "mean: 80.86006725165767 usec\nrounds: 3242"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mm_sparse",
            "value": 20.107935645136358,
            "unit": "iter/sec",
            "range": "stddev: 0.00126426284645496",
            "extra": "mean: 49.731609333147865 msec\nrounds: 21"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_add_sparse",
            "value": 209.26130356747225,
            "unit": "iter/sec",
            "range": "stddev: 0.0009297746972612424",
            "extra": "mean: 4.778714377441356 msec\nrounds: 257"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_mul_sparse",
            "value": 188.1909622486649,
            "unit": "iter/sec",
            "range": "stddev: 0.00019604103659316013",
            "extra": "mean: 5.31375145783386 msec\nrounds: 166"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_nop_sparse",
            "value": 970370.95386269,
            "unit": "iter/sec",
            "range": "stddev: 1.859886996536609e-7",
            "extra": "mean: 1.0305337314759555 usec\nrounds: 191939"
          },
          {
            "name": "benchmark/python/benchmarks/regression_benchmark.py::test_sddmm_sparse",
            "value": 20.272902892727608,
            "unit": "iter/sec",
            "range": "stddev: 0.0038779119607092677",
            "extra": "mean: 49.326926947335444 msec\nrounds: 19"
          }
        ]
      }
    ]
  }
}