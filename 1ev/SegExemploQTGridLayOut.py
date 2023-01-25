import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QPushButton, QGridLayout, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit)


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora PyQt6")

        grid = QGridLayout()

        grid.addWidget(QLineEdit(), 0, 0, 1, 3)
        grid.addWidget(QPushButton('1'), 1, 0)
        grid.addWidget(QPushButton('2'), 1, 1)
        grid.addWidget(QPushButton('3'), 1, 2)
        grid.addWidget(QPushButton('4'), 2, 0)
        grid.addWidget(QPushButton('5'), 2, 1)
        grid.addWidget(QPushButton('6'), 2, 2)
        grid.addWidget(QPushButton('7'), 3, 0)
        grid.addWidget(QPushButton('8'), 3, 1)
        grid.addWidget(QPushButton('9'), 3, 2)
        grid.addWidget(QPushButton('0'), 4, 0, 1, 3)
        grid.setContentsMargins(6, 2, 2, 2)

        grid.addWidget(QPushButton("+"), 0, 3)
        grid.addWidget(QPushButton("-"), 1, 3)
        grid.addWidget(QPushButton("X"), 2, 3)
        grid.addWidget(QPushButton("/"), 3, 3)
        grid.addWidget(QPushButton("="), 4, 3)

        container = QWidget()
        container.setLayout(grid)
        self.setCentralWidget(container)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
