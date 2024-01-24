from PyQt5 import QtWidgets as qtw

from mass_spec_utils.data_import.mzml import MZMLFile

import os

def upload_file(self, file_type):
    
    dialog = qtw.QFileDialog()
    if file_type == "mzml":
        selected_file = dialog.getOpenFileName(None, "Import mzML", "", "mzML data files (*.mzml)")
        if selected_file[0] != "":
            self.stored_mzml = MZMLFile(selected_file[0]) 
    elif file_type == "p":
        selected_file = dialog.getOpenFileName(None, "Import Pickle", "", "Pickle File (*.p)")
    elif file_type == "mgf":
        selected_file = dialog.getOpenFileName(None, "Import MGF", "", "mgf File (*.mgf)")
    elif file_type == "folder":
        options = qtw.QFileDialog.Options()
        options |= qtw.QFileDialog.ShowDirsOnly
        selected_folder = dialog.getExistingDirectory(None, 'Select Folder', options=options)
        folder_name = selected_folder.split("/")[-1]
        self.FileNameLabel.setText(folder_name)
        self.file_name = folder_name
        self.file_location = selected_folder

    if file_type != "folder":  
        if selected_file == "":
            file_name = ""
            file_location = ""
            self.FileNameLabel.setText("")
        else:
            file_name = os.path.basename(selected_file[0])
            file_location = selected_file[0]
            self.FileNameLabel.setText(file_name)
        self.file_name = file_name
        self.file_location = file_location
    self.emit_name()