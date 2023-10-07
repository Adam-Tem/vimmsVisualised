from PyQt5 import QtCore as qtc

from Utils.Controllers.TopN import RunTopNController


def controllerSelection(self):
    controller = self.ControllerComboBox.currentText()

    match controller:
        case "TopN Controller":
            # self.loadWidget.showLoadingWidget()
            RunTopNController(self)
            # self.loadWidget.addExitButton()