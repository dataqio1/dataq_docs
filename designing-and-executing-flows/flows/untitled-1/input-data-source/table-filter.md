---
description: From Version 7_14
---

# Table Filter

### Table Filter

The "Data Filter" functionality is a critical enhancement designed to address the need for targeted data testing. This feature allows users to conduct tests on a specific subset of records, rather than the entire data set. Here’s how you can create a data filter:

**Steps to Create a Data Filter:**

1. Select a Test Case: Begin by choosing an existing test case or create a new test case in your testing environment.
2. In Source/Target Data Source: Click on the 'Table' radio button, connection and schema.
3. Select Tables: Choose one or more tables from your database that you wish to test. Once selected, click on “Add Selected” to include them in your test case.
4. Apply Filter: Click on the "Apply Filter" button to proceed to the filter condition input stage.
5. Enter Filter Conditions: Define the specific conditions to filter your data. This step is crucial as it determines the subset of data to be tested.



{% hint style="info" %}
To filter records with an ID greater than 500, enter the condition: \
`id > 500`
{% endhint %}

{% hint style="info" %}
For a more complex filter, such as selecting records where the ID is greater than 599924 and the age is over 70, enter:\
`id > 599924 and age > 70.`
{% endhint %}

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-06-06 at 12.15.30 PM.png" alt=""><figcaption><p>Apply Filter Screenshot</p></figcaption></figure>

For a more complex filter, such as selecting records where the ID is greater than 599924 and the age is over 70, enter: `id > 599924 and age > 70`. Once the filter condition is entered, it is applied to the selected table(s). Only the data that meets these conditions will be included in your test case.

By following these steps, you can efficiently focus your testing efforts on specific, relevant subsets of data, making your testing process more precise and effective.

{% embed url="https://vimeo.com/948293423/734449602e?share=copy" %}
