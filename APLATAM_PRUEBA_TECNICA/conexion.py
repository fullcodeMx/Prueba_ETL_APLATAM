import mysql.connector

# Configuración de la base de datos en Railway
# Aquí se guardan los detalles de conexión a la base de datos
DB_CONFIG = {
    "host": "monorail.proxy.rlwy.net",  # Dirección del host de la base de datos
    "port": 36716,                      # Puerto de conexión a la base de datos
    "user": "root",                     # Usuario de la base de datos
    "password": "AMQvzlgsvrCRqqRBWDycqlmtDaAeEBlf",  # Contraseña para la conexión
    "database": "railway"               # Nombre de la base de datos a la que nos conectamos
}

# Función para conectar a la base de datos
# Intenta establecer una conexión con la base de datos usando los parámetros de DB_CONFIG
def conectar_db():
    try:
        # Intentamos realizar la conexión a la base de datos
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn  # Retorna la conexión si es exitosa
    except mysql.connector.Error as err:
        # En caso de error, imprimimos un mensaje con la descripción del error
        print("❌ Error en la base de datos:", err)
        return None  # Retorna None si la conexión falla
