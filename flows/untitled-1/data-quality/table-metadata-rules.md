# Table metadata rules

* Minimum record count: This will define a test case which will check for minimum record count during each input validation process and will fail if the record count received is less than the defined threshold.
* Maximum record count : This will define a test case which will check for maximum record count during each input validation process and will fail if the record count received is more than the defined threshold.
* Column name : When this option is checked, this will create a test case to check for if the column names are changed with reference to column names when the original flow is created.
* Data types : This option when checked will create a test case and will be evaluated during each execution if the datatypes of the elements are changed. 
  * Note : This option is always available for Table input and SQL input and cannot be selected if the Infer schema option is not selected in the file input.
* New columns : This column when checked will create test cases to be evaluated for the presence of more  columns than when the flow is created.
* Removed columns : This column when checked will create test cases to be evaluated for the presence of less number of columns than when the flow is created.
* Delimiters : This option will create a test case to check if all rows have same number of delimiters and this option is available only for file input with delimiters.

