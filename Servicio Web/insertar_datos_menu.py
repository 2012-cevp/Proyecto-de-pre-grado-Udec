import time
import threading
import datetime
from monedas import Monedas_Peticiones
from conexion_insertar import Transacciones

def hora(segundos):
    while True:
        #Definiendo la hora de inserción de los datos
        #hora = datetime.datetime.now()
        #los formatos para el Dolar y el Euro estan en [año - mes - día]      
        # y para el Bitcoin en formato [Año-mes-día Hora:minuto:segundo]
        hora_dol_eur = datetime.datetime.now().strftime('%Y-%m-%d')
        hora_btc = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return hora_dol_eur, hora_btc
        time.sleep(segundos)

def demora_btc(segundos):
    while True:
        btc = Monedas_Peticiones.precio_btc()
        prediccion_btc = btc+1.50
        insertando_btc = Transacciones.insertar_btc(hora(None)[1], btc, prediccion_btc)
        print(f'El valor del Bitcoin es: {btc} y la hora es: {hora(None)[1]}')
        print(type(btc))
        print(type(prediccion_btc))
        time.sleep(segundos)

def demora_usd(segundos):
        while True:
            usd = Monedas_Peticiones.precio_dolar()
            print(f'El valor del dolar es: {usd}')
            prediccion_usd = usd+50.21
            insertando_dolar = Transacciones.insertar_usd(hora(None)[0], usd, prediccion_usd)
            time.sleep(segundos)

def demora_eur(segundos):
    while True:
        eur = Monedas_Peticiones.precio_euro()
        print(f'El valor del euro es: {eur}')
        prediccion_eur = eur+40.21
        insertando_dolar = Transacciones.insertar_eur(hora(None)[0], eur, prediccion_eur)
        time.sleep(segundos)



# Aqui creamos el hilo.
# El primer argumento es el nombre de la funcion que contiene el codigo.
# El segundo argumento es una lista de argumentos para esa funcion, es importante poner una , al fin ya que asume una lista de argumentos (siempre debe quedar así)
if __name__ == '__main__':
    
    hilo_hora = threading.Thread(target = hora, args = (3600,))
    hilo_btc = threading.Thread(target=demora_btc, args=(3600,))
    hilo_usd = threading.Thread(target=demora_usd, args=(3900,))
    hilo_eur = threading.Thread(target=demora_eur, args=(3900,))

    #Iniciando el hilo que queremos ejecutar
    hilo_hora.start()
    hilo_btc.start()
    hilo_usd.start()
    hilo_eur.start()

