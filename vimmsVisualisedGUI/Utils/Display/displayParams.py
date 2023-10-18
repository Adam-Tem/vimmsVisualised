from PyQt5 import QtWidgets as qtw
from PyQt5 import sip
from Utils.Display.createWidgets import createWidgets
from Utils.Controllers.controllerSelection import controllerSelection
from Utils.Display.createScrollArea import createScrollArea

def displayParams(self):

    try:
        if self.param_layout:
            sip.delete(self.param_layout)
    except:
         pass

    widget_names = createWidgets(selected_controller=self.ControllerComboBox.currentText())
    for child_widget in self.ParamsBox.findChildren(qtw.QWidget):
            child_widget.deleteLater()

    self.param_layout = qtw.QGridLayout(self)
    self.param_layout.setVerticalSpacing(10)
    param_count = 0
    
    row = 0
    col = 0
    for value in widget_names:

        new_widget = value[0][1](parent=self.ParamsBox)
        new_widget.setObjectName(value[0][0])
        new_widget.setAccessibleName(value[0][0])
        new_label = value[1][1](text=value[1][0], parent=self.ParamsBox)
        if param_count % 3 == 0:
            row = row + 1
            col = 0
        param_count = param_count + 1
        
        self.param_layout.addWidget(new_label, row, col)
        col = col + 1
        self.param_layout.addWidget(new_widget, row, col)
        col = col + 1
  
    if len(widget_names) > 0:
        self.SimulateButton = qtw.QPushButton(parent=self.ParamsBox, text="Simulate")
        self.SimulateButton.clicked.connect(lambda: controllerSelection(self))
        self.SimulateButton.setBaseSize(200, 75)
        self.SimulateButton.setObjectName("Simulate")
        self.param_layout.addWidget(self.SimulateButton, row + 1, 5, 2, 2)
        self.SimulateButton.setVisible(True)

    self.ParamsBox.setLayout(self.param_layout)
    createScrollArea(self)