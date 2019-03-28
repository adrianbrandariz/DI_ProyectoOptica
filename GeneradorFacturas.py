import gi
gi.require_version ('Gtk','3.0')

from gi.repository import Gtk
from sqlite3 import dbapi2
from reportlab.platypus import (SimpleDocTemplate,PageBreak, Image,
                                Spacer,Paragraph,Table,TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class FiestraPrincipal ():

    def __init__(self):

        # La base de datos y el cursor que se emplea para manejar los datos:
        self.bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = self.bbdd.cursor()

        # Se recibe la GUI desde un archivo .glade:
        builder = Gtk.Builder()
        builder.add_from_file("generadorFacturas.glade")

        self.codigoVentaText = builder.get_object("codigoVentaText")
        facturaSimpleButton = builder.get_object("facturaSimpleButton")
        facturaSimpleButton.connect("clicked", self.on_facturaSimpleButton_clicked)
        facturaDetalladaButton = builder.get_object("facturaDetalladaButton")
        facturaDetalladaButton.connect("clicked", self.on_facturaDetalladaButton_clicked)

        mainWindow = builder.get_object("mainWindow")

        mainWindow.show()

    def on_facturaSimpleButton_clicked(self, control):
        # Se genera el contenido total de las tablas Cabezera+contenido consulta"""
        facturaVenta = [["Optica Brandariz", "", "", ""],
                        ["CIF: 5533116B", "", "", ""],
                        ["Direccion: Calle Falsa 123", "", "", ""],
                        ["", "", "", ""],
                        ['Producto', 'Cantidad', 'Precio Unidad', 'Precio Total']]
        self.cursorAux = self.bbdd.cursor()
        ventas = []
        # Para factura simple se requiere el nombre del producto, cantidad del producto, precio unidad y precio total:
        consulta = self.cursor.execute("select * from ventas where indicador='" + self.codigoVentaText.get_text() + "'")
        for registro in consulta:
            producto = self.cursorAux.execute("select descripcion, precio from productos where referencia='" + registro[3] + "'")
            print(registro[3])
            for detallesProducto in producto:
                print("Descripcion: " + detallesProducto[0])
                print("Precio: " + str(detallesProducto[1]))
            print("Cantidad:" + str(registro[4]))
            print("Precio total: " + str(detallesProducto[1] * registro[4]))
            ventas.append([detallesProducto[0], registro[4], detallesProducto[1], (detallesProducto[1] * registro[4])])
        for elemento in ventas:
            facturaVenta.append(elemento)

        self.i = 0
        self.sumaTotal = 0
        for registroVenta in facturaVenta:
            if (self.i >= 5):
                print(registroVenta)
                self.x = 0
                for datoVenta in registroVenta:
                    if (self.x == 3):
                        self.sumaTotal = self.sumaTotal + datoVenta
                    self.x = self.x + 1
            self.i = self.i + 1
        print(self.sumaTotal)
        facturaVenta.append(["", "", "", self.sumaTotal])
        # Se genera el documento .pdf:
        doc = SimpleDocTemplate("FS_" + self.codigoVentaText.get_text() + "_" + registro[2] + ".pdf", pagesize=A4)
        guion = []
        tabla = Table(facturaVenta)
        tabla.setStyle(TableStyle(
            [
                ('BACKGROUND', (0, 4), (-1, 4), colors.darkgreen),
                ('BACKGROUND', (-1, -1), (-1, -1), colors.darkgreen),
                ('TEXTCOLOR', (0, 4), (3, 4), colors.white),
                ('TEXTCOLOR', (-1, -1), (-1, -1), colors.white),
                ('BOX', (0, 4), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 4), (-1, -1), 1, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]
        ))
        guion.append(tabla)
        doc.build(guion)

    def on_facturaDetalladaButton_clicked(self, control):
        for datoCliente in self.cursor.execute("select dni, nombre, direccion from clientes where dni in (select dnicliente from ventas where indicador='" + self.codigoVentaText.get_text() + "')"):
            self.dni = datoCliente[0]
            self.nombre = datoCliente[1]
            self.direccion = datoCliente[2]
        # Se genera el contenido total de las tablas Cabezera+contenido consulta"""
        facturaVenta = [["Optica Brandariz", "", "", "", ""],
                        ["CIF: 5533116B", "", "", "", ""],
                        ["Direccion: Calle Falsa 123", "", "", "", ""],
                        ["", "", "", "", ""],
                        [self.nombre, "", "", "", ""],
                        [self.dni, "", "", "", ""],
                        [self.direccion, "", "", "", ""],
                        ["", "", "", "", ""],
                        ['Producto', 'Cantidad', 'Precio S/IVA', 'Precio Unidad', 'Precio Total']]
        self.cursorAux = self.bbdd.cursor()
        ventas = []
        # Para factura simple se requiere el nombre del producto, cantidad del producto, precio unidad y precio total:
        consulta = self.cursor.execute("select * from ventas where indicador='" + self.codigoVentaText.get_text() + "'")
        for registro in consulta:
            producto = self.cursorAux.execute(
                "select descripcion, precio from productos where referencia='" + registro[3] + "'")
            print(registro[3])
            for detallesProducto in producto:
                print("Descripcion: " + detallesProducto[0])
                print("Precio: " + str(detallesProducto[1]))
            print("Cantidad:" + str(registro[4]))
            print("Precio total: " + str(detallesProducto[1] * registro[4]))
            precioSIva = detallesProducto[1] - ((detallesProducto[1]/100)*21)
            ventas.append([detallesProducto[0], registro[4], precioSIva, detallesProducto[1], (detallesProducto[1] * registro[4])])
        for elemento in ventas:
            facturaVenta.append(elemento)
        self.i = 0
        self.sumaTotal = 0
        for registroVenta in facturaVenta:
            if (self.i >= 9):
                print(registroVenta)
                self.x = 0
                for datoVenta in registroVenta:
                    if (self.x == 4):
                        self.sumaTotal = self.sumaTotal + datoVenta
                    self.x = self.x + 1
            self.i = self.i + 1
        print(self.sumaTotal)
        facturaVenta.append(["", "", "", "", self.sumaTotal])
        # Se genera el documento .pdf:
        doc = SimpleDocTemplate("FD_" + self.codigoVentaText.get_text() + "_" + registro[2] + ".pdf", pagesize=A4)
        guion = []
        tabla = Table(facturaVenta)
        tabla.setStyle(TableStyle(
            [
                ('BACKGROUND', (0, 8), (-1, 8), colors.darkgreen),
                ('BACKGROUND', (-1, -1), (-1, -1), colors.darkgreen),
                ('TEXTCOLOR', (0, 8), (-1, 8), colors.white),
                ('TEXTCOLOR', (-1, -1), (-1, -1), colors.white),
                ('BOX', (0, 8), (-1, -1), 1, colors.black),
                ('INNERGRID', (0, 8), (-1, -1), 1, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]
        ))
        guion.append(tabla)
        doc.build(guion)

if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()