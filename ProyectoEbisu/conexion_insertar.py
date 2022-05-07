from cursor_pool import CursorDelPool
class Transacciones():
    
    
    _INSERTAR_BTC = f'INSERT INTO bitcoin (`Fecha`, `Precio`, `Prediccion`,`Prediccion_sig`)  VALUES (%s, %s, %s, %s)'
    _INSERTAR_USD = 'INSERT INTO dolar (`Fecha`, `Precio`, `Prediccion`, `Prediccion_sig`)  VALUES (%s, %s, %s, %s)'
    _INSERTAR_EUR = 'INSERT INTO euro (`Fecha`, `Precio`, `Prediccion`, `Prediccion_sig`)  VALUES (%s, %s, %s, %s)'
    
    #_SELECT_BTC = f'SELECT * FROM moneda.bitcoin ORDER BY idbitcoin LIMIT 2'
    _SELECT_BTC = f'SELECT DATE_FORMAT(Fecha, "%Y-%m-%d %H:%i:%S"), Precio, Prediccion, Prediccion_sig FROM bitcoin ORDER BY idbitcoin DESC LIMIT 4'
    _SELECT_USD = f'SELECT DATE_FORMAT(Fecha, "%Y-%m-%d"), Precio, Prediccion, Prediccion_sig FROM dolar ORDER BY iddolar DESC LIMIT 5'
    _SELECT_EUR = f'SELECT DATE_FORMAT(Fecha, "%Y-%m-%d"), Precio, Prediccion, Prediccion_sig FROM euro ORDER BY ideuro DESC LIMIT 4'
    
    @classmethod
    def insertar_btc(cls, Fecha, Precio, Prediccion, Prediccion_sig):
        with CursorDelPool() as cursor:
            valores = (Fecha, Precio, Prediccion, Prediccion_sig)
            cursor.execute(cls._INSERTAR_BTC, valores)
            return cursor.rowcount
        
    @classmethod
    def insertar_usd(cls, Fecha, Precio, Prediccion, Prediccion_sig):
        with CursorDelPool() as cursor:
            valores = (Fecha, Precio, Prediccion, Prediccion_sig)
            cursor.execute(cls._INSERTAR_USD, valores)
            return cursor.rowcount
    
    @classmethod
    def insertar_eur(cls, Fecha, Precio, Prediccion, Prediccion_sig):
        with CursorDelPool() as cursor:
            valores = (Fecha, Precio, Prediccion, Prediccion_sig)
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
            prediccion_siguiente_btc = []
            for registro in registros:
                fecha = registro[0]
                precio = registro[1]
                prediccion = registro[2]
                prediccion_sig_btc = registro[3]
                precios.append(precio)
                fechas.append(fecha)
                prediccion_bitcoin.append(prediccion)
                prediccion_siguiente_btc.append(prediccion_sig_btc)
            return list(reversed(precios)), list(reversed(fechas)), list(reversed(prediccion_bitcoin)), list(reversed(prediccion_siguiente_btc))
        
        
    @classmethod
    def seleccionar_usd(cls):
        with CursorDelPool() as cursor:
            
            cursor.execute(cls._SELECT_USD)
            registros = cursor.fetchall()
            precios_dolar = []
            fechas_dolar = []
            prediccion_dolar = []
            prediccion_siguiente_dolar = []
            for registro in registros:
                fecha = registro[0]
                precio = registro[1]
                prediccion = registro[2]
                prediccion_sig_usd = registro[3]
                precios_dolar.append(precio)
                fechas_dolar.append(fecha)
                prediccion_dolar.append(prediccion)
                prediccion_siguiente_dolar.append(prediccion_sig_usd)
            return list(reversed(precios_dolar)), list(reversed(fechas_dolar)), list(reversed(prediccion_dolar)), list(reversed(prediccion_siguiente_dolar))
        
    @classmethod
    def seleccionar_eur(cls):
        with CursorDelPool() as cursor:
            
            cursor.execute(cls._SELECT_EUR)
            registros = cursor.fetchall()
            precios_euro = []
            fechas_euro = []
            prediccion_euro = []
            prediccion_siguiente_euro = []
            for registro in registros:
                fecha = registro[0]
                precio = registro[1]
                prediccion = registro[2]
                pred_sig_eur = registro[3]
                precios_euro.append(precio)
                fechas_euro.append(fecha)
                prediccion_euro.append(prediccion)
                prediccion_siguiente_euro.append(pred_sig_eur)
            return list(reversed(precios_euro)), list(reversed(fechas_euro)), list(reversed(prediccion_euro)), list(reversed(prediccion_siguiente_euro))
