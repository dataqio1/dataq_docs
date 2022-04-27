---
description: Recommended for single server.
---

# Manual Steps

#### Steps to create DataQ server in AWS Cloud

* Create ec2 instance of type **T3.xlarge** to support upto five concurrent jobs.(Select **T3.2xlarge** to support upto 10 concurrent jobs. )
* EC2 Instance should be launched in private subnet.
* Follow the steps in [untitled.md](../../untitled.md "mention") for installing DataQ server.
* Create AWS Load Balancer and route http traffic to the ec2 instance created above.&#x20;
* [Create SSL Certificate](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-server-cert.html) and expose only HTTPS traffic to the load balancer.

