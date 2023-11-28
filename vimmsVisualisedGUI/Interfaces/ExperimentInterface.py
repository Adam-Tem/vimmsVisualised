from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

from vimms.Box import BoxGrid
from vimms.BoxManager import BoxSplitter, BoxManager

from ExperimentPage import Ui_experimentForm
from Utils.CustomWidgets import QMzmlUpload
from Utils.Experiment.addFullscanToList import add_fullscan_to_list
from Utils.Experiment.constructExperimentCase import construct_experiment_case
from Utils.Display.displayParams import displayParams
from Utils.Parameters.ParamWidgets import *
from Utils.Experiment.runExperiment import run_experiment
from Utils.Experiment.viewSummary import view_summary
from Utils.Experiment.newExperiment import new_experiment
from Utils.Experiment.removeFullscan import remove_option

class ExperimentPage(qtw.QWidget, Ui_experimentForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.file_name = ""
        self.file_location = ""
        self.experiment = ""
        self.fullscan_list = []
        self.experiment_case_list = []
        self.summary = ""
        geom = BoxManager(
        box_geometry = BoxGrid(),
        box_splitter = BoxSplitter(split=True)
        )

        self.SummaryGroupBox.setHidden(True)

        fullscan_upload_button = QMzmlUpload(parent=self.FullscanGroupBox)
        fullscan_upload_button.setObjectName("fullscan_upload_button")
        fullscan_upload_button.move(225, 0)

        pickle_env_button = QBooleanButton(parent = self)
        pickle_env_button.setObjectName("pickle_env_button")
        pickle_env_button.move(155, 390)
        pickle_env_button.lower()
        self.ExperimentHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.InjectionUndoButton.setIcon(qtg.QIcon("Images/undo.png"))
        self.CaseUndoButton.setIcon(qtg.QIcon("Images/undo.png"))

        self.AddFullscanButton.clicked.connect(
            lambda: add_fullscan_to_list(self, self.FullscanNamesScrollArea, 
                                        fullscan_upload_button.file_name, self.NoOfInjectionsSpinBox.value()))
        
        self.InjectionUndoButton.clicked.connect(
            lambda: remove_option(self, self.FullscanNamesScrollArea, "fullscan")
        )

        self.CaseUndoButton.clicked.connect(
            lambda: remove_option(self, self.ExperimentNamesScrollArea, "case")
        )

        self.ControllerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ParamsBox,self.ControllerComboBox.currentText(), 
            [False, ""], CONTROLLERS, CONTROLLER_PARAMS, [True,"Experiment"] ))
        
        self.AddExperimentCaseButton.clicked.connect(
            lambda: construct_experiment_case(self, self.ControllerComboBox.currentText(),self.ParamsBox,
                                              pickle_env_button.current_selection(), self.CaseNameTextEdit.text(),
                                              self.fullscan_list, geom)
        )

        self.RunExperimentButton.clicked.connect(
            lambda: run_experiment(self, self.experiment_case_list)
        )
        self.ViewSummaryButton.clicked.connect(
            lambda: view_summary(self)
        )
        self.NewExperimentButton.clicked.connect(
            lambda: new_experiment(self)
        )