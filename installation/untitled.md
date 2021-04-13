# Linux Server

## Download software

```text
wget https://dataops-store.s3.amazonaws.com/dataops_server.zip
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

Start the server with wither sudo or user with admin privileges.

```text
 ./start_server.sh
```

### Open the browser and go to the url : http://&lt;HOST\_URL&gt;

Note : host is the server url or the ip address



Enable 

