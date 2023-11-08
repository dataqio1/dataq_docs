# Server Improvement

Vexdata collects execution metrics to improve processes and optimize the code. The following metrics are collected (job duration, compute resources allocated, type of job, size of job). 

```
startTime
endTime
executorCores
executorMemory
numExecutors
status
flowName
execId
root
jobType
LICENSE_NAME
IPAddress
```

{% hint style="info" %}
**We never collect your organization's raw data. **
{% endhint %}

If your organization would like to opt out of this process, open the _.env_ file and set the flag _STORE_CENTRAL_FLAG=2_.
