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
> s3n://**&lt;S3\_Bucket&gt;**/
>
> **s3AwsIamRole**
>
> arn:aws:iam::**XYZ**:role/Redshift\_Role





![Redshift Configuration](../../../.gitbook/assets/redshift_config.png)

## SQL Server

To add an SQL Server connection, you will have to provide:

* Connection name, which you will assign to this connection for internal use.
* A JDBC URL. A sample JDBC URL is shown under this text.

> jdbc:sqlserver://XXXXXX:1433;databaseName=XXXXXXX;

* Credentials, which will be a username and a password that will provide access to this database.

![SQL Server Configuration](../../../.gitbook/assets/sql_connection.png)

## Postgres

To add a PostgresSQL connection, you will have to provide:

* Connection name, which you will assign to this connection for internal use.
* A JDBC URL. A sample JDBC URL is shown under this text.

> jdbc:postgresql://&lt;jdbcHost&gt;:XXXX/&lt;jdbcDatabaseName&gt;

* Credentials, which will be a username and a password that will provide access to this database.



If SSL is enabled, additional parameters will be required for the JDBC URL as shown under this text. 

> jdbc:postgresql://&lt;jdbcHost&gt;:XXXX/&lt;jdbcDatabaseName&gt;&ssl=true**&sslmode=require&sslfactory=org.postgresql.ssl.NonValidatingFactory**

![Postgres Configuration](../../../.gitbook/assets/postgres.png)

## Snowflake

To add a Snowflake connection, you will have to provide:

* Connection name, which you will assign to this connection for internal use.
* A JDBC URL. A sample JDBC URL is shown under this text.

> jdbc:snowflake://XXX72530.us-east-1.snowflakecomputing.com/?db=&lt;jdbcDatabaseName&gt;&schema=&lt;schemaName&gt;

* Credentials, which will be a username and a password that will provide access to this database.

