<h1 align="center">Imanku Prueba Técnica ⚙️</h1>

## Pre-Requisitos
- Tener Python instalado con una versión superior a la 3.8.
- Tener instalado pip como instalador de paquetes.

## Como Usarlo
1. Ve al directorio donde quieras crear el proyecto y clona el repositorio

    ```
    git clone https://github.com/Fer-Bar/imanku_test.git
    ```
2. Crea un entorno virtual:
    ```
    python3 -m venv venv
    ```
    Una vez creado puedes activarlo.
    <br>
    
    En Windows ejecutando:
    ```
    venv\Scripts\activate.bat
    ```
    En Unix o MacOS, ejecutando:
    ```
    source venv/bin/activate
    ```   
3. Instala las depedencias `pip install -r requirements.txt`
4. Los datos de la conexión con la db se encuentran en el archivo [connection.py](polls/connection.py)
4. Ejecutar [main.py](main.py) para correr la aplicación web.
5. Para crear las tablas en consola(cli) ejecuta `flask create_tables` y para crear el "superusuario" ejecuta
`flask create_user_to_test`. Estas son las credenciales con las que tiene que entrar a la página de login
después de crear el "superusuario" (email='pepe@gmail.com', password='pepe').
6. Para introducir los datos del archivo excel dado y el archivo json, ejecuta en consola
`flask populate_db_with_counties`(excel) y `flask populate_db_with_election`(json).


