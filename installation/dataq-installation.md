# Windows Installation

###

### Windows Requirements

Enable linux containers ([Documentation](https://docs.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/linux-containers)).

{% hint style="info" %}
Validate docker linux containers is enabled by executing the below commands

Run below command to validate linux containers are enabled. Below command should ouput "Hello World"

```
docker run --rm busybox echo hello_world
```
{% endhint %}

```
docker -version
# Should output version
docker-compose -version
# Should output version
docker run --rm busybox echo hello_world
# Should print "Hello World"
```



### Installation Procedure

1. Download the _dataops\_server.zip_ file from this [URL](https://dataops-store.s3.amazonaws.com/dataops\_server.zip).
2. Extract (unzip) the file.
3. Run the _start\_server.bat_ file.



###

### Set License Name and License Key (Optional -for paid subscription) <a href="#mickey" id="mickey"></a>

Edit the .env file and update the following three properties using the licensing information values provided to you by email after purchaseing DataQ. Be certain to update the default value of the LICENSE\_NAME with the value shown in the email.

```
LICENSE_COMPANY_NAME=<Name>
LICENSE_NAME=<Name>
LICENSE_KEY=<key>
```





### Set Server URL (Optional -If running jobs on Hadoop cluster/Kubernetes)

The default value for the server is _**http**://dq-nginx_. Set it to the server's URL if cluster (Hadoop, EMR, Databricks) is being used for jobs processing.

```
HOST_URL=< URL ex: dv.example.com or, if there is no URL, you can also set IP addrress>
```

{% hint style="info" %}
If https keys are provided, set the HOST\_URL to **https**://\<server URL>&#x20;
{% endhint %}

### Increase  Memory, CPU, Swap space for better performance (Running docker first time)



on Windows 10 using Docker Desktop, To update memory and CPU for docker containers:

1. Right click on the Docker whale in the system tray and choose "Settings"
2. Go to "Advanced" on the left
3. Set  CPUs and  memory is available to containers here.
4. Refer to [link](prerequisites.md) for memory and cpu settings.

### Start the server&#x20;

To start the server : start\_server.bat

To stop the server : stop\_server.bat



{% hint style="warning" %}
Do not use localhost in the URL.
{% endhint %}

## HTTPS Setup(Optional)

You will need to have https [certificate and keys](https://www.knownhost.com/wiki/security/ssl).

1. Rename the _.crt_ file to secure_.crt,_ and move it to _\<server\_folder>/my\_data/keys/_.
2. Rename the _.key_ file to secure_.key_ and move it to _\<server\_folder>/my\_data/keys/._









