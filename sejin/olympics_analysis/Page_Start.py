from __future__ import print_function
import pandas as pd
import easygui
from PyQt5.QtCore import *
from PyQt5 import uic, QtGui
from PyQt5 import QtWidgets

class warning_signal(QObject):
    warning = pyqtSignal()

class ui_Firstwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        uic.loadUi('resources/UI/bigdata_1.ui', self)

        # Signal 정의
        self.w = warning_signal()
        self.w.warning.connect(self.warning_event)

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
        self.pixmap = QtGui.QPixmap(f'resources/DP_logo/DP_logo_3.png')
        self.pixmap = self.pixmap.scaled(540, 290)
        self.logo.setPixmap(self.pixmap)
        self.logo.setObjectName("olympics_logo")
        self.logo.show()

    # Warning. 열 수는 있지만 csv파일이 아님
    def warning_event(self):
        QtWidgets.QMessageBox.warning(self,'Alert1', ".csv파일로 다시 선택해주세요")

    # excel Upload 버튼
    @pyqtSlot()
    def excel_upload(self):
        path = easygui.fileopenbox(multiple=True)
        # csv파일이 아닐 때 경고창 띄우기
        try :
            df_path = pd.read_csv(path[0])
            self.Save_File = df_path
            print(self.Save_File.head())
            self.excel_label.setText((path[0]))
        except :
            self.w.warning.emit()


