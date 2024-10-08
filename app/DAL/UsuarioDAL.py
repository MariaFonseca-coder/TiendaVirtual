import mysql.connector
from mysql.connector import Error

class UsuarioDAL:
    def __init__(self, db):
        self.db = db

    def obtenerUsuarioPorID(self, userID):
        try:
            cursor = self.db.cursor()
            query = "SELECT ID_Usuario, Nombre_Usuario, contrasena, Rol, Fecha_Creacion FROM usuario WHERE ID_Usuario = %s"
            cursor.execute(query, (userID,))
            resultado = cursor.fetchone()  # Obtener un solo resultado
            if resultado:
                return {
                    'ID_Usuario': resultado[0],
                    'Nombre_Usuario': resultado[1],
                    'contrasena': resultado[2],
                    'Rol': resultado[3],
                    'Fecha_Creacion': resultado[4]
                }
            else:
                return None
        except Error as e:
            print(f"Error al obtener usuario: {e}")
            return None
        finally:
            cursor.close()

    def obtenerUsuarioPorUsername(self, username):
        try:
            cursor = self.db.cursor()
            query = "SELECT ID_Usuario, Nombre_Usuario, contrasena, Rol, Fecha_Creacion FROM usuario WHERE Nombre_Usuario = %s"
            cursor.execute(query, (username,))
            resultado = cursor.fetchone()  # Obtener un solo resultado
            if resultado:
                return {
                    'ID_Usuario': resultado[0],
                    'Nombre_Usuario': resultado[1],
                    'contrasena': resultado[2],
                    'Rol': resultado[3],
                    'Fecha_Creacion': resultado[4]
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None
        finally:
            cursor.close()

    def crearUsuario(self, usuario):
        try:
            cursor = self.db.cursor()
            query = "INSERT INTO usuario (ID_Usuario, Nombre_Usuario, contrasena, Rol) VALUES (%s, %s, %s, %s)"
            valores = (usuario.userID, usuario.username, usuario.password, usuario.role)
            cursor.execute(query, valores)
            self.db.commit()  # Confirma la transacción
            return cursor.lastrowid  # Devuelve el ID del usuario creado
        except Error as e:
            print(f"Error al crear usuario: {e}")
            self.db.rollback()  # Revierte la transacción en caso de error
            return None
        finally:
            cursor.close()

    def editarUsuario(self, usuario):
        try:
            cursor = self.db.cursor()
            query = """
                UPDATE usuario 
                SET Nombre_Usuario = %s, contrasena = %s, Rol = %s 
                WHERE ID_Usuario = %s
            """
            valores = (usuario.username, usuario.password, usuario.role, usuario.userID)
            cursor.execute(query, valores)
            self.db.commit()  # Confirma los cambios
            return cursor.rowcount  # Devuelve el número de filas afectadas
        except Error as e:
            print(f"Error al editar usuario: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()

    def eliminarUsuario(self, userID):
        try:
            cursor = self.db.cursor()
            query = "DELETE FROM usuario WHERE ID_Usuario = %s"
            cursor.execute(query, (userID,))
            self.db.commit()
            return cursor.rowcount  # Devuelve el número de filas eliminadas
        except Error as e:
            print(f"Error al eliminar usuario: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()

    def actualizarContrasena(self, userID, newPassword):
        """Actualiza la contraseña de un usuario."""
        try:
            cursor = self.db.cursor()
            query = "UPDATE usuario SET contrasena = %s WHERE ID_Usuario = %s"
            cursor.execute(query, (newPassword, userID))
            self.db.commit()
            return cursor.rowcount
        except Error as e:
            print(f"Error al actualizar contraseña: {e}")
            self.db.rollback()
            return None
        finally:
            cursor.close()
