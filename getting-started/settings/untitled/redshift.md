# Databases/Warehouses

Some of the databases and warehouse available when clicking on _Add New Connection_ might require more information than the one shown in the previous section, or could have extra options.

## Redshift

To add a Redshift connection, you will have to provide:

* Connection name, which you will assign to this connection for internal use.
* A JDBC URL. A sample JDBC URL is shown under this text.

> jdbc:redshift://redshift-cluster-1.XXXXXXXXXX.us-east-1.redshift.amazonaws.com:5439/dev?ssl=false

* Credentials, which will be a username and a password that will provide access to this database.

Optionally, you may provide _s3TempDir_ and _s3AwsIamRole_ for better performance, as explained in the following link.

{% embed url="https://awsdba.cloud/2019/05/10/redshift-iam-role-for-copy-unload-to-s3/" %}

> **s3TempDir**
>
> s3n://**\<S3\_Bucket>**/
>
> **s3AwsIamRole**
>
> arn:aws:iam::**XYZ**:role/Redshift\_Role

![Redshift Configuration](../../../.gitbook/assets/redshift\_config.png)

## SQL Server

To add an SQL Server connection, you will have to provide:

* Connection name, which you will assign to this connection for internal use.
* A JDBC URL. A sample JDBC URL is shown under this text.

> jdbc:sqlserver://XXXXXX:1433;databaseName=XXXXXXX;

* Credentials, which will be a username and a password that will provide access to this database.

![SQL Server Configuration](../../../.gitbook/assets/sql\_connection.png)

## Postgres

To add a PostgresSQL connection, you will have to provide:

* Connection name, which you will assign to this connection for internal use.
* A JDBC URL. A sample JDBC URL is shown under this text.

> jdbc:postgresql://\<jdbcHost>:XXXX/\<jdbcDatabaseName>

* Credentials, which will be a username and a password that will provide access to this database.

If SSL is enabled, additional parameters will be required for the JDBC URL as shown under this text.

> jdbc:postgresql://\<jdbcHost>:XXXX/\<jdbcDatabaseName>\&ssl=true\*\*\&sslmode=require\&sslfactory=org.postgresql.ssl.NonValidatingFactory\*\*

![Postgres Configuration](../../../.gitbook/assets/postgres.png)



#### Create a new read only user for Postgres Testing

The user id should only have read permission on the data. Also, DataQ needs permission to read metadata. The user id should have read only permissions on the following system tables

```
pg_class
information_schema.table_constraints
information_schema.columns
pg_namespace
pg_catalog
```



## Snowflake

To add a Snowflake connection, you will have to provide:

* Connection name, which you will assign to this connection for internal use.
* A JDBC URL. A sample JDBC URL is shown under this text.

> jdbc:snowflake://XXX72530.us-east-1.snowflakecomputing.com/?db=\<jdbcDatabaseName>\&schema=\<schemaName>

* Credentials, which will be a username and a password that will provide access to this database.

![Snowflake Configuration](<../../../.gitbook/assets/snowflake (1).png>)





## Oracle <a href="#snowflake" id="snowflake"></a>

It is recommended to create a read only user account in Oracle. The user id needs to have access to the following system tables to read the metadata of all the tables.&#x20;

1. sys.dba\_tables
2. sys.dba\_constraints
3. sys.dba\_cons\_columns
4. sys.all\_users
5. all\_ind\_columns
6. all\_indexes
7. all\_cons\_columns
8. all\_constraints

​

