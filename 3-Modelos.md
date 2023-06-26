# Modelos en Django

## 🗂️ Estructura del proyecto actualizada
```
proyecto1/
    boards/
        migrations/
            0001_initial.py
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

Esto permite que nuestra clase `Author` herede todas las propias opciones y métodos de Django, lo que facilita su uso como modelo de base de datos con todas las características que eso implica.

## 📝 Commits realizados

### 📝 [Commit 1: Explicación ModelForm](https://github.com/zubus/TD-Django-0027/commit/f98a9b577d3a228f7c64cc0055cf8ba9fad1b60e)

1. **proyecto1/boards/forms.py**: En este archivo, hicimos la conexión entre el modelo `Author` y el formulario `AuthorForm` a través de la importación de `ModelForm`. Al crear la clase `AuthorForm` y hacerla heredar de `ModelForm`, ahora podemos utilizar un formulario basado en el modelo `Author`. La clase Meta de `AuthorForm` especifica qué modelo y campos se utilizarán en el formulario.

   Este cambio es esencial para comprender cómo Django puede manejar los formularios basados en un modelo directamente sin necesitar campos de formulario regulares.

2. **proyecto1/boards/migrations/0001_initial.py**: Este archivo se genera automáticamente cuando ejecutamos `python manage.py makemigrations` y se basa en los cambios realizados en los modelos. Hasta ahora, se han creado dos modelos (`Author` y `Book`), y este archivo contiene las instrucciones necesarias para crear esas tablas en la base de datos.

   Aprender sobre las migraciones es un paso crucial, ya que refuerza la comprensión de cómo Django maneja la conexión entre los modelos de Python y la base de datos subyacente.

3. **proyecto1/boards/models.py**: Aquí, definimos dos modelos: `Author` y `Book`. Estos modelos ayudan a representar la estructura de los datos en nuestra aplicación y están estrechamente relacionados con la base de datos.

   Crear y comprender la estructura de los modelos es crucial para trabajar con Django, ya que esto es lo que nos permite aprovechar su ORM (Object-Relational Mapping) y mantener una interacción limpia y organizada entre nuestra aplicación y la base de datos.

4. **proyecto1/boards/templates/boards/author.html**: Este archivo de plantilla define la estructura HTML para la página de registro de autores. Aquí mostramos el formulario `AuthorForm` utilizando el tag `{{ form }}`.

   La creación de plantillas vinculadas a los formularios basados en modelos es importante para aprender cómo Django nos permite generar vistas basadas en la estructura de nuestros modelos directamente.

5. **proyecto1/boards/urls.py**: En este archivo, agregamos una nueva ruta "createauthor/" asociada con la función de vista `create_author`.

   Este cambio ayuda a ilustrar cómo vincular una URL en particular con una vista específica en Django.

6. **proyecto1/boards/views.py**: Aquí se implementa la función de vista `create_author`. Esta función de vista crea instancias del formulario `AuthorForm`, muestra un formulario vacío (en solicitudes GET) y procesa los datos del formulario (en solicitudes POST).

   Con esta función de vista, los principiantes pueden aprender cómo Django maneja y controla la lógica de los formularios.

### 📝 [Commit 2: Se agregan ejemplos 2 y 3](https://github.com/zubus/TD-Django-0027/commit/b7790db24e23582a380a81d0e53d5ff50245884c)

1. **proyecto1/boards/forms.py**: En este archivo, añadimos la nueva clase `InputForm` que hereda de `forms.Form` para mostrar cómo agregar diferentes tipos de campos al formulario. Estos campos servirán como un ejemplo práctico de cómo personalizar formularios.

2. **proyecto1/boards/templates/boards/datosform.html**: Este archivo de plantilla muestra cómo utilizar la clase `InputForm` en nuestras vistas. Se crea una estructura de formulario similar a la vista 'author', pero esta vez usando la clase `InputForm`.

   Con este template, se ejemplifica cómo Django puede mostrar diferentes formularios que no están necesariamente vinculados a un modelo en particular.

3. **proyecto1/boards/urls.py**: Agregamos una nueva ruta "datosform/" y la asociamos con la función de vista `datosform_view`. Este cambio nos enseña cómo añadir nuevas rutas a nuestro proyecto Django y conectarlas con sus respectivas funciones de vista.

4. **proyecto1/boards/views.py**: Implementamos la función de vista `datosform_view`. Esta función de vista maneja únicamente las solicitudes GET. Aunque no procesa los datos del formulario, nos muestra cómo crear y presentar un formulario en Django a través de una función de vista y una plantilla.
