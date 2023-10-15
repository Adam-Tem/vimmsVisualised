from PyQt5 import QtWidgets as qtw
from Utils.Display.createWidgets import createWidgets
from Utils.Controllers.controllerSelection import controllerSelection

def displayParams(self):

    widget_names = createWidgets(selected_controller=self.ControllerComboBox.currentText())
    for child_widget in self.ParamsBox.findChildren(qtw.QWidget):
            child_widget.deleteLater()

    self.ParamsBox.setHidden(False)
    x = 20
    y = 20
    label_width = 110
    label_height = 20
    input_width = 60
    input_height = 20
    param_count = 0
    
    for value in widget_names:

        new_widget = value[0][1](parent=self.ParamsBox)
        new_widget.setAccessibleName(value[0][0])
        new_label = value[1][1](text=value[1][0], parent=self.ParamsBox)
        if param_count % 3 == 0:
            x = 20
            y = y + 25
        param_count = param_count + 1
        
        new_label.setGeometry(x, y, label_width, label_height)
        new_label.setVisible(True)
        x = x + 110

        new_widget.setGeometry(x, y, input_width, input_height)
        new_widget.setVisible(True)
        x = x + 70
  
    if len(widget_names) > 0:
        self.SimulateButton = qtw.QPushButton(parent=self.ParamsBox, text="Simulate")
        self.SimulateButton.clicked.connect(lambda: controllerSelection(self))
        self.SimulateButton.setGeometry(200, y + 25, 200, 75)
        self.SimulateButton.setVisible(True)
