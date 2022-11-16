import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QCheckBox
from PyQt6.QtCore import Qt


class QTCheckBox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTCheckBox")

        caixaV = QVBoxLayout()

        self.check1 = QCheckBox("Home")
        self.check2 = QCheckBox("Muller")
        # check1.setCheckState(Qt.CheckState.Checked)
        #self.check2.setChecked(True)
        self.check1.stateChanged.connect(self.on_check1_stateChanged)
        self.check2.stateChanged.connect(self.on_check2_stateChanged)

        caixaV.addWidget(self.check1)
        caixaV.addWidget(self.check2)

        contedor = QWidget()
        contedor.setLayout(caixaV)

        self.setCentralWidget(contedor)
        self.show()

    def on_check2_stateChanged(self, estado):
        if self.check1.isChecked():
            self.check1.setChecked(False)
        self.check2.setChecked(True)
        print("Es homo")
        print(Qt.CheckState(estado) == Qt.CheckState.Checked)

    def on_check1_stateChanged(self, estado):
        if self.check2.isChecked():
            self.check2.setChecked(False)
        self.check2.setChecked(True)


if __name__ == "__main__":
    applicacion = QApplication(sys.argv)
    fiestra = QTCheckBox()
    applicacion.exec()
