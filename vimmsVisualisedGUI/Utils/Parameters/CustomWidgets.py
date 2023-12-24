from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from Utils.Display.setCharge import setButtonText
from Utils.UploadFile import *

class QIonModeButton(qtw.QPushButton):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("Positive")
        self.setStyleSheet("color:white; background-color:green;")
        self.clicked.connect(lambda: setButtonText(self, ["Positive", "Negative"]))

class QFileUpload(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button = qtw.QPushButton()
        self.button.setText("...")
        self.button.setStyleSheet("text-align: center;")
        self.button.setFixedSize(20,20)

        self.FileNameLabel = FileLabel()
        self.FileNameLabel.setText("...")
        self.FileNameLabel.setFixedHeight(20)
        self.FileNameLabel.setMaximumWidth(20)
        self.file_location = ""
        self.file_name = ""
        layout = qtw.QHBoxLayout()
        layout.addWidget(self.button, alignment=qtc.Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.FileNameLabel, alignment=qtc.Qt.AlignmentFlag.AlignTop)
        
        self.setLayout(layout)

class FileLabel(qtw.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def enterEvent(self, event):
        length = len(self.text())
        self.setMaximumWidth(length * 6)

    def leaveEvent(self, event):
        self.setMaximumWidth(40)

class QMzmlUpload(QFileUpload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "mzml"))

class QMgfUpload(QFileUpload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "mgf"))

class QBooleanButton(qtw.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("True")
        self.setStyleSheet("color:white; background-color:green;")
        self.clicked.connect(lambda: setButtonText(self, ["True", "False"]))

    def current_selection(self):
        if self.text() == "True":
            return True
        else:
            return False

def change_edit_value(self, option):
    
    self.edit_text.setText(str(self.vals[option]))

def update_edit_value(self, val_to_change):
    self.vals[val_to_change] = int(self.edit_text.text())   

class QScoringParams(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.combo_box = qtw.QComboBox()
        self.edit_text = qtw.QLineEdit()
        self.vals = {}
        self.combo_box.currentIndexChanged.connect(
            lambda: change_edit_value(self, self.combo_box.currentText()))
        self.edit_text.textChanged.connect(
            lambda: update_edit_value(self, self.combo_box.currentText()))
        layout = qtw.QHBoxLayout()
        layout.addWidget(self.combo_box, alignment=qtc.Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.edit_text, alignment=qtc.Qt.AlignmentFlag.AlignTop)
        self.setLayout(layout)
    
