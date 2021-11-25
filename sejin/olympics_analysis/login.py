import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog

class LoginWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI(self)
        self.btnf


    def initUI(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)

        btn = QPushButton(self)


        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(btn)
        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()

        QDialog.l