# API Source

To provide API as input 

* Provide Python script which can execute one more APIs to get the output.
* The final API should write the output to a specific location "**/tmp/dq\_output\_file\_name.json**"
* Provide sample output json for schema.

{% hint style="info" %}
Ensure the sample output \(few records\) represents all the columns.
{% endhint %}

```text
# Sample python code snippet for API

import requests
import json

 
API_KEY = "d25a07df6199416b87816551ebf80b0744c50b8c2fa385909c0820cfde80a3c5"
PDL_VERSION = "v5"
PDL_URL = "https://dataq-testing-data.s3.amazonaws.com/conversation.json"
 
 
params = {
   "api_key": API_KEY,
   "name": ["sean thorne"],
   "company": ["peopledatalabs.com"]
}
 
json_response = requests.get(PDL_URL, params=params).json()
json_text = json.dumps(json_response)
f = open("/tmp/dq_output_file_name.json", "w")
f.write(json_text)
f.close()
```



{% file src="../../../.gitbook/assets/conversation.json" caption="Sample API output file\(json\)" %}



