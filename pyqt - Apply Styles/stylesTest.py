from PyQt6 import QtWidgets, uic
import sys
import os

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('stylesTest.ui', self)

        self.pushButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        self.pushButton.setStyleSheet(
                        "background-color: red; "
                        "font-family: times; "
                        "font-size: 20px;")

        # Show Window
        self.show()


os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()
