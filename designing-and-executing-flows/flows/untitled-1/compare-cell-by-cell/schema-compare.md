# Schema Compare

This type of comparison will compare the table schema, which is to say, compares the columns with their data types.

If data types don't match then its a failure.

**Schema Compare Flow** 

* Drag Source component from left to the canvas
* Choose the Input Source Configuration and select the tables for Schema compare 
* Drag Target component from left to the canvas. 
* Choose the Input Source Configuration and select the tables for Schema compare 
* Drag Data Compare component and join the connections
* Select Schema Comparison
* In Mapping tab, the tables with same name are auto mapped. Map the tables and columns to compare the schema 
* Save and Execute the flow

![Schema Compare Mapping](../../../../.gitbook/assets/schemacompare2.png)

**Schema Compare Result** shows

**Summary** presents the number of tables matched/mismatched count and the total columns matched/mismatched count

**Details**  arranges the total tables matched and mismatched information based on the Column Data Type

![Schema Compare Summary Result](../../../../.gitbook/assets/image%20%282%29.png)

![Schema Compare Details ](../../../../.gitbook/assets/image%20%284%29.png)



