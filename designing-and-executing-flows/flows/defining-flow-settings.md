# Defining Test Case Settings

* Test Case settings can be defined in a per-test case basis.
* The following are the test case settings, which can be set individually or when a batch of test cases is to be executed. Users can access these settings by clicking on the Step 3 Configuration) of the test case.
  * **"Select Cluster to Execute the job"** is a setting used to specify where this test case will be executed.
    * A list of server cluster managers is provided in the dropdown menu, and it can be set to an AWS environment, Databricks, or on the local server.
    * The number of threads and memory to be allocated to this execution can also be set here.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Data Comparison Methods** can also be defined for the data compare test cases where user can defined the comparison will be hash compare / Outer Join Compare / In Memory compare. Choosing the Optimal Data Comparison Algorithm

&#x20;             The most suitable comparison algorithm should be selected based on the specifics of the input              datasets and the configuration. Adjust this setting only if you possess a comprehensive understanding of the following algorithms:

1. Hash Compare: This method is ideal under the following conditions: There is a single, numeric primary key in both source and target tables. Both the source and target datasets are situated in databases or data warehouse systems.

Note: Hash Compare is not suitable for input datasets that are files (e.g., CSV, JSON) or APIs.

2. Outer Join Compare: Choose this method when the source and target databases reside on the same physical server, such as Oracle, MySQL, and others.
3. In Memory Compare: This technique is the most versatile, but it is also the most time-consuming.

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Notification** is a setting that can be used to receive an email notification when the test case is completed with the result of the test case. This tab allows users to set the email destination for the notification. Note that more than one email can be set. We have 2 methods to get notifications
  * Email- Email to multiple people can be sent on test case executions
  * Slack - Notification on slack channel can be sent reagarding test case executions.

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

***
