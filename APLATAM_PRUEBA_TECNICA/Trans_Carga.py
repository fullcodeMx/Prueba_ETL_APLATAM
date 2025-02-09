import requests
from datetime import datetime
from conexion import conectar_db  # Importamos la función para conectar con la base de datos


def transformador_carga_noticias(FECHA_INICIO, FECHA_FIN):
    """
    Transforma y carga datos en la tabla NOTICIAS eliminando registros existentes en el rango de fechas
    especificado y luego insertando nuevos datos desde la tabla EXTRACTOR_NOTICIAS.

    Parámetros:
        FECHA_INICIO (str): Fecha de inicio en formato 'YYYY-MM-DD'.
        FECHA_FIN (str): Fecha de fin en formato 'YYYY-MM-DD'.
    """

    conn = conectar_db()  # Establece la conexión con la base de datos
    if conn:
        try:
            cursor = conn.cursor()

            # Eliminar registros dentro del rango de fechas especificado
            query_delete = f"""
                DELETE FROM NOTICIAS 
                WHERE DATE(fecha_publicacion) BETWEEN '{FECHA_INICIO}' AND '{FECHA_FIN}'
            """
            cursor.execute(query_delete)
            conn.commit()

            # Insertar nuevos datos transformados en la tabla NOTICIAS
            query_insert = """
                INSERT INTO NOTICIAS (id_fuente, id_autor, id_fecha, fecha_publicacion, titulo, descripcion, url)
                SELECT  
                    f.id_fuente AS id_fuente,
                    a.id_autor AS id_autor,
                    t.id_fecha AS id_fecha,
                    n.fecha_publicacion,                    
                    UPPER(n.titulo) AS titulo,
                    UPPER(n.descripcion) AS descripcion,
                    n.url 
                FROM
                    railway.EXTRACTOR_NOTICIAS AS n
                LEFT JOIN 
                    FUENTE AS f ON n.fuente = f.fuente
                LEFT JOIN 
                    AUTOR AS a ON n.autor = a.autor
                LEFT JOIN 
                    TIEMPO AS t ON DATE(n.fecha_publicacion) = t.fecha_calendario
            """
            cursor.execute(query_insert)
            conn.commit()

            print("✅️ Todos los registros han sido eliminados e insertados en la tabla NOTICIAS")

        except Exception as e:
            print(f"❌ Error al eliminar e insertar datos en NOTICIAS: {e}")

        finally:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión con la base de datos
