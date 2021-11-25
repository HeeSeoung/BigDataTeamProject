from __future__ import print_function
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from datetime import datetime
from Analysis import Ui_AnalysisWindow
from login import LoginWindow

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    '''
    레이아웃 인스턴스 생성
    그냥 login.py는 복붙했는데 저렇게만 가져오면 되고,
    QT.designer에서 수정한 모듈은 저렇게 가져와야 함.
    '''
    # Ctrl+CV
    login = LoginWindow()
    # QT
    MainWindow = QtWidgets.QMainWindow()
    AnalysisWindow = Ui_AnalysisWindow()
    AnalysisWindow.setupUi(MainWindow)

    #Widget 추가
    widget.addWidget(login)
    widget.addWidget(MainWindow)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(768)
    widget.setFixedWidth(1080)
    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()