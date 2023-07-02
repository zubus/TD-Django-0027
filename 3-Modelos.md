# Modelos en Django

## 🗂️ Estructura del proyecto actualizada
``` shell
proyecto1/
    boards/
        migrations/
            0001_initial.py
            0002_boards.py
            0003_alter_boards_options.py
        static/
            boards/
                img/
                    gatito.png
                    perrito.png
        templates/
            boards/
                author.html
                base.html
                datosform.html
                example.html
                fecha.html
                formulario1.html
                gracias.html
                name.html
                register.html
                login.html
        admin.py
        forms.py
        models.py
        urls.py
        views.py
    proyecto1/
```

## 📘 ¿Qué son los modelos en Django?

Los modelos en Django son clases de Python que representan y definen la estructura de los datos almacenados en una base de datos. Son una parte esencial del *framework* Django y permiten una fácil interacción con la base de datos mediante la manipulación de objetos y métodos de Python en lugar de escribir consultas SQL a mano.

## 🗄️ SQLite

SQLite es una base de datos ligera y de archivo único compatible con Django por defecto. Cuando empezamos un proyecto en Django, se crea automáticamente un archivo de base de datos SQLite llamado `db.sqlite3`.

## 📜 Migrations

En Django, las _migrations_ son archivos de Python que rastrean las modificaciones realizadas en el esquema de la base de datos a lo largo del tiempo, lo que permite realizar cambios en la base de datos sin afectar los datos existentes.

### Makemigrations

`makemigrations` es un comando de Django que crea archivos de migración en función de los cambios detectados en los modelos. Estos archivos describen los cambios realizados en la estructura de la base de datos y permiten a Django aplicar esas modificaciones al esquema real de la base de datos.

### Migrate

`migrate` es otro comando de Django que aplica las migraciones pendientes a la base de datos. Al ejecutar este comando, Django sincroniza la estructura real de la base de datos con la estructura definida en las migraciones recién creadas.

## 🧬 Herencia de models.Model

Para crear un modelo en Django, primero creamos una clase que herede de `models.Model`:

```python
from django.db import models

class Author(models.Model):
    # Campos del modelo

```

Esto permite que nuestra clase `Author` herede todas las opciones y métodos propios de Django, lo que facilita su uso como modelo de base de datos con todas las características que eso implica.

## 🔒 Permisos y seguridad

En esta sección, se han realizado varias modificaciones relacionadas con la seguridad y la gestión de permisos.

Se ha agregado un modelo llamado `Boards` que representa un tablero y se le ha asignado un permiso llamado `es_miembro_1`. Esto se ha configurado en el archivo `models.py`.

En el archivo `admin.py` se han realizado los siguientes cambios:
- Se han agregado los modelos `Author` y `Boards` al panel de administración de Django.
- Se ha añadido una clase `OnlyReadAdmin` que define que los campos `created` y `updated` solo pueden ser de solo lectura en el panel administrativo.
- Se ha creado una clase `AuthorAdmin` que personaliza la visualización y búsqueda de los autores en el panel de administración.
- Se ha agregado una acción personalizada `actualizar_nombre` que actualiza el nombre de los autores seleccionados en el panel de administración.

## Commits realizados

### 📝 [Commit 1: Explicación ModelForm](https://github.com/zubus/TD-Django-0027/commit/f98a9b577d3a228f7c64cc0055cf8ba9fad1b60e)

En este commit, se realizaron los siguientes cambios:

1. **proyecto1/boards/forms.py**: Se estableció la conexión entre el modelo `Author` y el formulario `AuthorForm` a través de la importación de `ModelForm`. Al crear la clase `AuthorForm` y hacerla heredar de `ModelForm`, se puede utilizar un formulario basado en el modelo `Author`. La clase `Meta` de `AuthorForm` especifica qué modelo y campos se utilizarán en el formulario.

2. **proyecto1/boards/migrations/0001_initial.py**: Este archivo se generó automáticamente al ejecutar `python manage.py makemigrations` y se basa en los cambios realizados en los modelos. Hasta ahora, se han creado dos modelos (`Author` y `Book`), y este archivo contiene las instrucciones necesarias para crear esas tablas en la base de datos.

3. **proyecto1/boards/models.py**: Aquí, se definieron dos modelos: `Author` y `Book`. Estos modelos ayudan a representar la estructura de los datos en la aplicación y están estrechamente relacionados con la base de datos.

4. **proyecto1/boards/templates/boards/author.html**: Este archivo de plantilla define la estructura HTML para la página de registro de autores. Se muestra el formulario `AuthorForm` utilizando la etiqueta `{{ form }}`.

5. **proyecto1/boards/urls.py**: Se agregó una nueva ruta "createauthor/" asociada con la función de vista `create_author`.

6. **proyecto1/boards/views.py**: Se implementó la función de vista `create_author`. Esta función de vista crea instancias del formulario `AuthorForm`, muestra un formulario vacío (en solicitudes GET) y procesa los datos del formulario (en solicitudes POST).

### 📝 [Commit 2: Se agregan ejemplos 2 y 3](https://github.com/zubus/TD-Django-0027/commit/b7790db24e23582a380a81d0e53d5ff50245884c)

En este commit, se realizaron los siguientes cambios:

1. **proyecto1/boards/forms.py**: Se agregó la nueva clase `InputForm` que hereda de `forms.Form` para mostrar cómo agregar diferentes tipos de campos al formulario. Estos campos sirven como un ejemplo práctico de cómo personalizar formularios.

2. **proyecto1/boards/templates/boards/datosform.html**: Esta plantilla muestra cómo utilizar la clase `InputForm` en nuestras vistas. Se crea una estructura de formulario similar a la vista 'author', pero esta vez se utiliza la clase `InputForm`.

3. **proyecto1/boards/urls.py**: Se agregó una nueva ruta "datosform/" y se asoció con la función de vista `datosform_view`.

4. **proyecto1/boards/views.py**: Se implementó la función de vista `datosform_view`. Esta función de vista maneja únicamente las solicitudes GET. Aunque no procesa los datos del formulario, muestra cómo crear y presentar un formulario en Django mediante una función de vista y una plantilla.

### 📝 [Commit 3: Se instala Crispy Form y se crea el formulario de registro](https://github.com/zubus/TD-Django-0027/commit/ce061b4c6bda50aee505b22bbf3623ca85a44a95)

1. **proyecto1/boards/forms.py**: En este archivo, agregamos la clase `UserRegisterForm`, que hereda de `UserCreationForm`. Este formulario se utilizará para registrar nuevos usuarios. Especificamos un campo de correo electrónico como obligatorio y detallamos qué campos se deben llenar en este formulario.

2. **proyecto1/boards/templates/boards/register.html**: Este archivo de plantilla define cómo se verá en el navegador la página de registro. Utilizamos el etiquetado de crispy_forms para mostrar el formulario, permitiendo así un diseño amigable del formulario creado en `UserRegisterForm`.

3. **proyecto1/boards/urls.py**: Agregamos una ruta nueva hacia `/register/` en el URLconf. Cualquier solicitud que venga a esta URL será manejada por la función de vista `register_view`.

4. **proyecto1/boards/views.py**: Implementamos `register_view` la cual maneja las solicitudes GET y POST a la URL `/register/`. En una solicitud GET, el servidor devuelve un formulario de registro vacío. Cuando recibe una solicitud POST, el servidor procesa los datos del formulario y, si son válidos, registra al usuario, inicia una nueva sesión para el usuario y lo redirige a la página de agradecimiento. Si los datos no son válidos, se muestra un mensaje de error.

5. **proyecto1/proyecto1/settings.py**: Añadimos crispy_forms a la lista de aplicaciones instaladas para nuestro proyecto Django. Adicionalmente, especificamos la plantilla de crispy_forms a utilizar.

### 📝 [Commit 4: Se crea un login y un logout para la aplicación](https://github.com/zubus/TD-Django-0027/commit/9d3f889ba372d4f30209ecd1504f7de403e36c91)

1. **proyecto1/boards/templates/boards/base.html**: En este archivo, modificamos la barra de navegación para mostrar el nombre de usuario cuando un usuario ha iniciado sesión. También, añadimos un enlace para que los usuarios puedan cerrar su sesión.

2. **proyecto1/boards/templates/boards/login.html**: Este archivo de plantilla define cómo se verá la página de inicio de sesión en el navegador. Al igual que con el formulario de registro, utilizamos el etiquetado de crispy_forms para mostrar el formulario de inicio de sesión.

3. **proyecto1/boards/templates/boards/register.html**: Añadimos un mensaje indicando que si el usuario ya tiene una cuenta puede iniciar sesión visitando la página de login.

4. **proyecto1/boards/urls.py**: Agregamos rutas nuevas para el inicio y cierre de sesión en el URLconf. Cualquier solicitud que venga a estas URLs será manejada por las funciones de vista `login_view` y `logout_view`, respectivamente.

5. **proyecto1/boards/views.py**: Implementamos `login_view` y `logout_view`. `login_view` maneja las solicitudes GET y POST a la URL `/login/`. En una solicitud GET, el servidor devuelve un formulario de inicio de sesión vacío. Cuando recibe una solicitud POST, el servidor procesa los datos del formulario y, si son válidos, inicia una nueva sesión para el usuario y lo redirige a la página de agradecimiento. Si los datos no son válidos, se muestra un mensaje de error. Por otro lado, `logout_view` simplemente termina la sesión del usuario y redirige a la página de inicio de sesión.

### 📝 [Commit 5: Se agrega permiso en Boards, además de LoginRequiredMixin y PermissionRequiredMixin](https://github.com/zubus/TD-Django-0027/commit/52edc3ce72864340cbac01907fce94aeb346ee54)

1. **proyecto1/boards/migrations/0002_boards.py** y **proyecto1/boards/migrations/0003_alter_boards_options.py**: Se crearon dos archivos de migración. El primero para crear el modelo Boards (una tabla en la base de datos) y el segundo para establecer opciones/permisos para el modelo Boards.

2. **proyecto1/boards/models.py**: Creamos el modelo `Boards`, que contendrá el título y descripción de un board en específico. También hicimos uso de `verbose_name` y `verbose_name_plural` para dar nombres legibles  a los modelos. Además, definimos un método `get_absolute_url` para devolver una URL a una instancia de modelo específica.

3. **proyecto1/boards/templates/boards/base.html**: Actualizamos la barra de navegación para mostrar el nombre de usuario sólo cuando un usuario ha iniciado sesión.

4. **proyecto1/boards/views.py**: Implementamos el uso de `LoginRequiredMixin` y `PermissionRequiredMixin` para restringir el acceso a ciertas vistas basadas en clases. Estos mixins aseguran que sólo los usuarios autenticados que tengan los permisos necesarios puedan acceder a estas vistas.

### 📝 [Commit 6: Se agregan modificaciones y los modelos al panel de Admin de Django](https://github.com/zubus/TD-Django-0027/commit/400db097650400a3c2c2c50503203a9b2104e70c)

1. **proyecto1/boards/admin.py**: Este archivo fue modificado para personalizar el panel de administración de Django. Definimos un par de clases, `OnlyReadAdmin` y `AuthorAdmin`, para modificar la forma en la que los modelos de Book y de Author se exhiben en el panel de administración.

2. **proyecto1/boards/models.py**: Se hicieron modificaciones en los modelos para que sean más amigables al usuario. Se definieron nombres legibles en español para las instancias del modelo usando `verbose_name`.

3. **proyecto1/boards/views.py**: Agregamos los decoradores `login_required` y `permission_required` a nuestras vistas basadas en funciones para restringir el acceso a usuarios autenticados con los permisos necesarios.

### 📝 [Commit 7: Ultimas modificaciones panel admin](https://github.com/zubus/TD-Django-0027/commit/93c4f7a3c493d79333d73e34ec29f3d6687aaa55)

1. **proyecto1/boards/admin.py**: Nuevas personalizaciones en el panel de administración. Añadimos una acción para actualizar el nombre de todas las filas seleccionadas en el modelo Author en el panel administrativo.

2. **proyecto1/boards/models.py**: Se añadió un método `get_absolute_url` atodos nuestros modelos. Este método es útil para obtener la URL de una instancia de un modelo.

3. **proyecto1/boards/views.py**: Se añadió la vista `AuthorUpdateView`, que permite actualizar el nombre de un autor. Además, se modificaron las vistas `BookDetailView` y `AuthorDetailView` para hacer uso del método `get_absolute_url` al redirigir al usuario.

4. **proyecto1/boards/templates/boards/author_detail.html** y **proyecto1/boards/templates/boards/book_detail.html**: Se utilizaron las nuevas vistas para permitir al usuario actualizar fácilmente el nombre de un autor o ver los detalles de un libro. Para esto, se añadieron enlaces al formulario de actualización y a las páginas de detalles respectivas.
