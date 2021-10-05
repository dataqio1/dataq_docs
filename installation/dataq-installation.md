# Windows Installation

### Windows Requirements

Enable linux containers \([Documentation](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/linux-containers)\).

{% hint style="info" %}
Validate docker linux containers is enabled by executing the below commands

Run below command to validate linux containers are enabled. Below command should ouput "Hello World"

```text
docker run hello-world
```
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

Open an internet browser and go to your own host's URL : http://&lt;HOST\_URL&gt;

If installing on the local machine, URL will be http://127.0.0.1

**Note**: Host is the server's URL or the IP address.

{% hint style="warning" %}
Do not use localhost in the URL.
{% endhint %}

## HTTPS Setup

You will need to have https [certificate and keys](https://www.knownhost.com/wiki/security/ssl).

1. Rename the _.crt_ file to secure_.crt,_ and move it to _&lt;server\_folder&gt;/my\_data/keys/_.
2. Rename the _.key_ file to secure_.key_ and move it to _&lt;server\_folder&gt;/my\_data/keys/._











