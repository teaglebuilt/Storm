# Storm

> Command Line Interface for load testing services

Simplify load testing in a quick and orderly fashion from your fingertips in your terminal workspace. This is not ready for use.



```
 Successful requests     3000
    Slowest                 0.010s
    Fastest                 0.001s
    Average                 0.003s
    Total time              2.400s
    Requests Per Minute     90000
    Requests Per Second     125
```



```
Failed example:
    results.successful_requests()
Expected:
    2
Got nothing
**********************************************************************
6 items had failures:
   1 of   2 in stats.Results.average
   1 of   2 in stats.Results.fastest
   1 of   2 in stats.Results.request_per_min
   1 of   2 in stats.Results.request_per_sec
   2 of   2 in stats.Results.slowest
   1 of   2 in stats.Results.successful_requests
***Test Failed*** 7 failures.
```