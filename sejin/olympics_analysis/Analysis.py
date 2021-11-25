# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

olympics_dict = {2016 : "리우", 2020 : "도쿄"}
eng_to_han = {"리우" : "rio", "도쿄" : "tokyo"}


class Ui_AnalysisWindow(object):
    def setupUi(self, MainWindow):

        # Main 윈도우 세팅
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 754)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # set vertical Layout
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 130, 101, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # set Button Layout (vertical Layout)
        self.ButtonLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ButtonLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonLayout.setObjectName("ButtonLayout")

        # set Button
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.ButtonLayout.addWidget(self.pushButton_9)

        # 처음 왼쪽 메뉴바 세팅
        year = 2020
        menu_start_w = 10
        menu_start_h = 10

        # set Olympics LOGO
        lo_w = 160
        lo_h = 120
        self.setOlympicsLOGO(menu_start_w,menu_start_h, lo_w, lo_h, year)

        # set Olympics 개최년도
        la_w = 160
        la_h = 30
        la_start_h = menu_start_h+lo_h+5
        self.setOlympicsYEAR(menu_start_w, la_start_h, la_w, la_h, year)


        # 메인 윈도우 화면 중앙으로 옮기기
        MainWindow.setCentralWidget(self.centralwidget)

        # 메뉴바 생성
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # 상태창 생성
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 몰라
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))

    def setOlympicsLOGO(self, start_w, start_h, width, height, year):
        # 이미지 담을 라벨을 생성
        self.olympics_logo = QtWidgets.QLabel(self.centralwidget)
        self.olympics_logo.setGeometry(QtCore.QRect(start_w, start_h, width, height))
        # 이미지 가져오기, resize
        self.pixmap = QtGui.QPixmap(f'resources/Olympics_logo/{eng_to_han[olympics_dict[year]]}.png')
        self.pixmap = self.pixmap.scaled(width-1, height-1)
        # 이미지 세팅
        self.olympics_logo.setPixmap(self.pixmap)
        self.olympics_logo.setObjectName("olympics_logo")
        self.olympics_logo.show()

    def setOlympicsYEAR(self, start_w, start_h, width, height, year):
        self.when_olympics = QtWidgets.QLabel(self.centralwidget)
        self.when_olympics.setGeometry(QtCore.QRect(start_w, start_h, width, height))
        olympics_name = olympics_dict[year]
        year = str(year)
        self.when_olympics.setText(f"{year} {olympics_name}올림픽 통계")
        self.when_olympics.setAlignment(QtCore.Qt.AlignCenter)
        self.when_olympics.setObjectName("when_olympics")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AnalysisWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
