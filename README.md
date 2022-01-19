# Template del taller "Introducción a FastAPI"

## Bienvenido
Con esta plantilla comenzaremos nuestro proyecto de crear una pequeña API de notas usando FastAPI, aquí tienes una pequeña guía de instalación de las dependencias y herramientas:

### ¡Antes de iniciar!
Necesitamos tener instalado:

[![Visual Studio Code](https://img.shields.io/badge/-Visual%20Studio%20Code-blue?logo=visualstudiocode&logoColor=white&style=for-the-badge)](https://code.visualstudio.com/)

[![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/downloads/)

[![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white&style=for-the-badge)](https://git-scm.com/downloads)


### Instalación y creación del enntorno virtual
1. Creamos una carpeta donde se encontrará nuestro proyecto:
```bash
$ mkdir notas_api
$ cd notas-api/
```
2. Clonamos el repositorio con git:
```bash
$ git clone https://github.com/daniel692a/template-fastapi.git
$ cd template-fastapi/
```
3. Creamos el entorno virtual con python
```bash
$ python3 -m venv env
# PowerShell
$ py -m venv env
```
4. Activamos el ambiente e instalamos las dependencias que se encuentran listadas en `requirements.txt`
```bash
$ source env/bin/activate
# PowerShell
$ env\Scripts\Activate.ps1
# CMD
$ env\Scripts\activate.bat


(env)$ pip install -r requirements.txt

fastapi -------------------> 100%
uvicorn -------------------> 100%
```

5. Comenzamos a editar el archivo `main.py`, añadiendo nuestros endpoints.
6. Iniciamos el servidor en local con uvicorn:
```bash
(env)$ uvicorn main:app --reload
```
7. Para ver la documentación con *Swagger* al final de la ruta `localhost:8000` escribimos `/docs`


