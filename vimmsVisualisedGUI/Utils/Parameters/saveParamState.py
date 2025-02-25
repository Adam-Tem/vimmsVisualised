from PyQt5 import QtWidgets as qtw

from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY
from Utils.PeakPicking.parsePeakPickingParams import parse_peak_picking_params
from Utils.Parameters.parseAdvancedParams import parse_advanced_params
import json
import os

def save_param_state(self, selected_controller, current_index = 0):

    global save_directory

    saved_state = {}
    if current_index == 0:
        saved_state["selected_controller"] = selected_controller
        param_names = identify_params(selected_controller)
        params = parse_params(self.ParamsBox, param_names)
        saved_state["params"] = params
    elif current_index == 1:
        saved_state["params"] = parse_advanced_params(self.AdvancedParamsGroupBox)
    else:
        saved_state["selected_peak_picking"] = self.PeakPickingComboBox.currentText()
        saved_state["params"] = parse_peak_picking_params(
                                                            self.PeakPickingComboBox.currentText(),
                                                          self.PeakPickingParamTab)

    options = qtw.QFileDialog.Options()
    file_dialog = qtw.QFileDialog(self)
    file_dialog.setOptions(options)
    file_dialog.setDirectory(os.path.join(SAVE_DIRECTORY, "saved_states"))
    file_dialog.setNameFilter("JSON files (*.json)")

    if file_dialog.exec_() == qtw.QFileDialog.Accepted:
        file_path = file_dialog.selectedFiles()[0]
        if file_path[-5:] != ".json":
            file_path = file_path + ".json"

        with open(file_path, 'w') as json_file:
            json.dump(saved_state, json_file)