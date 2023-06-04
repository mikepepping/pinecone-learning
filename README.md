# Pinecone Learning

This is just a repo for learning how to crudely convert web data to vector embeddings and upload to pinecone.
The goal is just to learn the naive fundamentals of creating semantic search via pinecone.

## How do I used these scripts? (because I will forget)

1. Run `scraping/scrape_data.py` to scrape all Generation 1 kanto pokeon profiles from bulbapedia.
2. Run `embeddings/convert_html_to_embeddings.py` to convert all pages into vector embeddings that are then saved to `embeddings.json`.
3. Run `embeddings/upload_to_pinecone.py` to load `embeddings.json` and upload the vectors to pinecone in batches.
4. Edit `querys/query.py` so that that it contains the query you want to search for.
5. Run `querys/query.py` and it will display the top 4 results for your semantic search.

