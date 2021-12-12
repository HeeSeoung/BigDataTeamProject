import argparse
import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import QTimer, Qt, QCoreApplication
import PySide2.QtWidgets as QtWidgets
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pallete import set_pallete
from qt_material import apply_stylesheet, QtStyleTools
from multiprocessing import freeze_support
from make_graph import *
import pandas as pd

freeze_support()
QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

app = QApplication([])
app.processEvents()
app.setQuitOnLastWindowClosed(False)
app.lastWindowClosed.connect(lambda: app.quit())


class MainWindow(QMainWindow):
    def __init__(self, theme):
        self.theme = theme
        super(MainWindow, self).__init__()
        self.main = QUiLoader().load('resources/ui/test_window.ui', self)
        self.main.setWindowTitle("Data Pursuit")
        self.setWindowIcon(QIcon('resources/pic/DP_logo_3.png'))

        # 색상 세팅
        color_pallete = set_pallete(theme)

        # 툴바에 이미지 세팅
        self.toolbar = self.findChild(QToolBar,"toolBar_vertical")
        # Text 버튼
        btn1 = QAction("Olympics Analysis", self)
        btn1.setStatusTip("This is your button")
        # Olympic 이미지 버튼
        btn2 = QAction(QIcon("./resources/pic/olympic.png"), "&Your button", self)
        btn2.setStatusTip("This is your button")
        self.toolbar.addAction(btn1)
        self.toolbar.addAction(btn2)


        # 1페이지 올림픽 동향
        self.graphLayout1_1 = self.findChild(QGridLayout, "graphLayout1_1")
        self.graphLayout1_1.addWidget(setGraph1_1(color_pallete))

        self.graphLayout1_2 = self.findChild(QGridLayout, "graphLayout1_2")
        self.graphLayout1_2.addWidget(setGraph1_2(color_pallete))

        self.graphLayout1_3 = self.findChild(QGridLayout, "graphLayout1_3")
        self.graphLayout1_3.addWidget(setGraph1_3(color_pallete))

        self.graphLayout2_1 = self.findChild(QGridLayout, "graphLayout2_1")
        self.graphLayout2_1.addWidget(setGraph2_1(color_pallete)) #finish

        self.graphLayout2_2 = self.findChild(QGridLayout, "graphLayout2_2")
        self.graphLayout2_2.addWidget(setGraph2_2(color_pallete))

        self.graphLayout2_3 = self.findChild(QGridLayout, "graphLayout2_3")
        self.graphLayout2_3.addWidget(setGraph2_3(color_pallete))

        # 3페이지 GDP
        self.graphLayout3_1 = self.findChild(QGridLayout, "graphLayout3_1")
        self.graphLayout3_1.addWidget(setGraph3_1(color_pallete)) #finish

        self.graphLayout3_2 = self.findChild(QGridLayout, "graphLayout3_2")
        self.graphLayout3_2.addWidget(setGraph3_2(color_pallete)) #finish



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    color_list =['red', 'cyan', 'teal', 'lightgreen', 'blue', 'amber', 'pink', 'purple', 'yellow']
    bgcolor_list = ['dark', 'light']
    parser.add_argument('--color', '-c', help='choose one >> [red, cyan, teal, lightgreen, blue, amber, pink, purple, yellow]',default="blue")
    parser.add_argument('--bgcolor', '-b' ,help ='choose one >> [dark, light]', default = "dark")
    opt = parser.parse_args()
    if (opt.color not in color_list) or (opt.bgcolor not in bgcolor_list):
        exit()
    else :
        theme = f"{opt.bgcolor}_{opt.color}.xml"#"dark_blue.xml"
        apply_stylesheet(app, theme=theme)

        window = MainWindow(theme)
        window.main.show()
        app.exec_()
