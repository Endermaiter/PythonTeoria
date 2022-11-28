from PyQt6.QtCore import QAbstractListModel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage

tick = QImage('/home/dam2a/Escritorio/ENDERMAITER/DI/Tick.png')


class ModeloListaTarefas(QAbstractListModel):
    def __init__(self, listaTarefas=None):
        super().__init__()
        self.listaTarefas = listaTarefas or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            estado, texto = self.listaTarefas[indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            estado, texto = self.listaTarefas[indice.row()]
            if estado:
                return tick

    def rowCount(self, index):
        return len(self.listaTarefas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModeloListaTarefas()
    sys.exit(app.exec())
