from PyQt6.QtCore import QAbstractListModel
from PyQt6.QtCore import Qt


class ModeloListaTarefas(QAbstractListModel):
    def __init__(self, listaTarefas=None):
        super().__init__()
        self.listaTarefas = listaTarefas or []

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            estado, texto = self.listaTarefas[indice.row()]
            return texto

    def rowCount(self, index):
        return len(self.listaTarefas)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModeloListaTarefas()
    sys.exit(app.exec())
