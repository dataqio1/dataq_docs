---
description: >-
  Vexdata provides ability to write test cases in English which are converted to
  SQL.
---

# Writing SQL test cases in English

<figure><img src="../../../../.gitbook/assets/Screenshot 2024-05-08 at 3.52.21 PM.png" alt=""><figcaption><p>SQL Rule</p></figcaption></figure>

Write the test case in English in the **AI Prompt** section and click on Generate SQL.&#x20;



{% hint style="warning" %}
Ensure that all the tables required for this test case are selected in the source section. This is necessary to generate SQL from English.
{% endhint %}

Our software enhances the ease and accuracy of data quality testing by allowing users to write test cases in natural language, powered by OpenAI. Below are examples to guide you in creating effective test cases for both single-table and multi-table test scripts.

#### Sample Data

1.  **Users Table**

    | user\_id | name    | age | credit\_limit |
    | -------- | ------- | --- | ------------- |
    | 1        | Alice   | 25  | 5000          |
    | 2        | Bob     | 34  | 15000         |
    | 3        | Charlie | 29  | 7000          |
2.  **Orders Table**

    | order\_id | user\_id | order\_amount | order\_date |
    | --------- | -------- | ------------- | ----------- |
    | 101       | 1        | 300           | 2024-01-15  |
    | 102       | 2        | 2200          | 2024-01-18  |
    | 103       | 1        | 450           | 2024-02-05  |

#### English Inputs and Corresponding SQL

1. **Validate that no users are underage**
   * **English**: Ensure that all users are at least 18 years old in users table
   *   **SQL**:

       ```sql
       SELECT * FROM Users WHERE age < 18;
       ```
2. **Validate that no users are beyond retirement age in Users table**
   * **English**: Check that no user is older than 65.
   *   **SQL**:

       ```sql
       SELECT * FROM Users WHERE age > 65;
       ```
3. **Validate that all users have a positive credit limit**
   * **English**: Confirm that every user has a credit limit greater than zero in users table.
   *   **SQL**:

       ```sql
       SELECT * FROM Users WHERE credit_limit <= 0;
       ```
4. **Ensure total orders in Orders table do not exceed credit limits in Users table**
   * **English**: Validate that the sum of order amounts for each user does not exceed their credit limit.
   *   **SQL**:

       ```sql
       SELECT u.user_id, u.name, SUM(o.order_amount) AS total_orders, u.credit_limit
       FROM Users u
       JOIN Orders o ON u.user_id = o.user_id
       GROUP BY u.user_id
       HAVING SUM(o.order_amount) > u.credit_limit;
       ```
5. **Check for active users with no orders**
   * **English**: Identify users in users table who have not placed any orders.
   *   **SQL**:

       ```sql
       SELECT u.user_id, u.name
       FROM Users u
       LEFT JOIN Orders o ON u.user_id = o.user_id
       WHERE o.order_id IS NULL;
       ```

These examples provide a clear demonstration of how English test case inputs can be translated into SQL queries to validate data across different scenarios in a database system.
