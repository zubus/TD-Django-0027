# 🚀 Creación de la primera aplicación en Django (`boards`)

Este tutorial te guiará en la creación de la primera aplicación dentro de tu proyecto Django llamado `miprimerproyecto`. La aplicación se llamará `boards`. Asegúrate de tener activado el entorno virtual "mientornovirtual" antes de continuar.

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

## 4. 🚀 ¡Listo!

No olvides siempre activar el entorno virtual antes de trabajar en tu proyecto para mantener las dependencias aisladas.
