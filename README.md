# tercera-preentrega_diego-diaz
Este proyecto permite ingresar Clientes, Productos y Categorias. Además de realizar una búsqueda ya sea por clientes y productos.

Instalacion

pip install django

pip install django-bootstrap4

python manage.py migrate

python manage.py makemigrations

Uso del Proyecto

1.- En la web se encuentra un header que contiene un menú con sus respectivos formularios permitiendo así, ingresar datos por el momento.
2.- Clientes: Para el ingreso de clientes solo se requiere un nombre, apellido, teléfono y email. 
3.- Productos: En el registro de productos, se solicita un nombre, precio y seleccionar una categoría previamente registrada.
4.- Categorias: Solo basta ingresar un nombre en el formulario para el registro de Categorías. 
5.- En el Inicio o Home de la web, hay un pequeño formulario para buscar un producto y cliente. Al ingresar un texto, este filtrará en los Models de Producto y Cliente para desplegar el resultado de la búsqueda al presionar el botón buscar.