from StartPage import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

import sys
qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons


class StartPage(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


if __name__ == "__main__":
    app = qtw.QApplication([])
    widget = StartPage()
    widget.show()

    app.exec_()

