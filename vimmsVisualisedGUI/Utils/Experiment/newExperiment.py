
from vimms.Box import BoxGrid
from vimms.BoxManager import BoxSplitter, BoxManager

def new_experiment(self):
    self.file_name = ""
    self.file_location = ""
    self.fullscan_list = []
    self.experiment_case_list = []
    self.summary = ""
    geom = BoxManager(
    box_geometry = BoxGrid(),
    box_splitter = BoxSplitter(split=True)
    )
    self.CaseNameTextEdit.setText("")
<<<<<<< HEAD
    self.ExperimentTitleTextEdit.setText("")
=======
>>>>>>> 84f8a4c4993f6138f7d9b613ad41a8f79e35b62d
    self.ControllerComboBox.setCurrentIndex(0)
    self.ExperimentNamesLabel.setText("")
    self.FullscanNamesLabel.setText("")
    self.fullscan_upload_button.FileNameLabel.setText("")
    self.ViewSummaryButton.setEnabled(False)
    self.SummaryGroupBox.setHidden(True)