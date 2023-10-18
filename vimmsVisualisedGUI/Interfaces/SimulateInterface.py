from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from SimulatePage import Ui_SimulateForm

from vimmsVisualisedGUI.Utils.UploadFile import *
from Utils.setCharge import *
from Utils.Controllers.controllerSelection import *
from Utils.Display.displayParams import *
from Utils.LoadingWidget import *


class SimulatePage(qtw.QWidget, Ui_SimulateForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        
        

        self.fileName = ""
        self.fileLocation = ""
        self.loadWidget = LoadingWidget()

        self.SimulateHomeButton.setIcon(qtg.QIcon("Images/home.png"))

        self.SelectFileButton.clicked.connect(lambda: upload_file(self, "p"))
        self.ControllerComboBox.currentIndexChanged.connect(lambda: displayParams(self))