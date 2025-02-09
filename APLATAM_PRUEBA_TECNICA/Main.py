from datetime import datetime
from conexion import conectar_db  # Importamos las funciones desde conexion.py
from Preparacion_Entorno import (crear_tabla_extractor,crear_tabla_NOTICIAS,crear_tabla_tiempo,insertar_datos_tiempo,eliminar_datos_tiempo,
                                 crear_tabla_fuente,crear_tabla_autor)
from Extractor import obtener_noticias,guardar_noticias,dimension_fuentes,dimension_autor
from Trans_Carga import transformador_carga_noticias

### Ejecución del proceso

if __name__ == "__main__":

    ######Esta configuración es para cargas iniciales de información
    FECHA_INICIO = "2025-02-08"
    FECHA_FIN = "2025-02-09"
    ##### cuando tengamos listas las cargas iniciales se tendrán que comentar y solo activar las cargas incrementales

    ##FECHA_INICIO = datetime.today().strftime("%Y-%m-%d")
    ##FECHA_FIN = datetime.today().strftime("%Y-%m-%d")

#####################################
###preparación de entorno (tablas)###
#####################################
    crear_tabla_autor()
    crear_tabla_fuente()
    crear_tabla_extractor()
    crear_tabla_tiempo()
    eliminar_datos_tiempo()
    insertar_datos_tiempo()
    crear_tabla_NOTICIAS()
#######################################

#############################################
##Extractor, Transformador y Carga de datos##
#############################################
    noticias = obtener_noticias(FECHA_INICIO, FECHA_FIN)
    if noticias:
       guardar_noticias(noticias)
       dimension_fuentes()
       dimension_autor()
       transformador_carga_noticias(FECHA_INICIO, FECHA_FIN)