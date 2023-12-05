from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from SimulatePage import Ui_SimulateForm

from vimmsVisualisedGUI.Utils.UploadFile import *
from Utils.setCharge import *
from Utils.Controllers.controllerSelection import *
from Utils.Display.displayParams import *
from Utils.LoadingWidget import *
from Utils.Parameters.ParamWidgets import CONTROLLER_PARAMS, CONTROLLERS
from Utils.Parameters.loadParamState import load_param_state
from Utils.Parameters.saveParamState import save_param_state


class SimulatePage(qtw.QWidget, Ui_SimulateForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.file_name = ""
        self.file_location = ""
        
        self.SimulateHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.LoadParamsButton.setIcon(qtg.QIcon("Images/folder.svg"))
        self.SaveParamsButton.setIcon(qtg.QIcon("Images/save.png"))

        self.SelectFileButton.clicked.connect(lambda: upload_file(self, "p"))
        self.ControllerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ParamsBox,self.ControllerComboBox.currentText(), 
            [True, "Simulate"], CONTROLLERS, CONTROLLER_PARAMS,[True,"Simulate"] ))
        
        self.SaveParamsButton.clicked.connect(
            lambda: save_param_state(self,
                                     self.ControllerComboBox.currentText())
        )

        self.LoadParamsButton.clicked.connect(
            lambda: load_param_state(self)
        )