import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200,800)
        self.color = QColor(Qt.red)

        self.rect_circle = QRect(0,0,50,50)
        self.rect_circle.moveCenter(QPoint(self.width() / 2, self.rect_circle.height() / 2))

        self.step = QPoint(0,5)
        self.y_direction = 1

        timer = QTimer(self, interval=10)
        timer.timeout.connect(self.update_position)
        timer.start()

    def paintEvent(self, event):
        bounce = QPainter(self)
        bounce.setPen(Qt.black)
        bounce.setBrush(Qt.red)
        bounce.drawEllipse(self.rect_circle)

    def update_position(self):
        if self.rect_circle.bottom() > self.height() and self.y_direction == 1:
            self.y_direction = -1
        if self.rect_circle.top() < 0 and self.y_direction == -1:
            self.y_direction = 1

        self.rect_circle.translate(self.step * self.y_direction)
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())