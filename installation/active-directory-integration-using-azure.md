---
description: Integrate with Active Directory for SSO
---

# Active Directory Integration Using Azure

This section includes the steps to register DataQ software in Azure via App Registration. App registration is required so that DataQ software can authenticate with Azure Active Directory to provide Azure users access to DataQ.



### Sign into Azure Portal

https://portal.azure.com/&#x20;

Go to App Registration&#x20;

● Type Azure Active Directory in the Search Bar.&#x20;

Click on Azure Active Directory.&#x20;

![](../.gitbook/assets/unknown.png)

● Click App registration on the left pane.

![](<../.gitbook/assets/unknown (1).png>)

Register DataQ App&#x20;

● Click New registration.&#x20;

![](<../.gitbook/assets/unknown (2).png>)

● Name: Type Name of the App – exp. dms-authorizer.&#x20;

Supported Account types: Select Accounts in this organizational directory only (Default Directory only - Single tenant).&#x20;

Redirect URI (Optional):&#x20;

Select a platform – Web&#x20;

Value - http://localhost:8081/login/oauth2/code/azure&#x20;

Click Register.&#x20;

![](<../.gitbook/assets/unknown (3).png>)

● Copy the Application (client) ID – This ID will be used in your application settings.

![](<../.gitbook/assets/unknown (4).png>)

Create Client Secret&#x20;

● Click Certificates & secrets in left Pane.&#x20;

![](<../.gitbook/assets/unknown (5).png>)

● Click New client secret.&#x20;

![](<../.gitbook/assets/unknown (6).png>)

● Description: Type Description of the Secret – exp. dms-authorizer. Expires: Select Set to Custom.&#x20;

Start: Select the start date.&#x20;

End: Select date in future till when secret must be valid.&#x20;

Click Add.&#x20;

![](<../.gitbook/assets/unknown (7).png>)

● Save the value in a safe place as it will not be available later.&#x20;

Click the copy picture.

![](<../.gitbook/assets/unknown (8).png>)

\
