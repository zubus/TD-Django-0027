## Módulo 6 - Sesiones 5 y 6

### 🗂️ Estructura del proyecto
```
proyecto1/
    boards/
        static/
            boards/
                img/
                    gatito.png
                    perrito.png
        templates/
            boards/
                base.html
                example.html
                fecha.html
                formulario1.html
                gracias.html
                name.html
        forms.py
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
Puedes encontrar la información sobre filtros y tags en la [Documentación de Django](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/) y en [w3schools](https://www.w3schools.com/django/ref_tags_filter.php).

### 📝 [Commit 6: Agregar archivos estáticos y tag "url" en Django Templates](https://github.com/zubus/TD-Django-0027/commit/e6e200191501691d1b4bbaa2c81493289f44b8c7)

En este commit, se explica cómo agregar archivos estáticos en el Django Template, así como el uso del tag "url". Los cambios realizados incluyen:

1. Se añadieron imágenes de gatito y perrito en la carpeta `proyecto1/boards/static/boards/img/` .

2. Se modificó el archivo `proyecto1/boards/templates/boards/fecha.html` para incluir el uso de imágenes estáticas con la etiqueta `{% static %}`.

3. Se creó un archivo de ejemplo `proyecto1/boards/templates/boards/example.html`. Este archivo muestra cómo utilizar el objeto `persona` para presentar el nombre y apellido en un template.

4. Se actualizó el archivo `proyecto1/boards/views.py` para crear una función de vista para el archivo `example.html`, que utiliza la clase `Persona` para crear un objeto `persona` con el nombre y apellido, y lo envía como parte del contexto.

5. Se modificó el archivo `proyecto1/boards/urls.py` para agregar una nueva ruta que enlaza a la función de vista creada en el paso 4: `example/`, con el nombre `"example"`.

6. Se añadió el tag `{% url %}` en el archivo `proyecto1/boards/templates/boards/fecha.html`, que genera la URL para la vista a la que se dirige el botón en la tarjeta.

Con estos cambios, ahora se pueden mostrar imágenes estáticas en el template y utilizar el tag "url" para enlazar a otras vistas en el proyecto.

### 📝 [Commit 7: Añadir formularios tanto de manera manual como con `forms.Form`](https://github.com/zubus/TD-Django-0027/commit/6123c1ac9093c691c4a046c7a80017b65dad79f3)

En este commit, se agregan formularios de dos maneras diferentes: manualmente y utilizando la clase `forms.Form` de Django. Los cambios incluyen:

1. Creación del archivo `proyecto1/boards/forms.py`:

```python
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='enter your name:', max_length=100)
    pet = forms.CharField(label='enter pet name:', max_length=100)
    country = forms.CharField(label='enter your country:', max_length=100)
```

En este archivo, se crea una nueva clase `NameForm` que hereda de `forms.Form`. Se definen tres campos de tipo `CharField` con etiquetas y longitudes máximas específicas.

2. Creación del archivo `proyecto1/boards/templates/boards/formulario1.html`:

```html
{% extends 'boards/base.html' %}

{% block contenido %}
<div class="row">
    <form action="/getname/" method="post">
        {% csrf_token %}
        <label for="your_name">tu nombre: </label>
        <input id="your_name" type="text" name="your_name" value="">
        <input type="submit" value="OK">
    </form>
</div>
{% endblock contenido %}
{% block prueba %}{% endblock prueba %}
```

En este template, se crea un formulario simple de manera manual incluyendo el campo `your_name` y el botón de envío.

Respecto a `{% csrf_token %}` en el template `formulario1.html`, eso es una etiqueta especial que se utiliza para agregar un token de seguridad CSRF (Cross-Site Request Forgery) al formulario. 

CSRF es una vulnerabilidad que puede permitir a un atacante falsificar una solicitud a un sitio web y realizar acciones no deseadas en nombre del usuario. Django incluye medidas de seguridad para proteger contra esto, y una de ellas es el uso del token CSRF.

Al incluir la etiqueta `{% csrf_token %}` dentro del formulario, se agrega automáticamente un campo oculto con el token CSRF. Esto es necesario para que Django pueda verificar que los formularios enviados provienen de la página actual y no de un ataque CSRF.

3. Creación del archivo `proyecto1/boards/templates/boards/name.html`:

```html
{% extends 'boards/base.html' %}

{% block contenido %}
<form action="/getname/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
</form>
{% endblock contenido %}
{% block prueba %}{% endblock prueba %}
```

En este template, se crea un formulario que utiliza `NameForm` para definir y renderizar sus campos automáticamente.

4. Creación del archivo `proyecto1/boards/templates/boards/gracias.html`:

```html
{% extends 'boards/base.html' %}
{% block contenido %}
<h1 class="text-success"> Los datos han sido enviados correctamente</h1>
{% endblock contenido %}
{% block prueba %}{% endblock prueba %}
```
Aquí se muestra un mensaje cuando el formulario ha sido enviado correctamente.

5. Actualización del archivo `proyecto1/boards/urls.py` para agregar rutas necesarias:

```python
from .views import (get_date_view, name_view, mostrar, formulario_nombre,
                    get_name, thanks)

urlpatterns = [
    # ... otras rutas ...
    path("formulario/", formulario_nombre, name="formulario"),
    path("getname/", get_name, name="get_name"),
    path("thanks/", thanks, name="thanks"),
]
```

6. Actualización del archivo `proyecto1/boards/views.py` para agregar las funciones de vistas correspondientes a los nuevos formularios y plantillas:

```python
from .forms import NameForm

# ... otras funciones de vista ...

def formulario_nombre(request):
    return render(request, 'boards/formulario1.html')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
        context= {'form':form}
        return render(request, 'boards/name.html',context)

def thanks(request):
    return render(request, "boards/gracias.html")
```

Esta función de vista maneja las solicitudes (`request`) enviadas al formulario. A través del método `POST`, se verifica si el formulario ha sido enviado. 

- Si es una solicitud `POST`, el formulario `NameForm` se crea utilizando los datos enviados (`request.POST`). Luego, se verifica si el formulario es válido mediante el método `is_valid()`. Si lo es, se redirige al usuario a la página de agradecimiento (`/thanks/`) utilizando `HttpResponseRedirect`.

- Si es una solicitud `GET` o cualquier otro método de solicitud, se crea una instancia vacía del formulario `NameForm` y se renderiza el template `'boards/name.html'` junto con el contexto que contiene el formulario.

Con estos cambios, se han implementado dos métodos diferentes para crear formularios en Django.

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

### 🛠️ Cómo agregar archivos estáticos y el tag "url" en tus templates

#### 1. Agregar archivos estáticos

Coloca tus archivos estáticos (imágenes, CSS, JavaScript) en una carpeta denominada `static` dentro de la aplicación en la que se utilizarán. En este ejemplo, se colocaron las imágenes `gatito.png` y `perrito.png` en la carpeta `proyecto1/boards/static/boards/img/`.

Carga el archivo estático en tu template utilizando `{% load static %}`. Luego, utiliza la etiqueta `{% static 'ruta/al/archivo' %}` para agregar el archivo estático en tu HTML. Por ejemplo:

```html
{% load static %}
<img src="{% static 'boards/img/gatito.png' %}" class="card-img-top" alt="...">
```

#### 2. Añadir el tag "url" en tu template

Utiliza el tag `{% url 'nombre_de_la_vista' %}` para generar la URL de una vista en tu template. Por ejemplo:

```html
<a href="{% url 'name' %}" class="btn btn-primary">Ir a name</a>
```

Esto generará la URL para la vista llamada `name` y creará un enlace a la página correspondiente.

### 🔄 Reutilización y mantenimiento del código: Herencia de templates

La herencia de templates en Django es una técnica que permite reutilizar el código HTML en diferentes archivos de plantillas. Mediante la creación de un archivo de template base (por ejemplo, `base.html`), se pueden definir bloques de contenido que otros templates pueden sobrescribir o extender.
