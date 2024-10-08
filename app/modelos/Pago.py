class Pago:
    def __init__(self, idPago, idPedido, monto, metodoPago):
        self.idPago = idPago
        self.idPedido = idPedido
        self.monto = monto
        self.metodoPago = metodoPago

    def actualizarPago(self, nuevoMonto=None, nuevoMetodo=None):
        if nuevoMonto is not None:
            self.monto = nuevoMonto
        if nuevoMetodo:
            self.metodoPago = nuevoMetodo
        # Código para actualizar el pago en la base de datos
        pass

    def mostrarPago(self):
        return f"Pago ID: {self.idPago}, Pedido ID: {self.idPedido}, Monto: {self.monto}, Método de Pago: {self.metodoPago}"
