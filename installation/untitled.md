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

{% hint style="info" %}
Since Docker-compose version V2,  docker-compose is changed to docker compose. Dollow below steps to apply symlink.
{% endhint %}

```bash
# For newer version of docker compose, we need to symlink to docker-compose 
 sudo ln -sf /usr/local/bin/docker-compose /usr/libexec/docker/cli-plugins/docker-compose

 
  # Note: If the plugins directory doesn't exist, create it first:
  sudo mkdir -p /usr/libexec/docker/cli-plugins
  sudo ln -sf /usr/local/bin/docker-compose /usr/libexec/docker/cli-plugins/docker-compose



```

### Set License Name and License Key (<mark style="color:blue;">**Optional**</mark> <mark style="color:blue;">-for paid subscription</mark>) <a href="#mickey" id="mickey"></a>



Edit the .env file and update the following three properties using the licensing information values provided to you by email after purchasing Vexdata. Be certain to update the default value of the LICENSE\_NAME with the value shown in the email.

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

1.  **Update the Software** Replace `NEW_VERSION` with the provided version (e.g., `7_35`), and run the following command:

    ```
    ./update_software.sh NEW_VERSION
    ```
2.  **Start the Server**

    ```
    ./start_server.sh
    ```



## HTTPS Setup

You will need to have https [certificate and keys](https://www.knownhost.com/wiki/security/ssl).

## Create a `.p12` (PKCS#12) File for HTTPS from a Key File

To enable **HTTPS**, you need a **`.p12` (PKCS#12) keystore** that contains your SSL certificate and private key.

***

### **1️⃣ Convert Your Key File to a `.p12` Keystore**

If you have a **private key (`.key`)** and a **certificate (`.crt` or `.pem`)**, use `openssl` to create a `.p12` file.

#### **🔹 Convert `.key` + `.crt` to `.p12`**

```sh
openssl pkcs12 -export -inkey your-key.key -in your-certificate.crt -out keystore.p12 -name myalias
```

&#x20;**Explanation**:

• -export → Creates an exportable keystore.

• -inkey your-key.key → Specifies your private key.

• -in your-certificate.crt → Your SSL certificate.

• -out keystore.p12 → Output .p12 file.

• -name myalias → Alias name for the key entry.



🔹 You’ll be prompted to enter an export password.

🔹 Remember this password—you’ll use it in app.properties.

1. Copy the keystore.p12 file created above to **my\_data/keys/**

**Set below properties in app.properties file**

1. Update the SSL\_PATH and SSL\_PWD in app.properties file with keystore path and the password created above.
2. Update HOST\_URL and EXTERNAL\_HOST\_URL with the URL associated with the certificates.
   1. Example : https://dq.mycompany.com
3. Update port to EXTERNAL\_PORT=443
4. Set TOTAL\_SYSTEM\_MEMORY= Total System Memory - 8GB





