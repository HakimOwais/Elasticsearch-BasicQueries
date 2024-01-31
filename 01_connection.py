from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    ["http://localhost:9200"],
    verify_certs=False,  
)
print(es.ping())
##create index
es.indices.create(index="welcome")
##display all indices
indices=es.indices.get_alias()
for index in indices:
    print(index)