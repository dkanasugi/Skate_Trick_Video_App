# Author - Maximillian Renga
# CST 205
# 5.3.18
from PIL import Image
import sys
import random
import string

from PyQt5.QtWidgets import QApplication, QFontDialog, QMainWindow, QWidget, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QMessageBox
from PyQt5.QtCore import pyqtSlot, QCoreApplication

def randString():
    kaiba = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    s=""
    for i in range(7):
        next = random.randrange(len(kaiba))
        s=s+kaiba[next]
    return s

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Captcha')
        self.home()

    def home(self):
        self.s=randString()
        label= QLabel(self)
        label.setText('Enter captcha')
        label.move(100, 10)
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 55)
        self.cap = QLabel(self)
        self.cap.setText(self.s)
        self.cap.move(100, 30)
        btn = QPushButton("Submit", self)
        btn.clicked.connect(self.onClick)
        btn.move(100, 100)
        self.show()

    @pyqtSlot()
    def onClick(self):
        guess = self.textbox.text()
        if guess != self.s:
            QMessageBox.question(self, 'FAILURE', "Incorrect Captcha", QMessageBox.Ok, QMessageBox.Ok)
        else:
            exit()
captcha = QApplication(sys.argv)
GUI = Window()
sys.exit(captcha.exec())
