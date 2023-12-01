# ETL Testing/Cell By Cell Compare

This compare option will compare the data, or columns, of the source and target tables on various checks.

To create a _Cell By Cell Compare_ flow:

* Drag a _Source_ component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables to compare.
* Drag a \_Target \_component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables to compare
* Drag a _Data Compare_ component and join the connections.
* Select _ETL Testing/Cell By Cell Comparison_ from the drop-down menu that appears at the bottom of the screen.
* Select the primary key. By default, the primary key is selected for the tables. If the key is not selected, the system shows a warning sign for the user to select the _Primary Key_.
* Save and execute the flow.

[Data Compare Options](https://app.gitbook.com/@Vexdata/s/docs/flows/untitled-1/compare-cell-by-cell/cell-by-cell-compare/sql-transformation)

<figure><img src="../../../../../.gitbook/assets/Screenshot (417).png" alt=""><figcaption><p>Cell By Cell Compare Tables Mapping</p></figcaption></figure>



<figure><img src="../../../../../.gitbook/assets/Screenshot 2023-12-01 at 5.21.16 PM.png" alt=""><figcaption></figcaption></figure>

Vexdata can compare the selected source and destination tables to view:

* _Cell Level Validation Results._
* _Record Count Validations_
* _Source and Destination key Distributions._

<figure><img src="../../../../../.gitbook/assets/Screenshot (420).png" alt=""><figcaption><p>Cell by Cell Comparison Results Overview</p></figcaption></figure>





## Source to Target Mappings

There are primarily three ways to do the mapping.



1. When the table names and column names are same between source and target, they are automatically mapped.
2.  User can explicitly edit the mapping by deleting or perform custom mapping.

    Steps to perform custom mapping are below



{% embed url="https://www.loom.com/share/7d13d4eff9254390a4e93d4408443050?sid=18ebdb16-8dd1-4c21-aedb-fbeb0be5a8f1" %}
Steps to edit mapping between source to target columns
{% endembed %}



3. User uploads a mapping file.&#x20;

User can upload custom mapping file. Below is the sample file tamplate

[Download](https://dataops-store.s3.amazonaws.com/sample\_mapping.csv) sample mapping file.

The CSV file should contain the following headers:

1. **source\_table\_name**: The name of the table in the source database.
2. **target\_table\_name**: The name of the table in the target database where the data is to be migrated or integrated.
3. **source\_column\_name**: The name of the column in the source table.
4. **target\_column\_name**: The name of the column in the target table that corresponds to the source column.
5. **key\_column**: A flag (usually a boolean or similar indicator) to denote if the source column is a key column (primary key, foreign key, etc.). The value of key\_column should be **true/false**.&#x20;

{% hint style="warning" %}
For every table mapping there should be atleast one column which has key\_column true.&#x20;
{% endhint %}









<figure><img src="../../../../../.gitbook/assets/Screenshot (421).png" alt=""><figcaption><p>Cell by Cell Comparison Stats</p></figcaption></figure>
