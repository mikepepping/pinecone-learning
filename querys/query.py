import os
import pinecone
from sentence_transformers import SentenceTransformer

def query(query: str):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vector = model.encode(query).tolist()

    api_key = os.environ.get('PINECONE_API_KEY')
    print(api_key)
    server_environment = os.environ.get('PINECONE_ENVIRONMENT')
    print(server_environment)

    pinecone.init(api_key = api_key, environment = server_environment)

    index_name = pinecone.list_indexes()[0]
    print(f""" Index: {index_name} """)
    index = pinecone.Index(index_name)

    return index.query(
            vector = query_vector,
            top_k=5,
            include_values=False
            )['matches']

if __name__ == '__main__':
    print(query('strong against grass'))



