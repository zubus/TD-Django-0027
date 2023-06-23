## Módulo 6 - Sesión 5

### 🗂️ Estructura del proyecto
```
proyecto1/
    boards/
        templates/
            boards/
                base.html
                fecha.html
        urls.py
        views.py
    proyecto1/
        settings.py
```

### 📝 Commits realizados

### 📝 [Commit 1: Mostrar fecha actual en una vista](https://github.com/zubus/TD-Django-0027/commit/8c487c0ec4797abacb45faf3e9a696ae02902a74)

En este commit, se añadió una vista en Django para mostrar la fecha actual. Los cambios realizados incluyen:

1. Creación del archivo `fecha.html` en la carpeta `boards/templates/boards`. Este archivo contiene el código HTML que muestra la fecha actual utilizando la variable `{{ fecha }}`.

2. En `boards/urls.py`, se añadió una nueva ruta que enlaza a la función `get_date_view()` en el archivo `boards/views.py`. La ruta es `date/` y su nombre es `"get_date"`.

3. En `boards/views.py`, se definió la función `get_date_view(request)`, que obtiene la fecha actual usando la función `datetime.now()` y la pasa al contexto (`context`) como `fecha`. A continuación, la función `render()` se utiliza para mostrar `fecha.html` con el contexto provisto.

### 📝 [Commit 2: Añadir ejemplo con nombre al mostrar fecha](https://github.com/zubus/TD-Django-0027/commit/16bb68d046b0216cdc944beeacf09022260cbdf9)

En este commit, se actualizó el ejemplo anterior para incluir un nombre en la URL y mostrar un mensaje de bienvenida con el nombre en `fecha.html`. Los cambios incluyen:

1. Modificación de `fecha.html` para agregar un mensaje de bienvenida con la variable `{{ nombre }}`.

2. En `boards/urls.py`, se actualizó la ruta que enlaza a `get_date_view()` para aceptar una variable `name`. La ruta es ahora `date/<str:name>/` y su nombre sigue siendo `"get_date"`.

3. En `boards/views.py`, la función `get_date_view(request, name)` se modificó para aceptar un parámetro adicional, `name`. Luego, se añade el `name` al contexto y se muestra en `fecha.html`.

### 📝 [Commit 3: Añadir Bootstrap 5 a `fecha.html` y al proyecto](https://github.com/zubus/TD-Django-0027/commit/f3f3854b29ff9735e78bb759ad5909e7cc4f5eee)

Se añadió Bootstrap 5 al proyecto para estilizar `fecha.html`. Los cambios incluyen:

1. Modificación de `fecha.html` para cargar e importar las etiquetas necesarias de Bootstrap 5.
2. En el archivo `proyecto1/settings.py`, se añadió la aplicación `"bootstrap5"` a la lista de aplicaciones instaladas.

### 📝 [Commit 4: Añadir base.html con navbar y heredar desde `fecha.html`](https://github.com/zubus/TD-Django-0027/commit/e7b910c6de5e4c40badc5a36cae77a4a6ed8b2ca)

En este commit, se introdujo la herencia de templates de Django añadiendo un archivo `base.html` con un navbar y luego heredando su estructura desde `fecha.html`. Los cambios incluyen:

1. Creación del archivo `base.html` en la carpeta `boards/templates/boards`. Este archivo contiene la estructura base del proyecto, incluyendo la etiqueta de bloque `{% block contenido %}` que permite a otros templates heredar y modificar el contenido de esta sección.

2. Modificación de `fecha.html` para heredar de `base.html` utilizando la etiqueta `{% extends 'boards/base.html' %}` y luego definir su contenido específico dentro de un bloque `{% block contenido %}`.

Con estos cambios, hemos implementado el sistema de herencia de templates de Django que permite reutilizar código HTML base en diferentes páginas del proyecto, facilitando el mantenimiento y la coherencia visual del sitio web.

### 📝 [Commit 5: Agregar ejemplos de filtros y tags](https://github.com/zubus/TD-Django-0027/commit/ee78ebe49b6b4fac504387a93e0267a24c0d0c8f)

En este commit, se agregan ejemplos de filtros y tags en `fecha.html` y `base.html`. Los cambios incluyen:

1. En `base.html`, se añade un bloque de título `{% block titulo %}{% endblock titulo %}` que permite a los templates que heredan de `base.html` personalizar el título de la página.
   
2. Modificación de `fecha.html` para incluir un ejemplo de filtro que convierte el mensaje de bienvenida a mayúsculas usando `{% filter upper %}` y `{% endfilter %}`.

3. En `fecha.html`, se añade el bloque de prueba `{% block prueba %}` en el que se muestran algunas acciones condicionales como `{% if ... %}`, `{% elif ... %}` y `{% else %}` junto con un ejemplo de bucle `{% for ... %}`.

4. En `views.py`, se importa la función `randint` para obtener números enteros aleatorios y se añaden más variables al contexto para incluir frutas y un número aleatorio.

Con estos cambios, hemos demostrado el uso de filtros y tags en Django Template Language, que permite mayor control sobre la presentación y manipulación de datos en los templates del proyecto.

### 📚 Conceptos clave

#### 1. Templates

Un template en Django es un archivo HTML que contiene marcado HTML y etiquetas de plantilla propias de Django. Estos templates se utilizan para generar el contenido de un sitio web de manera dinámica y permiten separar la lógica de presentación de la lógica de negocio en una aplicación web.

#### 2. Lenguaje de plantillas de Django (DTL)

El Lenguaje de Plantillas de Django (DTL, por sus siglas en inglés) es un sistema de marcado que permite agregar lógica de presentación (como bucles y condicionales) y datos dinámicos directamente en el archivo HTML. DTL incluye etiquetas (como `{% for %}`, `{% if %}`) y variables (como `{{ variable }}`) para incluir dicha lógica.

### 🛠️ Cómo utilizar el sistema de templates

#### 1. Renderización de templates

En tu archivo `views.py`, importa la función `render()` de Django y crea una función de vista que renderiza el template con un contexto específico. En el ejemplo de los commits previos se usa el archivo `fecha.html` y la función `get_date_view(request, name)`, donde el contexto contiene el nombre y la fecha actual:

```python
from django.shortcuts import render
import datetime

def get_date_view(request, name):
    fecha_actual = datetime.datetime.now()
    context = {
        'fecha': fecha_actual,
        'nombre': name
    }
    return render(request, 'boards/fecha.html', context)
```

#### 2. Conectar la vista con el template mediante la URL

En tu archivo `urls.py`, crea una nueva ruta que apunte a la función de vista `get_date_view(request, name)` que acabas de crear. En nuestro ejemplo, la ruta utilizada es `date/<str:name>/`, lo que significa que la URL debe ser seguida por el nombre del usuario. 

```python
from django.urls import path
from .views import get_date_view

urlpatterns = [
    # ... otras rutas ...
    path("date/<str:name>/", get_date_view, name="get_date"),
]
```

De esta manera, al acceder a la URL `date/Nombre`, se renderizará `fecha.html` con los datos proporcionados en el contexto.

#### 3. Filtros

Los filtros en Django permiten aplicar transformaciones a las variables dentro de los templates. Por ejemplo, el filtro `upper` transforma una cadena de texto en mayúsculas y se puede usar de la siguiente manera en un template:

```html
{% filter upper %}
    <h1>Bienvenido {{nombre}}</h1>
{% endfilter %}
```

#### 4. Tags

Los tags en Django son pequeñas piezas de código que agregan lógica adicional a los templates sin necesidad de modificar el archivo `views.py`. Ejemplos de tags incluyen `{% if %}`, `{% for %}`, `{% block %}`, entre otros. Estos tags añaden estructuras condicionales, bucles y bloques personalizables en los templates.

```html
{% for fruta in frutas %}
    <li>{{fruta}}</li>
{% endfor %}
```

### 🛠️ Cómo agregar filtros, condicionales y bucles a tus templates

1. En tu archivo HTML, coloca el filtro, tag o bucle dentro de las etiquetas del bloque de contenido.

2. Envía las variables requeridas desde la vista como parte del contexto.

3. No olvides proporcionar los datos de prueba en tu vista para poder probar las funcionalidades de los filtros, condicionales y bucles en tus templates.

### 🔄 Reutilización y mantenimiento del código: Herencia de templates

La herencia de templates en Django es una técnica que permite reutilizar el código HTML en diferentes archivos de plantillas. Mediante la creación de un archivo de template base (por ejemplo, `base.html`), se pueden definir bloques de contenido que otros templates pueden sobrescribir o extender.
