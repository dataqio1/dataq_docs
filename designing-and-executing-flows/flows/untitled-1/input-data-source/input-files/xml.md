# XML

XML files can be used as data input by uploading a file, specifying an \_s3 \_path (**s3a**://\<file\_path>), or providing an HDFS location.

This way, the parsing tool can correctly interpret each `<record>` element as a separate entry, ensuring accurate data extraction and processing. Make sure the `rowtag` matches exactly with the element names in your XML file, including any case sensitivity.

We also have option&#x20;

* Flatten Data of XML  - Flattening the data involves converting complex and nested XML structures into a table-like format, making it easier to handle and analyze. This can be achieved through various tools and libraries that support XML flattening, allowing you to specify parameters for the transformation process.
* Drop All Null Records - Selecting this option will ignore all Null records

{% embed url="https://vimeo.com/1029743369/3cddd4f27c?share=copy&ts=0" %}
Add XML as a source File
{% endembed %}
