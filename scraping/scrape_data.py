import typing
import requests
import re
from random import randint
from time import sleep
from bs4 import BeautifulSoup

base_url = "https://bulbapedia.bulbagarden.net"

def scrape_pokemon_links(path: str):
    response = requests.get(base_url + path)
    print(response)
    if response.status_code != requests.codes.ok:
        raise requests.exceptions.RequestException('failed to load url')
    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for link in soup.find_all('a', { "title": re.compile("^.*\(Pokémon\).*") }):
        if re.match('^User', link.get('title')):
            continue 
        links.append(link.get('href'))

    return links

def scrape_pokemon_data(path :str):
    print(f"""Fetching - {path}""")
    try:
        response = requests.get(base_url + path)
        if response.status_code != requests.codes.ok:
            print(f"""Warning: - Failed to fetch data {response.status_code}""")
        pokemon_page = BeautifulSoup(response.content, 'html.parser')
        return pokemon_page
    except requests.exceptions.RequestException as e:
        print("Failed to fetch pokemon data")
        print(e.message)
        return None

def scrape(link_url: str):
    pokemon_data_links = scrape_pokemon_links(link_url)
    for link in pokemon_data_links:
        data = scrape_pokemon_data(link)
        with open(f"""pages/{data.title.text.split()[0]}.html""", 'w+') as file:
            print("Saving html document")
            file.write(data.prettify())
        wait_time = randint(2, 10)
        print("Politely waiting.. " + str(wait_time) + "seconds")
        sleep(wait_time)


if __name__ == '__main__':
    scrape("/wiki/Category:Pok%C3%A9mon_in_the_Kanto_Pok%C3%A9dex")

