---
description: Update DataQ Software
---

# Updating Software

### Steps to update the DataQ Softare



#### 1.   Delete the file **current\_version.txt** __&#x20;

from the location dataops\_server/my\_data/current\_version.txt

Command : `rm my_data/current_version.txt`&#x20;

{% hint style="info" %}
mydata exists inside dataops\_server folder.
{% endhint %}

#### 2.   Restart the server

run below command to restart the server

_Command :_ `./restart.sh`

{% hint style="info" %}
Run the command from dataops\_server folder
{% endhint %}
