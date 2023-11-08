# Linux Installation

## Software Download and Installation

The URL will be sent to you through email, along with your license key. After receiving it, use the _wget_ command to retrieve the URL.

```
wget https://dataops-store.s3.amazonaws.com/dataops_server.zip
```

After retrieving the file, unzip it with the _unzip_ command.

```
# unzip the folder
unzip dataops_server.zip
# change to the folder 
cd dataops_server
```

### Set License Name and License Key (<mark style="color:blue;">**Optional**</mark> <mark style="color:blue;"></mark><mark style="color:blue;">-for paid subscription</mark>) <a href="#mickey" id="mickey"></a>

Edit the .env file and update the following three properties using the licensing information values provided to you by email after purchasing DataQ. Be certain to update the default value of the LICENSE\_NAME with the value shown in the email.

```
LICENSE_COMPANY_NAME=<Name>
LICENSE_NAME=<Name>
LICENSE_KEY=<key>
```

{% hint style="success" %}
Setting License Key and Name are not required for Starter\_Version
{% endhint %}

### Set Server URL (Optional -If running jobs on Hadoop cluster/Kubernetes)

The default value for the server is _**http**://dq-nginx_. Set it to the server's URL if cluster (Hadoop, EMR, Databricks) is being used for jobs processing.

```
HOST_URL=< URL ex: dv.example.com or, if there is no URL, you can also set IP addrress>
```

{% hint style="info" %}
If https keys are provided, set the HOST\_URL to **https**://\<server URL>
{% endhint %}

## Starting the server

When running for the first time, get the latest software by running below command

```
 ./update_software.sh
```

Start the server either with the _sudo_ command, or by logging in as a user with admin privileges.

```
 ./start_server.sh
```

Open an internet browser and go to your own host's URL : http://\<HOST\_URL>

If installing on the local machine, URL will be http://127.0.0.1

**Note**: Host is the server's URL or the IP address.

{% hint style="warning" %}
Do not use localhost in the URL.
{% endhint %}

## Update the software

Follow the steps below to update the software with patches and upgrades.

1.  Update the file app.properties with the new updated version provided.&#x20;

    (To update version to 3.7 from 3.6 : ex SERVER\_VERSION=3.6 --> SERVER\_VERSION=3.7)
2. Stop the server (`./stop_server.sh`)
3. Update the software (`./update_software.sh`)
4. Start the server (`./start_server.s`h)



## HTTPS Setup

You will need to have https [certificate and keys](https://www.knownhost.com/wiki/security/ssl).

1. Rename the _.crt_ file to secure.crt and move it to _\<server\_folder>/my\_data/keys/_.
2. Rename the _.key_ file to secure.key and move it to _\<server\_folder>/my\_data/keys/._
