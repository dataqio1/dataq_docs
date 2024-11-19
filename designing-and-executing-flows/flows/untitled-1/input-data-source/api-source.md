# API Input

To provide an API as data input:

* Upload a Python script which can execute and produce output in CSV or JSON format.
* The output location will be passed as first argument**.**
* Provide a sample output JSON for the schema.

{% hint style="warning" %}
Ensure the sample output (few records) represents all of the columns.
{% endhint %}

Sample Python code snippet for an API\_:\_

```python
import json
import csv
import requests
import sys
import pandas as pd
def download_json(url):
    response = requests.get(url)
    data = response.json()
    return data['emp_hash']
def write_to_csv(data, output_path):
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
if __name__ == "__main__":
    output_path = sys.argv[1]
    url = "https://dataq-testing-data.s3.amazonaws.com/Input+Files/emp_hash.json"
    data = download_json(url)
    write_to_csv(data, output_path)
```

{% file src="../../../../.gitbook/assets/conversation.json" %}
Sample API output file(json)
{% endfile %}
