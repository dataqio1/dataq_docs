# Configure Table/s from Database

To select one or more tables :

* Select the _Connection Name_ from the drop down menu.
* Select the schema.
* Select the checkboxes for all the tables that need to be validated.
* Click on _Add Selected_ at the bottom 

![](../../../../.gitbook/assets/screen-shot-2021-03-05-at-3.07.09-pm.png)

**Advanced Options** : For large tables, it is recommended to provide a partition column so DataQ can pull the data in parallel. 

Dataq can autodetect the partition column however it is recomended for user to provide this.

**Rules for selecting the partition column :**

* The column should have index.
* The column should be numeric or date column.
* If the columm is string type, ensure the bucket size is not too low for a distinct value.
  * Example : If you have to choose between city and person\_name, select city as partition column as the person\_name is highly unique.







If the column is of type 



