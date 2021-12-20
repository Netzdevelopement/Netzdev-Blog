import sys
from PyQt5 import QtCore, QtWidgets


class Demo(QtWidgets.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.label = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.v_layout = QtWidgets.QVBoxLayout(self)
        self.v_layout.addWidget(self.label)
        self.retranslateUi()

    def retranslateUi(self):
        self.label.setText(QtWidgets.QApplication.translate('Demo', "Hello, World"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())