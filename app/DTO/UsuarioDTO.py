class UsuarioDTO:
    def __init__(self, userID, username, role, fechaCreacion, password=None):
        self.userID = userID
        self.username = username
        self.fechaCreacion = fechaCreacion
        self.password = password
        
        # Validación de roles permitidos
        if role not in ["admin", "empleado"]:
            raise ValueError("El rol debe ser 'admin' o 'empleado'.")
        self.role = role
