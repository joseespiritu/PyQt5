import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowOpacity(0.3)
    w.show()

    sys.exit(app.exec_())