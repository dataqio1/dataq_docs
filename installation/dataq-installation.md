# Windows Installation

### Windows Requirements

Enable linux containers \([Documentation](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/linux-containers)\).

{% hint style="info" %}
Validate docker linux containers is enabled by executing the below commands
{% endhint %}

```text
docker -version
# Should output version
docker-compose -version
# Should output version
docker run --rm busybox echo hello_world
# Should print "Hello World"
```



### Installation Procedure

1. Download the _dataops\_server.zip_ file from this [URL](https://dataops-store.s3.amazonaws.com/dataops_server.zip).
2. Extract \(unzip\) the file.
3. Run the _start\_server.bat_ file.









