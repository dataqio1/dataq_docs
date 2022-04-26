---
description: CFN(Cloud Formation) Scripts are provided for easy installation
---

# AWS

## CFN(Cloud Formation) Scripts Download



## Prerequisites

1. Ensure jq and "aws cli" are installed
2. Permissions for aws account to create ec2 instance, load balancer.&#x20;

### Download CFN Scripts&#x20;

```
//clone the CFN scripts.
git clone https://bitbucket.org/fireman10/dq_devops.git

// cd to ec2_cfn 
cd dq_devops/ec2_cfn

```



1.  Create a new file from the template file  in ./cfn/cfn\_templates_parameters/infrastructure/\<ENV\__TEMPLATE>.account.region.ec2-infra.cfn.parameters.json.&#x20;

    Replace ENV\_TEMPLATE with the environment. ex : dev, prod

    If creating the server in dev environment, the new file name can be : **dev.account.region.ec2-infra.cfn.parameters.json** &#x20;
2.  &#x20;Below five properties are mandatory.



    * VPCId
    * PrivateSubnets
    * PublicSubnets
    * KeyPairName
    * ALBSSLPolicy
    * ACMCertificateArn
3. Update the CFN Stack Tags File as needed in ./cfn/cfn\_templates\_parameters/common/env.account.region.cfn-stack.tags.json
4. Update both the Parameter and Stack Tags files name ( env.account.region.emr-infra.cfn.parameters.json and env.account.region.cfn-stack.tags.json ) with corresponding env/account/region values you need.
5.  Update **sed** command under **replace\_template\_parameters()** function in the script(ec2\_cfn/shell\_scripts/ec2\_infra\_deploy.sh) as below,



    * If running the scripts in Mac, UPDATE all 'sed' commands in below Format: > sed -i '' "s/ParameterNameValue/${PARAMETER\_NAME}/g" $PARAMETER\_FILE
    * If running the scripts in LINUX, UPDATE all 'sed' commands in below Format: > sed -i "s/ParameterNameValue/${PARAMETER\_NAME}/g" $PARAMETER\_FILE

    \








Below five properties are mandatory.

[Follow the read me file in the git repo](https://bitbucket.org/fireman10/dq\_devops/src/master/ec2\_cfn/)

Download&#x20;
