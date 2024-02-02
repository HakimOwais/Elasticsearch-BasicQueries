# Add Document To Elasticsearch Index Using Rest API
import requests

url="http://localhost:9200/"
headers={
    "Content-Type":"application/json",
}
json_data={
    "message":"this is added using python and rest api and id 1",
     "count":10
}
response=requests.put(url+"test_index_using_api/_doc/1?pretty"
                      ,headers=headers,json=json_data)
print(response)