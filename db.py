import mysql.connector
from config import Config  # Importar la configuración

def crear_conexion_bd():
    """Crear y devolver la conexión a la base de datos usando la configuración de config.py."""
    try:
        conexion = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
