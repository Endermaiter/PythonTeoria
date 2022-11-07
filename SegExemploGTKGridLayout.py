import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Calculadora GTK")

        grid = Gtk.Grid()

        # declaracion de variables y su posicion

        # grid.attach(widget, columnas a su izquierda, filas hacia arriba, columnas que ocupa, filas que ocupa)

        grid.attach(Gtk.Entry(), 0, 0, 3, 1)
        grid.attach(Gtk.Button(label="1"), 0, 1, 1, 1)
        grid.attach(Gtk.Button(label="2"), 1, 1, 1, 1)
        grid.attach(Gtk.Button(label="3"), 2, 1, 1, 1)
        grid.attach(Gtk.Button(label="4"), 0, 2, 1, 1)
        grid.attach(Gtk.Button(label="5"), 1, 2, 1, 1)
        grid.attach(Gtk.Button(label="6"), 2, 2, 1, 1)
        grid.attach(Gtk.Button(label="7"), 0, 3, 1, 1)
        grid.attach(Gtk.Button(label="8"), 1, 3, 1, 1)
        grid.attach(Gtk.Button(label="9"), 2, 3, 1, 1)
        grid.attach(Gtk.Button(label="0"), 0, 4, 3, 1)

        grid.attach(Gtk.Button(label="+"), 3, 0, 1, 1)
        grid.attach(Gtk.Button(label="-"), 3, 1, 1, 1)
        grid.attach(Gtk.Button(label="x"), 3, 2, 1, 1)
        grid.attach(Gtk.Button(label="/"), 3, 3, 1, 1)
        grid.attach(Gtk.Button(label="="), 3, 4, 1, 1)

        # espaciadores

        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.set_column_spacing(5)
        grid.set_row_spacing(5)
        grid.set_margin_top(5)
        grid.set_margin_bottom(5)
        grid.set_margin_left(5)
        grid.set_margin_right(5)

        # añadir la grid a la ventana y mostrar

        self.add(grid)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    MainWindow()
    Gtk.main()
