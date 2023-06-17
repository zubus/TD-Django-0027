# 🎉 Instalación de Django en Windows: Paso a paso 🚀

En este README aprenderás a instalar un proyecto de Django en Windows utilizando tanto la consola de comandos (terminal) de Windows como Git Bash. Seguiremos los siguientes pasos:

1. 🐍 Instalación de Python y Pip.
2. 🌐 Creación del entorno virtual (`mientornovirtual`).
3. 🎆 Instalación de Django.
4. 📝 Creación del proyecto de Django (`miprimerproyecto`).

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
