class DireccionDTO:
    def __init__(self, idDireccion, idCliente, direccionLinea1, ciudad, pais):
        self.idDireccion = idDireccion
        self.idCliente = idCliente
        self.direccionLinea1 = direccionLinea1
        self.ciudad = ciudad
        self.pais = pais

    def to_dict(self):
        """Convierte el DTO en un diccionario."""
        return {
            'idDireccion': self.idDireccion,
            'idCliente': self.idCliente,
            'direccionLinea1': self.direccionLinea1,
            'ciudad': self.ciudad,
            'pais': self.pais
        }
