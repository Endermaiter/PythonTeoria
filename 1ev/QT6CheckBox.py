import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QCheckBox, \
                            QButtonGroup, QRadioButton
from PyQt6.QtCore import Qt


class QTCheckBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTCheckBox")

        caixaV = QVBoxLayout()

        contedor = QWidget(self)
        contedor.setLayout(caixaV)

        self.check1 = QCheckBox("Home")
        self.check1.setCheckState(Qt.CheckState.Checked)
        self.check1.stateChanged.connect(self.on_checkHome_stateChanged)

        self.check2 = QCheckBox("Muller")
        self.check2.stateChanged.connect(self.on_checkMuller_stateChanged)

        caixaV2 = QVBoxLayout()
        caixaV2W = QWidget()
        caixaV2W.setLayout(caixaV2)
        grupoXenero = QButtonGroup(contedor)
        caixaV3 = QVBoxLayout()
        caixaV3W = QWidget()
        caixaV3W.setLayout(caixaV3)
        caixaH = QVBoxLayout()
        grupoOcupado = QButtonGroup(caixaH)


        self.opcionH = QRadioButton("Home", caixaV2W)
        grupoXenero.addButton(self.opcionH)
        self.opcionH.toggled.connect(self.on_opcion_toggled)

        self.opcionM = QRadioButton("Muller", caixaV2W)
        grupoXenero.addButton(self.opcionM)
        self.opcionM.toggled.connect(self.on_opcion_toggled)

        self.opcionA = QRadioButton("Ambos", caixaV2W)
        grupoXenero.addButton(self.opcionA)
        self.opcionA.toggled.connect(self.on_opcion_toggled)

        self.opcionPa = QRadioButton("Parado", caixaV3W)
        grupoOcupado.addButton(self.opcionPa)
        self.opcionPa.toggled.connect(self.on_opcion_toggled)
        self.opcionAc = QRadioButton("Activo", caixaV3W)
        grupoOcupado.addButton(self.opcionAc)
        self.opcionAc.toggled.connect(self.on_opcion_toggled)
        self.opcionPe = QRadioButton("Pensionista", caixaV3W)
        grupoOcupado.addButton(self.opcionPe)
        self.opcionPe.toggled.connect(self.on_opcion_toggled)

        caixaV.addWidget(self.check1)
        caixaV.addWidget(self.check2)

        caixaV2 = QVBoxLayout()
        caixav3 = QVBoxLayout()
        caixaV.addLayout(caixaH)
        caixaH.addLayout(caixaV2)
        caixaH.addLayout(caixav3)
        caixaV2.addWidget(self.opcionH)
        caixaV2.addWidget(self.opcionM)
        caixaV2.addWidget(self.opcionA)
        caixaV3.addWidget(self.opcionPa)
        caixaV3.addWidget(self.opcionAc)
        caixaV3.addWidget(self.opcionPe)


        caixaV.addWidget(self.check1)
        caixaV.addWidget(self.check2)

        self.setCentralWidget(contedor)
        self.show()

    def on_checkHome_stateChanged(self, estado):
        if self.check2.isChecked():
            self.check2.setChecked(False)
        self.check2.setChecked(True)
        print("Es home")
        print(Qt.CheckState(estado) == Qt.CheckState.Checked)

    def on_checkMuller_stateChanged(self, estado):
        if self.check1.isChecked():
            self.check1.setChecked(False)
        self.check2.setChecked(True)
        print("Es muller")
        print(Qt.CheckState(estado) == Qt.CheckState.Checked)

    def on_opcion_toggled(self):
        print("A")

if __name__ == "__main__":
    applicacion = QApplication(sys.argv)
    fiestra = QTCheckBox()
    applicacion.exec()
