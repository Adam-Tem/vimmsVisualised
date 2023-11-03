from PyQt5 import QtWidgets as qtw
from Utils.CustomWidgets import *
from vimms.Common import POSITIVE, NEGATIVE

def parse_params(param_box, constructor_params):
    params = {}
    for val in constructor_params:
        child = param_box.findChild(qtw.QWidget, val)
        if child == None:
            continue
        if type(child) == QIonModeButton:
            if child.text() == "positive":
                params[child.accessibleName()] = POSITIVE
            else:
                params[child.accessibleName()] = NEGATIVE
            continue

        if type(child) == QBooleanButton:
            if child.text() == "positive":
                params[child.accessibleName()] = True
            else:
                params[child.accessibleName()] = False
            continue

        if type(child) in [QMzmlUpload, QMgfUpload]:
            params[child.accessibleName()] = child.file_name
            continue
        
        if type(child) == qtw.QComboBox:
            if child.currentText() != "":
                params[child.accessibleName()] = child.currentText()
            continue
        if child.text() == "Simulate":
            continue

        if child.text() != "" and type(child) != qtw.QLabel and child.accessibleName() != "":
            params[child.accessibleName()] = float(child.text())
    return params