import pickle
from keras.models import load_model
import numpy as np 
from conexion_insertar import Transacciones



def load_object(filename):
    with open(''+filename ,'rb') as f:
         loaded = pickle.load(f)
    return loaded


def modeloBitcoin():
    loaded_scaler = load_object('Escalador_bitcoin.pkl')
    modelo_btc = load_model('Modelo Bitcoin LSTM.h5')
    return loaded_scaler, modelo_btc

def modeloEuro():
    load_scaler_eur = load_object('Escalador_euro.pkl')
    modelo_eur = load_model('Modelo_euro.h5')
    return load_scaler_eur, modelo_eur
    
def modeloDolar():
    load_scaler_dol = load_object('Escalador_dolar.pkl')

    modelo_dol = load_model('Modelo_dolar.h5')
    return load_scaler_dol, modelo_dol


if __name__ == '__main__':
    escalador, modelo = modeloDolar()
    valores = Transacciones.seleccionar_usd()[0]
    print(valores)
    usd = 4050
    valores.append(usd)
    valores = valores[1:]
    print(valores)
    valores = np.reshape(valores, (-1,1))
    valor_escalado = escalador.fit_transform(valores)
    valor_escalado = valor_escalado.reshape(1, len(valores), 1)
    print(valor_escalado)
    prediccion = modelo.predict(valor_escalado)
    prediccion_desescalada = escalador.inverse_transform(prediccion)
    prediccion_def = round(int(prediccion_desescalada),2)
    print(f'El valor predecido es: {prediccion_def}, tipo de dato: {type(prediccion_def)}')