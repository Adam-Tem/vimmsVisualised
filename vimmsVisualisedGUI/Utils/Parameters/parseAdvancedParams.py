from PyQt5 import QtWidgets as qtw
from vimms.Controller.base import AdvancedParams

def parse_advanced_params(adv_param_group_box):

    adv_param_dict = {}
    for child_widget in adv_param_group_box.findChildren(qtw.QWidget):
        if type(child_widget) == qtw.QLineEdit and child_widget.accessibleName() != "":
            adv_param_dict[child_widget.accessibleName()] = float(child_widget.text())
        elif type(child_widget) == qtw.QComboBox:
            adv_param_dict[child_widget.accessibleName()] = child_widget.currentText()
        elif type(child_widget) == qtw.QGroupBox:
            vals = []
            i = 0
            for sub_text_input in child_widget.findChildren(qtw.QLineEdit):
                vals.append(float(sub_text_input.text()))
                i += 1
            adv_param_dict[child_widget.accessibleName()] = tuple(vals)

    return adv_param_dict