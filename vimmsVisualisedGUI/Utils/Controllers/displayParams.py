from PyQt5 import QtWidgets as qtw

def displayParams(self):
    for child_widget in self.ParamsBox.findChildren(qtw.QWidget):
            child_widget.setVisible(False)

    self.ParamsBox.setHidden(False)
    controller_param_dict = {
        "TopN Controller": [("IonModeLabel", "IonModeButton"), ("IsolWidthLabel", "IsolWidthTextEdit"), 
                            ("NoOfInjectionsLabel", "NoOfInjectionsSpinBox"),
                  ("RTTolLabel", "RTTolTextEdit"), ("MZTolLabel", "MZTolTextEdit"),("MinMS1Label", "MinMS1TextEdit"), 
                  ("RTMinLabel", "RTMinTextEdit"), ("RTMaxLabel", "RTMaxTextEdit")]
    }

    to_be_displayed = controller_param_dict[self.ControllerComboBox.currentText()]
    possible_widgets = [qtw.QPushButton, qtw.QSpinBox, qtw.QLineEdit, qtw.QComboBox]

    x = 20
    y = 20
    label_width = 110
    label_height = 20
    input_width = 60
    input_height = 20
    
    param_count = 0
    

    for label, input in to_be_displayed:
        if param_count % 3 == 0:
            x = 20
            y = y + 30
        param_count = param_count + 1
        param_label = self.ParamsBox.findChild(qtw.QLabel, label)
        param_label.setVisible(True)
        param_label.setGeometry(x, y, label_width, label_height)
        x = x + 110
        for qtype in possible_widgets:
            param_input = self.ParamsBox.findChild(qtype, input)
            if param_input:
                param_input.setVisible(True)
                param_input.setGeometry(x, y, input_width, input_height)
        x = x + 70

    self.SimulateButton.setVisible(True)
    self.SimulateButton.setGeometry(200, y + 50, 200, 75)
