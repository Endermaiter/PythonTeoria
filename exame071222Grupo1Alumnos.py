import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QCheckBox, QTextEdit, QPushButton, QComboBox, QSlider,
                             QGroupBox, QVBoxLayout, QHBoxLayout, QWidget, QBoxLayout, QListWidget)



class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 7-12_2022")

        caixaMain = QVBoxLayout()

        caixaSuperior = QHBoxLayout()
        caixaMain.addLayout(caixaSuperior)

        caixaInferior = QHBoxLayout()
        caixaMain.addLayout(caixaInferior)

        caixaDiscoAnimado = QVBoxLayout()
        lblCede = QLabel()
        lblCede.setPixmap(QPixmap("/home/dam2a/Escritorio/ENDERMAITER/DI/CDico.jpeg"))
        chkAnimado = QCheckBox("Animado")
        caixaDiscoAnimado.addWidget(lblCede)
        caixaDiscoAnimado.addWidget(chkAnimado)
        caixaSuperior.addLayout(caixaDiscoAnimado)

        caixaLista = QVBoxLayout()
        self.lista = QListWidget()
        caixaLista.addWidget(self.lista)
        caixaSuperior.addLayout(caixaLista)

        caixaBotons = QVBoxLayout()
        caixaSaltarECombo = QHBoxLayout()
        btnEngadirPista = QPushButton("Engadir pista a reproducir")
        btnSubirLista = QPushButton("Subir na lista")
        btnSubirLista.pressed.connect(self.on_botonSubirLista_pressed)
        btnBaixarLista = QPushButton("Baixar na lista")
        btnBaixarLista.pressed.connect(self.on_botonBaixarLista_pressed)

        btnSaltar = QPushButton("Saltar")
        cmbSaltar = QComboBox()
        caixaBotons.addWidget(btnEngadirPista)
        caixaBotons.addWidget(btnSubirLista)
        caixaBotons.addWidget(btnBaixarLista)
        caixaSaltarECombo.addWidget(btnSaltar)
        caixaSaltarECombo.addWidget(cmbSaltar)
        caixaBotons.addLayout(caixaSaltarECombo)
        caixaSuperior.addLayout(caixaBotons)

        caixaLabels = QVBoxLayout()
        lblSon = QLabel("Son:")
        lblRitmo = QLabel("Ritmo:")
        lblVolume = QLabel("volume:")
        caixaLabels.addWidget(lblSon)
        caixaLabels.addWidget(lblRitmo)
        caixaLabels.addWidget(lblVolume)
        caixaInferior.addLayout(caixaLabels)

        caixaSliders = QVBoxLayout()
        cmbSon = QComboBox()

        cmbSon.addItems(["Maracas", "Marimba", "Triángulo", "Timbales"])
        cmbSon.currentTextChanged.connect(self.on_combo_currentTextChanged)

        self.sldRitmo = QSlider(Qt.Orientation.Horizontal)
        self.sldVolume = QSlider(Qt.Orientation.Horizontal)
        # self.sldVolume.mouseMoveEvent(self.sliderVolume())

        caixaSliders.addWidget(cmbSon)
        caixaSliders.addWidget(self.sldRitmo)
        caixaSliders.addWidget(self.sldVolume)
        caixaInferior.addLayout(caixaSliders)

        caixaGroupBox = QVBoxLayout()
        caixaChecks = QVBoxLayout()

        opcionsReproduccion = QGroupBox ("Opcións de reproducción")
        self.chkAsincrono = QCheckBox("Asíncrono")
        self.chkENome = QCheckBox("É nome de ficheiro")
        self.chkXMlPersistente = QCheckBox("XML Persistente")

        self.chkAsincrono.stateChanged.connect(self.on_checkAsincrono_stateChanged)
        self.chkENome.stateChanged.connect(self.on_checkEnome_stateChanged)
        self.chkXMlPersistente.stateChanged.connect(self.on_checkXMLPersistente_stateChanged)

        caixaChecks.addWidget(self.chkAsincrono)
        caixaChecks.addWidget(self.chkENome)
        caixaChecks.addWidget(self.chkXMlPersistente)

        caixaGroupBox.addWidget(opcionsReproduccion)
        opcionsReproduccion.setLayout(caixaChecks)
        caixaInferior.addLayout(caixaGroupBox)


        ventana = QWidget()
        ventana.setLayout(caixaMain)

        self.setCentralWidget(ventana)
        self.show()

    def on_combo_currentTextChanged(self, texto):
        print(texto)

    def on_checkAsincrono_stateChanged(self):
        if self.chkAsincrono.isChecked():
            self.lista.addItem(self.chkAsincrono.text())

    def on_checkEnome_stateChanged(self):
        if self.chkAsincrono.isChecked():
            self.lista.addItem(self.chkENome.text())

    def on_checkXMLPersistente_stateChanged(self):
        if self.chkAsincrono.isChecked():
            self.lista.addItem(self.chkXMlPersistente.text())

    def on_botonSubirLista_pressed(self):
        indices = self.lista.selectedItems()
        if indices:
            indice = indices[0]
            row = self.lista.row(indice)
            row-1
            self.lista.clearSelection()

    def on_botonBaixarLista_pressed(self):
        indices = self.lista.selectedItems()
        if indices:
            indice = indices[0]
            row = self.lista.row(indice)
            row+1
            self.lista.clearSelection()

    def sliderVolume(self):
        if self.sldVolume.isSliderDown():
            print(self.sldVolume.value())




if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()