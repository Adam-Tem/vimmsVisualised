from PyQt5 import QtWidgets as qtw

from StartPage import Ui_Form

class StartPage(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)