# 🎉 Instalación de Django en Windows: Paso a paso 🚀

En este README aprenderás a instalar un proyecto de Django en Windows utilizando tanto la consola de comandos (terminal) de Windows como Git Bash. Seguiremos los siguientes pasos:

1. [🐍 Instalación de Python y Pip](https://github.com/zubus/TD-Django-0027#1--instalación-de-python-y-pip)
2. [🌐 Creación del entorno virtual (mientornovirtual)](https://github.com/zubus/TD-Django-0027#2--creación-del-entorno-virtual-mientornovirtual)
3. [🎆 Instalación de Django](https://github.com/zubus/TD-Django-0027#3--instalación-de-django)
4. [📝 Creación del proyecto de Django (miprimerproyecto)](https://github.com/zubus/TD-Django-0027#4--creación-del-proyecto-de-django-miprimerproyecto)
5. [📂 Archivos y directorios más importantes en un proyecto Django recién creado](https://github.com/zubus/TD-Django-0027#5--archivos-y-directorios-más-importantes-en-un-proyecto-django-recién-creado)
6. [🔧Comandos básicos de Django en la terminal](https://github.com/zubus/TD-Django-0027#6--Comandos-básicos-de-Django-en-la-terminal)
7. [📘Explicación del archivo settings.py de Django](https://github.com/zubus/TD-Django-0027#7--Explicación-del-archivo-settings.py-de-Django)

## 1. 🐍 Instalación de Python y Pip

Antes de comenzar, asegúrate de tener Python 3.8 o superior instalado. Para verificar si ya lo tienes instalado, abre la consola de comandos (cmd) y ejecuta:

```
python --version
```

También es necesario tener instalado `pip`. Para verificar si lo tienes instalado, ejecuta:

```
pip --version
```

Si necesitas descargar Python o Pip, visita la página oficial de [Python](https://www.python.org/downloads/) y sigue las instrucciones para instalarlos en Windows.

## 2. 🌐 Creación del entorno virtual (`mientornovirtual`)

Un entorno virtual te permite aislar las dependencias de tu proyecto de Django de las dependencias globales de tu sistema.

Abre la consola de comandos (terminal) o Git Bash y navega hasta la carpeta donde deseas crear tu entorno virtual. Por ejemplo, si deseas crearlo en `C:\proyectos\`, ejecuta:

```
cd C:\proyectos
```

A continuación, ejecuta el siguiente comando para crear un entorno virtual llamado `mientornovirtual`:

```
python -m venv mientornovirtual
```

### Activación del entorno virtual

- **🖥️ Si usas la terminal de Windows**, activa el entorno virtual ejecutando:

  ```
  mientornovirtual\Scripts\activate
  ```

- **🦊 Si usas Git Bash**, activa el entorno virtual con el siguiente comando:

  ```
  source mientornovirtual/Scripts/activate
  ```

Verás que el nombre de tu entorno virtual aparece al inicio de la línea de comandos, indicando que está activado.

## 3. 🎆 Instalación de Django

Con el entorno virtual activado, instala Django utilizando el siguiente comando:

```
pip install django
```

Una vez que la instalación haya finalizado, verifica que Django se instaló correctamente ejecutando:

```
django-admin --version
```

## 4. 📝 Creación del proyecto de Django (`miprimerproyecto`)

Ahora que tienes Django instalado, es hora de crear tu primer proyecto. Ejecuta el siguiente comando para crear un proyecto llamado `miprimerproyecto` en la carpeta actual:

```
django-admin startproject miprimerproyecto
```

Navega a la carpeta del proyecto:

```
cd miprimerproyecto
```

Por último, inicia el servidor de desarrollo de Django:

```
python manage.py runserver
```

Abre tu navegador y visita [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Verás la página de bienvenida de Django, lo que significa que has instalado y configurado correctamente tu proyecto de Django en Windows.

¡Listo!

## 5. 📂 Archivos y directorios más importantes en un proyecto Django recién creado

```
mientornovirtual/
miprimerproyecto/
├─ miprimerproyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└─ manage.py
```

0. **mientornovirtual (entorno virtual)**: El entorno virtual no es parte del proyecto Django, pero es recomendable tenerlo en cuenta debido a su importancia en el desarrollo con Django. Puedes mover el entorno virtual a otra carpeta de tu equipo si así lo deseas, pero recuerda siempre activarlo antes de trabajar con tu proyecto Django. Contiene las bibliotecas y dependencias específicas de tu proyecto para aislarlas de las dependencias globales del sistema.

1. **miprimerproyecto (carpeta raíz)**: Contiene todo el proyecto y sus aplicaciones. Todos los archivos y directorios relacionados con el proyecto se ubicarán dentro de esta carpeta.

2. **miprimerproyecto (subcarpeta)**: Esta carpeta contiene la configuración principal del proyecto.

    - **__init__.py**: Este archivo vacío indica que el directorio que lo contiene es un paquete Python. Esto permite importar módulos desde esta carpeta.

    - **asgi.py**: Este archivo define la configuración de ASGI (Asynchronous Server Gateway Interface) para el proyecto. ASGI es una especificación más moderna que permite a tu aplicación Django funcionar en servidores asíncronos, como Daphne o Hypercorn.

    - **settings.py**: Aquí puedes configurar todo tipo de ajustes para tu proyecto, como la base de datos, el middleware, las aplicaciones instaladas, la configuración de correo electrónico, etc. Es uno de los archivos más importantes a personalizar al desarrollar un proyecto de Django.

    - **urls.py**: Este archivo contiene las definiciones de las URL para el proyecto. Aquí es donde se asignan las rutas URL a las vistas de tus aplicaciones Django.

    - **wsgi.py**: Este archivo define la configuración de WSGI (Web Server Gateway Interface) para el proyecto. WSGI es una especificación que permite a tu aplicación Django funcionar en servidores sincrónicos, como Gunicorn o uWSGI.

3. **manage.py**: Este archivo es un archivo ejecutable de línea de comandos. Actúa como interfaz entre el desarrollador y el proyecto, permitiendo ejecutar comandos útiles como `runserver`, `makemigrations` o `migrate`, entre otros.

## 6. 🔧 Comandos básicos de Django en la terminal

- `django-admin startproject miproyecto`: Crea un nuevo proyecto Django llamado `miproyecto`.
- `python manage.py startapp miapp`: Crea una nueva aplicación Django llamada `miapp` dentro del proyecto en el que te encuentras.
- `python manage.py runserver`: Inicia el servidor de desarrollo de Django en el puerto 8000.
- `python manage.py makemigrations`: Genera migraciones basadas en los cambios realizados en los modelos de las aplicaciones.
- `python manage.py migrate`: Aplica las migraciones pendientes a la base de datos.
- `python manage.py createsuperuser`: Crea un nuevo superusuario con acceso al panel de administración de Django.
- `python manage.py shell`: Abre una shell de Python con el entorno de tu proyecto cargado, lo que te permite interactuar con tus modelos y otras partes de Django.
- `python manage.py collectstatic`: Recopila todos los archivos estáticos de tus aplicaciones en el directorio `STATIC_ROOT`.
- `python manage.py test`: Ejecuta las pruebas del proyecto.

## 7. 📘 Explicación del archivo settings.py de Django

El archivo `settings.py` de Django es uno de los archivos más importantes en cualquier proyecto de Django, ya que es el lugar donde se definen y configuran diversos aspectos de la aplicación utilizando estructuras de datos de Python como listas y diccionarios. Estas configuraciones incluyen aspectos como el tipo de base de datos a utilizar, la configuración de correo electrónico, la internacionalización, entre otros. Las distintas secciones del archivo `settings.py`, creado por defecto en Django, se explican a continuación en detalle.

### Importación de módulos y definición de rutas del proyecto

```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
```

Esta parte del archivo importa el módulo `Path` de la biblioteca `pathlib` para manejar las rutas del proyecto de una manera más fácil y legible. `BASE_DIR` almacena el directorio base del proyecto, es decir, la ruta absoluta del directorio que contiene el archivo `settings.py`.

### Configuración de seguridad y depuración

```python
SECRET_KEY = ""

DEBUG = True

ALLOWED_HOSTS = []
```

* `SECRET_KEY`: Es una cadena única que Django utiliza para proporcionar seguridad criptográfica a la aplicación. Nunca debe revelarse y debe cambiarse para cada proyecto en producción.
* `DEBUG`: Es un valor booleano (`True`/`False`) que determina si la aplicación está en modo de depuración o no. Cuando está en `True`, Django mostrará páginas de error detalladas, incluidos los errores de servidor. Este valor debe estar en `False` en entornos de producción.
* `ALLOWED_HOSTS`: Es una lista de cadenas que definen los nombres de host en los que se permite que la aplicación se ejecute. En entornos de desarrollo, esta lista puede estar vacía, pero en producción, debe incluir todos los nombres de host válidos de la aplicación.

### Definición de aplicaciones, middleware y configuración de URL

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    # ...
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # ...
]

ROOT_URLCONF = "proyecto1.urls"
```

* `INSTALLED_APPS`: Es una lista de las aplicaciones que forman parte del proyecto. Por defecto, incluye aplicaciones de Django como el administrador y la autenticación de usuarios, pero puedes agregar tus propias aplicaciones a la lista para incluirlas en tu proyecto.
* `MIDDLEWARE`: Es una lista de los middleware que la aplicación utiliza. Son componentes que procesan las solicitudes y respuestas y pueden modificarlos o generar otros efectos secundarios antes de que lleguen a las vistas o se envíen al cliente.
* `ROOT_URLCONF`: Es la ubicación del módulo de configuración de URLs del proyecto.

### Configuración de plantillas

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        # ...
    },
]
```

`TEMPLATES` es una lista de configuraciones para las plantillas de Django. Puede contener múltiples motores de plantillas y configuraciones, pero generalmente solo se utiliza uno, el motor de plantillas de Django.

### Aplicación WSGI

```python
WSGI_APPLICATION = "proyecto1.wsgi.application"
```

Esta línea define la ubicación de la aplicación `WSGI`, que es la interfaz entre el servidor web y la aplicación de Django.

### Configuración de la base de datos

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

`DATABASES` es un diccionario que contiene las configuraciones de las bases de datos que se utilizarán en el proyecto. Por defecto, se utiliza SQLite como base de datos, pero puedes cambiarla a otro sistema de bases de datos como PostgreSQL, MySQL, etc.

### Validación de contraseñas

```python
AUTH_PASSWORD_VALIDATORS = [
    # ...
]
```

Esta lista contiene configuraciones para diferentes validadores de contraseñas que se ejecutan cuando un usuario crea o cambia su contraseña en la aplicación. Puedes agregar o eliminar validadores según las reglas de contraseñas que desees aplicar en tu proyecto.

### Internacionalización

```python
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True
```

Estas configuraciones definen el idioma y la zona horaria por defecto del proyecto, así como si se debe aplicar internacionalización (soporte para múltiples idiomas) y la conversión de zonas horarias.

### Archivos estáticos y clave de campo primario por defecto

```python
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

* `STATIC_URL`: Es la URL base para los archivos estáticos del proyecto (CSS, JavaScript, imágenes, etc.).
* `DEFAULT_AUTO_FIELD`: Es el tipo de campo primario utilizado por defecto en los modelos de Django. 

Recuerda siempre revisar la [documentación oficial de Django]([https://docs.djangoproject.com/en/4.2/topics/settings/](https://docs.djangoproject.com/en/4.2/)) y la [referencia completa de configuración](https://docs.djangoproject.com/en/4.2/ref/settings/).
