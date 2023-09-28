from PyQt5 import QtWidgets as qtw
import os

def upload_mzml(self):
    
    dialog = qtw.QFileDialog()
    selectedFile = dialog.getOpenFileName(None, "Import mzML", "", "mzML data files (*.mzml)")
    fileName = os.path.basename(selectedFile[0])
    fileLocation = selectedFile[0]
    self.ExtractFileNameLabel.setText(fileName)
    self.fileName = fileName
    self.fileLocation = fileLocation