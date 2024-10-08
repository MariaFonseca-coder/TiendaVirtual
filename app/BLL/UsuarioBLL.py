from app.modelos import Administrador, Empleado

class UsuarioBLL:
    def __init__(self, dal):
        self.dal = dal

    def crear_usuario(self, admin, nuevo_usuario):
        """Permitir que solo los administradores puedan crear usuarios."""
        if isinstance(admin, Administrador):
            return self.dal.crear_usuario(nuevo_usuario)
        else:
            raise PermissionError("Solo los administradores pueden crear usuarios.")

    def editar_usuario(self, admin, usuario_editado):
        """Permitir que solo los administradores puedan editar usuarios."""
        if isinstance(admin, Administrador):
            return self.dal.editar_usuario(usuario_editado)
        else:
            raise PermissionError("Solo los administradores pueden editar usuarios.")

    def eliminar_usuario(self, admin, userID):
        """Permitir que solo los administradores puedan eliminar usuarios."""
        if isinstance(admin, Administrador):
            return self.dal.eliminar_usuario(userID)
        else:
            raise PermissionError("Solo los administradores pueden eliminar usuarios.")

    def ver_usuario(self, usuario, userID):
        """Permitir que tanto los administradores como los empleados puedan ver detalles de los usuarios."""
        if isinstance(usuario, (Administrador, Empleado)):  # Ambos roles pueden ver usuarios
            return self.dal.obtenerUsuarioPorID(userID)
        else:
            raise PermissionError("Solo los administradores o empleados pueden ver usuarios.")

    def crear_cliente(self, usuario, nuevo_cliente):
        """Permitir que tanto los administradores como los empleados puedan crear clientes."""
        if isinstance(usuario, (Administrador, Empleado)):  # Ambos roles pueden crear clientes
            return self.dal.crear_cliente(nuevo_cliente)  # Asumiendo que tienes esta función en DAL
        else:
            raise PermissionError("Solo los administradores o empleados pueden crear clientes.")

    def editar_cliente(self, usuario, cliente_editado):
        """Permitir que tanto los administradores como los empleados puedan editar clientes."""
        if isinstance(usuario, (Administrador, Empleado)):  # Ambos roles pueden editar clientes
            return self.dal.editar_cliente(cliente_editado)
        else:
            raise PermissionError("Solo los administradores o empleados pueden editar clientes.")

    def ver_cliente(self, usuario, idCliente):
        """Permitir que tanto los administradores como los empleados puedan ver los detalles de los clientes."""
        if isinstance(usuario, (Administrador, Empleado)):  # Ambos roles pueden ver clientes
            return self.dal.obtener_cliente_por_id(idCliente)
        else:
            raise PermissionError("Solo los administradores o empleados pueden ver clientes.")

    def eliminar_cliente(self, admin, idCliente):
        """Permitir que solo los administradores puedan eliminar clientes."""
        if isinstance(admin, Administrador):
            return self.dal.eliminar_cliente(idCliente)
        else:
            raise PermissionError("Solo los administradores pueden eliminar clientes.")
