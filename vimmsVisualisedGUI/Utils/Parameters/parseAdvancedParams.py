from PyQt5 import QtWidgets as qtw
from vimms.Controller.base import AdvancedParams

def parse_advanced_params(self):

    adv_param_dict = {}
    for child_widget in self.AdvancedParamsGroupBox.findChildren(qtw.QWidget):
        if type(child_widget) == qtw.QLineEdit and child_widget.accessibleName() != "":
            adv_param_dict[child_widget.accessibleName()] = float(child_widget.text())
        elif type(child_widget) == qtw.QComboBox:
            adv_param_dict[child_widget.accessibleName()] = child_widget.currentText()
        elif type(child_widget) == qtw.QGroupBox:
            adv_param_dict[child_widget.accessibleName()] = (
                float(self.MS1ScanWindowMinTextEdit.text()), float(self.MS1ScanWindowMaxTextEdit.text()))
    
    return AdvancedParams(**adv_param_dict)