# 🎉 Instalación de Django en Windows: Paso a paso 🚀

En este README aprenderás a instalar un proyecto de Django en Windows utilizando tanto la consola de comandos (terminal) de Windows como Git Bash. Seguiremos los siguientes pasos:

1. [🐍 Instalación de Python y Pip](#1-instalación-de-python-y-pip)
2. [🌐 Creación del entorno virtual (mientornovirtual)](#2-creación-del-entorno-virtual-mientornovirtual)
3. [🎆 Instalación de Django](#3-instalación-de-django)
4. [📝 Creación del proyecto de Django (miprimerproyecto)](#4-creación-del-proyecto-de-django-miprimerproyecto)
5. [📂 Archivos y directorios más importantes en un proyecto Django recién creado](#5-archivos-y-directorios-más-importantes-en-un-proyecto-django-recién-creado)
6. [🔧 Comandos básicos de Django en la terminal](#6-comandos-básicos-de-django-en-la-terminal)

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

🥳 ¡Listo! Recuerda siempre revisar la [documentación oficial de Django](https://docs.djangoproject.com/en/stable/intro/tutorial01/).

## 5. 📂 Archivos y directorios más importantes en un proyecto Django recién creado

```
miprimerproyecto/
├─ miprimerproyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└─ manage.py
```

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
