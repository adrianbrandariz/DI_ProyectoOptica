import gi
gi.require_version ('Gtk','3.0')

from gi.repository import Gtk
from sqlite3 import dbapi2

class FiestraPrincipal ():

    def __init__(self):

        self.controlBloqueCliente = False
        self.controlBloqueProducto = False
        self.bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = self.bbdd.cursor()

        builder = Gtk.Builder()
        builder.add_from_file ("mainWindow.glade")

        mainWindow = builder.get_object("mainWindow")

        # Cuando se presione el boton botonAñadir ese bloque se hará visible, se inicia como invisible:
        self.newClienteBlock = builder.get_object("bloqueNuevoCliente")
        self.newProductoBlock = builder.get_object("bloqueNuevoProducto")

        # ComboBox:
        self.comboClientes = builder.get_object("cbListaClientes")
        clientes = self.cursor.execute("select dni, nombre from clientes")
        for cliente in clientes:
            self.comboClientes.append_text(cliente[0] + " - " + cliente[1])
        self.comboClientes.connect("changed", self.on_comboClientes_changed)
        self.comboProductos = builder.get_object("cbListaProductos")

        # Botones:
        addClienteButton = builder.get_object("botonAñadir")
        addClienteButton.connect("clicked", self.on_addClienteButton_clicked)
        editClienteButton = builder.get_object("botonEditar")
        removeClienteButton = builder.get_object("botonEliminar")
        applyClienteButton = builder.get_object("botonAplicar")
        applyClienteButton.connect("clicked", self.on_applyClienteButton_clicked)

        addProductoButton = builder.get_object("botonAñadirProducto")
        addProductoButton.connect("clicked", self.on_addProductoButton_clicked)
        editProductoButton = builder.get_object("botonEditarProducto")
        removeProductoButton = builder.get_object("botonEliminarProducto")
        applyProductoButton = builder.get_object("botonAplicarProducto")

        # Componentes bloque emergente Cliente:
        self.nombreCliente = builder.get_object("nombreClienteText")
        self.dniCliente = builder.get_object("dniClienteText")
        self.fechaCliente = builder.get_object("fechaClienteText")
        self.direccionCliente = builder.get_object("direccionClienteText")
        self.telefonoCliente = builder.get_object("telefonoClienteText")
        self.emailCliente = builder.get_object("emailClienteText")

        # Componentes bloque emergente Cliente:
        self.nombreNuevoCliente = builder.get_object("nombreNuevoCliente")
        self.dniNuevoCliente = builder.get_object("dniNuevoCliente")
        self.fechaNuevoCliente = builder.get_object("fechaNuevoCliente")
        self.direccionNuevoCliente = builder.get_object("direccionNuevoCliente")
        self.telefonoNuevoCliente = builder.get_object("telefonoNuevoCliente")
        self.emailNuevoCliente = builder.get_object("emailNuevoCliente")

        mainWindow.show()


    def on_addClienteButton_clicked (self, control):
        if (self.controlBloqueCliente == False):
            self.controlBloqueCliente = True
            self.newClienteBlock.set_visible(True)
        else:
            self.controlBloqueCliente = False
            self.newClienteBlock.set_visible(False)

    def on_applyClienteButton_clicked(self, control):
        nombre = self.nombreNuevoCliente.get_text()
        dni = self.dniNuevoCliente.get_text()
        fecha = self.fechaNuevoCliente.get_text()
        direccion = self.direccionNuevoCliente.get_text()
        telefono = self.telefonoNuevoCliente.get_text()
        email = self.emailNuevoCliente.get_text()
        if dni and nombre and fecha and direccion and telefono and email:
            self.cursor.execute("insert into clientes values ('" + dni + "', '" + nombre + "', '" + fecha + "', '" + direccion + "', " + telefono + ", '" + email + "')")
            self.bbdd.commit()
            self.newClienteBlock.set_visible(False)
            # Se limpian los campos:
            self.nombreNuevoCliente.set_text("")
            self.dniNuevoCliente.set_text("")
            self.fechaNuevoCliente.set_text("")
            self.direccionNuevoCliente.set_text("")
            self.telefonoNuevoCliente.set_text("")
            self.emailNuevoCliente.set_text("")

    def on_comboClientes_changed(self, combo):
        texto = combo.get_active_text()
        cliente = self.cursor.execute("select * from clientes where dni='" + texto.split(" - ")[0] + "'")
        for dato in cliente:
            self.nombreCliente.set_text(dato[0])
            self.dniCliente.set_text(dato[1])
            self.fechaCliente.set_text(dato[2])
            self.direccionCliente.set_text(dato[3])
            self.telefonoCliente.set_text(str(dato[4]))
            self.emailCliente.set_text(dato[5])

    def on_addProductoButton_clicked (self, control):
        if (self.controlBloqueProducto == False):
            self.controlBloqueProducto = True
            self.newProductoBlock.set_visible(True)
        else:
            self.controlBloqueProducto = False
            self.newProductoBlock.set_visible(False)

if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()