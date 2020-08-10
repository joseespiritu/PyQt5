import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen

image_path = r"C:\Users\Jose Luis Espiritu\Pictures\panda.jpg"

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap(image_path)

    def paintEvent(self, event):

        # Draw on image
        pen = QPen()
        pen.setWidth(5)

        # Upload Image
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        painter.setPen(pen)
        painter.drawEllipse(300,300,150,150)

def main():
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()

    sys.exit(app.exec_())

main()