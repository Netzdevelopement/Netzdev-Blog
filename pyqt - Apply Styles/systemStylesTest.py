from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QStyleFactory
print(QStyleFactory.keys())
import sys
import os

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('systemStylesTest.ui', self)

        # Show Window
        self.show()


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Windows')
window = Ui()
app.exec()

