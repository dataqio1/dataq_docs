# Schema Compare

This type of comparison will compare the table schema, which is to say, compares the columns with their data types. If data types don't match, then the test is considered as failed.

**Schema Compare Flow **

* Drag a _Source_ component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables for schema compare.
* Drag a _Target _component from the palette to the canvas.
* Choose the _Input Source Configuration_ and select the tables for schema compare. 
* Drag a _Data Compare_ component and join the connections. 
* Select _Schema Comparison_ from the drop-down menu that appears at the bottom of the screen.
* In the _Mapping_ tab, the tables with the same name are auto mapped. You can manually map the other tables and the corresponding columns. 
* Save and execute the flow.

![Schema Compare Mapping](../../../../.gitbook/assets/schemacompare2.png)

_Schema Compare Result_ shows how well the source and target schema match.

_Summary_ presents the  matched/mismatched tables count and the total matched/mismatched columns count.

_Details_ arranges the total tables matched and mismatched information based on the _Column Data Type._

![Schema Compare Summary Result](<../../../../.gitbook/assets/image (2).png>)

![Schema Compare Details ](<../../../../.gitbook/assets/image (4).png>)

