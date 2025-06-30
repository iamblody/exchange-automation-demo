import requests
from bs4 import BeautifulSoup

def fetch_exchange_rates(currency_codes=None):
    if currency_codes is None:
        currency_codes = ["USD", "EUR", "GBP"]

    try:
        url = "https://www.tcmb.gov.tr/kurlar/today.xml"
        response = requests.get(url)
        response.encoding = "utf-8"

        soup = BeautifulSoup(response.content, "lxml-xml")

        data = []
        for code in currency_codes:
            currency = soup.find("Currency", {"CurrencyCode": code})
            if currency:
                name = currency.find("Isim").text
                buy = currency.find("ForexBuying").text
                sell = currency.find("ForexSelling").text
                data.append([name, buy, sell])

        return data

    except Exception as e:
        print(f"[ERROR] Failed to fetch exchange data: {e}")
        return []
