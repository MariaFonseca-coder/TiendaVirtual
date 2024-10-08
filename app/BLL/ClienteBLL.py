from app.DTO import ClienteDTO

class ClienteBLL:
    def __init__(self, dal):
        self.dal = dal

    def registrarCliente(self, clienteDto):
        """Registra un nuevo cliente a través de la capa DAL."""
        if clienteDto.nombre and clienteDto.email:
            cliente = ClienteDTO(
                clienteDto.idCliente, 
                clienteDto.nombre, 
                clienteDto.apellido, 
                clienteDto.email, 
                clienteDto.telefono, 
                clienteDto.fechaRegistro
            )
            return self.dal.registrarCliente(cliente)
        else:
            raise ValueError("Nombre y correo electrónico son obligatorios.")

    def obtenerClientePorID(self, idCliente):
        """Obtiene los datos de un cliente por su ID."""
        return self.dal.obtenerClientePorID(idCliente)

    def actualizarCliente(self, clienteDto):
        """Actualiza los datos del cliente."""
        if clienteDto.idCliente:
            return self.dal.actualizarCliente(clienteDto)
        else:
            raise ValueError("El ID del cliente es obligatorio para la actualización.")

    def eliminarCliente(self, idCliente):
        """Elimina un cliente de la base de datos."""
        if idCliente:
            return self.dal.eliminarCliente(idCliente)
        else:
            raise ValueError("El ID del cliente es obligatorio para la eliminación.")
