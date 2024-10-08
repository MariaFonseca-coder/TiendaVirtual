class Categoria:
    def __init__(self, idCategoria, nombre, descripcion):
        self.idCategoria = idCategoria
        self.nombre = nombre
        self.descripcion = descripcion

    def actualizarCategoria(self, nuevoNombre=None, nuevaDescripcion=None):
        if nuevoNombre:
            self.nombre = nuevoNombre
        if nuevaDescripcion:
            self.descripcion = nuevaDescripcion
        # Código para actualizar la categoría en la base de datos
        pass
    
    def mostrarCategoria(self):
        return f"Categoría: {self.nombre} - {self.descripcion}"
