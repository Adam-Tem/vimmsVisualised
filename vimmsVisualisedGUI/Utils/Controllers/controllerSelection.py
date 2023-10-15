from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from Utils.Controllers.TopN import runTopNController
from Utils.Controllers.TopNSmartRoi import runTopNSmartRoiController

def controllerSelection(self):
    controller = self.ControllerComboBox.currentText()

    match controller:
        case "TopN Controller":
            # self.loadWidget.showLoadingWidget()
            runTopNController(self)
            # self.loadWidget.addExitButton()
        case "TopN Smart ROI Controller":
            runTopNSmartRoiController(self)
