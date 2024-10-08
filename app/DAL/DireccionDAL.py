import mysql.connector
from mysql.connector import Error

class DireccionDAL:
    def __init__(self, db):
        self.db = db

    def agregarDireccion(self, direccion):
        """Agrega una nueva dirección a la base de datos."""
        try:
            cursor = self.db.cursor()
            query = """
                INSERT INTO direccion (ID_direccion, ID_cliente, direccion_Linea1, Ciudad, Pais)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (direccion.idDireccion, direccion.idCliente, direccion.direccionLinea1, direccion.ciudad, direccion.pais)
            cursor.execute(query, valores)
            self.db.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al agregar dirección: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()

    def obtenerDireccionesPorCliente(self, idCliente):
        """Obtiene todas las direcciones asociadas a un cliente."""
        try:
            cursor = self.db.cursor()
            query = "SELECT ID_direccion, ID_cliente, direccion_Linea1, Ciudad, Pais FROM direccion WHERE ID_cliente = %s"
            cursor.execute(query, (idCliente,))
            resultados = cursor.fetchall()
            direcciones = []
            for resultado in resultados:
                direccion = {
                    'idDireccion': resultado[0],
                    'idCliente': resultado[1],
                    'direccionLinea1': resultado[2],
                    'ciudad': resultado[3],
                    'pais': resultado[4]
                }
                direcciones.append(direccion)
            return direcciones
        except Error as e:
            print(f"Error al obtener direcciones: {e}")
            return None
        finally:
            cursor.close()

    def actualizarDireccion(self, direccion):
        """Actualiza una dirección en la base de datos."""
        try:
            cursor = self.db.cursor()
            query = """
                UPDATE direccion 
                SET direccion_Linea1 = %s, Ciudad = %s, Pais = %s 
                WHERE ID_direccion = %s AND ID_cliente = %s
            """
            valores = (direccion.direccionLinea1, direccion.ciudad, direccion.pais, direccion.idDireccion, direccion.idCliente)
            cursor.execute(query, valores)
            self.db.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error al actualizar dirección: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()

    def eliminarDireccion(self, idDireccion):
        """Elimina una dirección de la base de datos."""
        try:
            cursor = self.db.cursor()
            query = "DELETE FROM direccion WHERE ID_direccion = %s"
            cursor.execute(query, (idDireccion,))
            self.db.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error al eliminar dirección: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()
