# draggable.py
from PyQt5.QtCore import Qt, QPoint


#<------实现鼠标拖拽------>
class Draggable(object):
    def __init__(self, window):
        self.window = window
        self.drag_position = QPoint()
        # print("初始化成功")
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.window.frameGeometry().topLeft()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # print(self.drag_position)
            self.window.move(event.globalPos() - self.drag_position)
            event.accept()
