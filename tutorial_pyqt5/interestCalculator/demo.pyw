import sys
from PyQt5.QtWidgets import QApplication, QDialog, QComboBox, QDoubleSpinBox, QVBoxLayout, QGridLayout, QLabel

class AppDemo(QDialog):
    def __init__(self):
        super().__init__()

        principalLabel = QLabel('Principal: ')

        self.principalSpinBox = QDoubleSpinBox()
        self.principalSpinBox.setRange(0, 100_000_000)
        self.principalSpinBox.setValue(1000)
        self.principalSpinBox.setPrefix('$')
        self.principalSpinBox.valueChanged.connect(self.calculate_interest)

        rateLabel = QLabel('Rate: ')

        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(0, 100)
        self.rateSpinBox.setValue(10)
        self.rateSpinBox.setSuffix('%')
        self.rateSpinBox.valueChanged.connect(self.calculate_interest)

        yearLabel = QLabel('Year: ')
        self.yearsComboBox = QComboBox()
        self.yearsComboBox.addItem('1 year')
        self.yearsComboBox.addItems(
            ['{0} years'.format(year) for year in range(2,26)]
        )
        self.yearsComboBox.currentIndexChanged.connect(self.calculate_interest)

        amountLabel = QLabel('Amount: ')
        self.dollarLabel = QLabel()

        gridLayout = QGridLayout()
        gridLayout.addWidget(principalLabel, 0, 0)
        gridLayout.addWidget(self.principalSpinBox, 0, 1)
        gridLayout.addWidget(rateLabel, 1, 0)
        gridLayout.addWidget(self.rateSpinBox, 1, 1)
        gridLayout.addWidget(yearLabel, 2, 0)
        gridLayout.addWidget(self.yearsComboBox, 2 ,1)
        gridLayout.addWidget(amountLabel, 3, 0)
        gridLayout.addWidget(self.dollarLabel, 3, 1)

        vLayout = QVBoxLayout()
        vLayout.addLayout(gridLayout)
        self.setLayout(vLayout)

        self.calculate_interest()

    def calculate_interest(self):
        p = self.principalSpinBox.value()
        r = self.rateSpinBox.value()
        y = self.yearsComboBox.currentIndex() + 1
        amt = p * ((1 + (r / 100.0)) ** y)
        self.dollarLabel.setText('$ {0:.2f}'.format(amt))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())