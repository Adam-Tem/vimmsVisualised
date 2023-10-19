from PyQt5 import QtWidgets as qtw

def createScrollArea(self):
    scroll = qtw.QScrollArea(parent=self)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(340)
    scroll.setFixedWidth(600)
    scroll.setGeometry(0, 200, 600, 340)
    scroll.setWidget(self.ParamsBox)
    scroll.setVisible(True)