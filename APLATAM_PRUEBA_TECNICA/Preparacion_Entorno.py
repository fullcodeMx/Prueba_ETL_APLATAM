from datetime import datetime, timedelta
from conexion import conectar_db  # Importamos la función de conexión desde el archivo de conexión

# Función para crear la tabla AUTOR si no existe
def crear_tabla_autor():
    conn = conectar_db()  # Conectamos a la base de datos
    if conn:
        try:
            cursor = conn.cursor()  # Creamos un cursor para ejecutar la consulta
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS AUTOR (
                    id_autor INT AUTO_INCREMENT PRIMARY KEY,  # ID único para cada autor
                    autor VARCHAR(255)                        # Nombre del autor
                )
            """)
            conn.commit()  # Confirmamos los cambios en la base de datos
            print("✅ Tabla `AUTOR` verificada.")
        except Exception as e:
            print(f"❌ Error al crear/verificar la tabla AUTOR: {e}")
        finally:
            cursor.close()  # Cerramos el cursor
            conn.close()    # Cerramos la conexión

# Función para crear la tabla FUENTE si no existe
def crear_tabla_fuente():
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS FUENTE (
                    id_fuente INT AUTO_INCREMENT PRIMARY KEY,  # ID único para cada fuente
                    fuente VARCHAR(255)                        # Nombre de la fuente
                )
            """)
            conn.commit()
            print("✅ Tabla `FUENTE` verificada.")
        except Exception as e:
            print(f"❌ Error al crear/verificar la tabla FUENTE: {e}")
        finally:
            cursor.close()
            conn.close()

# Función para crear la tabla EXTRACTOR_NOTICIAS si no existe
def crear_tabla_extractor():
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS EXTRACTOR_NOTICIAS (
                    id INT AUTO_INCREMENT PRIMARY KEY,       # ID único para cada noticia
                    fuente VARCHAR(255),                     # Fuente de la noticia
                    autor VARCHAR(255),                      # Autor de la noticia
                    titulo TEXT,                             # Título de la noticia
                    descripcion TEXT,                        # Descripción de la noticia
                    url TEXT,                                # URL de la noticia
                    fecha_publicacion DATETIME               # Fecha y hora de publicación
                )
            """)
            conn.commit()
            print("✅ Tabla `EXTRACTOR_NOTICIAS` verificada.")
        except Exception as e:
            print(f"❌ Error al crear/verificar la tabla EXTRACTOR_NOTICIAS: {e}")
        finally:
            cursor.close()
            conn.close()

# Función para crear la tabla TIEMPO si no existe
def crear_tabla_tiempo():
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS TIEMPO (
                    id_fecha INT AUTO_INCREMENT PRIMARY KEY,  # ID único para cada fecha
                    año INT,                                 # Año de la fecha
                    mes INT,                                 # Mes de la fecha
                    fecha_calendario DATE,                   # Fecha en formato calendario
                    trimestre INT,                           # Trimestre de la fecha
                    semana INT,                              # Semana del año
                    semestre INT                             # Semestre del año
                )
            """)
            conn.commit()
            print("✅ Tabla `TIEMPO` verificada.")
        except Exception as e:
            print(f"❌ Error al crear/verificar la tabla TIEMPO: {e}")
        finally:
            cursor.close()
            conn.close()

### Llenado de información para la tabla TIEMPO ###

# Función para generar los datos para la tabla TIEMPO
def generar_datos_tiempo():
    fecha_inicio = datetime(2025, 1, 1)  # Fecha de inicio para los datos
    fecha_fin = datetime(2030, 12, 31)  # Fecha final para los datos
    delta = timedelta(days=1)            # Incremento de un día para cada iteración
    datos = []                           # Lista para almacenar los datos generados

    while fecha_inicio <= fecha_fin:
        # Obtención de los valores para cada columna
        año = fecha_inicio.year
        mes = fecha_inicio.month
        fecha_calendario = fecha_inicio.strftime('%Y-%m-%d')
        trimestre = (mes - 1) // 3 + 1
        semana = fecha_inicio.isocalendar()[1]
        semestre = 1 if mes <= 6 else 2

        datos.append((año, mes, fecha_calendario, trimestre, semana, semestre))  # Añadimos los datos a la lista
        fecha_inicio += delta  # Avanzamos un día

    return datos

# Función para eliminar todos los registros de la tabla TIEMPO
def eliminar_datos_tiempo():
    conn = conectar_db()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM TIEMPO")  # Eliminamos todos los registros de la tabla TIEMPO
            conn.commit()
            print(f"✅ Se han eliminado los registros en la tabla TIEMPO.")
        except Exception as e:
            print(f"❌ Error al eliminar datos en la tabla TIEMPO: {e}")
        finally:
            cursor.close()
            conn.close()

# Función para insertar los datos generados en la tabla TIEMPO
def insertar_datos_tiempo():
    datos = generar_datos_tiempo()  # Generamos los datos
    conn = conectar_db()

    if conn:
        try:
            cursor = conn.cursor()
            cursor.executemany(
                "INSERT INTO TIEMPO (año, mes, fecha_calendario, trimestre, semana, semestre) VALUES (%s, %s, %s, %s, %s, %s)",
                datos  # Insertamos todos los datos generados
            )
            conn.commit()
            print(f"✅ Se han insertado {len(datos)} registros en la tabla TIEMPO.")
        except Exception as e:
            print(f"❌ Error al insertar datos en la tabla TIEMPO: {e}")
        finally:
            cursor.close()
            conn.close()

# Función para crear la tabla NOTICIAS con las claves foráneas relacionadas
def crear_tabla_NOTICIAS():
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS NOTICIAS (
                    id_noticias INT AUTO_INCREMENT PRIMARY KEY,  # ID único para cada noticia
                    id_fuente INT,                               # ID de la fuente (clave foránea)
                    id_autor INT,                                # ID del autor (clave foránea)
                    id_fecha INT,                                # ID de la fecha (clave foránea)
                    fecha_publicacion DATETIME,                  # Fecha y hora de publicación
                    titulo TEXT,                                 # Título de la noticia
                    descripcion TEXT,                            # Descripción de la noticia
                    url TEXT,                                    # URL de la noticia
                    CONSTRAINT fk_noticias_fuente FOREIGN KEY (id_fuente) REFERENCES railway.FUENTE (id_fuente) ON DELETE CASCADE ON UPDATE CASCADE,
                    CONSTRAINT fk_noticias_autor FOREIGN KEY (id_autor) REFERENCES railway.AUTOR (id_autor) ON DELETE SET NULL ON UPDATE CASCADE,
                    CONSTRAINT fk_tiempo FOREIGN KEY (id_fecha) REFERENCES TIEMPO(id_fecha) ON DELETE SET NULL ON UPDATE CASCADE
                )
            """)
            conn.commit()
            print("✅ Tabla `NOTICIAS` verificada.")
        except Exception as e:
            print(f"❌ Error al crear/verificar la tabla NOTICIAS: {e}")
        finally:
            cursor.close()
            conn.close()
