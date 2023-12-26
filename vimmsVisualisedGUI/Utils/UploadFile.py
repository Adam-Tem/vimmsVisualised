from PyQt5 import QtWidgets as qtw

import os

def upload_file(self, file_type):
    
    dialog = qtw.QFileDialog()
    if file_type == "mzml":
        selected_file = dialog.getOpenFileName(None, "Import mzML", "", "mzML data files (*.mzml)")
    elif file_type == "p":
        selected_file = dialog.getOpenFileName(None, "Import Pickle", "", "Pickle File (*.p)")
    elif file_type == "mgf":
        selected_file = dialog.getOpenFileName(None, "Import MGF", "", "mgf File (*.mgf)")
        
    file_name = os.path.basename(selected_file[0])
    file_location = selected_file[0]
    self.FileNameLabel.setText(file_name)
    self.file_name = file_name
    self.file_location = file_location
    self.emit_name()