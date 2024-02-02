
from vimms.Box import BoxGrid
from vimms.BoxManager import BoxSplitter, BoxManager

def new_experiment(self):
    self.file_name = ""
    self.file_location = ""
    self.fullscan_list = []
    self.experiment_case_list = []
    self.experiment_name_list = []
    self.summary = ""
    geom = BoxManager(
    box_geometry = BoxGrid(),
    box_splitter = BoxSplitter(split=True)
    )
    self.CaseNameTextEdit.setText("")
    self.ExperimentTitleTextEdit.setText("")
    self.ControllerComboBox.setCurrentIndex(0)
    self.ExperimentNamesLabel.setText("")
    self.FullscanNamesLabel.setText("")
    self.fullscan_upload_button.FileNameLabel.setText("")
    self.ViewSummaryButton.setEnabled(False)
    self.SummaryGroupBox.setHidden(True)