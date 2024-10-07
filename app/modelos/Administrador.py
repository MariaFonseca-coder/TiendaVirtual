class Administrador(Usuario):
    def __init__(self, userID, username, password, fechaCreacion=None):
        super().__init__(userID, username, password, "admin", fechaCreacion)
