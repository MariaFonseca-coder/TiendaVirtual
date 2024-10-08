import hashlib
from datetime import datetime
from flask import session

class Usuario:
    def __init__(self, userID=None, username=None, password=None, role=None, fechaCreacion=None):
        self.userID = userID
        self.username = username
        self.password = self._hash_password(password) if password else None  # Hash si se proporciona contraseña
        self.role = role
        self.fechaCreacion = fechaCreacion if fechaCreacion else datetime.now()

    def _hash_password(self, password):
        """Método privado para hacer hash de la contraseña."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verificar_password(self, password_input):
        """Verifica si la contraseña ingresada coincide con el hash almacenado."""
        return self.password == hashlib.sha256(password_input.encode()).hexdigest()

    def login(self, username_input, password_input, dal):
        """Proceso de autenticación y manejo de sesión con Flask."""
        # Obtener el usuario desde la base de datos usando el DAL
        usuario_data = dal.obtenerUsuarioPorUsername(username_input)
        
        if usuario_data:
            # El DAL devuelve los detalles del usuario, asignarlos al objeto
            self.userID = usuario_data['ID_Usuario']
            self.username = usuario_data['Nombre_Usuario']
            self.password = usuario_data['contrasena']
            self.role = usuario_data['Rol']
            self.fechaCreacion = usuario_data['Fecha_Creacion']
            
            # Verificar la contraseña ingresada con la almacenada
            if self.verificar_password(password_input):
                # Iniciar sesión guardando la información en la sesión de Flask
                session['userID'] = self.userID
                session['username'] = self.username
                session['role'] = self.role
                print(f"Usuario {self.username} ha iniciado sesión correctamente.")
                return True
            else:
                print("Contraseña incorrecta.")
                return False
        else:
            print("Usuario no encontrado.")
            return False
    
    def logout(self):
        """Cerrar la sesión del usuario y limpiar datos de la sesión de Flask."""
        session.clear()  # Limpia todos los datos de la sesión
        print(f"Usuario {self.username} ha cerrado sesión.")
        return True

    def resetPassword(self, newPassword):
        """Reemplaza la contraseña actual por una nueva."""
        self.password = self._hash_password(newPassword)
        print(f"La contraseña del usuario {self.username} ha sido actualizada.")
        # Aquí puedes integrar el cambio de contraseña con la capa de acceso a datos (DAL)
        pass

    def __str__(self):
        """Representación en cadena del objeto Usuario."""
        return f"Usuario(ID: {self.userID}, Nombre: {self.username}, Rol: {self.role}, Fecha de Creación: {self.fechaCreacion})"
