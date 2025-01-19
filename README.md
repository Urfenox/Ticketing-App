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

### Levantando el proyecto

 1. Crea un entorno virtual.
```sh
py -m venv .venv
```
 2. Activa el entorno virtual.
```sh
source .venv/bin/activate
```
 3. Instala las dependencias Python necesarias
```sh
pip install -r requirements.txt
```
 4. Hacemos las migraciones  
```sh
py manage.py migrate
```
 5. Iniciamos el servidor  
```sh
py manage.py runserver
```

> #### Información ensamblado  
> Versión 2.3  
> retro-compatible.  
