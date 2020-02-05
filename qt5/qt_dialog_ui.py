""" Show a simple dialog designed in UI using PyQt5 """
# pip install pyqt5==5.12

import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog

class AppDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AppDialog, self).__init__(parent)
        self.setWindowTitle("PyQt5 -- Dialog app")

        ui_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dialog.ui')
        self.ui_widget = uic.loadUi(ui_file, self)
        self.ui_widget.buttonBox.accepted.connect(self.on_accept)
        self.ui_widget.buttonBox.rejected.connect(self.on_reject)
        
        # Note: Trick to connect same Qt signal with parameter
        self.ui_widget.comboBox.currentIndexChanged[int].connect(self.on_combobox_itemChanged_index)
        self.ui_widget.comboBox.currentIndexChanged[str].connect(self.on_combobox_itemChanged_string)

        self.ui_widget.pushButton_browseFolder.clicked.connect(self.on_click_browseFolder)
        self.ui_widget.pushButton_browseFile.clicked.connect(self.on_click_browseFile)

    @pyqtSlot(int)
    def on_combobox_itemChanged_index(self, idx):
        self.ui_widget.label_selectedItem_int.setText("Selected Index # " + str(idx))

    @pyqtSlot(str)
    def on_combobox_itemChanged_string(self, txt):
        print(type(txt), txt)
        self.ui_widget.label_selectedItem_str.setText(" @ " + txt)

    @pyqtSlot()
    def on_click_browseFolder(self):
        dir = QFileDialog.getExistingDirectory(self, "Open Directory", "/", QFileDialog.ShowDirsOnly)
        if dir:
            self.ui_widget.label_folder.setText(dir)

    @pyqtSlot()
    def on_click_browseFile(self):
        file,_ = QFileDialog.getOpenFileName(self, "Open file", "/", "Text file (*.txt) ;; All Files (*)")
        if file:
            self.ui_widget.label_file.setText(file)

    def on_accept(self):
        print("on_accept")

    def on_reject(self):
        print("on_reject")

def run_app():
    app = QtWidgets.QApplication(sys.argv)

    icon_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.png')
    app.setWindowIcon(QtGui.QIcon(icon_file))

    dlg = AppDialog()
    dlg.show()
    app.exec_()

run_app()
