import mysql.connector
from mysql.connector import Error

class ClienteDAL:
    def __init__(self, db):
        self.db = db

    def registrarCliente(self, cliente):
        """Registra un nuevo cliente en la base de datos."""
        try:
            cursor = self.db.cursor()
            query = """
                INSERT INTO cliente (ID_cliente, Nombre, Apellido, Correo, contrasena, Telefono)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            valores = (cliente.idCliente, cliente.nombre, cliente.apellido, cliente.email, cliente.password, cliente.telefono)
            cursor.execute(query, valores)
            self.db.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error al registrar cliente: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()

    def obtenerClientePorID(self, idCliente):
        """Obtiene un cliente por su ID."""
        try:
            cursor = self.db.cursor()
            query = "SELECT ID_cliente, Nombre, Apellido, Correo, Telefono, Fecha_Registro FROM cliente WHERE ID_cliente = %s"
            cursor.execute(query, (idCliente,))
            resultado = cursor.fetchone()
            if resultado:
                return {
                    'idCliente': resultado[0],
                    'nombre': resultado[1],
                    'apellido': resultado[2],
                    'email': resultado[3],
                    'telefono': resultado[4],
                    'fechaRegistro': resultado[5]
                }
            else:
                return None
        except Error as e:
            print(f"Error al obtener cliente: {e}")
            return None
        finally:
            cursor.close()

    def actualizarCliente(self, cliente):
        """Actualiza los datos de un cliente en la base de datos."""
        try:
            cursor = self.db.cursor()
            query = """
                UPDATE cliente 
                SET Nombre = %s, Apellido = %s, Correo = %s, Telefono = %s 
                WHERE ID_cliente = %s
            """
            valores = (cliente.nombre, cliente.apellido, cliente.email, cliente.telefono, cliente.idCliente)
            cursor.execute(query, valores)
            self.db.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error al actualizar cliente: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()

    def eliminarCliente(self, idCliente):
        """Elimina un cliente de la base de datos."""
        try:
            cursor = self.db.cursor()
            query = "DELETE FROM cliente WHERE ID_cliente = %s"
            cursor.execute(query, (idCliente,))
            self.db.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error al eliminar cliente: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()
