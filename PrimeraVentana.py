"""Instalar el paquete PyQt6 en el interprete de python"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A miña primeira fiestra con PyQt6")

        boton = QPushButton("Púlsame!!")
        boton.clicked.connect(self.on_button_clicked)

        caixaV = QVBoxLayout()
        caixaV.addWidget(boton)

        contedor = QWidget()
        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)
        self.show()

    def on_button_clicked(self):
        print("O boton foi pulsado")


applicacion = QApplication(sys.argv)
fiestra = FiestraPrincipal()
applicacion.exec()

"""Instalar el paquete PyGObject y el paquete PyGObject-stubs en el interprete de python"""

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class FiestraPrincipal2(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("A miña primeira fiestra gtk")

        box = Gtk.Box(spacing=6)
        self.add(box)
        boton = Gtk.Button(label="Pulsame!!!")
        boton.connect("clicked", self.on_button_clicked)
        box.pack_start(boton, True, True, 0)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_button_clicked(self, str):
        print("O boton foi pulsado")


if __name__ == "__main__":
    FiestraPrincipal2()
    Gtk.main()
