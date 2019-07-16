the problem is this:

```bash
2019-07-16 09:16:20,584 - INFO - reading qasm file...
2019-07-16 09:16:25,140 - INFO - parsed qasm file: 13392 ops
2019-07-16 09:18:24,564 - INFO - optimized circuit: 1854 ops in 119.42398381233215 
2019-07-16 09:18:24,654 - INFO - stats: misses 74115, dupes: 6505723
```
which means that 98.87% of comparisons has been done at least twice.

Insight: the 


```bash
2019-07-16 10:00:49,046 - INFO - reading qasm file...
2019-07-16 10:00:53,691 - INFO - parsed qasm file: 13392 ops
2019-07-16 10:01:46,964 - INFO - optimized circuit: 1854 ops in 53.273059129714966 
2019-07-16 10:01:47,044 - INFO - stats: misses 843915, dupes: 31864

```

down to 3% duplication...I wonder what that is? 