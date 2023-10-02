from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from SimulatePage import Ui_SimulateForm

class SimulatePage(qtw.QWidget, Ui_SimulateForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.SimulateHomeButton.setIcon(qtg.QIcon("Images/home.png"))