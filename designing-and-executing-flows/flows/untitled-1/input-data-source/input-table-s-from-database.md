# Configure Table/s from Database

To select one or more tables:

* Select the _Connection Name_ from the drop down menu.
* Select the desired schema.
* Select the checkboxes for all the tables that need to be validated.
* Click on _Add Selected_ at the bottom. 

![](../../../../.gitbook/assets/screen-shot-2021-03-05-at-3.07.09-pm.png)

#### Advanced Options

For large tables, it is recommended to provide a partition column so DataQ can pull the data in parallel. DataQ can autodetect the partition column; however, it is recommended that users provide this partition.

**Rules for selecting the partition column :**

* The column should have an index.
* The column should be numeric or a date-column.
* If the column is of string-type, ensure the bucket size is not too low for a distinct value.
  * Example : If you have to choose between city and person\_name, select city as partition column, as person\_name is highly unique.

