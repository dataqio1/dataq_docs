# Import/Export Rules

### Overview

The Import/Export Rules feature lets you efficiently manage Data Quality rules by importing them from Excel templates and exporting existing rules for backup, sharing, or migration.

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-10-15 at 2.16.48 PM.png" alt=""><figcaption></figcaption></figure>



### Accessing Import/Export Rules



To access the Import/Export Rules functionality:



1. Navigate to your **Test Cases** list
2. Locate the Data Quality test case you want to work with
3. Click on the **(N) Rules** link in the DQ Rules column (where N is the number of rules)
4. The **DQ Rules** dialog will open, displaying all rules for the selected dataset

### Export DQ Rules



<figure><img src="../../../../.gitbook/assets/Screenshot 2025-10-15 at 2.18.13 PM.png" alt=""><figcaption></figcaption></figure>

#### Overview

The Export feature allows you to download all existing Data Quality rules for a specific dataset into an Excel file. This is useful for:

* Creating backups of your rules
* Sharing rules with team members
* Migrating rules to other test cases or environments
* Using as a template for bulk rule creation

#### Steps to Export Rules



1. Open the **DQ Rules** dialog (as described above)
2. Click the **Export DQ Rules** button (cyan/teal button on the left)
3. The system will automatically generate and download an Excel file containing all your rules
4. The exported file will be named with the dataset name and timestamp

####

### Import DQ Rules

<figure><img src="../../../../.gitbook/assets/Screenshot 2025-10-15 at 2.19.50 PM.png" alt=""><figcaption></figcaption></figure>

#### Overview

There are primarily three formats to import the Data Quality Rules.



**JSON**: Once rules are exported, they can be imported into the same or different test cases. Use cases include exporting existing rules from one test case to another or migrating a single test case between environments.

**SQL**: You can connect to any database to import data. If your data matches the specified format below, rules will be populated accordingly.

**Excel**: Whether you’re using SQL or Excel, the data format needs to be consistent. Refer to the attached Excel template.

{% file src="../../../../.gitbook/assets/template.xlsx" %}



#### Prerequisites



Before importing rules, ensure you have:

1. A valid Excel template file (download the template from this documentation page)
2. All required columns filled in the template
3. Valid SQL syntax for SQL-based rules
4. Correct column names that match your target dataset

#### Steps to Import Rules



1. Open the **DQ Rules** dialog for your target dataset
2. Click the **Import DQ Rules** button (white/outlined button)
3. A file browser dialog will open
4. Select your prepared Excel file (.xlsx format)
5. Click **Open** to upload the file
6. The system will process and validate the rules
7. Successfully imported rules will appear in the rules list immediately





## Excel/SQL Template Structure :

**Test Case Structure Guide**

* **TEST\_CASE\_ID**\
  Unique identifier for each test case.\
  &#xNAN;_&#x46;ormat_: TC-XXX (e.g., TC-101, TC-102)
* **TEST\_CASE\_NAME**\
  Clear description of the validation objective, explaining the business or technical rule.
* **SQL\_EXECUTE\_COLUMN\_DQ**\
  SQL query utilizing INFORMATION\_SCHEMA tables that outputs a single value or count. No placeholders are present.
* **SQL\_EXECUTE\_COLUMN\_DQ\_EXPECTED\_RESULT**\
  &#xNAN;_&#x46;ormat for Expected Result_:
  * For COUNTS\_VALIDATION: Use =0, >10, <100
  * For DATA\_VALIDATION: Use =VALUE, >30, <1000
* **TEST\_CASE\_SEVERITY**
  * _Warning_: Non-critical, informational
  * _Severe_: Critical, requires immediate action
* **DQ\_SQL\_TYPE**
  * _COUNTS\_VALIDATION_: Returns count of records.

#### Rule Types Supported

Currently only SQL rules can be imported in SQL and Excel:



1. **SQL Rules**: Custom SQL queries that return validation results
2. &#x20;  \- Must return a numeric value or boolean result
3. &#x20;  \- Can include complex queries with joins, aggregations, and window functions
4. **Column Level Rules**: Validation rules applied to specific columns
5. &#x20;  \- Specify the target column name
6. &#x20;  \- Define validation criteria



