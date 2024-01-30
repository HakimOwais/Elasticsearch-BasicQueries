from elasticsearch import Elasticsearch

# Replace these with your Elasticsearch credentials
# username = "your_username"
# password = "your_password"

# Connect to Elasticsearch
es = Elasticsearch(
    ["http://localhost:9200"],
    # http_auth=(username, password),
    # scheme="https",  # Use "https" if your Elasticsearch is configured for SSL
    verify_certs=False,  # Set to True if your Elasticsearch has a valid SSL certificate
)

# Define index mapping with a dense_vector field
index_mapping = {
    "mappings": {
        "properties": {
            "vector_field": {
                "type": "dense_vector",
                "dims": 3,  # Specify the dimensionality of your vectors
            },
            # Add other fields as needed
        }
    }
}

# Create the index
index_name = "second_index"
es.indices.create(index=index_name, body=index_mapping)

# Sample data with vectors
sample_data = [
    {"vector_field": [1.0, 2.0, 3.0]},
    {"vector_field": [4.0, 5.0, 6.0]},
    # Add more documents with vectors
]

# Index the data
for i, doc in enumerate(sample_data):
    es.index(index=index_name, body=doc, doc_type="doc", id=i + 1)

# Search for documents with vectors
query_vector = [2.0, 3.0, 4.0]  # Replace with the vector you want to search for
search_query = {
    "query": {
        "dense_vector": {
            "vector_field": {
                "vector": query_vector,
                "similarity": "COSINE",  # Use COSINE similarity for vector searches
            }
        }
    }
}

search_results = es.search(index=index_name, body=search_query)
print("Search Results:")
print(search_results)
