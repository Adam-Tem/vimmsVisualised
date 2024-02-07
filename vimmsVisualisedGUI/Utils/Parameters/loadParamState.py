from PyQt5 import QtWidgets as qtw
import json
from Utils.Parameters.CustomWidgets import QBooleanButton, QIonModeButton

def load_param_state(self, current_index=0):

    if current_index == 0:
         param_box_of_interest = self.ParamsBox
         desc = "Choose a saved controller config"
    elif current_index == 1:
         param_box_of_interest = self.AdvancedParamsGroupBox
         desc = "Choose a saved advanced parameter config"
    else:
         param_box_of_interest = self.PeakPickingParamsBox
         desc = "Choose a saved XCMS config"
    dialog = qtw.QFileDialog()

    saved_param_file_name = dialog.getOpenFileName(None, desc, "", "JSON files (*.json)")[0]
    with open(saved_param_file_name, 'r') as saved_param_file:
        params = json.load(saved_param_file)

    if current_index == 0:
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

                elif type(child_widget) == qtw.QGroupBox:
                     i = 0
                     for sub_text_input in child_widget.findChildren(qtw.QLineEdit):
                          sub_text_input.setText(str(int(params["params"][param_name][i])))
                          i += 1
                elif type(child_widget) == qtw.QLineEdit:
                     child_widget.setText(str(int(params["params"][param_name])))