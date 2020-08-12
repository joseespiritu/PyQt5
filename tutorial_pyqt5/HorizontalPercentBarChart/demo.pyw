import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QHorizontalPercentBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        chartView = QChartView(chart)
        self.setCentralWidget(chartView)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())