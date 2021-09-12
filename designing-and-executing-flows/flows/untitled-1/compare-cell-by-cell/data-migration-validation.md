# Data Migration Validation

This comparison option is used to compare same type of schema.

**Data Migration Validation Flow** 

* Drag Source component from left to the canvas. 
* Drag Target component from left to the canvas. 
* Choose Input Source Configuration and select the tables for Data Profile Compare 
* Drag Data Compare component and join the connections
* Select Data Migration Validation 
* In Mapping tab, the tables with same name are auto mapped.                                                                Map the other tables and corresponding columns with same type. 
  * If the column type differs then system shows the red icon with a message to the user as "Schema should be same for data migration compare"  beside the table mapping.                                            Remove the column/table if different type of column is mapped
  * Data Types should be same for “Data Migration“ validation.
* Save and Execute the flow



* Drag a _Source_ component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables for _Data Migration Validation_.
* Drag a _Target_ component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables for _Data Migration Validation_. 
* Drag a _Data Compare_ component and join the connections. 
* Select _Data Migration Validation_ from the drop-down menu that appears at the bottom of the screen.
* In the _Mapping_ tab, the tables with the same name are auto mapped. You can manually map the other tables and the corresponding columns. 
  * If the column type differs, the system will show a red icon with the following message to the user _"Schema should be same for data migration compare"_  beside the table mapping. 
  * Remove the column/table if different type of columns are mapped.
  * Data types should be the same for _Data Migration validation_.
* Save and execute the flow.



![Data Migration Validation Comparison](../../../../.gitbook/assets/dmv1.png)



![Data Migration Validation Mapping](../../../../.gitbook/assets/dmv_mapping.png)



We can compare the selected source and destination tables to view 

* _Source and Destination Record Distribution._
* _Source and Destination Data Mismatches._
* Success/failure results of each mapped column are shown in _Test Case Report_.



![Data Migration Validation Summary Results](../../../../.gitbook/assets/dmv_summary%20%281%29.png)





![Data Migration Validation Summary Results](../../../../.gitbook/assets/dmv_result.png)



![Data Migration Validation Test Case Report](../../../../.gitbook/assets/dmv_tstcases.png)



