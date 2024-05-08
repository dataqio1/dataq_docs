# Data Quality

Vexdata.io enables users to create and manage data quality rules applicable to various data sources, including traditional databases, NoSQL databases like MongoDB, file-based data, and streaming data. These rules help ensure that data meets business quality standards before it is processed or analyzed.

### How to Create a Data Quality Test Case

### Step 1: Initiate a New Test Case

Navigate to the "New Test Case" dropdown in the top right corner of the Vexdata.io interface and select "Data Quality" to start defining a new data quality test case.



<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-08 at 5.34.05 PM.png" alt=""><figcaption></figcaption></figure>

### Step 2: Define the Source Data

Specify the source data for the test case. This data can originate from single or multiple datasets and may be drawn from various databases or files.



<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-08 at 5.35.35 PM.png" alt=""><figcaption><p>Two source datasets</p></figcaption></figure>

In the screenshot above, the user is validating a CSV file (radio button selected). To validate it, the CSV file needs to cross-referenced with lookup tables in Snowflake.

### Step 3: Write Data Quality Rules

There are two modes of data quality execution. Depending on the type of input source, the mode is selected automatically. The two modes are data in databases and files.&#x20;

**Option 1: Data Quality Rules on Database (like Oracle, Postgres, Snowflake)**

For data sourced from a database or Data Warehouse (DWH), apply one of the following rule types:

1. **SQL Queries**:
   * Write SQL queries to express business rules.
   * Any record returned by the SQL query is considered as bad data.
   *   Example: Validate that no users are registered with an invalid age.

       ```sql
       SELECT user_id, age FROM users WHERE age <= 0 OR age >= 150;
       ```
   * If this query returns any records, the test case fails.
2. **Column Level Conditions**:
   * Directly specify conditions for individual columns.
   * Example: Age in the users table should be between 1 and 149.
     * Bad Data Example: Age = 0 or Age = 150
     * Good Data Example: Age = 25

**Option 2: Data Quality Rules on Files(CSV, Excel, Json, XML) and No-SQL (Mongo)**

For data from files, MongoDB, or streaming sources, rules are executed in-memory. The following four rule types are available.

1. **SQL Queries**:
   * Similar to database input, write SQL-like queries for in-memory data checks.
   *   Example: Ensure that transaction amounts are positive.

       ```sql
       SELECT * FROM transactions WHERE amount <= 0;
       ```
2. **Column Level Conditions**:
   * Example: Validate transaction dates are within the current year.
     * Bad Data Example: Date = '2021-06-15'
     * Good Data Example: Date = '2024-05-01'
3. **Foreign Key Validation**:
   * Validate that foreign key values exist in the referenced table.
   * Example: Ensure every listed state in the 'users' table exists in the 'states' table.
4. **Table Metadata Rules**:
   * Set rules regarding table structure changes.
     * Fail if unexpected changes occur, like column additions or deletions.

### Step 4: Configuration and Execution

After defining all data quality rules:

* Click "Next" to proceed to configuration.
* Assign a name to the test case.
* Optionally, schedule and run the test case to enforce data quality checks.

### Example of Good vs. Bad Data

To further understand what is considered as good and bad data, let's consider a sample rule:

**Rule**: "Validate that age is between 1 and 149 in the users table."

* **Good Data Example**:
  * User: Alice, Age: 25 (within the acceptable range)
* **Bad Data Example**:
  * User: Bob, Age: 150 (outside the acceptable range)

This rule helps ensure that the data adheres to realistic and business-specific age constraints.











