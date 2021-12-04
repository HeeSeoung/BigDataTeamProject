from __future__ import print_function
import pandas as pd
import PyQt5.QtWidgets
import easygui
from PyQt5.QtCore import *
from PyQt5 import uic, QtGui
import sys
from PyQt5 import QtWidgets
from AnalysisPage import Analysis_UI

class First_Ui(QtWidgets.QMainWindow):
    # Load UI
    def __init__(self):
        super(First_Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('resources/UI/bigdata_1.ui', self) # Load the .ui file

        # UI 정보 가져오기
        # 1. logo 가져오기
        self.logo = self.findChild(QtWidgets.QLabel, "logo_label")
        self.set_logo_image()

        # 2. Excel 불러오기 버튼 만들기
        self.excel_btn = self.findChild(QtWidgets.QToolButton, "fileUpload")
        self.excel_label =self.findChild(QtWidgets.QLineEdit, "excel_edit")
        self.Save_File = pd.DataFrame() #요기에 저장됨!
        self.excel_btn.clicked.connect(self.excel_upload)


        # 3. Start Button 만들기
        self.start_btn = self.findChild(QtWidgets.QPushButton, "start_btn")
        self.start_btn.clicked.connect(self.NextButton)

        # 4. Exit Button 만들기
        self.exit_btn = self.findChild(QtWidgets.QPushButton, "exit_btn")
        self.exit_btn.clicked.connect(QCoreApplication.instance().quit)

        # 5. Progress Bar 만들기
        self.progress_bar = self.findChild(QtWidgets.QProgressBar, "pg_bar_name")




    # Start_btn 연습용 코드
    def printButtonPressed(self):
        print('눌렷넹')


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

    def NextButton(self):
        widget.setCurrentIndex(widget.currentIndex() +1)


if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)

    # 화면 전환용 Widget 생성
    widget = PyQt5.QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    firstUI = First_Ui()
    AnalysisUI = Analysis_UI()

    # Widget에 추가
    widget.addWidget(firstUI)
    widget.addWidget(AnalysisUI)

    # 화면 띄우기
    widget.setFixedWidth(1080)
    widget.setFixedHeight(768)
    widget.show()

    app.exec_()


