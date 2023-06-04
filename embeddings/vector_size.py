import os
import json

def calc_largest_vector():
    largest_vector = 0
    embedding_data = {}
    with open('./embeddings.json', 'r') as embedding_file:
        embedding_data = json.load(embedding_file)

    for document_file in embedding_data.keys():
        vectors = embedding_data[document_file]
        for vector_index, vector in enumerate(vectors):
            largest_vector = max(largest_vector, len(vector))
    print(largest_vector)

if __name__ == '__main__':
    calc_largest_vector()
