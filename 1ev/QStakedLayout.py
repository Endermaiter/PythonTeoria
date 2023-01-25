import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QPushButton, QGridLayout, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QStackedLayout)

from Colors import Color


class QStakedLayoutClass(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo QStakedLayout")

        caixaV = QVBoxLayout()
        caixaH = QHBoxLayout()

        rButton = QPushButton("Vermello")
        rButton.pressed.connect(self.activaTarxeta1)
        caixaH.addWidget(rButton)

        bButton = QPushButton("Azul")
        bButton.pressed.connect(self.activaTarxeta2)
        caixaH.addWidget(bButton)

        gButton = QPushButton("Verde")
        gButton.pressed.connect(self.activaTarxeta3)
        caixaH.addWidget(gButton)

        self.esquema = QStackedLayout()
        caixaV.addLayout(caixaH)
        caixaV.addLayout(self.esquema)

        self.esquema.addWidget(Color("red"))
        self.esquema.addWidget(Color("blue"))
        self.esquema.addWidget(Color("green"))
        self.esquema.addWidget(Color("orange"))
        self.esquema.addWidget(Color("purple"))
        self.esquema.addWidget(Color("pink"))
        self.esquema.addWidget(Color("yellow"))
        self.esquema.addWidget(Color("brawn"))

        self.esquema.setCurrentIndex(3)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.show()

    def activaTarxeta1(self):
        self.esquema.setCurrentIndex(0)

    def activaTarxeta2(self):
        self.esquema.setCurrentIndex(1)

    def activaTarxeta3(self):
        self.esquema.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QStakedLayoutClass()
    sys.exit(app.exec())
