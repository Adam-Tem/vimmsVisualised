from PyQt5 import QtWidgets as qtw
from PyQt5 import sip
from Utils.Display.createWidgets import createWidgets
from Utils.Controllers.controllerSelection import controllerSelection
from Utils.Display.createScrollArea import createScrollArea
from Utils.Display.createExecuteButton import create_execute_button

def displayParams(param_box, combo_box_text, execute_button_type, potential_constructors, potential_params):
    try:
        sip.delete(param_box.layout())
    except:
         pass

    widget_names = createWidgets(combo_box_text, potential_constructors, potential_params)
    for child_widget in param_box.findChildren(qtw.QWidget):
            child_widget.deleteLater()

    param_layout = qtw.QGridLayout(param_box)
    param_layout.setVerticalSpacing(10)
    param_count = 0
    
    row = 0
    col = 0
    for value in widget_names:
        new_widget = value[0][1](parent=param_box)
        new_widget.setObjectName(value[0][0])
        new_widget.setAccessibleName(value[0][0])
        new_label = value[1][1](text=value[1][0], parent=param_box)
        if param_count % 3 == 0:
            row = row + 1
            col = 0
        param_count = param_count + 1
        
        param_layout.addWidget(new_label, row, col)
        col = col + 1
        param_layout.addWidget(new_widget, row, col)
        col = col + 1
  
    if len(widget_names) > 0:
        if execute_button_type[0]:
            execute_button = create_execute_button(param_box, combo_box_text, execute_button_type[1])

            param_layout.addWidget(execute_button, row + 1, col + 1, 2, 2)
        param_box.setLayout(param_layout)
        # createScrollArea(param_box, height = col*85)