import json
import os.path
import sys
from Page.MyGame import GameWindow
from Page.WelcomePage import WelcomeWindow
from PyQt5.QtWidgets import QApplication
from Page.OrderPage import OrderPage
class StartGame(object):
    def __init__(self, app):
        self.app = app
        self.task = None  # 我们将在这里存储ChromosomeProcessor实例
        self.welcomePage = None
        self.initJson("start")
    def run(self):
        self.welcomePage = WelcomeWindow()
        self.welcomePage.show()
        self.welcomePage.EasyModelBtn.clicked.connect(lambda : self.StartGame(1, 100, 'easy'))
        self.welcomePage.MiddleModelBtn.clicked.connect(lambda : self.StartGame(1, 500, 'medium'))
        self.welcomePage.HardModelBtn.clicked.connect(lambda : self.StartGame(1, 1000, 'hard'))
        self.welcomePage.OrderChartBtn.clicked.connect(self.OrderShow)
    #验证账号密码
    def StartGame(self, start, end, sub):
        self.myGame = GameWindow(start, end, sub)
        self.myGame.setLoginWindow(self.welcomePage)  # 设置登录窗口的引用
        self.myGame.gameFinished.connect(self.onGameFinished)
        self.welcomePage.close()
        self.myGame.show()
    def OrderShow(self):
        self.OrderPage = OrderPage()
        self.OrderPage.setLoginWindow(self.welcomePage)  # 设置登录窗口的引用
        self.OrderPage.ClearScore.clicked.connect(lambda :self.initJson('clear'))
        self.welcomePage.close()
        self.OrderPage.show()
    def initJson(self, mode):
        if os.path.exists('./bestScore.json') and mode == 'start':
            return
        initial_scores = {
            'easy': 0,
            'medium': 0,
            'hard': 0
        }
        with open('./bestScore.json', 'w') as file:
            json.dump(initial_scores, file, indent=4)
        if mode == 'clear':
            self.OrderPage.read_high_scores('./bestScore.json')
        # 写入JSON文件
    def onGameFinished(self):
        # 这里是游戏结束时需要执行的代码
        score = self.myGame.score
        mode = self.myGame.mode
        # 根据模式定义JSON文件名
        try:
            with open('./bestScore.json', 'r') as file:
                scores = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            scores = {}
        # 更新对应模式的分数
        current_score = scores.get(mode, 0)
        scores[mode] = max(current_score, score)
        # 写入JSON文件
        with open('./bestScore.json', 'w') as file:
            json.dump(scores, file, indent=4)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    run = StartGame(app)
    run.run()
    sys.exit(app.exec_())
