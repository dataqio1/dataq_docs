---
description: >-
  Recommended when installation needs to be automated or have large number of
  DataQ servers to be deployed.
---

# Cloud Formation Scripts (command line)

## CFN(Cloud Formation) Scripts Download

## Prerequisites

1. Ensure jq and "aws cli" are installed
2. Permissions for aws account to create ec2 instance, load balancer.
3. Ensure the private subnet where Vexdata server is installed has out going traffic enabled.

### Download CFN Scripts

```
//clone the CFN scripts.
git clone https://bitbucket.org/fireman10/dq_devops.git

// cd to ec2_cfn 
cd dq_devops/ec2_cfn

```

1.  Create a new file from the template file in dq\_devops/ec2\_cfn/cfn/cfn\_templates\_parameters/infrastructure/\<ENV>.\<ACCOUNT\_>.\<REGION>.ec2-infra.cfn.parameters.json

    Replace ENV with the environment. ex : dev, prod\\

    Replace _ACCOUNT_ with the environment. ex : Vexdatadv

    Replace REGION with the environment. ex : us-east-1

    Replace ENV with the environment. ex : dev, prod

If creating the server in dev environment, the new file name can be : **dev.account.region.ec2-infra.cfn.parameters.json**

1. Below five properties are mandatory.
   * VPCId
   * PrivateSubnets
   * PublicSubnets
   * KeyPairName
   * ALBSSLPolicy
   * ACMCertificateArn\
     Note: PublicSubnets are coma separated values used by load balancer.
2. Update the CFN Stack Tags File as needed in ./cfn/cfn\_templates\_parameters/common/env.account.region.cfn-stack.tags.json
3. Update both the Parameter and Stack Tags files name ( env.account.region.emr-infra.cfn.parameters.json and env.account.region.cfn-stack.tags.json ) with corresponding env/account/region values you need.\
   File should be like this\
   dq\_devops/ec2\_cfn/cfn/cfn\_templates\_parameters/infrastructure/\<ENV>.\<ACCOUNT\_>.\<REGION>.region.cfn-stack.tags.json
4.  Update **sed** command under **replace\_template\_parameters()** function in the script(ec2\_cfn/shell\_scripts/ec2\_infra\_deploy.sh) as below,

    *   If running the scripts in Mac, UPDATE all 'sed' commands in below Format: >

        sed -i '' "s/ParameterNameValue/${PARAMETER\_NAME}/g" $PARAMETER\_FILE
    *   If running the scripts in LINUX, UPDATE all 'sed' commands in below Format: >

        sed -i "s/ParameterNameValue/${PARAMETER\_NAME}/g" $PARAMETER\_FILE

    \\
5.  Execute Infrastructure Shell Script:

    Below example will create infra for **dev** environment and account **Vexdata** with **internet-facing (public)** Application Load Balancer and **http** protocol.

```
// Execute below command to launch.
./ec2_infra_deploy.sh --stack-tag <STACK_NAME> --subsystem app --env <ENV_TEMPLATE> --account Vexdata --region us-east-1 --ec2-ami-id 'ami-0947d2ba12ee1ff75' --alb-scheme 'internet-facing' --alb-protocol 'http' --create-r53 'false' --r53-hosted-zone-id '' --r53-record-set-name ''

// example command 
./ec2_infra_deploy.sh --stack-tag Vexdata --subsystem app --env dev --account Vexdata --region us-east-1 --ec2-ami-id 'ami-0947d2ba12ee1ff75' --alb-scheme 'internet-facing' --alb-protocol 'http' --create-r53 'false' --r53-hosted-zone-id '' --r53-record-set-name ''
```

### Proceed with the following steps after successful installation

1. Login to the aws web console under cloud formation to confirm the stack is created successful.
2. Click on the stack name-> Outputs -> corresponding to the key "LoadBalancerDnsName", there will be a load balancer url. Click on the URL to login to Vexdata application.
3. if the jobs need to be executed on EMR cluster, ssh into the ec2 instance where Vexdata is running, and [URL needs to be set](../../untitled.md#set-server-url-optional-if-running-jobs-on-hadoop-cluster-kubernetes) in app.properties file.
