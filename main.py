import requests
from bs4 import BeautifulSoup
import time


def get_crypto_prices():
    url = 'https://kuna.io/trade/BTC_UAH'
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
    else:
        print('Failed to fetch data')
        return None


if __name__ == "__main__":
    while True:
        prices = get_crypto_prices()
        if prices:
            print("Crypto Prices:")
            for crypto, price in prices.items():
                print(f"{crypto}: {price}")
        else:
            print("Failed to fetch prices")

        # Обновление цен каждые 5 минут
        time.sleep(300)
