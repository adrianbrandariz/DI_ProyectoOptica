import gi
gi.require_version ('Gtk','3.0')

from gi.repository import Gtk
from sqlite3 import dbapi2

class FiestraPrincipal ():

    def __init__(self):

        # La base de datos y el cursor que se emplea para manejar los datos:
        self.bbdd = dbapi2.connect("bbdd.dat")
        self.cursor = self.bbdd.cursor()

        # Se recibe la GUI desde un archivo .glade:
        builder = Gtk.Builder()
        builder.add_from_file("generadorFacturas.glade")

        mainWindow = builder.get_object("mainWindow")

        mainWindow.show()