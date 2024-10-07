class Proveedor:
    def __init__(self, idProveedor, nombre, contacto, telefono):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono

    def actualizarProveedor(self, nuevoNombre=None, nuevoContacto=None, nuevoTelefono=None):
        if nuevoNombre:
            self.nombre = nuevoNombre
        if nuevoContacto:
            self.contacto = nuevoContacto
        if nuevoTelefono:
            self.telefono = nuevoTelefono
        # Código para actualizar el proveedor en la base de datos
        pass
    
    def mostrarProveedor(self):
        return f"{self.nombre} (Contacto: {self.contacto}, Teléfono: {self.telefono})"
