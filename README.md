# Proyecto_django_portafolio

Creacion de una aplicacion web donde se gestionan tareas y proyectos, utilizando autenticacion de usuario.
Este proyecto consiste en hacer un programa que aplique CRUD para tareas y proyectos creados por usuarios registrados, donde solo los usuarios puedan ver sus propios proyectos.
Se crean 2 apps, core y autenticacion, que albergan funciones diferentes, autenticacion se encarga de formularios de registro y login, ademas de contener html login y register para mantener la claridad de las funciones.
Se crean bases para cada app para modificar de forma independiente los templates y se enlazan los CSS a ellas.
En core se crean los modelos de tareas y otro de proyectos y formularios de creacion para cada uno de ellos
Se crean las vistas, que se conectan con los urls y cada proyecto y tarea tiene su id propia, por lo que las vistas que se utilizan para eliminar, actualizar y borrar actuan en ellas, se añade tambien que en los modelos se designa on_delete CASCADE en proyecto para eliminar todas sus tareas asociadas.
El CRUD comprende la edicion, eliminacion, creacion y lectura de proyectos, al igual que sus tareas asociadas al proyecto. El dashboard de core es la vista principal que maneja el usuario y es donde puede visualizar sus proyectos y tareas.
