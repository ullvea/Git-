import random
import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPolygon
from UI import Ui_MainWindow


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(600, 600)
        self.btn.move(250, 250)
        self.btn.setText('Рисовать')
        self.setWindowTitle("Yellow circles")
        self.flag = False
        self.btn.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            x, y = random.randint(50, 350), random.randint(50, 350)
            size = random.randint(5, 100)
            qp.drawEllipse(x, y, size, size)
            self.flag = False
            qp.end()

    def draw(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())