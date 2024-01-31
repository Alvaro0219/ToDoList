# Documentación de la aplicación TodoList

## Introducción

La sección de **Estructura de una Aplicación - TodoList** se centra en la creación de una aplicación web simple utilizando Flask.

## Descripción

La aplicación permite a los usuarios registrarse, iniciar sesión y realizar operaciones CRUD (crear, leer, actualizar, eliminar) sobre su lista de tareas.

## Instalación

1. Clonar el repositorio desde GitHub

    ```bash
    git clone https://github.com/Alvaro0219/ToDoList.git
    cd todo-list
    ```

2. Crear un entorno virtual

    ```bash
    python3 -m venv venv
    ```

3. Activar el entorno virtual

    ```bash
    venv\Scripts\activate
    ```

4. Instalar las dependencias

    ```bash
    pip install -r requirements.txt
    ```

## Iniciar la aplicación

```bash
python run.py
 ```
La aplicación estará disponible en [http://127.0.0.1:5000]

## Registro de Usuarios
- Accede a la página de registro.
- Completa el formulario con la información requerida.
- Haz clic en "Registrar".

## Inicio de Sesión
- Accede a la página de inicio de sesión.
- Ingresa tus credenciales.
- Haz clic en "Iniciar Sesión".

## Operaciones CRUD de Tareas

### Crear Tarea:
- Haz clic en "Nuevo".
- Completa el formulario.
- Haz clic en "Guardar".

### Leer Tareas:
- Accede a la página de lista de tareas.

### Actualizar Tarea:
- En la página de lista de tareas, encuentra la tarea que deseas editar.
- Haz clic en "Editar".
- Completa el formulario.
- Haz clic en "Guardar".

### Eliminar Tarea:
- En la página de lista de tareas, encuentra la tarea que deseas eliminar.
- Haz clic en el botón de eliminar.

