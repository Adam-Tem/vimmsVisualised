from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

from ExperimentPage import Ui_experimentForm
from Utils.CustomWidgets import QMzmlUpload
from Utils.Experiment.addFullscanToList import add_fullscan_to_list


class ExperimentPage(qtw.QWidget, Ui_experimentForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.file_name = ""
        self.file_location = ""
        self.fullscan_list = []

        fullscan_upload_button = QMzmlUpload(parent=self.FullscanGroupBox)
        fullscan_upload_button.setObjectName("fullscan_upload_button")
        fullscan_upload_button.move(10, 30)
        self.ExperimentHomeButton.setIcon(qtg.QIcon("Images/home.png"))

        self.AddFullscanButton.clicked.connect(lambda: add_fullscan_to_list(self, fullscan_upload_button.file_name, self.NoOfInjectionsSpinBox.value()))