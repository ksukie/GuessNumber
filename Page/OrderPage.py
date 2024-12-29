# -*- coding: utf-8 -*-
import json
import sys

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from Singal.Draggable import Draggable
class OrderPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setPosition()
        self.setStyle()
        self.setTool()
        self.read_high_scores('./bestScore.json')
        self.WelcomePage = None  # 添加一个属性来保存登录窗口的引用

    def read_high_scores(self, filename):
        # 尝试读取现有的分数记录
        try:
            with open(filename, 'r') as file:
                scores = json.load(file)
                self.E_BestScoreLabel.setText(self._translate("self", f"简单模式: {scores['easy']} 分 "))
                self.M_BestScoreLabel.setText(self._translate("self", f"中等模式: {scores['medium']} 分"))
                self.H_BestScoreLabel.setText(self._translate("self", f"困难模式: {scores['hard']} 分"))
        except :
            pass

    def setLoginWindow(self, WelcomePage):
        self.WelcomePage = WelcomePage  # 设置登录窗口的引用

    def goBackToWelcome(self):
        if self.WelcomePage:
            self.WelcomePage.show()  # 显示登录窗口
        self.close()  # 关闭当前窗口
    def mousePressEvent(self, event):
        self.draggable.mousePressEvent(event)
    def mouseMoveEvent(self, event):
        self.draggable.mouseMoveEvent(event)
    def setTool(self):
        self.draggable = Draggable(self)  #<------登陆界面拖拽功能------>
        self.CloseBtn.clicked.connect(self.close) # type: ignore
        self.goBackBtn.clicked.connect(self.goBackToWelcome)

    def setStyle(self, **kwargs):
        self.widget.setStyleSheet(
            "border-radius: 20px;\n"
            "background-color: #CDCDB4;\n"
        )
        self.widget1.setStyleSheet(
            "border-radius: 20px;\n"
            "background-color: #EEEED1;\n"
        )
        self.E_BestScoreLabel.setStyleSheet(
            # "background-color: #CDCDB4;\n"
            "border-radius: 15px;\n"
            "font: 16pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.M_BestScoreLabel.setStyleSheet(
            # "background-color: #CDCDB4;\n"
            "border-radius: 15px;\n"
            "font: 16pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.H_BestScoreLabel.setStyleSheet(
            # "background-color: #CDCDB4;\n"
            "border-radius: 15px;\n"
            "font: 16pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.TipLabel.setStyleSheet(
            "background-color: #EEEED1;\n"
            "border-radius: 15px;\n"
            "font: 24pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.goBackBtn.setStyleSheet(
            # "background-color: #EEEED1;\n"
            "border-radius: 15px;\n"
            "font: 26pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.CloseBtn.setStyleSheet(
            # "background-color: #EEEED1;\n"
            "border-radius: 15px;\n"
            "font: 26pt \"宋体\";"
            "color :#CD5555;"
            "font-weight: bold;"
        )
        self.ClearScore.setStyleSheet(
            "background-color: rgba(255, 48, 48, 168);\n"
            "border-radius: 15px;\n"
            "font: 16pt \"宋体\";"
            "color :white;"
            "font-weight: bold;"
        )

    def setPosition(self):
        self.widget.setGeometry(0, 0, 1080, 580)
        self.widget1.setGeometry(240, 40, 600, 500)
        self.goBackBtn.setGeometry(10, 10, 40, 40)
        self.TipLabel.setGeometry(150, 15, self.widget1.width() // 2, 60)
        self.E_BestScoreLabel.setGeometry(150, 90, self.widget1.width() // 2, 110)
        self.M_BestScoreLabel.setGeometry(150, 220, self.widget1.width()//2, 110)
        self.H_BestScoreLabel.setGeometry(150, 345, self.widget1.width()//2, 110)
        self.ClearScore.setGeometry(150, 450, self.widget1.width()//2, 30)
        self.CloseBtn.setGeometry(self.widget.width() - 60, 10, 40, 40)
    def setupUi(self):
        self.setObjectName("Frame")
        self.resize(1200, 700)
        self.setStyleSheet("")

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(self)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.E_BestScoreLabel = QtWidgets.QLabel(self.widget1)
        self.M_BestScoreLabel = QtWidgets.QLabel(self.widget1)
        self.H_BestScoreLabel = QtWidgets.QLabel(self.widget1)
        self.TipLabel = QtWidgets.QLabel(self.widget1)

        self.CloseBtn = QtWidgets.QPushButton(self.widget)
        self.ClearScore = QtWidgets.QPushButton(self.widget1)
        self.CloseBtn.setObjectName("CloseBtn")

        self.goBackBtn = QtWidgets.QPushButton(self.widget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.E_BestScoreLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.E_BestScoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.M_BestScoreLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.M_BestScoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.H_BestScoreLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.H_BestScoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TipLabel.setTextFormat(QtCore.Qt.MarkdownText)
    def retranslateUi(self):
        self._translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self._translate("self", "self"))
        self.CloseBtn.setText(self._translate("self", "×"))
        self.goBackBtn.setText(self._translate("Form", f"<"))
        self.TipLabel.setText(self._translate("Form", f"最高分排行榜"))
        self.ClearScore.setText(self._translate("Form", f"清空历史分数"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = OrderPage()
    frame.show()
    sys.exit(app.exec_())