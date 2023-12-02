from PyQt5 import QtWidgets as qtw
import json
from Utils.CustomWidgets import QBooleanButton, QIonModeButton
from Utils.setCharge import setButtonText

def load_param_state(self):

    if self.ParamTabs.currentIndex() == 0:
         param_box_of_interest = self.ParamsBox
         desc = "Choose a saved controller config"
    else:
         param_box_of_interest = self.XCMSParamsBox
         desc = "Choose a saved XCMS config"
    dialog = qtw.QFileDialog()

    saved_param_file_name = dialog.getOpenFileName(None, desc, "", "JSON files (*.json)")[0]
    with open(saved_param_file_name, 'r') as saved_param_file:
        params = json.load(saved_param_file)

    if self.ParamTabs.currentIndex() == 0:
        self.ControllerComboBox.setCurrentText(params["selected_controller"])

    for child_widget in param_box_of_interest.findChildren(qtw.QWidget):
            param_name = child_widget.accessibleName()
            if param_name in params["params"]:
                if type(child_widget) == QIonModeButton or type(child_widget) == QBooleanButton:
                    if params["params"][param_name] == "Negative" or params["params"][param_name] == "False":
                        child_widget.setStyleSheet("background-color: red; color: black;")
                        child_widget.setText(str(params["params"][param_name]))

                elif type(child_widget) == qtw.QSpinBox:
                    child_widget.setValue(int(params["params"][param_name]))
                else:
                     child_widget.setText(str(int(params["params"][param_name])))