from app.DTO import DireccionDTO


class Cliente:
    def __init__(self, idCliente, nombre, apellido, email, password, telefono, fechaRegistro):
        self.idCliente = idCliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.telefono = telefono
        self.fechaRegistro = fechaRegistro
        self.direcciones = []  # Lista de instancias de Direccion

    def registrarCliente(self):
        # Código para registrar un nuevo cliente
        pass
    
    def actualizarDatos(self, nuevoNombre=None, nuevoApellido=None, nuevoEmail=None, nuevoTelefono=None):
        if nuevoNombre:
            self.nombre = nuevoNombre
        if nuevoApellido:
            self.apellido = nuevoApellido
        if nuevoEmail:
            self.email = nuevoEmail
        if nuevoTelefono:
            self.telefono = nuevoTelefono
        # Código para actualizar los datos del cliente en la base de datos
        pass

    def resetPassword(self, newPassword):
        self.password = newPassword
        # Código para actualizar la contraseña
        pass

    def cargarDirecciones(self, direccion_dal):
        """Carga las direcciones del cliente desde la base de datos."""
        direcciones_data = direccion_dal.obtenerDireccionesPorCliente(self.idCliente)
        self.direcciones = [DireccionDTO(**direccion) for direccion in direcciones_data]

    def agregarDireccion(self, direccion, direccion_dal):
        """Agrega una nueva dirección y la inserta en la base de datos."""
        direccion_dal.agregarDireccion(direccion)
        self.direcciones.append(direccion)

    def eliminarDireccion(self, idDireccion, direccion_dal):
        """Elimina una dirección y la remueve de la base de datos."""
        direccion_dal.eliminarDireccion(idDireccion)
        self.direcciones = [dir for dir in self.direcciones if dir.idDireccion != idDireccion]

    def mostrarDirecciones(self):
        """Muestra todas las direcciones del cliente"""
        for direccion in self.direcciones:
            print(direccion.mostrarDireccion())
