# Proyecto de Base de Datos con MySQL

Este proyecto maneja la creación y gestión de tablas en una base de datos MySQL para almacenar información relacionada con autores, fuentes, noticias, y tiempos. Está diseñado para ejecutarse con Python, utilizando la biblioteca `mysql-connector` para interactuar con MySQL.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu entorno:

- **Python 3.x**: Asegúrate de tener una versión reciente de Python instalada. Puedes verificar tu versión ejecutando el siguiente comando en tu terminal o consola:
  ```bash
  python --version

###MySQL Server: Debes tener una instancia de MySQL en ejecución. Si estás utilizando servicios en la nube, asegúrate de tener las credenciales correctas para acceder a la base de datos.
Instalación
Clona el repositorio (o descarga los archivos del proyecto). Si estás usando Git, ejecuta:

bash
Copiar
Editar
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_repositorio>
Crea un entorno virtual (opcional pero recomendado): Si no tienes un entorno virtual, puedes crear uno con los siguientes comandos:

bash
Copiar
Editar
python -m venv env
Activa el entorno virtual:

En Windows:
bash
Copiar
Editar
.\env\Scripts\activate
En macOS/Linux:
bash
Copiar
Editar
source env/bin/activate
Instala las dependencias: Asegúrate de tener el archivo requirements.txt en el proyecto (si no lo tienes, puedes crear uno con las dependencias necesarias). Ejecuta el siguiente comando para instalar las bibliotecas necesarias:

bash
Copiar
Editar
pip install -r requirements.txt
Si no tienes el archivo requirements.txt, instala mysql-connector directamente con:

bash
Copiar
Editar
pip install mysql-connector
Configuración de la Base de Datos
Conexión a la Base de Datos: Asegúrate de modificar las credenciales de conexión a la base de datos en el archivo conexion.py (o donde se gestionen las configuraciones de conexión). Aquí es donde se especifican los datos como el host, usuario, contraseña y base de datos de MySQL.

python
Copiar
Editar
DB_CONFIG = {
    "host": "tu_host",
    "port": 3306,  # Cambia si usas otro puerto
    "user": "tu_usuario",
    "password": "tu_contraseña",
    "database": "tu_base_de_datos"
}
Ejecución del Proyecto
solo ejecuta el archivo Main.py , dicho archivo hará todo el procedimiento de : 
*creación de tablas 
*Extracción tranformación y carga de datos 


Estructura de la Base de Datos
El proyecto creará las siguientes tablas en la base de datos:

AUTOR: Almacena información sobre los autores.
id_autor: Identificador único del autor (clave primaria).
autor: Nombre del autor.

FUENTE: Almacena información sobre las fuentes.
id_fuente: Identificador único de la fuente (clave primaria).
fuente: Nombre de la fuente.


EXTRACTOR_NOTICIAS: Almacena las noticias extraídas.
id: Identificador único de la noticia (clave primaria).
fuente: Fuente de la noticia.
autor: Autor de la noticia.
titulo: Título de la noticia.
descripcion: Descripción de la noticia.
url: URL de la noticia.
fecha_publicacion: Fecha de publicación de la noticia.

TIEMPO: Almacena información sobre fechas y tiempos.
id_fecha: Identificador único de la fecha (clave primaria).
año: Año de la fecha.
mes: Mes de la fecha.
fecha_calendario: Fecha en formato calendario (YYYY-MM-DD).
trimestre: Trimestre de la fecha.
semana: Semana del año.
semestre: Semestre del año.

NOTICIAS: Relaciona noticias con fuentes, autores y fechas.
id_noticias: Identificador único de la noticia (clave primaria).
id_fuente: Clave foránea que referencia a FUENTE.
id_autor: Clave foránea que referencia a AUTOR.
id_fecha: Clave foránea que referencia a TIEMPO.
fecha_publicacion: Fecha y hora de publicación de la noticia.
titulo: Título de la noticia.
descripcion: Descripción de la noticia.

url: URL de la noticia.
Errores Comunes
Error de conexión: Si hay un error en la conexión a la base de datos, asegúrate de que las credenciales de la base de datos son correctas y que el servidor de MySQL está en ejecución.
Tablas ya existentes: Si las tablas ya existen en la base de datos, el código las verificará y no las recreará.