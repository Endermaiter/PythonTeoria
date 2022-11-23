import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        super().__init__()
        self.set_title("EXCELeINFO - Hojas")


        model1 = Gtk.ListStore(str)
        self.treeView1 = Gtk.TreeView(model1)
        self.treeView1.show()

        def add_column(nombre):
            column = Gtk.TreeViewColumn(nombre)
            self.treeView1.append_column(column)

        add_column("")

        model1.append(('Ola',))

        vBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vBox.add(Gtk.Label(label="Hojas Visibles"))
        vBox.add(self.treeView1)

        vBox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vBox2.add(Gtk.Button(label="Ocultar >>"))
        vBox2.add(Gtk.Button(label="<< Mostrar"))

        vBox3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vBox3.add(Gtk.Label(label="Hojas Ocultas"))
        #vBox3.add(self.treeVi)

        hBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        hBox.add(vBox)
        hBox.add(vBox2)
        hBox.add(vBox3)

        self.add(hBox)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    MainWindow()
    Gtk.main()
