import random
import sys
import io
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPolygon


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
            qp.setBrush(QColor(255, 255, 0))
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