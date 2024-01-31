from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    ["http://localhost:9200"],
    verify_certs=False,  
)
print(es.ping())

# Create index with sequence


