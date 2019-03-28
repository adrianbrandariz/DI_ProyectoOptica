Proyecto Optica para DI
=======================

Modulos:
--------
- Control y gestión de clientes
- Control y gestión de productos
- Control y gestión de ventas
- Creación de informes y facturas
- Base de datos

Descripción:
------------

Esta aplicación ha sido desarrollada y soportada bajo el lenguaje de Python.
La finalidad de esta aplicación es la simulación del funcionamiento de una
empresa, en este caso un óptica, en la que se pueden administrar los clientes,
los productos y las ventas. Además de ésto, esta aplicación es capaz de generar
informes de venta, tanto simples como detallados,

A continuación se pasará a explicar uno por uno, todos los módulos que posee:

1. Módulo de clientes:

En este módulo primeramente nos encontramos con un menú
desplegable que siempre mostrará a tiempo real los clientes almacenados en la
base de datos. En el momento que un cliente es seleccionado todos sus datos son
volcados a unos campos no editables para poder observarlos. Siempre se va a trabajar
sobre un usuario ya seleccionado, por lo que si se desea trabajar sobre otro usuario
tanto solo es necesario seleccionarlo en el menú desplegable. Disponemos, a su vez,
de tres botones de gestión:

*Añadir:* despliega un nuevo menú en el que se rellenarán los campos pertinentes para que,
una vez estén todos los campos cubiertos y se haga click sobre el botón aplicar, este
nuevo menú desaparezca y se inserte ese nuevo usuario en la base de datos.

*Editar:* vuelca los datos que se están mostrando actualmente sobre unos campos editables,
una vez suceda ésto, el usuario podrá modificar esos datos y hacer click en el botón
aplicar para que se guarden estos cambios en el cliente seleccionado.

*Eliminar:* este botón borrará de la base de datos el cliente que esté actualmente
seleccionado.

2. Módulo de clientes:

El funcionamiento de este módulo es exactamente igual que el de clientes, por lo que
cualquier explicación de la ejecución en el módulo de usuarios, se puede transportar
al control de productos.

3. Módulo de ventas:

Para realizar una venta se hará click en el único botón disponible que generará una
referencia de venta automática para ser diferenciada en la base de datos. En este momento
ya estará disponible un menú desplegable con todos los clientes disponibles, una vez sea
seleccionado un cliente, un producto y la cantidad, y se haga click en el botón de añadir,
el menú  que contiene los clientes se bloqueará para no cambiar entre otros usuarios, aunque
si que se podrán seguir añadiendo nuevos productos a ese cliente.
Una vez se considere que la venta ha concluído se hará click en el botón de imprimir,
lo que finalizará la venta y se abrirá una ventana emergente que pedirá la referencia de la
venta y se hará click en un botón u otro (venta simple o detallada) según la necesidad del
cliente. Esta acción generará un nuevo archivo .PDF que se identificará por lo siguiente:

*TipoFactura_ReferenciaVenta_DniCliente.pdf*

Estructura de la base de datos:
_______________________________

1. Clientes:

+------------+------------+-----------+-----------+-----------+-----------+
|    DNI     |   NOMBRE   | NACIMIENTO| DIRECCION | TELEFONO  |   EMAIL   |
+============+============+===========+===========+===========+===========+
|            |            |           |           |           |           |
+------------+------------+-----------+-----------+-----------+-----------+

2. Productos:

+------------+------------+-----------+-----------+
| REFERENCIA | DESCRIPCION|  STOCK    |  PRECIO   |
+============+============+===========+===========+
|            |            |           |           |
+------------+------------+-----------+-----------+

3. Ventas:

+------------+------------+-----------+-----------+-----------+
|    ID      |  INDICADOR | DNICLIENTE|  REFPROD  | CANTIDAD  |
+============+============+===========+===========+===========+
|            |            |           |           |           |
+------------+------------+-----------+-----------+-----------+