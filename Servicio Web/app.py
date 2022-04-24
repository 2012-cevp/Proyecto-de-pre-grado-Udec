from concurrent.futures import thread
from flask import Flask, render_template
from graficos import grafico_precios
from conexion_insertar import Transacciones
#from insertar_datos_menu import *
from flask_caching import Cache
import threading

app = Flask(__name__)


#hilo_hora = threading.Thread(target = hora, args = (3600,))
#hilo_hora.start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bitcoin')
def bitcoin():
    #while True:
    precios_btc, fechas_btc, prediccion_btc = Transacciones.seleccionar_btc()
    graf_btc = grafico_precios('Bitcoin', '\u20bf', fechas_btc, precios_btc, prediccion_btc)
        #hilo_grafico = threading.Thread(target=grafico_precios, args=('Bitcoin', '\u20bf', fechas_btc, precios_btc, prediccion_btc, ))
    #img_url = 'static/images/Bitcoin.svg?cache='
    return render_template('bitcoin.html', image_url = graf_btc)


@app.route('/dolar')
def dolar():
    #while True:
    precios_usd, fechas_usd, prediccion_usd = Transacciones.seleccionar_usd()
    graf_usd = grafico_precios('Dolar', '\u0024', fechas_usd, precios_usd, prediccion_usd)
    #img_url = 'static/images/Dolar.svg?cache='
    return render_template('dolar.html', image_url1 = graf_usd)
 
    
@app.route('/euro')
def euro():
    #while True:
    precios_eur, fechas_eur, prediccion_euro = Transacciones.seleccionar_eur()
    graf_eur = grafico_precios('Euro', '\u20ac', fechas_eur, precios_eur, prediccion_euro)
    #img_url = 'static/images/Euro.svg?cache=' 
    return render_template('euro.html', image_url2 = graf_eur)


'''  
hilo_btc = threading.Thread(target=demora_btc, args=(3600,))
hilo_btc.start()

time.sleep(10)

hilo_usd = threading.Thread(target=demora_usd, args=(3900,))
hilo_usd.start()

time.sleep(15)

hilo_eur = threading.Thread(target=demora_eur, args=(3900,))
hilo_eur.start()
'''

app.run(debug = True)

