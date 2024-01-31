from elasticsearch import Elasticsearch
import io

# Connect to Elasticsearch
es = Elasticsearch(
    ["http://localhost:9200"],
    verify_certs=False,  
)
# print(es.ping())

#search and display the index names based on the given search pattern
index_pattern="hello_*"
response=es.indices.get_alias(index=index_pattern)
if(len(response)>0):
    for index in response:
        delete_response=es.indices.delete(index=index)
        print(delete_response)
else:
    print("no index has been found for the given search pattern")
