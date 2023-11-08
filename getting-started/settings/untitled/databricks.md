# Run On

You can also add connections that run on Hadoop Cluster and Databricks.

## Static Hadoop Cluster

_Upcoming section_

## AWS EMR Cluster On Demand

A new cluster is created for each job and is terminated after completion of the job.

* Add a Hadoop Cluster connection.
* Select "_On Demand Cluster"_ check box on the top-right corner.
* Type a connection name, which you will assign to this connection for internal use.
* Provide the details as shown below

<figure><img src="../../../.gitbook/assets/image (52).png" alt=""><figcaption><p>Hadoop Configuration</p></figcaption></figure>

Configuring with On Demand Cluster enables jobs to leverage EMR cluster on demand. EMR cluster is launched on the fly and terminated on completing the job.



Description of the properties that are to be provided. Only four properties need to be updated.&#x20;



Below properties can be copied and require no change

* AWS\_SERVICE\_NAME=elasticmapreduce
* AWS\_EMR\_SERVICE\_ROLE=EMR\_DefaultRole ([Service role for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role.html))
* AWS\_EMR\_EC2\_SERVICE\_ROLE=EMR\_EC2\_DefaultRole ([Service Role for Cluster EC2 Instances](https://docs.amazonaws.cn/en\_us/emr/latest/ManagementGuide/emr-iam-role-for-ec2.html) )
* AWS\_EMR\_CLUSTER\_APPLICATION\_NAMES=Spark,Livy,Hive
* AWS\_EMR\_RELEASE\_LABEL=emr-5.31.0
* AWS\_EMR\_CLUSTER\_CREATE\_JOBNAME=EMRSparkCluster
* AWS\_EMR\_EC2\_MASTER\_INSTANCE\_TYPE=m5.2xlarge
* AWS\_EMR\_EC2\_SLAVE\_INSTANCE\_TYPE=m5.2xlarge
* EC2\_INSTANCE\_COST\_TYPE=SPOT Or ON\_DEMAND



Below five properties needs to be provided.

* AWS\_REGION=us-east-1 (Region, It is recommended to be in same subnet where DataQ server is running otherwise network connectivity needs to be established. )
* AWS\_EMR\_CLUSTER\_TAGS=Name:XYZ,Project:DataQ AWS\_NETWORK\_VPC=vpc-vpcid (Tags for auditing)
* AWS\_EMR\_S3\_LOG\_URI=s3://aws-logs-XYZ-us-east-1/elasticmapreduce/ (The S3 bucket should have the write access from the EMR Cluster. )
* AWS\_EC2\_INSTANCE\_SUBNET=subnet-XYZ (private subnet id where emr cluster will be launched.  It is recommended to be in same subnet where DataQ server is running otherwise network connectivity needs to be established.)
* AWS\_NETWORK\_VPC=vpc-XYZ (VPC id)

You can copy paste below contenet and the last five properties need to be changed. The description for the five propeerties is defined above.

```
AWS_EMR_SERVICE_ROLE=EMR_DefaultRole
AWS_EMR_EC2_SERVICE_ROLE=EMR_EC2_DefaultRole
AWS_SERVICE_NAME=elasticmapreduce
AWS_EMR_CLUSTER_APPLICATION_NAMES=Spark,Livy,Hive
AWS_EMR_RELEASE_LABEL=emr-5.31.0
AWS_EMR_CLUSTER_CREATE_JOBNAME=DataQSparkCluster
AWS_EMR_EC2_SERVICE_ROLE=EMR_EC2_DefaultRole
AWS_EMR_EC2_MASTER_INSTANCE_TYPE=m5a.2xlarge
AWS_EMR_EC2_SLAVE_INSTANCE_TYPE=m5a.2xlarge
EC2_INSTANCE_COST_TYPE=ON_DEMAND


AWS_REGION=us-east-1
AWS_EMR_CLUSTER_TAGS=<Name:customer_name,Project:DataQ>
AWS_NETWORK_VPC=<vps_id>
AWS_EC2_INSTANCE_SUBNET=<subnet-072956387c3bc1383>
AWS_EMR_S3_LOG_URI=<s3://aws-logs-865515016503-us-east-1/elasticmapreduce/>
```



{% hint style="info" %}
```
EC2_INSTANCE_COST_TYPE can be SPOT if cost is important 
however it is recommended to have it ON_DEMAND for time
critical jobs.
```
{% endhint %}

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

<figure><img src="../../../.gitbook/assets/image (37).png" alt=""><figcaption><p>Databricks Configuration</p></figcaption></figure>
