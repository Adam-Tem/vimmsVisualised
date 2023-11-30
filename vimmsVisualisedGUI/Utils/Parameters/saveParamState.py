from PyQt5 import QtWidgets as qtw

from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import CONTROLLERS
import json

def save_param_state(self, param_box, selected_controller):

    saved_state = {}
    saved_state["selected_controller"] = selected_controller
    param_names = identify_params(selected_controller, CONTROLLERS)
    params = parse_params(param_box, param_names)
    saved_state["params"] = params
    file_path = "results/saved_state.json"

    options = qtw.QFileDialog.Options()
    file_dialog = qtw.QFileDialog(self)
    file_dialog.setOptions(options)
    file_dialog.setNameFilter("JSON files (*.json)")

    if file_dialog.exec_() == qtw.QFileDialog.Accepted:
        file_path = file_dialog.selectedFiles()[0]
        if file_path[-5:] != ".json":
            file_path = file_path + ".json"

        with open(file_path, 'w') as json_file:
            json.dump(saved_state, json_file)