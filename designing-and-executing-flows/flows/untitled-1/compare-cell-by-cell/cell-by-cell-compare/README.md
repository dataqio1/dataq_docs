# ETL Testing/Cell By Cell Compare

This compare option will compare the data, or columns, of the source and target tables on various checks.

To create a _Cell By Cell Compare_ flow:

* Drag a _Source_ component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables to compare.
* Drag a _Target_ component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables to compare 
* Drag a _Data Compare_ component and join the connections. 
* Select _ETL Testing/Cell By Cell Comparison_ from the drop-down menu that appears at the bottom of the screen.
* In _Mapping_ tab, the tables with the same name are auto mapped. You can manually map the other tables and the corresponding columns. 
* Select the primary key. By default, the primary key is selected for the tables. If the key is not selected, the system shows a warning sign for the user to select the _Primary Key_.
* Save and execute the flow.

[Data Compare Options](https://app.gitbook.com/@dataq/s/docs/flows/untitled-1/compare-cell-by-cell/cell-by-cell-compare/sql-transformation)

![ETL Testing/Cell By Cell Compare](../../../../../.gitbook/assets/cellbycell.png)

![Cell By Cell Compare Tables Mapping](../../../../../.gitbook/assets/mapping.png)

DataQ can compare the selected source and destination tables to view:

* _Cell Level Validation Results._
* _Source and Destination Record Matching._ 
* _Source and Destination key Distributions._

![Cell By Cell Compare Summary Results](../../../../../.gitbook/assets/image%20%2811%29.png)

![Cell and Row Level Validation Results](../../../../../.gitbook/assets/cell_row_level_validation_results.png)

![Keys Level Validation Results](../../../../../.gitbook/assets/keys_level_validation_results.png)

