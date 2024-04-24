# Ticket-Proj
Re-aprendiendo Django.  
  
## Set-up
Debes tener [WampServer](https://www.wampserver.com/en/) o [XAMPP](https://www.apachefriends.org/es/download.html) o un proveedor MySQL.    
 1. Inicia WampServer.
 2. Dirigete al phpMyAdmin.
 3. Crea una nueva base de datos llamada `tickets`.
  
Instalamos [Django](https://www.djangoproject.com/)  
`pip install django`
  
Instalamos [MySqlClient](https://pypi.org/project/mysqlclient/)  
`pip install mysqlclient`
  
Hacemos las migraciones  
`py manage.py migrate`
  
Iniciamos el servidor  
`py manage.py runserver`
  
 