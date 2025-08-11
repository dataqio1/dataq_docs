# JSON

JSON files can be used as data input by uploading a file, specifying an \_s3 \_path (**s3a**://\<file\_path>), or providing an HDFS location.

* Multiline options can be set to false if the JSON structure is in single line. Default value for this is set to _True._
* JSON can be flattened, by checking the \_Flatten Data \_checkbox, if the JSON structure is in hierarchical format.
* JSON elements can be selected by specifying element names in the columns section and can be renamed using them as keywords. E.g. if _id_, first\_\_name _and_ last\_name _are the only three elements to be selected from a JSON with many distinct elements:_ isbn _as_ id, author.firstName _as_ first\_name _and_ author.\_lastName as last\_name.

<figure><img src="../../../../../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

Multi-line _False_ sample:

```
{ "isbn": "123-456-222","lastname": "Doe","firstname": "Jane"}
{"isbn": "123-456-777","lastname": "Smith","firstname": "Jane"}
```

Multi-line _True_ sample:

```
[
	{ "isbn": "123-456-222","lastname": "Doe","firstname": "Jane"},
	{"isbn": "123-456-777","lastname": "Smith","firstname": "Jane"}
]
```

{% hint style="info" %}
Root level columns can be selected above in a multi-root JSON structure. For selection of nested columns, use the _Select Columns_ shape from the palette.
{% endhint %}
