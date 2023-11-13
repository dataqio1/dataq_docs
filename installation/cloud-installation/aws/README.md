# AWS Cloud Deployment Architecture Diagram

<figure><img src="../../../.gitbook/assets/Vexdata.io%20Cloud%20Deployment%20Architecture.drawio%20(1).png" alt=""><figcaption></figcaption></figure>

* Vexdata.io is based of docker microservices.
* It is recommended to have all the incoming traffic to Vexdata.io is through the loadbalancer.
* Vexdata.io can connect to the databases in Cloud or on-prem.
* Vexdata.io requires out bound traffic to docker hub for software installation and software updates.
* Optionally Notifications(Email, Slack, Jira) can also be configured.
* By default metadata is stored on the same server. Metadata can also be configured in the cloud managed database RDS.
