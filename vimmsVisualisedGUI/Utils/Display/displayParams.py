from PyQt5 import QtWidgets as qtw
from PyQt5 import sip
from Utils.Display.createWidgets import create_widgets
from Utils.Display.adjustParamBoxSize import adjust_param_box_size
from Utils.Experiment.docstringTooltipParsing import docstring_tooltip_parsing
from Utils.Parameters.CustomWidgets import QBooleanButton, QScoringParams

def displayParams(param_box, combo_box_text, potential_params, has_scroll):
    
    try:
        current_widget_count = param_box.layout().count()
        sip.delete(param_box.layout())
    except:
         current_widget_count = 0
         pass

    widget_names = create_widgets(combo_box_text, potential_params)
    for child_widget in param_box.findChildren(qtw.QWidget):
            child_widget.deleteLater()

    param_layout = qtw.QGridLayout(param_box)
    param_layout.setVerticalSpacing(10)
    param_count = 0
    if potential_params != "Peak Picking":
        param_desc_dict = docstring_tooltip_parsing(combo_box_text)
    else:
        param_desc_dict = {}
    row = 0
    col = 0
    for value in widget_names:
        new_widget = value[0][1](parent=param_box)
        new_widget.setObjectName(value[0][0])
        new_widget.setAccessibleName(value[0][0])
        new_widget.setMinimumHeight(19)
        new_label = value[1][1](text=value[1][0], parent=param_box)
        if value[0][0] in param_desc_dict.keys():
            new_label.setToolTip(param_desc_dict[value[0][0]])
        if len(value) == 3:
            if type(new_widget) == QBooleanButton:  
                new_widget.setText("False")
                new_widget.setStyleSheet("background-color: red; color: black;")
            
            elif type(new_widget) == qtw.QComboBox:
                new_widget.addItem(str(value[2]))
                i = 3
                while i < len(value):
                    new_widget.addItem(str(value[i]))
                    i = i + 1
            elif type(new_widget) == QScoringParams:
                new_widget.vals = value[2]
                for option in value[2].keys():
                    new_widget.combo_box.addItem(option)
            else:
                new_widget.setText(str(value[2]))
            
        if param_count % 3 == 0:
            row = row + 1
            col = 0
        param_count = param_count + 1
        
        param_layout.addWidget(new_label, row, col)
        col = col + 1
        param_layout.addWidget(new_widget, row, col)
        col = col + 1
  
    if len(widget_names) > 0:

        print(len(widget_names))
        if len(widget_names) == 1:
            param_box.setHeight(30)
        else:
            param_box.setMinimumHeight((((len(widget_names) - 1)//3)+1) * 20)
        
    else:
        param_box.setMinimumHeight(0)
        
    if has_scroll:
        param_box.setFixedSize(531, row*35)
    else:
        adjust_param_box_size(param_box, len(widget_names), current_widget_count//2)

        param_box.setLayout(param_layout)
    