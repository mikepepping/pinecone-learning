import pinecone
import os
import json

# from https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
# by https://stackoverflow.com/users/14343/ned-batchelder
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def upload_to_pinecone():
    api_key = os.environ.get('PINECONE_API_KEY')
    print(api_key)
    server_environment = os.environ.get('PINECONE_ENVIRONMENT')
    print(server_environment)

    pinecone.init(api_key = api_key, environment = server_environment)

    index_name = pinecone.list_indexes()[0]
    print(f""" Index: {index_name} """)
    index = pinecone.Index(index_name)

    print("Loading embedding data into memory")
    embedding_data = {}
    with open('./embeddings.json', 'r') as embedding_file:
        embedding_data = json.load(embedding_file)
    
    print("Formatting document vectors for uploading")
    embeddings = []
    for doc_index, document_file in enumerate(embedding_data.keys()):
        vectors = embedding_data[document_file]
        for vector_index, vector in enumerate(vectors):
            embeddings.append((f"""{document_file}-{vector_index}""", vector, { "document" : document_file }))

    for i, batch in enumerate(chunks(embeddings, 100)):
        print(f"""Uploading batch {i}""")
        index.upsert(batch)


if __name__ == '__main__':
    print("===== Uploading to Pinecone =====")
    upload_to_pinecone()
    print("===== Finished =====")
