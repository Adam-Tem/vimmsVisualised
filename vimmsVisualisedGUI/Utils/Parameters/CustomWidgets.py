from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from qtrangeslider import QDoubleRangeSlider

from Utils.Display.setCharge import setButtonText
from Utils.UploadFile import *

class QIonModeButton(qtw.QPushButton):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("Positive")
        self.setStyleSheet("color:white; background-color:green;")
        self.clicked.connect(lambda: setButtonText(self, ["Positive", "Negative"]))

class QFileUpload(qtw.QWidget):

    file_upload = qtc.pyqtSignal(str)

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

    def emit_name(self):
        self.file_upload.emit(self.file_name)

class FileLabel(qtw.QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def enterEvent(self, event):
        length = len(self.text())
        self.setMaximumWidth(length * 6)
        if type(self.parent()) == qtw.QGroupBox:
            self.parent().setFixedWidth(length * 10)

    def leaveEvent(self, event):
        self.setMaximumWidth(40)
        if type(self.parent()) == qtw.QGroupBox:
            self.parent().setFixedWidth(80)

class QMzmlUpload(QFileUpload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stored_mzml = ""
        self.button.clicked.connect(lambda: upload_file(self, "mzml"))

class QMgfUpload(QFileUpload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "mgf"))

class PUpload(QFileUpload):
    p_upload = qtc.pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "p"))

class QFolderUpload(QFileUpload):
    folder_upload = qtc.pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "folder"))

class QXMLUpload(QFileUpload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "xml"))

class QExeUpload(QFileUpload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "exe"))

class QBatUpload(QFileUpload):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button.clicked.connect(lambda: upload_file(self, "bat"))

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



class QParamRangeSlider(qtw.QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.manipulate_vals_fn = lambda x: x
        self.reverse_fn = lambda x: x
        self.min_val = 0
        self.max_val = 99
        self.min_val_input = qtw.QLineEdit()
        self.max_val_input = qtw.QLineEdit()
        self.range_slider = QDoubleRangeSlider(qtc.Qt.Horizontal)
        self.range_slider.setFixedWidth(140)
        self.range_slider.setStyleSheet("""
                                        QSlider::handle:horizontal { background: #000000;
                                                                        height: 5px;
                                                                        width: 10px; }
                                        QRangeSlider {
                                        qproperty-barColor: #444444;}""")
        self.range_slider.valueChanged.connect(self.slider_change)
        self.range_slider.setValue((0,99))
        self.range_slider.setEnabled(False)
        
        self.min_val_input.setFixedWidth(40)
        self.max_val_input.setFixedWidth(40)
        self.min_val_input.setEnabled(False)
        self.max_val_input.setEnabled(False)

        self.min_val_input.editingFinished.connect(self.line_edit_changed)
        self.max_val_input.editingFinished.connect(self.line_edit_changed)
       
        self.layout = qtw.QGridLayout(self)
        self.layout.addWidget(self.min_val_input, 0,0)
        self.min_val_input.setAlignment(qtc.Qt.AlignLeft | qtc.Qt.AlignVCenter)
        self.layout.addWidget(self.max_val_input, 0,2)
        self.max_val_input.setAlignment(qtc.Qt.AlignRight | qtc.Qt.AlignVCenter)
        self.layout.addWidget(self.range_slider, 1,0,1,3)
        self.setLayout(self.layout)

    def slider_change(self):

        if self.range_slider.value()[0] != self.min_val:
            manipulated_min = self.manipulate_vals_fn(self.range_slider.value()[0])
            self.min_val_input.setText(str(round(manipulated_min, 1)))
            self.min_val = self.range_slider.value()[0]
        else:
            manipulated_max = self.manipulate_vals_fn(self.range_slider.value()[1])
            self.max_val_input.setText(str(round(manipulated_max, 1)))
            self.max_val = self.range_slider.value()[1]

    def line_edit_changed(self):
        if float(self.min_val_input.text()) != self.min_val:
            if float(self.min_val_input.text()) < self.min_val:
                self.min_val_input.setText(str(self.min_val))
                self.range_slider.setValue((self.reverse_fn(self.min_val), 
                                            self.reverse_fn(float(self.max_val_input.text()))))
            else:
                self.range_slider.setValue((self.reverse_fn(float(self.min_val_input.text())), 
                                            self.reverse_fn(float(self.max_val_input.text()))))
                
        elif float(self.max_val_input.text()) != self.max_val:
            if float(self.max_val_input.text()) > self.max_val:
                self.max_val_input.setText(str(self.max_val))
                self.range_slider.setValue((self.reverse_fn(float(self.min_val_input.text())), 
                                            self.reverse_fn(self.max_val)))
            else:
                self.range_slider.setValue((self.reverse_fn(float(self.min_val_input.text())), 
                                            self.reverse_fn(float(self.max_val_input.text()))))

    def set_vals(self, new_min_val, new_max_val):

        new_range = new_max_val - new_min_val
        multiplier = 100 / new_range
        new_manipulate_fn = lambda x: x/multiplier + new_min_val
        new_reverse_fn = lambda x: (x - new_min_val) * multiplier 
        self.manipulate_vals_fn = new_manipulate_fn
        self.reverse_fn = new_reverse_fn
        self.range_slider.setValue((0,99))
        self.range_slider.setEnabled(True)
        self.min_val_input.setEnabled(True)
        self.max_val_input.setEnabled(True)

        self.min_val = round(new_min_val, 1)
        self.max_val = round(new_max_val, 1)
        self.min_val_input.setText(str(round(new_min_val, 1)))
        self.max_val_input.setText(str(round(new_max_val, 1)))
        
    def disable_slider(self):
        self.min_val_input.setText("")
        self.max_val_input.setText("")
        self.range_slider.setEnabled(False)
        self.min_val_input.setEnabled(False)
        self.max_val_input.setEnabled(False)
