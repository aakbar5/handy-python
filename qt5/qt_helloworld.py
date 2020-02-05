""" Show a simple dialog using PyQt5 """
# pip install pyqt5==5.12

import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui

def run_app():
    app = QtWidgets.QApplication(sys.argv)

    icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.png')
    app.setWindowIcon(QtGui.QIcon(icon))

    window = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(QtWidgets.QLabel('PyQt5 -- Hello world'))
    layout.addWidget(QtWidgets.QPushButton('OK'))
    window.setLayout(layout)
    window.show()
    app.exec_()

run_app()
