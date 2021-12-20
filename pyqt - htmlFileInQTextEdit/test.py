from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
import os
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui',self)

        # QTextEdit
        try:
            self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        except:
            print("Cant find all TextEdits")

        f = QFile("test.html")
        f.open(QFile.ReadOnly|QFile.Text)
        istream = QTextStream(f)
        self.textEdit.setHtml(istream.readAll())
        f.close()

        # Show Window
        self.show()

def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()

if __name__ == '__main__':
    main()
