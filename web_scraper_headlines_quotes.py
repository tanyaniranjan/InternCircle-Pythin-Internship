import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("HEADLINES / QUOTES")
    print("-" * 40)

    quotes = soup.find_all("span", class_="text")

    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote.get_text(strip=True)}")

else:
    print("Failed to fetch the webpage.")
