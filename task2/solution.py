import requests
from bs4 import BeautifulSoup

BASE_URL = "https://ru.wikipedia.org"
START_URL = "/wiki/Категория:Животные_по_алфавиту"


def parse_page(url):
    response = requests.get(f'{BASE_URL}{url}')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    next_url = None
    link = soup.find('a', string='Следующая страница')
    if link:
        next_url = link.attrs.get('href')
    result = {}
    for group in soup.select("#mw-pages .mw-category-group"):
        letter = group.find("h3").text.strip()
        items = group.select("ul li a")
        count = len(items)
        result[letter] = result.get(letter, 0) + count
    return next_url, result


def get_animals():
    total = {}
    url = START_URL
    while url:
        next_url, result = parse_page(url)
        for letter, count in result.items():
            total[letter] = total.get(letter, 0) + count
        url = next_url
    return total


stats = get_animals()
with open("beasts.csv", "w", encoding="UTF-8") as file_out:
    for k, v in stats.items():
        file_out.write(f"{k},{v}\n")
