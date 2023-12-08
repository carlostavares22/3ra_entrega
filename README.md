# 3ra_entrega
3ra Entrega

## Modos de Ejecución Local:

Ubícate en la carpeta principal del proyecto y ejecuta el siguiente comando en tu entorno virtual de Python:

```bash python manage.py runserver ```

Si todo sale bien, podrás acceder al sitio en la siguiente dirección por defecto [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Verifica también en tu terminal la dirección donde está corriendo el servidor.

## Pruebas de Desarrollo:

Accede a [http://127.0.0.1:800/servicio o /producto](http://127.0.0.1:800/servicio o /producto) para registrar y agregar datos a la base de datos SQL.

El sitio cuenta con las siguientes funcionalidades:

- Navegación por las secciones del inicio, cliente, servicio y buscar cliente.
- Buscar cliente es una seccion para buscar datos en la base de datos del model Cliente (en versión beta) que reacciona únicamente a la búsqueda por nombre.

## Funciones de cada Pagina:

- Inicio: Se puede ingresar datos a la base de datos convinando ForeignKeys de Cliente y Servicio.
- Cliente: Ingresa datos de la base de datos. Esto incluyen nombre, telefono, email y direccion (opciona).
- Producto: Ingresa datos de la base de datos. Esto incluyen nombre, descripcion (opcional) y costo.

Estos ultimos generan las ForeignKey para el Inicio donde se crean facturas.

- Buscar Cliente: Seccion para buscar datos en la base de datos del model Cliente (en versión beta) que reacciona únicamente a la búsqueda por nombre.

## Proposito

Esta página esta pensada como un CRM de clientes para una empresa de reparaciones en la que los empleados deben generar los datos antes mencionados para crear y manejar la base de datos de la compañía.