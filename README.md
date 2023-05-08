Para correr proyecto, se deben instalar librerias que se encuentran en el archivo requirements.txt.

Para guardar los datos en la bd, se debe correr el archivo js "load_data.py" y cambiar la linea del archivo a la ruta donde se guardo el csv de la información.

Se necesira tener instalado PostgreSQL una base de datos llamada `proyecto_paipa`

Para crear migraciones se corre el comando `python manage.py makemigrations`

Para migrar a la bd se corre el comando `python manage.py migrate`

Para correr el proyecto se corre el comando `python manage.py runserver`