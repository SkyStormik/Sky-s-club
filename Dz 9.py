import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, currency_url):
        self.currency_url = currency_url
        self.rates = {}
    def get_exchange_rates(self):
        try:
            response = requests.get(self.currency_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            dollar_rate = soup.find('div', class_='dollar-rate').text.strip()
            self.rates['USD'] = float(dollar_rate.replace(',', '.'))
        except Exception as e:
            print(f"Помилка при отриманні курсу валюти: {e}")
    def convert_to_usd(self, amount, currency):
        if currency in self.rates:
            return amount / self.rates[currency]
        else:
            print(f"Курс для валюти {currency} не знайдений.")
            return None
currency_url = 'https://www.google.com/finance/quote/USD-UAH'
converter = CurrencyConverter(currency_url)
converter.get_exchange_rates()
amount = float(input("Введіть кількість валюти: "))
currency = input("Введіть код валюти (наприклад, UAH): ")
converted_amount = converter.convert_to_usd(amount, currency)
if converted_amount is not None:
    print(f"{amount} {currency} = {converted_amount:.2f} USD")
