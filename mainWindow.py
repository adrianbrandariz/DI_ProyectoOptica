import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Proyecto Optica")

        

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()