# -*- coding: utf-8 -*-
import random
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QRegExp, QTimer, pyqtSignal, Qt
from PyQt5.QtGui import QRegExpValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from Singal.Calculator import GetCalculator, TipForUser

from Singal.Draggable import Draggable
class GameWindow(QMainWindow):  # 继承自QWidget
    gameFinished = pyqtSignal()
    def __init__(self, start, end, mode):
        super().__init__()
        self.score = 100
        self.resize(1200, 660)
        self.start = start
        self.end = end
        self.mode = mode
        self.ans = random.randint(self.start, self.end)
        self.tried = 0
        self.initializeUI()
        self.setPosition()
        self.setStyle()
        self.setToolSingal()
        self.WelcomePage = None  # 添加一个属性来保存登录窗口的引用

    def setLoginWindow(self, WelcomePage):
        self.WelcomePage = WelcomePage  # 设置登录窗口的引用
    def mousePressEvent(self, event):
        self.draggable.mousePressEvent(event)
    def mouseMoveEvent(self, event):
        self.draggable.mouseMoveEvent(event)
    def goBackToWelcome(self):
        if self.WelcomePage:
            self.WelcomePage.show()  # 显示登录窗口
        self.close()  # 关闭当前窗口
    def initializeUI(self):
        self.setObjectName("Form")


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showAnswerButton = QtWidgets.QPushButton(self)
        self.showAnswerButton.setObjectName("ShowAnswer")

        self.welcomeUserLabel = QtWidgets.QLabel(self)
        self.welcomeUserLabel.setObjectName("WelcomeUserLabel")

        self.answerEdit = QtWidgets.QLineEdit(self)
        self.answerEdit.setObjectName("AnswerEdit")

        self.inputAnswerLabel = QtWidgets.QLabel(self)
        self.inputAnswerLabel.setObjectName("InputAnswerLabel")

        self.JudgeAnswerLabel = QtWidgets.QLabel(self)
        self.JudgeAnswerLabel.setObjectName("JudgeAnswerLabel")

        self.makeSureAnswerButton = QtWidgets.QPushButton(self)
        self.makeSureAnswerButton.setObjectName("MakeSureAnswer")

        self.tipAnswerLabel = QtWidgets.QLabel(self)
        self.tipAnswerLabel.setObjectName("TipAnswer")

        self.CloseBtn = QtWidgets.QPushButton(self)
        self.ExpandBtn = QtWidgets.QPushButton(self)
        self.ReduceBtn = QtWidgets.QPushButton(self)

        self.goBackBtn = QtWidgets.QPushButton(self)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.welcomeUserLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.inputAnswerLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.JudgeAnswerLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.tipAnswerLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.welcomeUserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.answerEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.inputAnswerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.JudgeAnswerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tipAnswerLabel.setAlignment(QtCore.Qt.AlignCenter)

    def setPosition(self):
        mulpity = self.width() // 890
        self.welcomeUserLabel.setGeometry(self.width() // 4, self.height() // 7, self.width() // 2, self.height() // 10)
        self.tipAnswerLabel.setGeometry(self.width() // 4, self.height() // 4, self.width() // 2, self.height() // 10)

        self.inputAnswerLabel.setGeometry(10, int(self.height() // 2.1), self.width() // 4, self.height() // 14)
        self.answerEdit.setGeometry(int(self.width() // 3.7), int(self.height() // 2.2), self.width() // 2, self.height() // 10)
        self.JudgeAnswerLabel.setGeometry(0, int(self.height() // 1.7), int(self.width()), self.height() // 18)
        self.makeSureAnswerButton.setGeometry(int(self.width() // 2.4), int(self.height() // 1.4), self.width() // 6, int(self.height() // 10.2))
        self.showAnswerButton.setGeometry(int(self.width() // 2.4), int(self.height() // 1.2), self.width() // 6, int(self.height() // 10.2))
        self.goBackBtn.setGeometry(10, 10, 40, 40)
        self.CloseBtn.setGeometry(self.width() - 60, 10, 40, 40)
        self.ExpandBtn.setGeometry(self.width() - 100, 10, 40, 40)
        self.ReduceBtn.setGeometry(self.width() - 140, 10, 40, 40)
        self.setFont(int(mulpity))
    def setStyle(self, **kwargs):
        self.welcomeUserLabel.setStyleSheet(
                                     "color: rgb(119,110,101);\n"
                                     # "background-color: green;\n"
                                     "border-radius: 10px;"
        )
        self.setStyleSheet(
                        "background-color: rgb(205, 193, 180);\n"
                        "border-radius: 10px;"
        )

        self.makeSureAnswerButton.setStyleSheet(
                                     "color: #EE4000;\n"
                                     "background-color: rgb(242, 177, 121);\n"
                                     "border-radius: 10px;"
        )
        self.showAnswerButton.setStyleSheet(
                                     "color: #EE4000;\n"
                                     "background-color: rgb(242, 177, 121);\n"
                                     "border-radius: 10px;"
        )
        self.tipAnswerLabel.setStyleSheet(
                                     "color: rgb(119,110,101);\n"
                                     "border-radius: 10px;"
        )
        self.inputAnswerLabel.setStyleSheet(
                                     "color: rgb(165,42,42);\n"
                                     "border-radius: 10px;"
        )
        self.answerEdit.setStyleSheet(
                                    "color: rgb(119,110,101);\n"
                                    "background-color: rgb(237, 224, 200);\n"
                                    "border-radius: 10px;"
        )
        self.JudgeAnswerLabel.setStyleSheet(
                                      "color: #EE4000;\n"
                                      # "background-color: rgb(237, 224, 200);\n"
                                      "border-radius: 10px;"
        )
        self.goBackBtn.setStyleSheet(
            # "background-color: #EEEED1;\n"
            "border-radius: 15px;\n"
            "font: 22pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.CloseBtn.setStyleSheet(
            # "background-color: #EEEED1;\n"
            "border-radius: 15px;\n"
            "font: 20pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.ExpandBtn.setStyleSheet(
            # "background-color: #EEEED1;\n"
            "border-radius: 15px;\n"
            "font: 26pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.ReduceBtn.setStyleSheet(
            # "background-color: #EEEED1;\n"
            "border-radius: 15px;\n"
            "font: 26pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        # 8B8B7A
        pass
    def setToolSingal(self):
        self.draggable = Draggable(self)
        self.answerEdit.setPlaceholderText(
            f"请输入您猜测的数字, 当前范围为{self.start}-{self.end}")  # 只要行编辑为空，设置此属性将使行编辑显示为灰色的占位符文本。默认情况下，此属性包含一个空字符串。这是非常好的使用方法，可以在用户输入密码前看到一些小提示信息。
        self.answerEdit.setMaxLength(7)  # 设置最长密码只能输入5位
        reg_exp = QRegExp("[0-9]+$")  # 正则输入， 只接受数字
        reg_validator = QRegExpValidator(reg_exp)
        self.answerEdit.setValidator(reg_validator)

        self.showAnswerButton.clicked.connect(self.showAnswer)
        self.makeSureAnswerButton.clicked.connect(self.JudgeAnswer)
        self.showAnswerButton.clicked.connect(self.ShowAnswer)
        self.goBackBtn.clicked.connect(self.goBackToWelcome)
        self.CloseBtn.clicked.connect(self.close) # type: ignore
        self.ExpandBtn.clicked.connect(self.toggleMaximizeRestore) # type: ignore
        self.ReduceBtn.clicked.connect(self.showMinimized) # type: ignore
        pass

    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    def showAnswer(self):
        self.answerEdit.clear()
        #告诉玩家答案, 退回主程序
    def JudgeAnswer(self):
        UserGuess = self.answerEdit.text()
        if UserGuess == '':
            return
        self.tried += 1
        self.JudgeAnswerLabel.setText(self._translate("Form", f"您已经尝试了{self.tried}次"))
        rList = GetCalculator(int(UserGuess), self.start, self.end, self.ans)
        if rList[0] == True:
            self.timer = QTimer(self)  # 创建QTimer实例
            self.timer.timeout.connect(self.updateCountdown)  # 连接timeout信号到autoReturn槽函数
            self.remaining_time = 5  # 设置初始剩余时间为5秒
            self.JudgeAnswerLabel.setText(self._translate("Form", f"恭喜您猜对正确答案{self.ans}  ╮(￣▽ ￣)╭  ! 点击左上角返回或{self.remaining_time}秒过后自动返回!"))
            self.timer.start(1000)  # 启动定时器，每1000毫秒（1秒）超时一次
            self.gameFinished.emit()
            #此处为猜对了, 进行返回操作
            pass
        else:
            if len(rList) != 1:
                #更新提示信息为Start-End
                self.start = rList[1]
                self.end = rList[2]
                self.SetAnswerLbael()
                pass
        self.score -= 2
        self.answerEdit.clear()
    def ShowAnswer(self):
        self.JudgeAnswerLabel.setText(self._translate("Form",
                                                      f"正确答案是{self.ans}  b(￣▽￣)d  ! 点击左上角返回"))

        self.makeSureAnswerButton.setEnabled(False)
        self.makeSureAnswerButton.setStyleSheet(
            "background-color: rgba(205, 205, 180, 128);"
            "color: grba(255, 255, 224, 128)")
        pass
    def updateCountdown(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.JudgeAnswerLabel.setText(self._translate("Form",
                                                          f"恭喜您猜对正确答案{self.ans}  ╮(￣▽ ￣)╭  ! 点击左上角返回或{self.remaining_time}秒过后自动返回"))
        else:
            self.timer.stop()  # 停止定时器
            self.goBackToWelcome()  # 执行跳转逻辑
    def SetAnswerLbael(self):
        self.tipAnswerLabel.setText(self._translate("Form", f"当前猜数字范围为{self.start}-{self.end}"))
        self.answerEdit.setPlaceholderText(
            f"请输入您猜测的数字, 当前范围为{self.start}-{self.end}")  # 只要行编辑为空，设置此属性将使行编辑显示为灰色的占位符文本。默认情况下，此属性包含一个空字符串。这是非常好的使用方法，可以在用户输入密码前看到一些小提示信息。
    def retranslateUi(self):
        self._translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self._translate("Form", "猜数字小游戏"))
        self.showAnswerButton.setText(self._translate("Form", "显示答案"))
        self.welcomeUserLabel.setText(self._translate("Form", "欢迎来到猜数字小游戏！"))
        self.inputAnswerLabel.setText(self._translate("Form", "输入您的猜测答案:"))
        self.makeSureAnswerButton.setText(self._translate("Form", "提交答案"))
        self.tipAnswerLabel.setText(self._translate("Form", f"当前猜数字范围为{self.start}-{self.end}"))
        self.JudgeAnswerLabel.setText(self._translate("Form", f"您已经尝试了0次"))
        self.goBackBtn.setText(self._translate("Form", f"<"))
        self.CloseBtn.setText(self._translate("self", "×"))
        self.ExpandBtn.setText(self._translate("self", "▢"))
        self.ReduceBtn.setText(self._translate("self", "-"))
    def setFont(self, mulpity):
        font = QFont()
        font.setFamily("楷体")
        font.setPointSize(15 + mulpity)
        self.showAnswerButton.setFont(font)
        self.makeSureAnswerButton.setFont(font)
        self.tipAnswerLabel.setFont(font)
        self.JudgeAnswerLabel.setFont(font)
        self.inputAnswerLabel.setFont(font)
        self.goBackBtn.setFont(font)
        font.setPointSize(13 + mulpity)
        self.answerEdit.setFont(font)
        font.setPointSize(20 + mulpity)
        self.welcomeUserLabel.setFont(font)
    def resizeEvent(self, a0):
        super().resizeEvent(a0)
        self.setPosition()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gameWindow = GameWindow(1, 1000, 'easy')
    gameWindow.show()
    sys.exit(app.exec_())
