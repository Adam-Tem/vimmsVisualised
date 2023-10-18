from PyQt5 import QtWidgets as qtw

from Utils.setCharge import setCharge

class QIonModeButton(qtw.QPushButton):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("Positive")
        self.setStyleSheet("color:white; background-color:green;")
        self.clicked.connect(lambda: setCharge(self))
