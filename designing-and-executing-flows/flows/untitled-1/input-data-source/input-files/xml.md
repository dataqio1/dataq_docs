---
description: We can add an XMl file as souce.
---

# XML

XML files can be used as data input by uploading a file, specifying an \_s3 \_path (**s3a**://\<file\_path>), or providing an HDFS location.

This way, the parsing tool can correctly interpret each `<record>` element as a separate entry, ensuring accurate data extraction and processing. Make sure the `rowtag` matches exactly with the element names in your XML file, including any case sensitivity.

We also have option&#x20;

* Flatten Data of XML  - Flattening the data involves converting complex and nested XML structures into a table-like format, making it easier to handle and analyze. This can be achieved through various tools and libraries that support XML flattening, allowing you to specify parameters for the transformation process.
* Drop All Null Records - Selecting this option will ignore all Null records in dataset.

{% embed url="https://www.loom.com/share/9f1ccd2052794e4285361459f84e8a4d?sid=196e2897-85ba-4389-a677-cc76940bfd91" %}

