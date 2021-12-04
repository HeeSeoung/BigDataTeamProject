from __future__ import print_function
import pandas as pd
import PyQt5.QtWidgets
import easygui
from PyQt5.QtCore import *
from PyQt5 import uic, QtGui
import sys
from PyQt5 import QtWidgets

class Analysis_UI(QtWidgets.QMainWindow):
    # Load UI
    def __init__(self):
        super(Analysis_UI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('resources/UI/bigdata_2.ui', self) # Load the .ui file

        # UI 정보 가져오기
        # 1. 무슨 올림픽인가요?
        self.nameOlympic = self.findChild(QtWidgets.QPushButton, "nameOlympic")

        # 2. Button Box 가져오기
        self.ButtonBox = self.findChild(QtWidgets.QFrame, "listOlympic")


        # 3. 그래프 시각화 페이지 4개 가져오기
        self.lt_widget = self.findChild(QtWidgets.QWidget,"widget")
        self.lb_widget = self.findChild(QtWidgets.QWidget, "widget_3")
        self.rt_widget = self.findChild(QtWidgets.QWidget, "widget_2")
        self.rb_widget = self.findChild(QtWidgets.QWidget, "widget_4")

        # 4. Return 버튼 가져오기
        self.return_btn = self.findChild(QtWidgets.QPushButton, "return_btn")
        self.return_btn.clicked.connect(self.return_button_pressed)




    # Start_btn 연습용 코드
    def return_button_pressed(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


    # Logo Image 세팅
    def set_logo_image(self):
        self.pixmap = QtGui.QPixmap(f'../resources/DP_logo/DP_logo_3.png')
        self.pixmap = self.pixmap.scaled(540, 290)
        self.logo.setPixmap(self.pixmap)
        self.logo.setObjectName("olympics_logo")
        self.logo.show()

    # excel Upload 버튼
    @pyqtSlot()
    def excel_upload(self):
        path = easygui.fileopenbox(multiple=True)
        df_path = pd.read_csv(path[0])
        self.Save_File = df_path
        print(self.Save_File.head())
        self.excel_label.setText((path[0]))

