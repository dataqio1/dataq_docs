# Data Quality

Vexdata.io enables users to create and manage data quality rules applicable to various data sources, including traditional databases, NoSQL databases like MongoDB, file-based data, and streaming data. These rules help ensure that data meets business quality standards before it is processed or analyzed.

### Steps to create a Data Quality Test Case

### Step 1: Initiate a New Test Case

Navigate to the "New Test Case" button in the top right corner of the Vexdata.io interface and select "Data Quality" Test Case Type to start defining a new data quality test case.

<figure><img src="../../../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

### Step 2: Define the Source Data

Specify the source data for the test case. This data can originate from single or multiple datasets and may be drawn from various databases or files. Refer to steps to [create a new source](input-data-source/).



<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-08 at 5.35.35 PM.png" alt=""><figcaption><p>Two source datasets</p></figcaption></figure>

In the screenshot above, the user is validating a CSV file (radio button selected). To validate it, the CSV file needs to cross-referenced with lookup tables in Snowflake.

### Step 3: Write Data Quality Rules

There are two modes of data quality execution. Depending on the type of input source, the mode is selected automatically.&#x20;

**Option 1: Data Quality Rules on Database (like Oracle, Postgres, Snowflake, etc)**

For data sourced from a database or Data Warehouse (DWH), apply one of the following rule types:

1.  **SQL Queries**:

    * Write SQL queries to express business rules.
    * Any record returned by the SQL query is considered as bad data.
    *   Example: Validate that no users are registered with an invalid age.

        ```sql
        SELECT user_id, age FROM users WHERE age <= 0 OR age >= 150;
        ```

    If this query returns any records, these records are considered as bad records and the test case fails.
2. **Column Level Conditions**:
   * Directly specify conditions for individual columns.
   *   Example rule : Age in the users table should be between 1 and 149.

       * Write SQL expression    `age > 0 and age < 150`

       If there are any records where age is below 1 and above 140, the rule will fail and those repords are reported.

In below screenshot, `TOTALPRICE > 0`&#x20;

The records for which TOTALPRICE <= 0 will be reported as bad data.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-08 at 6.19.45 PM.png" alt=""><figcaption></figcaption></figure>

**Option 2: Data Quality Rules on Files(CSV, Excel, Json, XML) and No-SQL (Mongo)**

For data from files, MongoDB, or streaming sources, rules are executed in-memory. The following four rule types are available.



1. **SQL Queries**:

* Similar to database input, write SQL-like queries for in-memory data checks.
* Example: Ensure that transaction amounts are positive. Refer to [section](data-quality/sql-rules.md) for writing rules in English.\




<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-08 at 7.24.54 PM.png" alt=""><figcaption></figcaption></figure>

2. **Column Level Conditions**:

* Directly specify conditions for individual columns.
*   Example rule : Age in the users table should be between 1 and 149.

    * Write SQL expression    `age > 0 and age < 150`

    If there are any records where age is below 1 and above 140, the rule will fail and those repords are reported.

In below screenshot, `TOTALPRICE > 0`&#x20;

The records for which TOTALPRICE <= 0 will be reported as bad data.

<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-08 at 6.19.45 PM.png" alt=""><figcaption></figcaption></figure>

3. **Foreign Key Validation**:

* Validate that foreign key values exist in the referenced table.
* Example: Ensure every listed state in the 'users' table exists in the 'states' table.

4. **Table Metadata Rules**:

Set rules regarding table structure changes.

* Select "Column Names" to ensure the column names remain unchanged.
* Select "Data Types" to verify that the column types are not altered.
* Select "New Columns" to trigger a rule failure when new columns are added.
* Select "Removed Columns" to trigger a rule failure when columns are removed.



<figure><img src="../../../.gitbook/assets/Screenshot 2024-05-08 at 6.05.27 PM.png" alt=""><figcaption></figcaption></figure>

### Step 4: Configuration and Execution

After defining all data quality rules:

* Click "Next" to proceed to configuration.
* Assign a name to the test case.
* Optionally, schedule and run the test case to enforce data quality checks.
