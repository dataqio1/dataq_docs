# SQL rules

 

* This tab can be used to define more than one test case with one SQL rule creating one test case.
* The result of SQL rule query should return zero rows for test case pass criteria. If one or more rows are returned, the test case is considered to be failed.
* Each SQL rule can be complex query involving one or more tables on the source  if the input is database.
* If the source is defined as a file, then the SQL rule can contain only one table, the name of which will be concatenation of name of the file and its extension.

