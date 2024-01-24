from PyQt5 import QtWidgets as qtw

def parse_xcms_params(xcms_params_box):

    xcms_params_dict = {}
    for child_widget in xcms_params_box.findChildren(qtw.QLineEdit):
            xcms_params_dict[child_widget.accessibleName()] = child_widget.text()
    return xcms_params_dict