from concurrent.futures import thread
from flask import Flask, render_template
from graficos import grafico_precios
from conexion_insertar import Transacciones
from insertar_datos_menu import *

app = Flask(__name__)


@app.route('/')
def home():
    #Precios Tabla BTC
    precios_btc, fechas_btc, prediccion_btc, prediccion_sig_btc = Transacciones.seleccionar_btc()
    precio_btc = precios_btc[-1]
    prediccion_b = prediccion_btc[-1]
    
    #Precios Tabla USD
    precios_usd, fechas_usd, prediccion_usd, prediccion_sig_usd = Transacciones.seleccionar_usd()
    precio = precios_usd[-1]
    prediccion_u = prediccion_usd[-1]
    
    #Precios Tabla EUR
    precios_eur, fechas_eur, prediccion_euro, prediccion_sig_eur = Transacciones.seleccionar_eur()
    precio_eur = precios_eur[-1]
    prediccion_e = prediccion_euro[-1]
    
    return render_template('Index.html', precio_btc = precio_btc, prediccion_btc = prediccion_b, precio_usd = precio, prediccion_usd = prediccion_u, precio_eur = precio_eur, prediccion_eur = prediccion_e)

@app.route('/bitcoin')
def bitcoin():

    precios_btc, fechas_btc, prediccion_btc, prediccion_siguiente_btc = Transacciones.seleccionar_btc()
    graf_btc = grafico_precios('Bitcoin', '\u20bf', fechas_btc, precios_btc, prediccion_btc)

    precio = precios_btc[-1]
    prediccion = prediccion_btc[-1]
    prediccion_siguiente = prediccion_siguiente_btc[-1]
    
    return render_template('Bitcoin.html', image_url = graf_btc, precio = precio, prediccion = prediccion, prediccion_sig = prediccion_siguiente)


@app.route('/dolar')
def dolar():
    precios_usd, fechas_usd, prediccion_usd, prediccion_sig_usd = Transacciones.seleccionar_usd()
    graf_usd = grafico_precios('Dolar', '\u0024', fechas_usd, precios_usd, prediccion_usd)
    
    precio = precios_usd[-1]
    prediccion = prediccion_usd[-1]
    prediccion_siguiente = prediccion_sig_usd[-1]
    
    return render_template('dolar.html', image_url1 = graf_usd, precio = precio, prediccion = prediccion, prediccion_sig = prediccion_siguiente)
 
    
@app.route('/euro')
def euro():
   
    precios_eur, fechas_eur, prediccion_euro, prediccion_sig_eur = Transacciones.seleccionar_eur()
    graf_eur = grafico_precios('Euro', '\u20ac', fechas_eur, precios_eur, prediccion_euro)
    
    precio = precios_eur[-1]
    prediccion = prediccion_euro[-1]
    prediccion_siguiente = prediccion_sig_eur[-1]
    return render_template('euro.html', image_url2 = graf_eur, precio = precio, prediccion = prediccion, prediccion_sig = prediccion_siguiente)

@app.route('/aboutus')
def aboutus():
    return render_template('about us.html')

@app.route('/aboutpro')
def aboutpro():
    return render_template('about pro.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

app.run(port = 5001)

