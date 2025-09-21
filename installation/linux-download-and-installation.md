# Linux - Download and Installation



### Prerequisites

Before starting the installation, ensure your system meets the following requirements:

* Docker and Docker Compose installed
* Administrative privileges (sudo access)
* At least 8GB available RAM
* Internet connectivity for downloading software

### Download Software

You will receive the download URL and license key via email after purchase. Use the provided URL to download the software package.

```bash
# Download the software package
wget https://dataops-store.s3.amazonaws.com/dataops_server.zip

# Extract the downloaded file
unzip dataops_server.zip

# Navigate to the installation directory
cd dataops_server
```

### Docker Compose Compatibility Fix

Docker Compose V2 (introduced in 2021) changed the command from `docker-compose` to `docker compose`. If you're using a newer version of Docker, create a symlink for compatibility:

```bash
# Create the plugins directory if it doesn't exist
sudo mkdir -p /usr/libexec/docker/cli-plugins

# Create symlink for docker-compose compatibility
sudo ln -sf /usr/local/bin/docker-compose /usr/libexec/docker/cli-plugins/docker-compose
```

**Note:** This step is only needed if you encounter `docker-compose` command not found errors.

### Configuration

#### License Configuration (Paid Subscriptions Only)

**For Starter Version users:** Skip this section as licensing is not required.

**For paid subscriptions:** Edit the `.env` file and update the following properties with the values provided in your purchase confirmation email:

```bash
LICENSE_COMPANY_NAME=<Your Company Name>
LICENSE_NAME=<License Name from email>
LICENSE_KEY=<License Key from email>
```

#### Server URL Configuration (Optional)

**Default setup:** VexData runs locally and no changes are needed.

**For cluster deployments:** If you're running jobs on Hadoop clusters, EMR, Databricks, or Kubernetes, update the server URL:

```bash
HOST_URL=<your-server-url.com or IP address>
```

**HTTPS deployments:** If you have SSL certificates, use:

```bash
HOST_URL=https://<your-server-url.com>
```

**Important:** Do not use `localhost` in the HOST\_URL as it may cause connectivity issues.

### Installation

#### First-Time Installation

1.  **Update to latest version:**

    ```bash
    ./update_software.sh <VERSION_NUMBER>
    ```

    Replace `<VERSION_NUMBER>` with the version provided (e.g., `7_35`).
2.  **Start the server:**

    ```bash
    ./start_server.sh
    ```
3. **Access the application:** Open your web browser and navigate to:
   * **Local installation:** `http://127.0.0.1`
   * **Remote installation:** `http://<HOST_URL>`

### Software Updates

To update VexData with patches and new versions:

1.  **Download and install updates:**

    ```bash
    ./update_software.sh <NEW_VERSION>
    ```
2.  **Restart the server:**

    ```bash
    ./start_server.sh
    ```

### HTTPS Setup (Optional)

#### Prerequisites

* SSL certificate file (`.crt` or `.pem`)
* Private key file (`.key`)
* OpenSSL installed on your system

#### Create PKCS#12 Keystore

Convert your SSL certificate and private key into a `.p12` keystore file:

```bash
openssl pkcs12 -export -inkey your-private-key.key -in your-certificate.crt -out keystore.p12 -name vexdata
```

**Parameters explained:**

* `-export`: Creates an exportable keystore
* `-inkey`: Your private key file
* `-in`: Your SSL certificate file
* `-out`: Output keystore file name
* `-name`: Alias for the certificate (use any descriptive name)

You'll be prompted to create an export password. **Remember this password** - you'll need it for configuration.

#### Install Keystore

Copy the generated keystore file to the keys directory on server :

```bash
cp keystore.p12 dataops_server/my_data/keys/
```

#### Configure HTTPS Settings

Edit the `app.properties` file and update the following settings:

```properties
# SSL Configuration
SSL_PATH=my_data/keys/keystore.p12
SSL_PWD=<your_keystore_password>

# URL Configuration
HOST_URL=https://<your-domain.com>
EXTERNAL_HOST_URL=https://<your-domain.com>

# Port Configuration
EXTERNAL_PORT=443

# System Memory (Total RAM minus 8GB for VexData software)
TOTAL_SYSTEM_MEMORY=<available_memory_in_GB>
```

**Example:**

```properties
SSL_PATH=my_data/keys/keystore.p12
SSL_PWD=mySecurePassword123
HOST_URL=https://vexdata.mycompany.com
EXTERNAL_HOST_URL=https://vexdata.mycompany.com
EXTERNAL_PORT=443
TOTAL_SYSTEM_MEMORY=24
```

### Troubleshooting

#### Common Issues

**Docker Compose command not found:**

* Ensure Docker is properly installed
* Run the symlink commands in the Docker Compose Compatibility section

**Permission denied errors:**

* Ensure you have sudo privileges
* Run installation commands with appropriate permissions

**Server won't start:**

* Check if ports 80/443 are available
* Verify your `.env` and `app.properties` configurations
* Check system memory requirements

**HTTPS certificate errors:**

* Verify certificate and key files are valid
* Ensure the keystore password is correct
* Check that the domain in HOST\_URL matches your certificate

#### Support

For additional support, consult the VexData documentation or contact support with specific error messages and system information.
