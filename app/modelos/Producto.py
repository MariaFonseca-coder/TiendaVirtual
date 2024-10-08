class Producto:
    def __init__(self, idProducto, nombre, descripcion, precio, color, idCategoria, idProveedor):
        self.idProducto = idProducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.color = color
        self.idCategoria = idCategoria
        self.idProveedor = idProveedor

    
    def actualizarProducto(self, nuevoNombre=None, nuevaDescripcion=None, nuevoPrecio=None, nuevoColor=None):
        if nuevoNombre:
            self.nombre = nuevoNombre
        if nuevaDescripcion:
            self.descripcion = nuevaDescripcion
        if nuevoPrecio:
            self.precio = nuevoPrecio
        if nuevoColor:
            self.Ccolorolor = nuevoColor
        # Código para actualizar el producto en la base de datos
        pass

    def mostrarProducto(self):
        return f"Producto: {self.nombre} - {self.descripcion}, Precio: {self.precio}, Color: {self.color}"
