from conexion_bd import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        try:
            self._conexion = Conexion.obtenerConexion()
            self._cursor = self._conexion.cursor()
            return self._cursor
        except Exception as e:
            print(f'Error al conectarse {e}')

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        if valor_excepcion:
            self._conexion.rollback()
            print(f'Ocurrió una excepción, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)