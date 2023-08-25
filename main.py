import requests
from bs4 import BeautifulSoup
import time

URL = 'https://kuna.io/trade/BTC_UAH'
REFRESH_INTERVAL = 300  # 5 minutes

def get_crypto_prices(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        crypto_prices = {}

        crypto_elements = soup.find_all('div', class_='coin-info')
        for crypto_element in crypto_elements:
            crypto_name = crypto_element.find('span', class_='coin-symbol').text.strip()
            crypto_price = crypto_element.find('span', class_='price').text.strip()
            crypto_prices[crypto_name] = crypto_price

        return crypto_prices

    print('Failed to fetch data')
    return None

def print_crypto_prices(prices):
    if prices:
        print("Crypto Prices:")
        for crypto, price in prices.items():
            print(f"{crypto}: {price}")
    else:
        print("Failed to fetch prices")

if __name__ == "__main__":
    while True:
        prices = get_crypto_prices(URL)
        print_crypto_prices(prices)
        time.sleep(REFRESH_INTERVAL)
