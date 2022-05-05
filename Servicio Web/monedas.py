import requests
from bs4 import BeautifulSoup
class Monedas_Peticiones():
    
    def precio_btc():
        url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1'
        r = requests.get(url)
        data = r.json()
        precio_btc = data[0:3][0]
        precio_hora = float(precio_btc[1])
        return precio_hora

    def precio_dolar():
        url = "https://au.investing.com/currencies/usd-cop"
        
        # Ejecutar GET-Request - LA RESPUESTA DEBE SER 200 OK ó [200]
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        #Precio del dolar
        precio_usd = html.find('span', {'data-test':"instrument-price-last"}).text.strip()
        precio_usd = precio_usd.replace(',', '')
        precio_usd = float(precio_usd)
        return precio_usd

    def precio_euro():
        url = "https://au.investing.com/currencies/eur-cop"
        response = requests.get(url)
        html = BeautifulSoup(response.text, 'html.parser')
        #precio EURO
        precio_eur = html.find('span', {'data-test':'instrument-price-last'}).text.strip()
        precio_eur = precio_eur.replace(',', '')
        precio_eur = float(precio_eur)
        return precio_eur