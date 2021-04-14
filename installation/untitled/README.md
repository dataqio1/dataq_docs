# Linux Server

## Download software

```text
# url will be sent in the email along with license key.

wget url

eg : wget https://dataops-store.s3.amazonaws.com/dataops_v2.0_server.zip
```

```text
#unzip the zip file
unzip dataops_server.zip

```

```text
cd dataops_server
```

### Set License Name and License Key

**Edit .env** file and update following two properties \(from the values you received in the email \). Replace the default value of the LICENSE\_NAME with the value received in email.

```text
LICENSE_NAME=<Name>
LICENSE_KEY=<key>
```

### Set Server URL

```text
HOST_URL=< URL ex: dv.example.com or if there is no URL can also set IP addr>
```

{% hint style="info" %}
If https keys are provided, set the HOST\_URL to **https**://&lt;server URL&gt; 
{% endhint %}

### Start the server

Start the server either with sudo or user with admin privileges.

```text
 ./start_server.sh
```

### Open the browser and go to the url : http://&lt;HOST\_URL&gt;

Note : Host is the server url or the ip address

### **Login and enable LDAP settings**

Login with default users sent in the email along with the License key. 

Note : For LDAP integration  Go to Settings --&gt; Properties and fill up the LDAP server details. Restart the server using ./restart\_server.sh for the changes to take effect.



![](../../.gitbook/assets/image%20%2842%29.png)

![](../../.gitbook/assets/image%20%2843%29.png)

