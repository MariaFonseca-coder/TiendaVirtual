class Inventario:
    def __init__(self, idInventario, idProducto, cantidadDisponible, campo):
        self.idInventario = idInventario
        self.idProducto = idProducto
        self.cantidadDisponible = cantidadDisponible
        self.campo = campo

    def actualizarInventario(self, nuevaCantidad=None, nuevoCampo=None):
        if nuevaCantidad is not None:
            self.cantidadDisponible = nuevaCantidad
        if nuevoCampo:
            self.campo = nuevoCampo
        # Código para actualizar el inventario en la base de datos
        pass

    def mostrarInventario(self):
        return f"Producto ID: {self.idProducto}, Cantidad Disponible: {self.cantidadDisponible}, Ubicación: {self.campo}"
