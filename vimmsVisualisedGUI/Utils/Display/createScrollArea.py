from PyQt5 import QtWidgets as qtw

def createScrollArea(param_box, page, row):
    if type(param_box.parent()) != qtw.QWidget:
        height = param_box.height()
        pos_to_match = param_box.pos()
        scroll = qtw.QScrollArea(param_box.parent())
        scroll.setSizeAdjustPolicy(qtw.QAbstractScrollArea.AdjustToContents)
        scroll.setWidgetResizable(True)
        scroll.setWidget(param_box)
        if page == "Experiment":
            scroll.setGeometry(pos_to_match.x(), pos_to_match.y(),600, 161)
        else:
            scroll.setGeometry(pos_to_match.x(), pos_to_match.y(),600, 161)
        scroll.setVisible(True)