# admin
En el caso iniciar con el proyecto :
Se debe agregar la carpeta auth con el archivo mysql.cnf y en el agregar los parametros de conexion para la base de datos
el formato es el siguiente :
    
    [client]
    database = 'nombre de la base de datos'
    user = 'usuario'
    password = 'contraseña'
    default-character-set = 'utf8'

Ademas se debe hacer la migracion de la aplicacion 
python manage.py migrate para construir toda la estructura de la base de datos
