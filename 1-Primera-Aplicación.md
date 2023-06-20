# 🚀 Creación de la primera aplicación en Django (`boards`)

Este tutorial te guiará en la creación de la primera aplicación dentro de tu proyecto Django llamado `miprimerproyecto`. La aplicación se llamará `boards`. Asegúrate de tener activado el entorno virtual "mientornovirtual" antes de continuar.

## 💁 Contenido

1. [Activación del entorno virtual (`mientornovirtual`)](https://github.com/zubus/TD-Django-0027/blob/main/1-Primera-Aplicaci%C3%B3n.md#1--activación-del-entorno-virtual-mientornovirtual)
2. [Creación de la aplicación `boards`](https://github.com/zubus/TD-Django-0027/blob/main/1-Primera-Aplicaci%C3%B3n.md#2--creación-de-la-aplicación-boards)
3. [Registro de la aplicación en Django](https://github.com/zubus/TD-Django-0027/blob/main/1-Primera-Aplicaci%C3%B3n.md#3--registro-de-la-aplicación-en-django)
4. [Estructura de directorios `static` en `boards`](https://github.com/zubus/TD-Django-0027/blob/main/1-Primera-Aplicaci%C3%B3n.md#4--estructura-de-directorios-static-en-boards)
5. [Uso del sistema `static` de Django y configuración en `settings.py`](https://github.com/zubus/TD-Django-0027/blob/main/1-Primera-Aplicaci%C3%B3n.md#5--uso-del-sistema-static-de-django-y-configuración-en-settingspy)
6. [¡Listo!](https://github.com/zubus/TD-Django-0027/blob/main/1-Primera-Aplicaci%C3%B3n.md#6--¡listo)

## 1. 🟢 Activación del entorno virtual (`mientornovirtual`)

Es importante que trabajes siempre dentro del entorno virtual para aislar las dependencias de tu proyecto. Activa el entorno virtual siguiendo las instrucciones para el terminal que estés utilizando:

1. **Windows Terminal**: Ejecuta el siguiente comando para activar el entorno virtual:

```
.\mientornovirtual\Scripts\Activate
```

2. **Git Bash**: Si estás utilizando Git Bash, ejecuta el siguiente comando para activar el entorno virtual:

```
source ./mientornovirtual/Scripts/activate
```

3. **Visual Studio Code**: Si estás utilizando Visual Studio Code, presiona `Ctrl + Shift + P` para abrir la paleta de comandos y escribe "Select Interpreter". Selecciona `Python: Select Interpreter` y elige el entorno virtual que acabas de crear (`mientornovirtual`).

Una vez activado, verás `(mientornovirtual)` al comienzo de la línea en la terminal.

## 2. 🎉 Creación de la aplicación `boards`

Después de activar el entorno virtual, ubícate dentro de la carpeta del proyecto `miprimerproyecto` y ejecuta el siguiente comando para crear la aplicación `boards`:

```
python manage.py startapp boards
```

Este comando crea una nueva carpeta llamada `boards` dentro de tu proyecto con la siguiente estructura:

```
boards/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

Cada uno de estos archivos tiene un propósito específico en la aplicación:

- `migrations/`: Aquí se almacenarán los archivos de migración de la base de datos.
- `admin.py`: Permite la configuración del administrador de Django para la aplicación.
- `apps.py`: Contiene la configuración de la aplicación.
- `models.py`: Aquí se definen los modelos de la base de datos.
- `tests.py`: Permite escribir tests para la aplicación.
- `views.py`: Contiene las vistas de la aplicación.

## 3. 📝 Registro de la aplicación en Django

Para que Django reconozca la nueva aplicación `boards`, es necesario registrarla en el archivo `settings.py` de tu proyecto. Abre el archivo `miprimerproyecto/settings.py` y busca la variable `INSTALLED_APPS`. Agrega `'boards'` a la lista, así:

```python
INSTALLED_APPS = [
    # ...
    'boards',
]
```

Ahora Django sabe que la aplicación `boards` forma parte de tu proyecto y puedes empezar a desarrollar funcionalidades.

## 4. 📂 Estructura de directorios `static` en `boards`

Para gestionar de manera eficiente los archivos estáticos de tu aplicación `boards`, crea dentro de la carpeta `boards` una nueva carpeta denominada `static`. Dentro de esta, crea las siguientes subcarpetas:

- `css`: Aquí almacenarás todos los archivos de hojas de estilo CSS de la aplicación.
- `html`: Aquí almacenarás todos los archivos de plantillas HTML de la aplicación.
- `js`: Aquí almacenarás todos los archivos de código JavaScript de la aplicación.

La nueva estructura de directorios dentro de `boards` debe verse así:

```
boards/
    static/
        css/
        html/
        js/
    migrations/
        __init__.py
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```

## 5. 📚 Uso del sistema `static` de Django y configuración en `settings.py`

El sistema `static` de Django permite administrar y servir los archivos estáticos, como imágenes, hojas de estilo CSS y código JavaScript, de manera eficiente y organizada. Django automáticamente busca y sirve contenido desde la carpeta `static` dentro de cada aplicación.

Para aprovechar al máximo el sistema `static`, es necesario configurarlo en el archivo `settings.py` de tu proyecto. Abre el archivo `miprimerproyecto/settings.py` y busca la variable `STATIC_URL`.

Por defecto, estará configurada como:

```python
STATIC_URL = '/static/'
```

Esto indica que Django busca y sirve los archivos estáticos desde la ruta `/static/` en cada aplicación.

## 6. 🚀 ¡Listo!
Recuerda siempre activar el entorno virtual antes de trabajar en tu proyecto para mantener las dependencias aisladas.
