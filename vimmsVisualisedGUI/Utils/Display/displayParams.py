from PyQt5 import QtWidgets as qtw
from PyQt5 import sip
from Utils.Display.createWidgets import createWidgets
from Utils.Display.createScrollArea import createScrollArea
from Utils.Display.createExecuteButton import create_execute_button
from Utils.Display.adjustParamBoxSize import adjust_param_box_size
from Utils.CustomWidgets import QBooleanButton

def displayParams(param_box, combo_box_text, execute_button_type, potential_constructors, potential_params, add_scroll):
    
    try:
        current_widget_count = param_box.layout().count()
        sip.delete(param_box.layout())
    except:
         current_widget_count = 0
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
        new_widget.setMinimumHeight(19)
        new_label = value[1][1](text=value[1][0], parent=param_box)
        if len(value) == 3:
            if type(new_widget) == QBooleanButton:  
                new_widget.setText("False")
                new_widget.setStyleSheet("background-color: red; color: black;")
            
            elif type(new_widget) == qtw.QComboBox:
                new_widget.addItem(str(value[2]))
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
        if execute_button_type[0]:
            execute_button = create_execute_button(param_box, combo_box_text, execute_button_type[1])

            param_layout.addWidget(execute_button, row + 1, col + 1, 2, 2)
        param_box.setMinimumHeight((((len(widget_names) - 1)//3)+1) * 20)
        
    else:
        param_box.setMinimumHeight(0)
        
    if not execute_button_type[0]:
        if add_scroll[0]:
            createScrollArea(param_box,add_scroll[1], row)
            param_box.setFixedSize(550, row*35)
        else:
            adjust_param_box_size(param_box, len(widget_names), current_widget_count//2)

        param_box.setLayout(param_layout)
    