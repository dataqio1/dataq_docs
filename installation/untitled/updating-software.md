---
description: Update DataQ Software
---

# Updating Software

### Steps to update the DataQ Softare



#### 1.   Update the server to latest patch

run below command to update the server

_Command :_ `./update_software.sh <version>`

{% hint style="warning" %}
Depending on the permission granted to the current user, sudo may have to be prepended to all the commands.&#x20;

ex : sudo `./update_software.sh`
{% endhint %}

{% hint style="info" %}
Run the command from dataops\_server folder
{% endhint %}

#### 2.   Start the server

run below command to restart the server

_Command :_ `./start_server.sh`
