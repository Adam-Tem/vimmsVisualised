from Utils.Controllers.TopN import runTopNController
from Utils.Controllers.TopNSmartRoi import runTopNSmartRoiController

def controllerSelection(self):
    controller = self.ControllerComboBox.currentText()

    match controller:
        case "TopN Controller":
            runTopNController(self)
            
        case "TopN Smart ROI Controller":
            runTopNSmartRoiController(self)