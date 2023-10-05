from Utils.Controllers.TopN import RunTopNController

def controllerSelection(self):
    controller = self.ControllerComboBox.currentText()

    match controller:
        case "TopN Controller":
            RunTopNController(self)