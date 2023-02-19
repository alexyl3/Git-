from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.clicled)
        self.x = -1
        self.y = -1
        self.k = 0
        self.setMouseTracking(True)

    def clicled(self):
        self.k = 1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        if self.k:
            qp.setBrush(QColor("yellow"))
            r = randint(0, 450)
            qp.drawEllipse(randint(0, 500 - r), randint(0, 500 - r), r, r)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
