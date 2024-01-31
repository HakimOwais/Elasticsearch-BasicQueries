from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    ["http://localhost:9200"],
    verify_certs=False,  
)

# index_name='hr'
# try:
#     response=es.search(index=index_name)
#     print(response)
# except Exception as e:
#     print(str(e))

index_name='hello_*'
try:
    response=es.search(index=index_name)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))
