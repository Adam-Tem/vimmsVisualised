from StartPage import Ui_Form
from ExtractGeneratePage import Ui_ExtractGenerateForm

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import os

# from "../vimms/Common.py" import save_obj
from vimms.Common import  save_obj, POSITIVE
from vimms.Roi import RoiBuilderParams
from vimms.Chemicals import ChemicalMixtureFromMZML

qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons


fileLocation = ""
fileName = ""
min_intensity = 0

def changePage(index):
    stackedWidget.setCurrentIndex(index)

class StartPage(qtw.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)


        self.ExtractGenerateButton.clicked.connect(lambda: changePage(1))

class ExtractGeneratePage(qtw.QWidget, Ui_ExtractGenerateForm):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.ExtractHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.ExtractHomeButton.clicked.connect(lambda: changePage(0))
        
        self.SelectFileButton.clicked.connect(lambda: upload_mzml(self))

        self.MinIntensityEdit.setText(str(min_intensity))

        self.ExtractDataButton.clicked.connect(lambda: extract_data(self, int(self.MinIntensityEdit.text()), fileLocation, fileName.split(".")[0]))

        def upload_mzml(self):
            global fileLocation, fileName
            dialog = qtw.QFileDialog()
            selectedFile = dialog.getOpenFileName(None, "Import mzML", "", "mzML data files (*.mzml)")
            fileName = os.path.basename(selectedFile[0])
            fileLocation = selectedFile[0]
            self.ExtractFileNameLabel.setText(fileName)

        def extract_data(self, min_roi_intensity, file_location, file_name):
            rp = RoiBuilderParams(min_roi_intensity)
            cm = ChemicalMixtureFromMZML(file_location, roi_params=rp)
            dataset = cm.sample(None, 2)
            save_location = os.path.dirname(os.path.abspath(file_location)) + "/ExtracctedData"
            out_name = os.path.join(save_location, file_name + '.p')
            save_obj(dataset, out_name)
            self.ExtractCompleteLabel.setText("Extraction Complete! Find result in Extracted Data folder.")
            self.ExtractCompleteLabel.setStyleSheet("background-color: green;")




if __name__ == "__main__":
    app = qtw.QApplication([])
    stackedWidget = qtw.QStackedWidget()
    stackedWidget.setGeometry(50, 25, 600, 500)
    homeWidget = StartPage()
    extractGenerateWidget = ExtractGeneratePage()
    stackedWidget.addWidget(homeWidget)
    stackedWidget.addWidget(extractGenerateWidget)
    stackedWidget.show()

    app.exec_()

