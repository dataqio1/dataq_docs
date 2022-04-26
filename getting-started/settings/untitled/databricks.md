# Run On

You can also add connections that run on Hadoop Cluster and Databricks.

## Hadoop Cluster

_Upcoming section_

## AWS EMR Cluster On Demand

* Add a \_Hadoop Cluster \_connection.
* Click on the _On Demand Cluster_ box on the top-right corner.
* Type a connection name, which you will assign to this connection for internal use.
* Provide the details as shown below

![AWS EMR Cluster Connection Configuration](../../../.gitbook/assets/aws\_hadoop.png)

Configuring with On Demand Cluster enables jobs to leverage EMR cluster on demand. EMR cluster is launched on the fly and terminated on completing the job.

* AWS\_EMR\_SERVICE\_ROLE=EMR\_DefaultRole ([Service role for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role.html))
* AWS\_EMR\_EC2\_SERVICE\_ROLE=EMR\_EC2\_DefaultRole ([Service Role for Cluster EC2 Instances](https://docs.amazonaws.cn/en\_us/emr/latest/ManagementGuide/emr-iam-role-for-ec2.html) )
* AWS\_REGION=us-east-1 (Region, It is recommended to be in same subnet where DataQ server is running otherwise network connectivity needs to be established. )
* AWS\_SERVICE\_NAME=elasticmapreduce
* AWS\_EMR\_CLUSTER\_TAGS=Name:XYZ,Project:DataQ AWS\_NETWORK\_VPC=vpc-vpcid (Tags for auditing)
* AWS\_EMR\_CLUSTER\_APPLICATION\_NAMES=Spark,Livy,Hive
* AWS\_EMR\_RELEASE\_LABEL=emr-5.31.0
* AWS\_EMR\_CLUSTER\_CREATE\_JOBNAME=EMRSparkCluster
* AWS\_EMR\_S3\_LOG\_URI=s3://aws-logs-XYZ-us-east-1/elasticmapreduce/ (The S3 bucket should have the write access from the EMR Cluster. )
* AWS\_EC2\_INSTANCE\_SUBNET=subnet-XYZ (private subnet id where emr cluster will be launched.  It is recommended to be in same subnet where DataQ server is running otherwise network connectivity needs to be established.)
* AWS\_EMR\_EC2\_MASTER\_INSTANCE\_TYPE=m5.2xlarge
* AWS\_EMR\_EC2\_SLAVE\_INSTANCE\_TYPE=m5.2xlarge
* AWS\_NETWORK\_VPC=vpc-XYZ (VPC id)

## Databricks

There are primarily two ways Databricks can be used.

* Existing Databricks cluster.
* Launch on demand cluster and terminate on completing the job.

To add a Databricks Cluster as a connection:

* Type a connection name, which you will assign to this connection for internal use.
* Provide cluster details, as shown below.

> DATABRICKS\_TOKEN=\<token>
>
> DATABRICKS\_INSTANCE=\<XXXXXXXXXXXXXX.cloud.databricks.com>

![Databricks Configuration](../../../.gitbook/assets/dbricks.png)
