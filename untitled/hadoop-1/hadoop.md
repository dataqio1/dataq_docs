# AWS EMR Cluster on demand

## Create on demand EMR cluster

* Click on Settings on top menu and Connections from left
* Click on "Run On" from top
* Provide the connection name
* Provide the details as shown below

![](../../.gitbook/assets/screen-shot-2021-04-21-at-9.23.17-pm.png)

Configuring on demand cluster enables jobs to leverage EMR cluster on demand. EMR cluster is launched on the fly and terminated on completing the job. 

* AWS\_EMR\_SERVICE\_ROLE=EMR\_DefaultRole  \([Service role for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role.html)\)
* AWS\_EMR\_EC2\_SERVICE\_ROLE=EMR\_EC2\_DefaultRole  \([Service Role for Cluster EC2 Instances](https://docs.amazonaws.cn/en_us/emr/latest/ManagementGuide/emr-iam-role-for-ec2.html) \)
* AWS\_REGION=us-east-1 \(Region\) 
* AWS\_SERVICE\_NAME=elasticmapreduce 
* AWS\_EMR\_CLUSTER\_TAGS=Name:XYZ,Project:DataQ AWS\_NETWORK\_VPC=vpc-vpcid 
* AWS\_EMR\_CLUSTER\_APPLICATION\_NAMES=Spark,Livy,Hive
* AWS\_EMR\_RELEASE\_LABEL=emr-5.31.0
* AWS\_EMR\_CLUSTER\_CREATE\_JOBNAME=EMRSparkCluster 
* AWS\_EMR\_S3\_LOG\_URI=s3://aws-logs-XYZ-us-east-1/elasticmapreduce/
* AWS\_EC2\_INSTANCE\_SUBNET=subnet-XYZ \(private subnet id where emr cluster is launched\)
* AWS\_EMR\_EC2\_MASTER\_INSTANCE\_TYPE=m5.2xlarge
* AWS\_EMR\_EC2\_SLAVE\_INSTANCE\_TYPE=m5.2xlarge 
* AWS\_NETWORK\_VPC=vpc-XYZ \(VPC id\)





![Hadoop Configuration](../../.gitbook/assets/hadoop2.png)

