"""Instalar el paquete PyQt6 en el interprete de python"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("A miña primeira fiestra con PyQt6")

        self.pulsado = 0
        self.caracteres = 0

        self.cadroTexto = QLineEdit()
        self.cadroTexto.setMaxLength(10)
        self.cadroTexto.setPlaceholderText("Escribe o teu nome")

        self.cadroTexto.returnPressed.connect(self.on_button_clicked)

        self.cadroTexto.selectionChanged.connect(self.on_cadroTexto_selectionChanged)

        # self.cadroTexto.textChanged.connect(self.on_cadroTexto_textChanged)

        self.cadroTexto.textEdited.connect(self.on_cadroTexto_keyTextEdited)

        # self.cadroTexto.keyPressEvent.connect(self.on_cadroTexto_keyPressEvent)

        boton = QPushButton("Púlsame!!")
        boton.clicked.connect(self.on_button_clicked)

        self.etiqueta = QLabel("Pulsa o boton.")
        fonte = self.etiqueta.font()
        fonte.setPointSize(30)
        self.etiqueta.setFont(fonte)
        self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        etiqueta2 = QLabel()
        etiqueta2.setPixmap(QPixmap("/home/dam2a/Imágenes/Marta.jpg"))

        caixaV = QVBoxLayout()
        caixaV.addWidget(self.cadroTexto)
        caixaV.addWidget(boton)
        caixaV.addWidget(self.etiqueta)
        caixaV.addWidget(etiqueta2)

        contedor = QWidget()
        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)
        self.show()

    def on_button_clicked(self):
        print("O boton foi pulsado")
        if self.pulsado > 0:
            self.etiqueta.setText(
                "Ola " + self.cadroTexto.text() + ". O boton foi pulsado " + str(self.pulsado) + " veces")
        else:
            self.etiqueta.setText("Ola " + self.cadroTexto.text())
            self.cadroTexto.setReadOnly(True)
            self.caracteres = 0
            self.cadroTexto = ""
        self.pulsado = self.pulsado + 1

    def on_cadroTexto_keyTextEdited(self):
        self.caracteres += 1
        print("Pulsaronse " + str(self.caracteres) + "caracteres")

    def on_cadroTexto_selectionChanged(self):
        print("Text Seleccionado: " + self.cadroTexto.selectedText())

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

        box = Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)

        boton = Gtk.Button(label="Pulsame !!!!")
        boton.connect("clicked", self.on_button_clicked)
        box.pack_start(boton, True, False, 4)

        self.etiqueta = Gtk.Label(label="Pulsame !!!!")
        box.pack_start(self.etiqueta, True, False, 4)

        imaxe = Gtk.Image.new_from_file("/home/dam2a/Imágenes/Marta.jpg")
        box.pack_start(imaxe, True, True, 4)

        self.add(box)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_button_clicked(self, referenciaBoton):
        print("O boton foi pulsado")
        self.etiqueta.set_text("O boton \"" + referenciaBoton.get_label() + "\" foi pulsado")


if __name__ == "__main__":
    FiestraPrincipal2()
    Gtk.main()
