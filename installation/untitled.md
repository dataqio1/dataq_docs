# Linux Installation

## Software Download and Installation

The URL will be sent to you through email, along with your license key. After receiving it, use the _wget _command to retrieve the URL.

```
wget https://dataops-store.s3.amazonaws.com/dataops_server.zip
```

After retrieving the file, unzip it with the _unzip_ command.

```
Unzip dataops_server.zip

cd dataops_server
```

### Set License Name and License Key (Optional)

Edit the .env file and update the following three properties using the licensing information values provided to you by email after purchaseing DataQ. Be certain to update the default value of the LICENSE\_NAME with the value shown in the email.

```
LICENSE_COMPANY_NAME=<Name>
LICENSE_NAME=<Name>
LICENSE_KEY=<key>
```

{% hint style="success" %}
Setting License Key and Name are not required for Starter\_Version
{% endhint %}

### Set Server URL (Optional)

The default value for the server is _**http**://dq-nginx_. Set it to the server's URL if cluster (Hadoop, EMR, Databricks) is being used for jobs processing.

```
HOST_URL=< URL ex: dv.example.com or, if there is no URL, you can also set IP addrress>
```

{% hint style="info" %}
If https keys are provided, set the HOST\_URL to **https**://\<server URL>&#x20;
{% endhint %}

## Starting the server

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

## HTTPS Setup

You will need to have https [certificate and keys](https://www.knownhost.com/wiki/security/ssl).

1. Rename the _.crt_ file to secure_.crt,_ and move it to _\<server\_folder>/my\_data/keys/_.
2. Rename the _.key_ file to secure_.key_ and move it to _\<server\_folder>/my\_data/keys/._

