class DireccionBLL:
    def __init__(self, dal):
        self.dal = dal

    def agregarDireccion(self, direccion_dto):
        """Agrega una nueva dirección a través de la capa DAL."""
        if direccion_dto.idCliente and direccion_dto.direccionLinea1:
            return self.dal.agregarDireccion(direccion_dto)
        else:
            raise ValueError("ID del cliente y dirección son obligatorios.")

    def obtenerDireccionesPorCliente(self, idCliente):
        """Obtiene todas las direcciones de un cliente."""
        return self.dal.obtenerDireccionesPorCliente(idCliente)

    def actualizarDireccion(self, direccion_dto):
        """Actualiza una dirección existente."""
        if direccion_dto.idDireccion and direccion_dto.idCliente:
            return self.dal.actualizarDireccion(direccion_dto)
        else:
            raise ValueError("El ID de la dirección y el ID del cliente son obligatorios para la actualización.")

    def eliminarDireccion(self, idDireccion):
        """Elimina una dirección."""
        if idDireccion:
            return self.dal.eliminarDireccion(idDireccion)
        else:
            raise ValueError("El ID de la dirección es obligatorio para la eliminación.")
