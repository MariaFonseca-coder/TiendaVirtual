class Direccion:
    def __init__(self, idDireccion, idCliente, direccionLinea1, ciudad, pais):
        self.idDireccion = idDireccion
        self.idCliente = idCliente
        self.direccionLinea1 = direccionLinea1
        self.ciudad = ciudad
        self.pais = pais

    def mostrarDireccion(self):
        return f"{self.direccionLinea1}, {self.ciudad}, {self.pais}"
