from elasticsearch import Elasticsearch
import io

# Connect to Elasticsearch
es = Elasticsearch(
    ["http://localhost:9200"],
    verify_certs=False,  
)

# delete index files given input directory
with io.open('input.txt','r', encoding='utf-8') as f1:
    data=f1.read()
    f1.close()
    
# print(data)
data=data.split("\n")
# print(data)

for index in data:
    try:
        response=es.indices.delete(index=index)
        print(response)
    except Exception as e:
        print(str(e))    
    