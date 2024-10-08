class ClienteDTO:
    def __init__(self, idCliente, nombre, apellido, email, telefono, fechaRegistro):
        self.idCliente = idCliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.fechaRegistro = fechaRegistro

    def to_dict(self):
        """Convierte el DTO en un diccionario."""
        return {
            'idCliente': self.idCliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'fechaRegistro': self.fechaRegistro
        }
