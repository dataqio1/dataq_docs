---
description: Map datasets and columns
---

# Data Compare Mapping

## Source to Target Mappings

There are three options for mapping datasets and columns from source to target.

1. When the table names and column names are same between source and target, they are automatically mapped.
2. User can explicitly edit the mapping by deleting or perform custom mapping. Steps to perform custom mapping are in the video below.



{% embed url="https://www.loom.com/share/7d13d4eff9254390a4e93d4408443050?sid=60541601-75a3-44e8-ae80-2dd632190e75" %}



3. **Upload** Dataset/Column mapping file.&#x20;

User can upload custom mapping file. This option is useful in the following scenarios.

* when the dataset names or column names are completely different .
* when user wants to map only certain datasets or columns.

The format of the csv file is&#x20;

| source\_table\_name | target\_table\_name | source\_column\_name | target\_column\_name | key\_column |
| ------------------- | ------------------- | -------------------- | -------------------- | ----------- |
|                     |                     |                      |                      |             |
|                     |                     |                      |                      |             |
|                     |                     |                      |                      |             |



[Download](https://dataops-store.s3.amazonaws.com/sample_mapping.csv) sample mapping file.

The CSV file should contain the following headers:

1. **source\_table\_name**: The name of the table in the source database.
2. **target\_table\_name**: The name of the table in the target database where the data is to be migrated or integrated.
3. **source\_column\_name**: The name of the column in the source table.
4. **target\_column\_name**: The name of the column in the target table that corresponds to the source column.
5. **key\_column**: A flag (usually a boolean or similar indicator) to denote if the source column is a key column (primary key, foreign key, etc.). The value of key\_column should be **true/false**.&#x20;



{% hint style="warning" %}
Mapping file is case sensitive. Ensure the table names, and column names have the same case as in the database.&#x20;
{% endhint %}

## SQL Transformation

* **SQL Transformation** : This feature can be used to apply an SQL Transformation function for all the _Source_ and _Target_ columns. This can be helpful, for instance, if in one of the columns from either \_Source \_or _Target_ the name has been written with uppercase, and the corresponding column from the other data source has the name in lowercase. The \_SQL Transformation \_can be used to write an SQL statement to change the column's names to uppercase. To do this:
  * Click on the icon under the _SQL_ column.
  * Provide the _SQL_ function in the _Text Field_ and click on _Done,_ or...
  * Slide the toggle and add predefined rules.
  * Go to Settings for [Add New Rule](https://app.gitbook.com/@Vexdata/s/docs/~/drafts/-MWOAN922BH54Ft3iFk_/settings) functionality.

<figure><img src="../../../../../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

## Tolerance

* **Tolerance** : Users can apply Tolerance for numeric (e.g., long, double, float, short, int.) , date and timestamp columns data types . Tolerance cannot be added to the key column.
  * Click on the icon under _Tolerance._
  * Select the _Operator_ and\_ \_type in the tolerance _Value._
  * Click on _Done._

<figure><img src="../../../../../.gitbook/assets/image (108).png" alt=""><figcaption></figcaption></figure>
