import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):
    def __init__(self):
        super().__init__()

        self.edit = QLineEdit('Your Name')
        self.edit.selectAll()

        self.button = QPushButton('Show Greeting')
        #self.button.clicked.connect(self.greeting)
        self.button.clicked.connect(lambda :print('Hello {0}'.format(self.edit.text())))

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

    #def greeting(self):
    #    print('Hello {0}'.format(self.edit.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = Form()
    demo.show()

    sys.exit(app.exec_())