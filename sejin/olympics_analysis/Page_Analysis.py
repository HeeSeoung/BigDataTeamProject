from __future__ import print_function
import pandas as pd
import PyQt5.QtWidgets
import easygui
from PyQt5.QtCore import *
from PyQt5 import uic, QtGui
import sys
from PyQt5 import QtWidgets



class ui_AnalysisWindow(object) :
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        uic.loadUi('resources/UI/bigdata_2.ui', self)
        # self.sports = ""
        # self.year = ""

        # 페이지 갱신됨(2021/12/02)
        # 초기화
        # self.csv_file = pd.read_csv('/resources/csv_file')
        self.olympic_logo = self.findChild(QtWidgets.QLabel,"olympic_logo")
        self.wordcloud = self.findChild(QtWidgets.QLabel,"Wordcloud")
        # self.set_Wordcloud()

        self.return_btn = self.findChild(QtWidgets.QPushButton,"return_btn")
        self.dropbox = self.findChild(QtWidgets.QComboBox,"cbox")
        self.search_btn = self.findChild(QtWidgets.QPushButton,"search_btn")

        # Graph Visualization
        self.graph1 = self.findChild(QtWidgets.QGraphicsView,"graph_1")
        self.graph2 = self.findChild(QtWidgets.QGraphicsView, "graph_2")
        self.graph3 = self.findChild(QtWidgets.QGraphicsView, "graph_3")
        self.graph4 = self.findChild(QtWidgets.QGraphicsView, "graph_4")


    # Logo Image 세팅
    def set_Wordcloud(self, sports):
        self.wc = QtGui.QPixmap(f'resources/wordcloud/{sports}.png')
        self.wc = self.wc.scaled(350, 320)
        self.wordcloud.setPixmap(self.wc)
        self.wordcloud.show()



