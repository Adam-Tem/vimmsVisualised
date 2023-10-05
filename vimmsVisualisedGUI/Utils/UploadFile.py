from PyQt5 import QtWidgets as qtw
import os

def upload_file(self, fileType):
    
    dialog = qtw.QFileDialog()

    if fileType == "mzml":
        selectedFile = dialog.getOpenFileName(None, "Import mzML", "", "mzML data files (*.mzml)")
    elif fileType == "p":
        selectedFile = dialog.getOpenFileName(None, "Import Pickle", "", "Pickle File (*.p)")
    fileName = os.path.basename(selectedFile[0])
    fileLocation = selectedFile[0]
    self.FileNameLabel.setText(fileName)
    self.fileName = fileName
    self.fileLocation = fileLocation