import requests
from bs4 import BeautifulSoup

url = "https://yfapi.net/v6/finance/quote"
query_usd = {"symbols": "USDCOP=X"}
query_eur = {"symbols":"EURCOP=X"}


headers = {'x-api-key': "3murJ8zwSm4D4nklwZRi72y8J9JO7i2771GKsBJY"}


class Monedas_Peticiones():

    def precio_btc():
        url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1'
        r = requests.get(url)
        data = r.json()
        precio_btc = data[0:3][0]
        precio_hora = float(precio_btc[1])
        return precio_hora

    def precio_dolar():
        response = requests.request("GET", url, headers=headers, params=query_usd)
        json_response = response.json()
        for i in json_response['quoteResponse']['result']:
            precio_usd = i['regularMarketPrice']
        return precio_usd

    def precio_euro():
        response = requests.request("GET", url, headers=headers, params=query_eur)
        json_response = response.json()
        for i in json_response['quoteResponse']['result']:
            precio_eur = i['regularMarketPrice']
        return precio_eur

print(Monedas_Peticiones.precio_euro())
print(Monedas_Peticiones.precio_btc())
print(Monedas_Peticiones.precio_dolar())