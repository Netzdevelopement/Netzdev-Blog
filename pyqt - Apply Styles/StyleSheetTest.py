from PyQt6 import QtWidgets, uic
import sys
import os

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('stylesTest.ui', self)
        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.show()


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QtWidgets.QApplication(sys.argv)
window = Ui()
with open('styles.qss', 'r') as f:
    style = f.read()
    app.setStyleSheet(style)
app.exec()
