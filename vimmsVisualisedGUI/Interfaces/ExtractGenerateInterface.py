from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from ExtractGeneratePage import Ui_ExtractGenerateForm

from Utils.ChangePage import *
from Utils.ExtractData import *
from Utils.UploadmzML import *
from Utils.GenerateData import *

class ExtractGeneratePage(qtw.QWidget, Ui_ExtractGenerateForm):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.fileName = ""
        self.fileLocation = ""
        self.min_intensity = 0

        self.ExtractHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        
        self.SelectFileButton.clicked.connect(lambda: upload_mzml(self))

        self.MinIntensityEdit.setText(str(self.min_intensity))

        self.ExtractDataButton.clicked.connect(lambda: extract_data(self, int(self.MinIntensityEdit.text()), self.fileLocation, self.fileName.split(".")[0]))

        self.GenerateDataButton.clicked.connect(lambda: GenerateData(self))

        