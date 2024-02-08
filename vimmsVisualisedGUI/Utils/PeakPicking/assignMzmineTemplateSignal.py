from Utils.Parameters.CustomWidgets import QXMLUpload

def assign_mzmine_template_signal(self):
    if self.PeakPickingComboBox.currentText() == "MZMine":
        self.PeakPickingParamsBox.findChildren(QXMLUpload)[0].file_upload.connect(self.check_run_exp_inputs)