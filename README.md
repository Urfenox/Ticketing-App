# Ticket-Proj
Re-aprendiendo Django.  
  
### Características
 - Crea tickets de soporte.
 - Envía comentarios a los tickets.
 - Cuerpo de tickets y comentarios compatibles con Markdown.
 - Adjunta archivos a los comentarios.
  
##### Lógicas
 - Un usuario puede crear tickets.
 - Un usuario puede ver todos los tickets, pero solo comentar en los propios.
 - Un Staff puede editar solo los campos `estado`, `categoria` y `prioridad`, mas no el contenido.
 - Un usuario puede editar su ticket, solo `asunto` y `mensaje`.
 - Un usuario no puede editar tickets cerrados.
 - Los tickets cerrados no aceptan comentarios.
 - Un Staff puede comentar en todos los tickets.
 - Un Staff puede eliminar cualquier ticket.
 - Se pueden crear cuentas, iniciar sesión y finalizarlas.
 - No se permite entrar a `tickets/` sin una sesión iniciada.
  
#### TODO
 - Mejorar el front-end **opcional*
  
## Set-up
Debes tener [WampServer](https://www.wampserver.com/en/) o [XAMPP](https://www.apachefriends.org/es/download.html) o un proveedor MySQL.    
 1. Inicia WampServer.
 2. Dirígete al phpMyAdmin.
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
> Versión 2.2  
> retro-compatible.  
