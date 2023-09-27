from StartPage import Ui_Form
from ExtractGeneratePage import Ui_ExtractGenerateForm

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import os

qtw.QApplication.setAttribute(qtc.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
qtw.QApplication.setAttribute(qtc.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons



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
        def upload_mzml(self):
            dialog = qtw.QFileDialog()
            fileName = dialog.getOpenFileName(None, "Import mzML", "", "mzML data files (*.mzml)")
            self.ExtractFileNameLabel.setText(os.path.basename(fileName[0]))

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

