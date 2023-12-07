---
description: Schema Monitoring
---

# Schema Monitoring

Schema monitoring feature provides a robust solution for tracking and managing schema changes in your database environment. This feature is designed to capture the schema of one or more specified tables at a given point in time and continuously compare this snapshot with the current schema. Key functionalities include:

* **Snapshot Capturing**: The feature takes a snapshot of the specified table(s) schema at a user-defined point in time. This snapshot serves as a reference for future comparisons.
* **Continuous Monitoring**: It actively monitors the schema of the targeted table(s) and detects any alterations made after the initial snapshot. This includes changes in table structure, such as added or dropped columns, modified data types, changes in constraints, and more.
* **Change Detection and Notification**: Upon detecting any schema changes, the system promptly notifies users. The notification details the specific alterations, providing a clear and concise overview of how the current schema differs from the original snapshot.
* **Error Reporting**: In the event of unauthorized or unintended schema modifications, the feature flags these as errors. This immediate reporting allows for quick response and rectification, ensuring data integrity and consistency.
* **Use Case Adaptability**: Ideal for environments where schema stability is crucial, such as in production databases or where regulatory compliance requires strict schema control.

This feature enhances the ability to maintain database integrity, comply with regulatory standards, and manage changes efficiently, making it an essential tool for database administrators and teams managing critical data assets.

## **Steps to create Schema Monitoring Test case**&#x20;



1. Click on "New Test Case" on Top and select "Schema Monitoring"

<figure><img src="../../../.gitbook/assets/Screenshot 2023-12-06 at 8.26.37 PM.png" alt=""><figcaption></figcaption></figure>

2. Select the connection name and schema name from the drop down.

<figure><img src="../../../.gitbook/assets/Screenshot 2023-12-06 at 8.27.26 PM.png" alt="" width="375"><figcaption></figcaption></figure>

3. Select the tables that you wish to monitor and click on "Add Selected" at the bottom.
4. Proceed to the next step by clicking "Next" at the bottom right corner of the screen.
5.  First time, we need to click on the button ("Get Latest Schema") to get the schema.

    <figure><img src="../../../.gitbook/assets/Screenshot 2023-12-06 at 8.29.56 PM.png" alt=""><figcaption></figcaption></figure>
6. You will see the schema of the tables selected and the time stamp at which the schema is collected.

<figure><img src="../../../.gitbook/assets/Screenshot 2023-12-06 at 8.31.42 PM.png" alt=""><figcaption></figcaption></figure>

7. Click on the bottom right corner to proceed to the next step.
8. Give a name to the test case and click on "Save and Execute"

![](<../../../.gitbook/assets/Screenshot 2023-12-06 at 8.34.41 PM.png>)

9. Optionally this test case can be scheduled to run at regular intervals to detect any changes in the schema and notify.



{% embed url="https://www.loom.com/share/3bb9113945dd49dfa57f875c0ce0cade?sid=5e0c9eb0-f04c-4b02-a22a-eff1cad06427" %}
Video to create Schema Monitoring Test case
{% endembed %}





