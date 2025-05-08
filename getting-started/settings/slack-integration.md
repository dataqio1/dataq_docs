# Slack Integration

Description:

We have a feature to send test case status as a slack notification. That means we can configure the slack webhook to send a notification in slack channel after a test case executed.

&#x20;

Pre-requisite for Slack Integration Configuration :

1. Open [Slack API](https://api.slack.com/messaging/webhooks) .
2. Click on “Create your slack app”.
3. It will navigate to “Create an app” pop up.\
   i. Select the option to create from scratch if wanted to create a new one.\
   ii. Close the pop up and get the webhook url for existing created app.

\
Create From Scratch :

1.  Provide required info like App name and select the workspace. Each Slack user has atleast one workspace assigned. So select the workspace in which you want to send notification. In our case its Dataq.io\
    \


    Open Screenshot 2025-04-22 at 9.25.26 PM-20250422-155537.png![](blob:https://app.gitbook.com/1f1fe2f9-5e45-4081-92d9-e4a812569aad)

&#x20;

Once you click Create App after providing the required info it will navigate to Slack API App page.\
Under Feature Section on left side menu look for an option called Incoming Webhook and click on it.

By default **Activate Incoming Webhooks** is off, click on the toggle button and make it on.

Once we do that we can see an option to “Add New Webhook to Workspace”. Click on that it will navigate to below page where we need to select the channel into which we will get the notification message.\
\


Open Screenshot 2025-04-22 at 9.40.53 PM-20250422-161057.png![](blob:https://app.gitbook.com/917a621a-c8c2-4ba2-8f16-71f03e3f2cd5)

\
Once you click Allow after giving the channel name, it will generate a Webhook url. Copy that webhook url and go to the Dataq → Settings → Integrations → Slack.

Paste the webhook url and click Test Connection.

Open Screenshot 2025-04-22 at 9.39.18 PM-20250422-160922.png![](blob:https://app.gitbook.com/f817d1b9-f08b-4444-951d-82e85ecd83fb)

We should get an general message to the channel which we selected while create webhook url..

Next step is while running the test case select the Slack check box on Notification option and click on Save and Run. We should see the notification in the channel in below format\
\


Open Screenshot 2025-04-22 at 9.47.44 PM-20250422-161746.png![](blob:https://app.gitbook.com/740c4bdf-c24d-4dd9-b71d-d6c48ca12424)

&#x20;

&#x20;
