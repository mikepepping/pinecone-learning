import os
import json
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

# this method returns a dict with the file name as the key
# and the value as an array of sentences from the html pages content
def read_in_html_pages(path: str):
    pages = {}
    files = os.listdir(path)
    file_count = len(files)

    for i, file in enumerate(files):
        print(f"""{i}/{file_count} - Converting {file}""")
        if not file.endswith(".html"):
            print("File skipped, not html file")
            continue

        with open(os.path.join(path, file), 'r') as html_file:
            soup = BeautifulSoup(html_file.read(), 'html.parser')
            content = soup.find('div', { "id": "mw-content-text" })
            if content is None:
                print(f"""Failed to find content for {file}""")
                continue
            pages[file] = content.text.split('.')
    return pages

# this method transforms pages of sentences into vector embeddings
def transform_pages_into_embeddings(pages):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings_per_page = {}
    page_count = len(pages.keys())
    for i, (k, v) in enumerate(pages.items()):
        print(f"""{i}/{page_count} - encoding page {k}""")
        embeddings_per_page[k] = model.encode(v).tolist()

    return embeddings_per_page

if __name__ == '__main__':
    print("===== Converting html pages... =====")
    pages = read_in_html_pages(os.path.join(os.getcwd(), "..", "scraping", "pages"))
    print("===== Encoding embeddings ====")
    embeddings = transform_pages_into_embeddings(pages)
    print("===== Saving Embeddings =====")
    print(embeddings["Zubat.html"])
    with open('embeddings.json', 'w+') as embedding_file:
        json.dump(embeddings, embedding_file)
