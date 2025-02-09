import requests
from datetime import datetime
from conexion import conectar_db  # Importamos la función de conexión a la base de datos


# Obtener noticias de la API
def obtener_noticias(FECHA_INICIO, FECHA_FIN):
    """
    Obtiene noticias desde la API de NewsAPI dentro del rango de fechas especificado.
    """
    API_KEY = "6c3523005d044a9bbdc713b1edccb524"
    URL = f"https://newsapi.org/v2/everything?q=tesla&from={FECHA_INICIO}&to={FECHA_FIN}&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()["articles"]
    else:
        print("Error al obtener noticias:", response.status_code)
        print("Respuesta:", response.text)  # Imprime el contenido completo de la respuesta
        return []


# Guardar noticias en la base de datos
def guardar_noticias(noticias):
    """
    Guarda las noticias obtenidas en la base de datos.
    """
    conn = conectar_db()
    if conn:
        cursor = conn.cursor()

        # Eliminar todos los registros existentes en la tabla
        cursor.execute("DELETE FROM EXTRACTOR_NOTICIAS")
        conn.commit()
        print("🗑️ Todos los registros han sido eliminados de la tabla EXTRACTOR_NOTICIAS.")

        # Insertar nuevas noticias
        query = """
            INSERT INTO EXTRACTOR_NOTICIAS (fuente, autor, titulo, descripcion, url, fecha_publicacion)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for noticia in noticias:
            fuente = noticia["source"]["name"]
            autor = noticia["author"] if noticia["author"] else "Desconocido"
            titulo = noticia["title"]
            descripcion = noticia["description"]
            url = noticia["url"]
            fecha_publicacion = datetime.strptime(noticia["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")

            cursor.execute(query, (fuente, autor, titulo, descripcion, url, fecha_publicacion))

        # Confirmar los cambios en la base de datos
        conn.commit()
        print("✅ Noticias de Tesla guardadas correctamente en extractor noticias.")

        cursor.close()  # Cerrar cursor
        conn.close()  # Cerrar conexión


# Procesar la dimensión de fuentes
def dimension_fuentes():
    """
    Elimina e inserta registros en la tabla de fuentes.
    """
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()

            cursor.execute("DELETE FROM FUENTE")
            conn.commit()

            cursor.execute(
                "INSERT INTO FUENTE (fuente) SELECT DISTINCT UPPER(fuente) AS fuente FROM railway.EXTRACTOR_NOTICIAS")
            conn.commit()
            print("✅️ Todos los registros han sido eliminados e insertados en la tabla fuentes")
        except Exception as e:
            print(f"❌ Error al eliminar e insertar datos en fuentes: {e}")
        finally:
            cursor.close()
            conn.close()


# Procesar la dimensión de autores
def dimension_autor():
    """
    Elimina e inserta registros en la tabla de autores.
    """
    conn = conectar_db()
    if conn:
        try:
            cursor = conn.cursor()

            cursor.execute("DELETE FROM AUTOR")
            conn.commit()

            cursor.execute(
                "INSERT INTO AUTOR (autor) SELECT DISTINCT UPPER(autor) AS autor FROM railway.EXTRACTOR_NOTICIAS")
            conn.commit()
            print("✅️ Todos los registros han sido eliminados e insertados en la tabla autor")
        except Exception as e:
            print(f"❌ Error al eliminar e insertar datos en autor: {e}")
        finally:
            cursor.close()
            conn.close()
