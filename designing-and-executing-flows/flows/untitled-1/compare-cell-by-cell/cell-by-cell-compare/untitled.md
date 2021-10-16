# Data Compare Mapping

The _Mapping_ tab can be used to see how the columns from the two data sources have been mapped. The tables with the same name are auto-mapped. You can manually map the other tables and the corresponding columns. 

On the right side of the screen, a list will show how the columns have been paired, and their data types. Two edit options appear on this list, which are:

* **SQL Transformation** : This feature can be used to apply an SQL Transformation function for all the _Source_ and _Target_ columns. This can be helpful, for instance, if in one of the columns from either _Source _or _Target_ the name has been written with uppercase, and the corresponding column from the other data source has the name in lowercase. The _SQL Transformation _can be used to write an SQL statement to change the column's names to uppercase. To do this:
  * Click on the icon under the _SQL_ column.
  * Provide the _SQL_ function in the _Text Field_ and click on _Done,_ or... 
  * Slide the toggle and add predefined rules.
  * Go to Settings for [Add New Rule](https://app.gitbook.com/@dataq/s/docs/\~/drafts/-MWOAN922BH54Ft3iFk\_/settings) functionality.
* **Tolerance** : Users can apply _Tolerance_ for all integer column data types, e.g., long, double, float, short, int., to have a tolerance for the comparison to succeed even if the data is not perfectly matching. _Tolerance_ cannot be added to the key column.
  * Click on the icon under _Tolerance._
  * Select the _Operator_ and_ _type in the tolerance _Value._
  * Click on _Done._

