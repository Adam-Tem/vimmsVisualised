from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from VisualisePage import Ui_VisualiseForm

class VisualisePage(qtw.QWidget, Ui_VisualiseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.VisualiseHomeButton.setIcon(qtg.QIcon("Images/home.png"))