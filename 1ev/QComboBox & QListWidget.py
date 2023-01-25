import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QPushButton, QGridLayout, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox,
                             QListWidget)


class ComboList(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo QCombobox e QListWidget")
        caixaV = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Home", "Muller", "Ambos"])
        self.combo.currentIndexChanged.connect(self.on_combo_currentIndexChanged)
        self.combo.currentTextChanged.connect(self.on_combo_currentTextChanged)
        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.textLine = QLineEdit()
        self.textLine.setPlaceholderText("Introduzca el elemento a añadir de la lista. Luego presione ENTER")
        self.textLine.returnPressed.connect(self.on_cadroTexto_returnPressed)

        self.lista = QListWidget()
        self.lista.addItems(["Ocupado", "Parado", "Pensionista"])
        self.lista.currentItemChanged.connect(self.on_lista_currentItemChanged)
        self.lista.currentTextChanged.connect(self.on_lista_currentTextChanged)

        caixaV.addWidget(self.textLine)
        caixaV.addWidget(self.combo)
        caixaV.addWidget(self.lista)
        contedor = QWidget()
        contedor.setLayout(caixaV)
        self.setCentralWidget(contedor)

        self.show()

    def on_combo_currentIndexChanged(self, indice):
        print(indice)
        print(self.combo.itemText(indice))

    def on_combo_currentTextChanged(self, texto):
        print(texto)

    def on_lista_currentItemChanged(self, elemento):
        print(elemento.text())

    def on_lista_currentTextChanged(self, texto):
        print(texto)

    def on_cadroTexto_returnPressed(self):
        self.lista.addItem(self.textLine.text())
        self.textLine.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ComboList()
    sys.exit(app.exec())
