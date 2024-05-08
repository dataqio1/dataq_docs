# Data Quality Testing

Vexdata.io enables users to create and manage data quality rules applicable to various data sources, including traditional databases, NoSQL databases like MongoDB, file-based data, and streaming data. These rules help ensure that data meets business quality standards before it is processed or analyzed.

### How to Create a Data Quality Test Case

#### Step 1: Initiate a New Test Case

Navigate to the "New Test Case" dropdown in the top right corner of the Vexdata.io interface and select "Data Quality" to start defining a new data quality test case.

#### Step 2: Define the Source Data

Specify the source data for the test case. This data can originate from single or multiple datasets and may be drawn from various databases or files.

#### Step 3: Choose the Execution Method

Depending on the type of input source, select one of the following options to apply data quality rules:

**Option 1: Database Input Data**

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

**Option 2: Non-Database Input Data**

For data from files, MongoDB, or streaming sources, rules are executed in-memory using these rule types:

1. **SQL Queries**:
   * Similar to database input, write SQL-like queries for in-memory data checks.
   *   Example: Ensure that transaction amounts are positive.

       ```sql
       sqlCopy codeSELECT transaction_id FROM transactions WHERE amount <= 0;
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

#### Step 4: Configuration and Execution

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











