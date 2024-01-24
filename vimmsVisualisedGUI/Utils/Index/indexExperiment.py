import os

def index_experiment(self, exp_folder):

    file_list = [f for f in os.listdir(exp_folder)]
    valid_files_in_folder = False
    for file in file_list:
        file_sections = file.split(".")
        if file_sections[-1] == "mzML":
            self.ExpMzmlComboBox.addItem(file_sections[0])
            self.ExpMzmlRadioButton.setEnabled(True)
            self.ExpMzmlComboBox.setEnabled(True)
            valid_files_in_folder = True
        elif file_sections[-1] == "pkl":
            self.TimingHistRadioButton.setEnabled(True)
            self.FragEventsRadioButton.setEnabled(True)
            valid_files_in_folder = True
    
    if valid_files_in_folder:
        self.ExpVisualiseButton.setEnabled(True)


    