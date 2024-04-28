# Ticket-Proj
Re-aprendiendo Django.  
  
### Caracteristicas
 - Crea tickets de soporte.
 - Envia comentarios a los tickets.
 - Cuerpo de tickets y comentarios compatibles con Markdown.
 - Adjunta archivos a los comentarios.
  
#### TODO
 - <del>Crear usuarios.</del>
   - <del>Crear Clientes.</del>
   - <del>Crear Staff.</del>
 - <del>Cada cliente puede publicar tickets.</del>
 - El cliente creador de un ticket puede comentar en su ticket mas no en otro.
 - El creador del ticket no puede eliminarlo, pero si editarlo (solo el asunto y el cuerpo).
 - Un Staff puede comentar en cualquier ticket.
 - Un Staff puede cerrar tickets y modificar ciertos valores (proridad, nivel y estado)
 - Mejorar el front-end **opcional*
  
## Set-up
Debes tener [WampServer](https://www.wampserver.com/en/) o [XAMPP](https://www.apachefriends.org/es/download.html) o un proveedor MySQL.    
 1. Inicia WampServer.
 2. Dirigete al phpMyAdmin.
 3. Crea una nueva base de datos llamada `tickets`.
  
Instalamos [Django](https://www.djangoproject.com/)  
`pip install django`
  
Instalamos [MySqlClient](https://pypi.org/project/mysqlclient/)  
`pip install mysqlclient`
  
Instalamos [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html)  
`pip install django-crispy-forms`  
`pip install crispy-bootstrap5`
  
Hacemos las migraciones  
`py manage.py migrate`
  
Iniciamos el servidor  
`py manage.py runserver`
  

> #### Información ensamblado  
> Versión 2.0  
> no retro-compatible.  
