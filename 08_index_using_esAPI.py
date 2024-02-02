# create index using elastic search api

import requests

response=requests.put("http://localhost:9200/text_index_using_api")
print(response.text)
