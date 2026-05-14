# Repositorio con ejercicios de Programación Orientada a Objetos en Python 
## 1. Crear el archivo .gitignore

Configurar el archivo .gitignore para restringir los archivos a sincronizar
````shell
*.pyc
__pycache__/
````

## 2. Indexar archivos y carpetas

Permite indexar todos los archivos y carpetas del proyecto, para identificar los cambios.

````shell
git add .
````

### 3. Crear un punto de control (COMMIT)

Crear un punto de control con los cambios con los cambios realizados en el proyecto.

````shell
git commit -m "CREATED .gitignore"
````

* CREATED - Crear nuevos archivos o directorios.
* UPDATE - Actualiza módulos del sistema.
* FIXED - Corregir errores del sistema.

## 4. Sincronizar los cambios en el repositorio.

Sincronizar los cambios con el repositorio.

````shell
git push -u origin main
````

