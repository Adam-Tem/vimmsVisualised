from PyQt5 import QtWidgets as qtw

from Utils.Parameters.CustomWidgets import QXMLUpload


def parse_peak_picking_params(selected_peak_picker, peak_picking_params_box):

        peak_picking_params_dict = {}
        if selected_peak_picker == "XCMS":
                for child_widget in peak_picking_params_box.findChildren(qtw.QLineEdit):
                        peak_picking_params_dict[child_widget.accessibleName()] = child_widget.text()
        else:
                for child_widget in peak_picking_params_box.findChildren(QXMLUpload):
                        peak_picking_params_dict[child_widget.accessibleName()] = child_widget.file_location         

        return peak_picking_params_dict