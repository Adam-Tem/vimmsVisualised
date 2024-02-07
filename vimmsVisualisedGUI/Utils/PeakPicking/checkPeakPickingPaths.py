import json

def check_peak_picking_paths(self, type):

    with open('userData.json', 'r') as file:
        installs = json.load(file)
    if installs[type] != "":
        self.AddPathGroupBox.setGeometry(0,400, 551, 161)
    else:
        self.AddPathGroupBox.setGeometry(0,25, 551, 161)
        if type == "R":
            self.AddPathLabel.setText("Please add the path to your install of Rscript:")
            self.BatBtnGroupBox.setVisible(False)
            self.ExeBtnGroupBox.setVisible(True)
            self.r_install = self.exe_upload_btn.file_location
            installs[type] = self.exe_upload_btn.file_location
        else:
            self.AddPathLabel.setText("Please add the path to your install of MZMine:")
            self.BatBtnGroupBox.setVisible(True)
            self.ExeBtnGroupBox.setVisible(False)
            self.mzmine_install = self.bat_upload_btn.file_location
            installs[type] = self.bat_upload_btn.file_location

        with open('userData.json', 'w') as file:
            json.dump(installs, file)