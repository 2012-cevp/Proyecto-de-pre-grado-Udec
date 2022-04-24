from audioop import reverse
from logging import exception
from cursor_pool import CursorDelPool
class Transacciones():
    
    
    _INSERTAR_BTC = f'INSERT INTO bitcoin (`Fecha`, `Precio`, `Prediccion`)  VALUES (%s, %s, %s)'
    _INSERTAR_USD = 'INSERT INTO dolar (`Fecha`, `Precio`, `Prediccion`)  VALUES (%s, %s, %s)'
    _INSERTAR_EUR = 'INSERT INTO euro (`Fecha`, `Precio`, `Prediccion`)  VALUES (%s, %s, %s)'
    
    #_SELECT_BTC = f'SELECT * FROM moneda.bitcoin ORDER BY idbitcoin LIMIT 2'
    _SELECT_BTC = f'SELECT DATE_FORMAT(Fecha, "%Y-%m-%d %H:%i:%S"), Precio, Prediccion FROM bitcoin ORDER BY idbitcoin DESC LIMIT 4'
    _SELECT_USD = f'SELECT DATE_FORMAT(Fecha, "%Y-%m-%d"), Precio, Prediccion FROM dolar ORDER BY iddolar DESC LIMIT 4'
    _SELECT_EUR = f'SELECT DATE_FORMAT(Fecha, "%Y-%m-%d"), Precio, Prediccion FROM euro ORDER BY ideuro DESC LIMIT 4'
    
    @classmethod
    def insertar_btc(cls, Fecha, Precio, Prediccion):
        with CursorDelPool() as cursor:
            valores = (Fecha, Precio, Prediccion)
            cursor.execute(cls._INSERTAR_BTC, valores)
            return cursor.rowcount
        
    @classmethod
    def insertar_usd(cls, Fecha, Precio, Prediccion):
        with CursorDelPool() as cursor:
            valores = (Fecha, Precio, Prediccion)
            cursor.execute(cls._INSERTAR_USD, valores)
            return cursor.rowcount
    
    @classmethod
    def insertar_eur(cls, Fecha, Precio, Prediccion):
        with CursorDelPool() as cursor:
            valores = (Fecha, Precio, Prediccion)
            cursor.execute(cls._INSERTAR_EUR, valores)
            return cursor.rowcount
    
    @classmethod
    def seleccionar_btc(cls):
        with CursorDelPool() as cursor:
            
            cursor.execute(cls._SELECT_BTC)
            registros = cursor.fetchall()
            precios = []
            fechas = []
            prediccion_bitcoin = []
            for registro in registros:
                fecha = registro[0]
                precio = registro[1]
                prediccion = registro[2]
                precios.append(precio)
                fechas.append(fecha)
                prediccion_bitcoin.append(prediccion)
            return list(reversed(precios)), list(reversed(fechas)), list(reversed(prediccion_bitcoin))
        
        
    @classmethod
    def seleccionar_usd(cls):
        with CursorDelPool() as cursor:
            
            cursor.execute(cls._SELECT_USD)
            registros = cursor.fetchall()
            precios_dolar = []
            fechas_dolar = []
            prediccion_dolar = []
            for registro in registros:
                fecha = registro[0]
                precio = registro[1]
                prediccion = registro[2]
                precios_dolar.append(precio)
                fechas_dolar.append(fecha)
                prediccion_dolar.append(prediccion)
            return list(reversed(precios_dolar)), list(reversed(fechas_dolar)), list(reversed(prediccion_dolar))
        
    @classmethod
    def seleccionar_eur(cls):
        with CursorDelPool() as cursor:
            
            cursor.execute(cls._SELECT_EUR)
            registros = cursor.fetchall()
            precios_euro = []
            fechas_euro = []
            prediccion_euro = []
            for registro in registros:
                fecha = registro[0]
                precio = registro[1]
                prediccion = registro[2]
                precios_euro.append(precio)
                fechas_euro.append(fecha)
                prediccion_euro.append(prediccion)
            return list(reversed(precios_euro)), list(reversed(fechas_euro)), list(reversed(prediccion_euro))

if __name__ == '__main__':
    
    valor = Transacciones.seleccionar_btc()
    print(valor)
    
    
'''  
    valores = Transacciones.seleccionar_btc()[0]
    fechas = Transacciones.seleccionar_btc()[1]
    #valores = list(reversed(valores))
    print(valores)
    print(fechas)
    print(type(fechas))

'''
      