from sys import argv, exit
from PyQt5.QtGui import QPainter, QColor
from random import randint
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clicled)
        self.k = 0

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
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            r = randint(0, 450)
            qp.drawEllipse(randint(0, 500 - r), randint(0, 500 - r), r, r)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
