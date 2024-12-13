---
description: Steps to executing a Test case
---

# Executing Test Cases

### Different ways of executing a test case

This documentation outlines the three methods available for executing test cases within the system. Each method caters to different scenarios and user needs.

#### 1. Executing a New Test Case

To run a new test case immediately upon creation:

* Navigate to the configuration step of creating a new Test Case.
* Enter the name of the Test Case and click the **Save** button.
* After saving, click the **Save & Run** button to execute the Test Case.
* The execution results will be automatically added to the **Test Runs** tab.

{% hint style="info" %}
Click on Save and the test case is saved and is visible in the "Test Case" page.
{% endhint %}

<figure><img src="../../.gitbook/assets/Screenshot 2024-05-10 at 9.29.23 AM.png" alt=""><figcaption></figcaption></figure>

#### 2. Batch Execution of Test Cases

For executing multiple test cases in a batch:

* Go to the **Test Case** tab.
* Select the desired Test Cases.
* Click on the **Execute Batch** button to open a popup window.
* In the popup window:
  * **Batch Name**: Provide a mandatory name for the batch.
  * **Change Execution Order**: Drag and rearrange the test cases as needed. The test case at the top of the list will execute first.
  * **Scheduling**:
    * By default, the batch is set to execute immediately under the option **One-time (now)**.
    * Optionally, set the batch to execute periodically by selecting **Periodically** and entering the required cron expression.



{% embed url="https://www.youtube.com/watch?v=1yEwIfclzIw" %}

#### 3. Re-executing Previous Batches

To rerun a batch from prior executions:

* Navigate to the **Test Runs** screen to view all previous batch executions.
* Locate the batch you wish to run and click the **Run Batch** button to execute it immediately.

By following these steps, users can efficiently manage and execute their test cases as individual runs or in batches, with options for immediate or scheduled execution.



<figure><img src="../../.gitbook/assets/Screenshot 2024-05-10 at 9.32.18 AM.png" alt=""><figcaption></figcaption></figure>
