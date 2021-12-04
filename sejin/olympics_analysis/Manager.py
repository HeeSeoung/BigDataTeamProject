import pandas as pd
from PyQt5 import QtWidgets, QtCore
from Page_Start import ui_Firstwindow
from Page_Analysis import ui_AnalysisWindow
import sys
from Preprocessing import AddNouns, textPreprocessing
from make_wordcloud import makeWC

raw_dataset = pd.DataFrame()
olympics_year = 0

class TaskThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
    taskFinished = QtCore.pyqtSignal()
    def preprocess(self, Save_File):
        raw_dataset = Save_File
        pre = AddNouns(raw_dataset)  # 명사 뽑아내기
        pre = textPreprocessing(pre)  # 텍스트 전처리
        pre = pre[pre['label'] == '양궁']
        # Wordcloud 생성
        for sport in pre['label'].unique():
            makeWC(pre, sport)
        pre.to_csv('./resources/pre.csv')
        print("완료")

class Firstwindow(QtWidgets.QMainWindow, ui_Firstwindow):

    def __init__(self, parent=None):
        super(Firstwindow, self).__init__(parent)
        self.setupUi(self)
        self.progress_bar.setRange(0,1)
        self.start_btn.clicked.connect(self.startButtonPressed)
        self.myLongTask = TaskThread()
        self.myLongTask.taskFinished.connect(self.onFinished)

    def startButtonPressed(self):
        self.progress_bar.setRange(0,0)
        self.myLongTask.preprocess(self.Save_File)
        # self.preprocess()
        # 완료되면 다음페이지로!
        # widget.setCurrentIndex(widget.currentIndex() + 1)
    def onFinished(self):
        self.progress_bar.setRange(0,1)
        self.progress_bar.setValue(1)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def preprocess(self):
    #     raw_dataset = self.Save_File
    #     pre = AddNouns(raw_dataset)  # 명사 뽑아내기
    #     pre = textPreprocessing(pre)  # 텍스트 전처리
    #     pre = pre[pre['label'] == '양궁']
    #     # Wordcloud 생성
    #     for sport in pre['label'].unique():
    #         makeWC(pre, sport)
    #     pre.to_csv('./resources/pre.csv')


class AnalysisWindow(QtWidgets.QMainWindow, ui_AnalysisWindow):
    def __init__(self, parent=None):
        super(AnalysisWindow, self).__init__(parent)
        self.setupUi(self)
        self.return_btn.clicked.connect(self.returnButtonPressed)

    def returnButtonPressed(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # 화면 전환용 Widget 생성
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    firstUI = Firstwindow()
    AnalysisUI = AnalysisWindow()

    # Widget에 추가
    widget.addWidget(firstUI)
    widget.addWidget(AnalysisUI)

    # 화면 띄우기
    widget.setFixedWidth(1080)
    widget.setFixedHeight(768)
    widget.show()

    app.exec_()
