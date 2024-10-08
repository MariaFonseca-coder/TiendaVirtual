class DetallePedido:
    def __init__(self, idDetallePedido, idPedido, idProducto, cantidad, precioUnitario):
        self.idDetallePedido = idDetallePedido
        self.idPedido = idPedido
        self.idProducto = idProducto
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario

    def actualizarDetalle(self, nuevaCantidad=None, nuevoPrecio=None):
        if nuevaCantidad is not None:
            self.cantidad = nuevaCantidad
        if nuevoPrecio is not None:
            self.precioUnitario = nuevoPrecio
        # Código para actualizar el detalle del pedido en la base de datos
        pass

    def mostrarDetalle(self):
        return f"Producto ID: {self.idProducto}, Cantidad: {self.cantidad}, Precio Unitario: {self.precioUnitario}"
