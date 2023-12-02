from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import Qt as qt

def createScrollArea(param_box, page, row):

    pos_to_match = param_box.pos()
    scroll = qtw.QScrollArea(param_box.parent())
    scroll.setSizeAdjustPolicy(qtw.QAbstractScrollArea.AdjustToContents)
    scroll.setWidgetResizable(True)
    scroll.setWidget(param_box)
    scroll.setHorizontalScrollBarPolicy(1)
    scroll.setVerticalScrollBarPolicy(qt.ScrollBarAlwaysOn)
    if page == "Experiment":
        scroll.setGeometry(pos_to_match.x(), pos_to_match.y(),557, 161)
    else:
        scroll.setGeometry(pos_to_match.x(), pos_to_match.y(),556, 161)
    scroll.setVisible(True)
    scroll.lower()