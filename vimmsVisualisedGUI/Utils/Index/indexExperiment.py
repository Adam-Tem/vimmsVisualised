import os

def index_experiment(self, exp_folder):
    self.ExpMzmlComboBox.clear()
    self.ExpPklComboBox.clear()

    file_list = [f for f in os.listdir(exp_folder)]
    
    valid_files_in_folder = False
    for file in file_list:
        file_sections = file.split(".")
        if file_sections[-1] == "mzML":
            self.ExpMzmlComboBox.addItem(file_sections[0])
            self.ExpMzmlRadioButton.setEnabled(True)
            self.FragEventsRadioButton.setEnabled(True)
            self.ExpMzmlComboBox.setEnabled(True)
            valid_files_in_folder = True
        if file == "pickle":
            pkl_list = [f for f in os.listdir(os.path.join(exp_folder, "pickle"))]
            for pkl in pkl_list:
                pkl_sections = pkl.split(".")
                self.ExpPklComboBox.addItem(pkl_sections[0] + " pickle")
            self.TimingHistRadioButton.setEnabled(True)
            self.ExpPklComboBox.setEnabled(True)
            
            valid_files_in_folder = True
    
    if valid_files_in_folder:
        self.ExpVisualiseButton.setEnabled(True)


    