---
description: Recommended for single server.
---

# Manual Install on ec2

#### Steps to create DataQ server in AWS Cloud

* Create ec2 instance of type **T3.xlarge** to support upto five concurrent jobs.(Select **T3.2xlarge** to support upto 10 concurrent jobs. )
* OPTIONAL STEP : If jobs need to be processed in EMR cluster, create the role  [#grant-permission-to-ec2-instance-to-launch-emr-clusters](manual-install-on-ec2.md#grant-permission-to-ec2-instance-to-launch-emr-clusters "mention") and attache the role to the ec2 instance.&#x20;
* EC2 Instance should be launched in private subnet.
* Follow the steps in [untitled.md](../../untitled.md "mention") for installing DataQ server.
* Create AWS Load Balancer and route http traffic to the ec2 instance created above.&#x20;
* [Create SSL Certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-server-cert.html) and expose only HTTPS traffic to the load balancer.





#### Create Role for EC2 instance to launch EMR Clusters&#x20;

* Create a role and attache the policy below.
* Create an S3 bucket so EMR cluster can write the logs. &#x20;
* Create an IAM policy from the [sample](https://dataops-store.s3.amazonaws.com/dataq\_server\_policy.json). Update the sample with the account number and bucket name from the above step.



&#x20;&#x20;



