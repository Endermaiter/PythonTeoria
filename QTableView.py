import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox, QListWidget, \
    QPushButton, QLineEdit, QListView
from PyQt6.QtCore import Qt


class ModeloTaboa(Qt.AbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self.datos = datos

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            return self.datos[indice.row()][indice.column()]

    def rowCount(self, indice):
        return len(self.datos)

# sin acabar la funcion columnCount()

    def columnCount(self, indice):
        return len(self.datos)


class QTableView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo QTableView")

        # caixaVMain = QVBoxLayout()
        # caixaVMain.setContentsMargins(3, 3, 3, 3)
        # caixaVMain.setSpacing(3)

        # widget = QWidget()
        # widget.setLayout(caixaVMain)
        # self.setCentralWidget(widget)
        # self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QTableView()
    sys.exit(app.exec())
