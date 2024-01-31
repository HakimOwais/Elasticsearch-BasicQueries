from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    ["http://localhost:9200"],
    verify_certs=False,  
)
print(es.ping())

# Create index with sequence

index_basename = "hello"
for i in range(1,6):
    response = es.indices.create(index=index_basename+"_"+str(i))
    print(response)
