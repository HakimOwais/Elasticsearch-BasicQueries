# Search specific index

import requests

index_name="owais"
response=requests.get("http://localhost:9200/"+index_name)
# print(response.text)
print(response.json())
print(response.json().keys())
