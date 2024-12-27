# Data Compare Options

These are some of the options present in the configuration page for _ETL Testing/Cell by Cell Compare._

* **Random Input Sample** : User can provide a number of sample records for comparison, which allows a maximum of 1000 records.
  * Type in the number of records to be compared under _Random Input Sample._
* **Compare Type**  :&#x20;

There are two options.

1. A = B : This option compares both A - B and B - A
2.  A Super set of B : This option compares only A - B. Data set A can have more records compared to dataset B and as long as all the records of B exist in A, this is considered as a pass.

    Example : Compare historical table with the daily load table.&#x20;

![](<../../../../../.gitbook/assets/Screenshot 2023-12-13 at 10.53.20 AM.png>)&#x20;

This option allows the user to chose the type of comparison being made. The first option requires that both source and target have the same amount of records for the test to be regarded as passed, whereas the second option allows for _A_ to have more records than _B_ and still pass the test.

<figure><img src="../../../../../.gitbook/assets/Screenshot 2024-12-17 161451.png" alt=""><figcaption><p>Compare Type</p></figcaption></figure>

