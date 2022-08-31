# Pre-requisite

Ensure all the pre-requisites are satisfied before proceeding with the installation.

### AWS Access and Permissions

* AWS Console access
* [Permissions to launch cloud formation stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-using-console.html)
*   Ensure you are in the correct region and have IAM permissions to create following resources &#x20;

    * EC2
    * S3
    * Loadbalancer
    * Security Groups
    * RDS Mariadb Database
    * Create entries in secrets manager (for database passwords)





### AWS Required information to create DataQ stack



* VPC Id : VPC in which DataQ server will be installed.
  * Ensure the VPC has at least two private subnets in two different availability zones.&#x20;
* Subnet Ids : Two private subnets in same VPC.&#x20;
  * Ensure the two subnets are in two different availability zones. This is required for the load balancer.&#x20;
* [ssh key pair ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
  * &#x20;This key pair will be used to login to the DataQ server.

