""" Manipulate QTHread in PyQt5 """
# pip install pyqt5==5.12

import sys
import os
import time
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QThread

class helperThreadImpl(QObject):
    sig_result = pyqtSignal(int)
    sig_update = pyqtSignal(int)

    def __init__(self, min=0, max=100, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.min = min
        self.max = max

    @pyqtSlot()
    def start(self):
        # do work here
        for num in range(self.min, self.max):
            QThread.msleep(300)
            self.sig_update.emit(num)

        self.sig_result.emit(100)

class AppDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AppDialog, self).__init__(parent)
        self.setWindowTitle("PyQt5 -- QThread app")

        ui_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qthread.ui')
        self.ui_widget = uic.loadUi(ui_file, self)
        self.ui_widget.buttonBox.accepted.connect(self.on_accept)
        self.ui_widget.buttonBox.rejected.connect(self.on_reject)
        
        self.ui_widget.pushButton_start.clicked.connect(self.on_click_start)
        self.ui_widget.pushButton_stop.clicked.connect(self.on_click_stop)

        self.ui_widget.progressBar.setValue(0)
        print("")

        self.thread_qt = QThread()

    def on_update_from_helper(self, tick):
        self.ui_widget.progressBar.setValue(tick)

    def on_result_from_helper(self, tick):
        self.ui_widget.progressBar.setValue(tick)
        print("Thread is completed")

    @pyqtSlot()
    def on_click_start(self):
        if self.thread_qt.isRunning():
            print("Thread is already running")
        else:
            print("Kicked off thread")
            self.helper_impl = helperThreadImpl(min=0, max=100)
            self.thread_qt.started.connect(self.helper_impl.start)
            self.helper_impl.sig_update.connect(self.on_update_from_helper)
            self.helper_impl.sig_result.connect(self.on_result_from_helper)
            self.helper_impl.moveToThread(self.thread_qt)
            self.thread_qt.start()

    @pyqtSlot()
    def on_click_stop(self):
        if self.thread_qt.isRunning():
            print("Ask thread to temrinate...")
            self.thread_qt.terminate()

            # It takes time, as per docs it depends on underlying OS
            self.thread_qt.wait()
            print("Thread is terminated")
        else:
            print("Thread is not active")

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
