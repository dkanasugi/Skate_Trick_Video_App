import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QGridLayout,
                                QVBoxLayout, QHBoxLayout, QApplication,
                                QLineEdit, QPushButton)
class Second(QWidget):
    def __init__(self):
        super(Second, self).__init__(parent)

class Window(QWidget):
        def __init__(self):
            QWidget.__init__(self)

            # Widgets
            self.label1 = QLabel("Skate Tricks!", self)
            self.label1.setWordWrap(True);

            self.label2 = QLabel("Enter tricks you want to watch!", self)
            self.label2.setWordWrap(True);

            self.textbox = QLineEdit(self)
            self.textbox.move(20,20)

            self.button = QPushButton("Search")
            self.button.clicked.connect(self.on_button_clicked)


            # Layout
            self.layout = QGridLayout()
            self.layout.addWidget(self.label1)
            self.layout.addWidget(self.label2)
            self.layout.addWidget(self.textbox)
            self.layout.addWidget(self.button)
            self.setLayout(self.layout)

            self.show()

        def on_button_clicked(self):
            ##tutorial need to be watched
            ##pyqt5





if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = Window()
        sys.exit(app.exec_())
