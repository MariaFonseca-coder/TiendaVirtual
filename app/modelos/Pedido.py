class Pedido:
    def __init__(self, idPedido, idCliente, fechaPedido, estado, total):
        self.idPedido = idPedido
        self.idCliente = idCliente
        self.fechaPedido = fechaPedido
        self.estado = estado
        self.total = total
        self.detalles = []  # Lista para almacenar los detalles del pedido (DetallePedido)

    def agregarDetalle(self, detallePedido):
        self.detalles.append(detallePedido)
        # Código para agregar el detalle del pedido a la base de datos
        pass

    def actualizarEstado(self, nuevoEstado):
        self.estado = nuevoEstado
        # Código para actualizar el estado del pedido en la base de datos
        pass

    def mostrar_pedido(self):
        detalles_str = "\n".join([detalle.mostrar_detalle() for detalle in self.detalles])
        return f"Pedido ID: {self.idPedido}, Cliente ID: {self.idCliente}, Fecha: {self.fechaPedido}, Estado: {self.estado}, Total: {self.total}\nDetalles:\n{detalles_str}"
