from PyQt5 import QtWidgets as qtw

from vimms.Common import POSITIVE, NEGATIVE
from vimms.BoxManager import BoxManager

from Utils.Parameters.CustomWidgets import *
from Utils.Parameters.ParamWidgets import PARSE_AS_INT, PARSE_AS_LOG

import numpy as np

def parse_params(param_box, constructor_params):
    params = {}
    for val in constructor_params:
        child = param_box.findChild(qtw.QWidget, val)
        if val == "grid":
            params["grid"] = BoxManager()
            continue
        if child == None:
            continue
        if type(child) == QIonModeButton:
            if child.text() == "Positive":
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
            if child.accessibleName() in PARSE_AS_INT:
                params[child.accessibleName()] = int(child.text())
            elif child.accessibleName() in PARSE_AS_LOG:
                params[child.accessibleName()] = np.log(int(child.text()))
            else:
                params[child.accessibleName()] = float(child.text())
    return params