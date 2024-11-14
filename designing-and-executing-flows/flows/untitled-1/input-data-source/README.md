# Define Data Source and Target

To make use of the data that comes from the _Data Connections_,\_ \_users can make use of the _Source_ and _Target_ shapes from the palette, which can be used to configure source and destination data stores.

After dropping any of these two shapes into the canvas and clicking on them, a window will appear at the bottom of the screen. This window will show two main tabs, one named _Config,_ and the other _Sample Data._ The _Config_ tab will provide four tabs from which the user can choose the type of data input. These options are:

[**Table Input** ](input-table-s-from-database.md)**:** This is used to configure a data store which is a from a database in the form of a table.

[**SQL Input**](input-sql-data.md) **:** Custom SQL queries can be defined in this tab to extract data from multiple tables. These queries can be nested queries to chain the SQL statements.

[**File Input**](input-files/) **:** This tab can be used if the data has to be taken from a file which is in one of the following formats: \_Parquet, AVRO, JSON, CSV \_or _Excel._

[**API Input**](api-source.md) **:** This tab can be used to call on an API to extract data. This is a request response pattern where API calls can be scheduled to extract data.

{% hint style="success" %}
**Note :** Currently table/s input and SQL input tabs can be used together as source or target datastores.
{% endhint %}
