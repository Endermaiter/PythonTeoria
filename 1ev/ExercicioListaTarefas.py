import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QGroupBox, QListWidget, \
    QPushButton, QLineEdit, QListView

from ModeloListaTarefas import ModeloListaTarefas


class ExercicioListaTarefas(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ExercicioListaTarefas")

        caixaVMain = QVBoxLayout()
        caixaVMain.setContentsMargins(3, 3, 3, 3)
        caixaVMain.setSpacing(3)

        self.modelo = ModeloListaTarefas([(False, "Miña primeira tarefa")])
        self.lista = QListView()
        self.lista.setModel(self.modelo)
        caixaVMain.addWidget(self.lista)

        caixaH = QHBoxLayout()
        caixaVMain.setContentsMargins(5, 5, 5, 5)
        caixaVMain.setSpacing(5)

        botonBorrar = QPushButton("Borrar")
        botonBorrar.pressed.connect(self.on_botonBorrar_pressed)

        botonFeito = QPushButton("Feito")
        botonFeito.pressed.connect(self.on_botonFeito_pressed)

        caixaH.addWidget(botonFeito)
        caixaH.addWidget(botonBorrar)
        caixaVMain.addLayout(caixaH)

        self.texto = QLineEdit()
        self.texto.returnPressed.connect(self.on_texto_keyPressed)
        self.texto.setPlaceholderText("Escribe aqui o teu texto")

        botonEngadir = QPushButton("Engadir Tarefa")
        botonEngadir.pressed.connect(self.on_botonEngadir_pressed)

        caixaVMain.addWidget(self.texto)
        caixaVMain.addWidget(botonEngadir)

        widget = QWidget()
        widget.setLayout(caixaVMain)
        self.setCentralWidget(widget)
        self.show()

    def on_texto_keyPressed(self):
        novaTarefa = self.texto.text()
        novaTarefa.strip()
        if novaTarefa:
            self.modelo.listaTarefas.append([False, novaTarefa])
            self.modelo.layoutChanged.emit()
            self.texto.setText("")

    def on_botonEngadir_pressed(self):
        novaTarefa = self.texto.text()
        novaTarefa.strip()
        if novaTarefa:
            self.modelo.listaTarefas.append([False, novaTarefa])
            self.modelo.layoutChanged.emit()
            self.texto.setText("")

    def on_botonBorrar_pressed(self):
        indices = self.lista.selectedIndexes()
        if indices:
            indice = indices[0]
            del self.modelo.listaTarefas[indice.row()]
            # self.modelo.remove(self.modelo.listaTarefas[indice.row()])
            self.modelo.layoutChanged.emit()
            self.lista.clearSelection()

    def on_botonFeito_pressed(self):
        indices = self.lista.selectedIndexes()
        if indices:
            indice = indices[0]
            fila = indice.row()
            estado, descripcionTarefa = self.modelo.listaTarefas[fila]
            self.modelo.listaTarefas[fila] = (True, descripcionTarefa)
            self.modelo.dataChanged.emit(indice, indice)
            self.lista.clearSelection()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExercicioListaTarefas()
    sys.exit(app.exec())
