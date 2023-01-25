import sys

import PyQt6.QtWidgets as qwd
from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class ModeloTabla(qwd.QWidget):
    def __init__(self):
        super().__init__()


class Interfaz(qwd.QWidget):

    def __init__(self):
        super().__init__()
        self.UIcomponents()

    def UIcomponents(self):
        self.setWindowTitle("Ejemplo TableView con BD")
        self.show()

        # layout
        grid = qwd.QGridLayout()

        # tabla
        self.table = qwd.QTableView()

        # Base de Datos
        bd = QSqlDatabase("QSQLITE")
        bd.setDatabaseName("bbdd.dat")
        bd.open()

        # MODELO TABLA
        self.modelo = QSqlTableModel(db=bd)
        self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        # QSqlTableModel.EditStrategy.OnRowChange
        # QSqlTableModel.EditStrategy.OnFieldChange
        self.table.setModel(self.modelo)
        self.modelo.setTable("usuarios")
        # (PARA ORDENAR LOS DATOS DE LA TABLA) self.modelo.setSort(0, Qt.SortOrder.DescendingOrder)
        self.modelo.select()
        self.modelo.setHeaderData(0, Qt.Orientation.Horizontal, "DNI")
        self.modelo.setHeaderData(1, Qt.Orientation.Horizontal, "NOMBRE")
        self.modelo.setHeaderData(2, Qt.Orientation.Horizontal, "DIRECCIÓN")
        # (PARA BORRAR COLUMNAS) self.modelo.removeColumns(2,1)

        # Boton para guardar y actualizar BD
        self.botonG = qwd.QPushButton("Actualizar")
        self.botonG.clicked.connect(self.on_botonG_clicked)

        # Boton para cancelar BD
        self.botonC = qwd.QPushButton("Cancelar")
        self.botonC.clicked.connect(self.on_botonC_clicked)

        # Buscador para filtrar
        self.buscador = qwd.QLineEdit()
        self.buscador.clicked.connect(self.on_buscador_clicked)

        # Añadimos tabla al grid
        grid.addWidget(self.table, 0, 0, 1, 4)
        grid.addWidget(self.botonG, 1, 0, 1, 2)
        grid.addWidget(self.botonC, 1, 2, 1, 2)
        grid.addWidget(self.buscador, 2, 0, 1, 4)

        # Ponemos un tamaño al layout
        self.setMinimumSize(300, 200)

        self.setLayout(grid)

    # Añadimos las funciones
    def on_botonG_clicked(self):
        self.modelo.submitAll()

    def on_botonC_clicked(self):
        self.modelo.revertAll()


if __name__ == "__main__":
    aplicacion = qwd.QApplication(sys.argv)
    ventana = Interfaz()
    aplicacion.exec()
