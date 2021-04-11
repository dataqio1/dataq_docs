# Column rules

* This tab is used to define any conditions/rules at the column level manually or can be autosuggested by system. Following are the different rules which can be defined at the column level
  * Empty check rule : Rule to create a test case which checks for if the column is empty. If the check box for this rule is checked,  during execution of the flow if the corresponding column has empty value in any row, this test case will be failed. 
  * Null check rule : This rule will pass during execution if the percentage of number of not nulls in this column falls below the defined threshold.
  * Unique check :  This rule will pass during execution if the percentage of number of unique values in this column falls below the defined threshold.
  * Left/Right spaces :
  * Min length: This rule will pass if all the values in the column are more than the defined minimum length.
  * Max length: This rule will pass if all the values in the column are less than maximum length.
  * Min value: This rule will pass if all the values in the column are more than the defined minimum value.
  * Max value: This rule will pass if all the values in the column are less than defined maximum value.
  * SQL where condition : A sql expression can be used to check if all rows satisfy this column condition. Even if one of the row fails to satisfy the condition then the test case is failed.
  * Regular expression : This builds a test case when given on a column, every value of the corresponding column should comply with the regular expression.
  * Prebuilt rules : Prebuilt rules can be added to apply at column level of each row. If any of the row does not satisfy the condition of the prebuilt rule, the test case will be failed.

![](../../../.gitbook/assets/columnrules.jpg)

* Auto Suggest : The above mentioned rules under Column rules will be auto suggested by the system except for SQL where condition and regular expression. Once the rules are auto suggested, user can edit them to customize specific scenarios.

