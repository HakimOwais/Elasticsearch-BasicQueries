import requests

# response=requests.get("http://localhost:9200/_cat/indices")
# print(response.text)
response=requests.get("http://localhost:9200/_cat/indices?format=json&pretty")
# print(response.json())
data=(response.json())
[print(row["index"]) for row in data]