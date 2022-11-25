import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox, QListWidget, \
    QPushButton, QLineEdit


class ExercicioListaTarefas(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ExercicioListaTarefas")

        caixaVMain = QVBoxLayout()
        caixaVMain.setContentsMargins(0, 0, 0, 0)
        caixaVMain.setSpacing(0)

        lista = QListWidget()
        caixaVMain.addWidget(lista)

        caixaH = QHBoxLayout()

        botonBorrar = QPushButton()
        botonFeito = QPushButton()

        caixaH.addWidget(botonFeito)
        caixaH.addWidget(botonBorrar)
        caixaVMain.addWidget(caixaH)

        texto = QLineEdit()
        botonEngadir = QPushButton()

        caixaVMain.addWidget(texto)
        caixaVMain.addWidget(botonEngadir)

        widget = QWidget()
        widget.setLayout(caixaVMain)
        self.setCentralWidget(widget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExercicioListaTarefas()
    sys.exit(app.exec())
