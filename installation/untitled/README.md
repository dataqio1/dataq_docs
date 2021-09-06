# Linux Installation

## Software Download and Installation

```text
The #URL will be sent to you through email, along with your license key.

Use wget to retrieve URL.

E.g. : wget https://dataops-store.s3.amazonaws.com/dataops_server.zip
```

```text
Unzip the zip file

Unzip dataops_server.zip
```

```text
cd dataops_server
```

### Set License Name and License Key

Edit the ****_**.env**_ file and update the following three properties \(using the values you received in the email\). Replace the default value of the LICENSE\_NAME with the value shown in the email.

```text
LICENSE_COMPANY_NAME=<Name>
LICENSE_NAME=<Name>
LICENSE_KEY=<key>
```

### Set Server URL

```text
# Default value is http://dq-nginx
# Set it to the server's URL if cluster (Hadoop, EMR, Databricks) is being used for jobs processing.
HOST_URL=< URL ex: dv.example.com or, if there is no URL, you can also set IP addrress>
```

{% hint style="info" %}
If https keys are provided, set the HOST\_URL to **https**://&lt;server URL&gt; 
{% endhint %}

## Starting the server

Start the server either with the _sudo_ command, or by logging in as a user with admin privileges.

```text
 ./start_server.sh
```

Open an internet browser and go to the following URL : http://&lt;HOST\_URL&gt;

**Note**: Host is the server's URL or the IP address.

{% hint style="warning" %}
Do not use localhost in the URL.
{% endhint %}

### **Login and enable LDAP settings**

Login with default credentials sent in the email. 

**Note**: For LDAP integration, go to _Settings_ --&gt; _Properties_ and fill up the LDAP server details. Restart the server by using _./restart\_server.sh_ for the changes to take effect.



![](../../.gitbook/assets/image%20%2842%29.png)

![](../../.gitbook/assets/image%20%2843%29.png)

