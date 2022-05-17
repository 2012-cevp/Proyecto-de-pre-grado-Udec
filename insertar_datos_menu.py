import time
import threading
import datetime
from monedas import Monedas_Peticiones
from conexion_insertar import Transacciones
from modelos import modeloBitcoin, modeloEuro, modeloDolar
import numpy as np

# Traemos el escalador y la carga del modelo del bitcoin, esto a traves de la instancia a la clase de modeloBitcoin()
escalador_btc, modelo_btc = modeloBitcoin()
escalador_euro, modelo_euro = modeloEuro()
escalador_dolar, modelo_dolar = modeloDolar()

def hora(segundos):
    while True:
        # Definiendo la hora de inserción de los datos
        #hora = datetime.datetime.now()
        # los formatos para el Dolar y el Euro estan en [año - mes - día]
        # y para el Bitcoin en formato [Año-mes-día Hora:minuto:segundo]
        hora_dol_eur = datetime.datetime.now().strftime('%Y-%m-%d')
        hora_btc = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return hora_dol_eur, hora_btc
        time.sleep(segundos)


def demora_btc(segundos):
    while True:
        # Hacemos el web scraping para el valor del bitcoin
        btc = Monedas_Peticiones.precio_btc()
        # Traigo los valores, como en este caso se retornan varios elementos, entonces le dire que solo me traiga el primer valor del return
        valores = Transacciones.seleccionar_btc()[0]

        # Reasginamos las dimensiones de la lista que tenemos en valores
        valores = np.reshape(valores, (-1, 1))
        valores = escalador_btc.fit_transform(valores)
        valores = valores.reshape(1, len(valores), 1)

        prediccion = modelo_btc.predict(valores)
        prediccion_desescalada = escalador_btc.inverse_transform(prediccion)
        prediccion_btc = round(float(prediccion_desescalada), 2)

        # Prediccion siguiente hora
        val_siguiente = Transacciones.seleccionar_btc()[0]
        val_siguiente.append(btc)
        val_siguiente = val_siguiente[1:]

        val_siguiente = np.reshape(val_siguiente, (-1, 1))
        valor_escalado = escalador_btc.fit_transform(val_siguiente)
        valor_escalado = valor_escalado.reshape(1, len(val_siguiente), 1)

        prediccion_sig = modelo_btc.predict(valor_escalado)
        prediccion_desescalada_sig = escalador_btc.inverse_transform(
            prediccion_sig)
        prediccion_def_sig = round(int(prediccion_desescalada_sig), 2)

        # Insertamos nuestras datos, en este caso traigo la hora, pero como no quiero que tenga un tiempo de pausa, simplemente
        # le pasamos el parametro None, como tambien se quiere tener la hora para el bitcoin entonces se trae la posición[1] del return que es hora_btc
        insertando_btc = Transacciones.insertar_btc(
            hora(None)[1], btc, prediccion_btc, prediccion_def_sig)
        time.sleep(segundos)



def demora_usd(segundos):
        while True:
            usd = Monedas_Peticiones.precio_dolar()
            valores_usd = Transacciones.seleccionar_usd()[0]
            valores_usd = np.reshape(valores_usd, (-1,1))
            valores_usd = escalador_dolar.fit_transform(valores_usd)
            valores_usd = valores_usd.reshape(1, len(valores_usd),1)
            
            #PREDICCION USD
            prediccion_usd = modelo_dolar.predict(valores_usd)
            prediccion_desescalada_usd = escalador_dolar.inverse_transform(prediccion_usd)
            prediccion_usd = round(float(prediccion_desescalada_usd), 2)
            
            #PREDICCIÓN SIGUIENTE DIA
            val_siguiente = Transacciones.seleccionar_usd()[0]
            val_siguiente.append(usd)
            val_siguiente = val_siguiente[1:]
            val_siguiente = np.reshape(val_siguiente, (-1,1))
            
            valor_escalado = escalador_dolar.fit_transform(val_siguiente)
            valor_escalado = valor_escalado.reshape(1, len(val_siguiente), 1)
            prediccion_sig = modelo_dolar.predict(valor_escalado)
            prediccion_desescalada_sig = escalador_dolar.inverse_transform(prediccion_sig)
            prediccion_def_sig = round(float(prediccion_desescalada_sig), 2)

            insertando_dolar = Transacciones.insertar_usd(hora(None)[0], usd, prediccion_usd, prediccion_def_sig)
            time.sleep(segundos)



def demora_eur(segundos):
    while True:
        eur = Monedas_Peticiones.precio_euro()
        valores_eur = Transacciones.seleccionar_eur()[0]
        # Reasginamos las dimensiones de la lista que tenemos en valores
        valores_eur = np.reshape(valores_eur, (-1, 1))
        valores_eur = escalador_euro.fit_transform(valores_eur)
        valores_eur = valores_eur.reshape(1, len(valores_eur), 1)
        # Prediccion EUR
        prediccion_eur = modelo_euro.predict(valores_eur)
        prediccion_desescalada_eur = escalador_euro.inverse_transform(prediccion_eur)
        prediccion_eur = round(float(prediccion_desescalada_eur), 2)

        # Prediccion siguiente dia
        val_siguiente = Transacciones.seleccionar_eur()[0]
        val_siguiente.append(eur)
        val_siguiente = val_siguiente[1:]

        val_siguiente = np.reshape(val_siguiente, (-1, 1))
        valor_escalado = escalador_euro.fit_transform(val_siguiente)
        valor_escalado = valor_escalado.reshape(1, len(val_siguiente), 1)

        prediccion_sig = modelo_euro.predict(valor_escalado)
        prediccion_desescalada_sig = escalador_euro.inverse_transform( prediccion_sig)
        prediccion_def_sig = round(float(prediccion_desescalada_sig), 2)

        insertando_eur = Transacciones.insertar_eur(hora(None)[0], eur, prediccion_eur, prediccion_def_sig)
        time.sleep(segundos)


# Aqui creamos el hilo.
# El primer argumento es el nombre de la funcion que contiene el codigo.
# El segundo argumento es una lista de argumentos para esa funcion, es importante poner una , al fin ya que asume una lista de argumentos (siempre debe quedar así)

hilo_hora = threading.Thread(target=hora, args=(3600,))
hilo_btc = threading.Thread(target=demora_btc, args=(3600,))
hilo_usd = threading.Thread(target=demora_usd, args=(3900,))
hilo_eur = threading.Thread(target=demora_eur, args=(3900,))

# Iniciando el hilo que queremos ejecutar
hilo_hora.start()
hilo_btc.start()
hilo_usd.start()
hilo_eur.start()
