# Improving the Server

DataQ collects execution metrics to improve processes and optimize the code. The following metrics are collected \(job duration, compute resources allocated, type of job, size of job\). 

```text
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
**We never collect your organization's raw data.** 
{% endhint %}



If your organization would like to opt out of this process, set the flag _STORE\_CENTRAL\_FLAG=2_ in the _**.env file.**_

