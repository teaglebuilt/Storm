# Storm

> Command Line Interface for load testing services

Simplify load testing in a quick and orderly fashion from your fingertips in your terminal workspace. This is not ready for use.

###  Coming to Pypi soon

sample command
```
storm -r 100 -c 10 https://google.com 
```
> Initial Output

```
.... Running!
Requests: 100
Concurrency: 10
JSON File: None
URL: https://google.com
```


> When complete

```
.... Done!
--- Results ---
Slowest                 1.446800993s
Fastest                 0.4680411059999998s
Average                 0.644037188s
Total Time              7.283678078s
Requests Per Min        824s
Requests Per Sec        14s
```

