from PyQt5 import QtWidgets as qtw

def createScrollArea(param_box, height):
    scroll = qtw.QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(height)
    scroll.setFixedWidth(600)
    scroll.setGeometry(0, 200, 600, height)
    scroll.setWidget(param_box)
    scroll.setVisible(True)