from mysql import *
from mysql.connector import pooling
import sys


class Conexion:
    _DATABASE = 'bqifo1pz07m1cxqswphy'
    _USERNAME = 'uqqvf5c2n9ccrnrv'
    _PASSWORD = '2dMBMtkM5AiuIEL4udm'
    _DB_PORT = '21374'
    _HOST = 'bqifo1pz07m1cxqswphy-mysql.services.clever-cloud.com'
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                #Aqui estaba el error faltaba un .
                cls._pool = pooling.MySQLConnectionPool(pool_name='mypool',
                                                       pool_size=cls._MAX_CON,
                                                       host=cls._HOST,
                                                       user=cls._USERNAME,
                                                       password=cls._PASSWORD,
                                                       port=cls._DB_PORT,
                                                       database=cls._DATABASE)
                #log.debug(f'Creación del pool exitoso: {cls._pool}')
                return cls._pool
            except Exception as e:
                #log.error(f'Ocurrio un problema al obtener el pool de conexiones {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_connection()
        #log.debug(f'Conexión establecida exitosamente: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        conexion.close()
        #log.debug(f'Liberando la conexión exitosamente: {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        