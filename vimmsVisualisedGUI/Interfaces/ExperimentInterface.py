from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from vimms.Box import BoxGrid
from vimms.BoxManager import BoxSplitter, BoxManager
from vimms.Experiment import Experiment

from ExperimentPage import Ui_experimentForm

from Graphing.createGraphLayout import create_graph_layout
from Graphing.ExperimentResultPlot import experiment_result_plot
from Utils.Display.displayParams import displayParams
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Experiment.addFullscanToList import add_fullscan_to_list
from Utils.Experiment.constructExperimentCase import construct_experiment_case
from Utils.Experiment.newExperiment import new_experiment
from Utils.Experiment.removeFullscan import remove_option
from Utils.Experiment.viewSummary import view_summary
from Utils.Parameters.CustomWidgets import QMzmlUpload
from Utils.Parameters.loadParamState import load_param_state
from Utils.Parameters.ParamWidgets import *
from Utils.Parameters.parseAdvancedParams import parse_advanced_params
from Utils.Parameters.saveParamState import save_param_state
from Utils.Threads.workerThreads import ExperimentWorker
from Utils.XCMS.parseXCMSParams import parse_xcms_params

class ExperimentPage(qtw.QWidget, Ui_experimentForm):

    start_exp = qtc.pyqtSignal(list, dict)
    mzml_upload = qtc.pyqtSignal()
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
        create_graph_layout(self)
        self.worker = ExperimentWorker()
        self.worker_thread = qtc.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.start_exp.connect(self.worker.run)
        self.worker.experiment_finished.connect(self.set_experiment_and_summary)
           
        self.scrollArea.setWidget(self.ParamsBox)
        self.AdvancedParamsScrollArea.setWidget(self.AdvancedParamsGroupBox)
        self.SummaryGroupBox.setHidden(True)


        self.fullscan_upload_button = QMzmlUpload(parent=self.MzmlUploadGroupBox)
        self.fullscan_upload_button.setObjectName("fullscan_upload_button")
        self.MzmlUploadGroupBox.setLayout(self.fullscan_upload_button.layout())
        self.mzml_upload.connect(self.check_mzml_file)

        pickle_env_button = QBooleanButton(parent = self)
        pickle_env_button.setObjectName("pickle_env_button")
        pickle_env_button.move(155, 390)
        pickle_env_button.lower()
        self.ExperimentHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.InjectionUndoButton.setIcon(qtg.QIcon("Images/undo.png"))
        self.CaseUndoButton.setIcon(qtg.QIcon("Images/undo.png"))
        self.LoadParamsButton.setIcon(qtg.QIcon("Images/folder.svg"))
        self.SaveParamsButton.setIcon(qtg.QIcon("Images/save.png"))

        self.AddFullscanButton.clicked.connect(
            lambda: add_fullscan_to_list(self, self.FullscanNamesScrollArea, 
                                        self.fullscan_upload_button.file_name, self.NoOfInjectionsSpinBox.value()))
        
        self.InjectionUndoButton.clicked.connect(
            lambda: remove_option(self, self.FullscanNamesScrollArea, "fullscan")
        )

        self.CaseUndoButton.clicked.connect(
            lambda: remove_option(self, self.ExperimentNamesScrollArea, "case")
        )

        self.SaveParamsButton.clicked.connect(
            lambda: save_param_state(self,
                                     self.ControllerComboBox.currentText(),
                                     self.ParamTabs.currentIndex())
        )

        self.LoadParamsButton.clicked.connect(
            lambda: load_param_state(self, self.ParamTabs.currentIndex())
        )

        self.ControllerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ParamsBox,
                                  self.ControllerComboBox.currentText(), 
            CONTROLLERS, CONTROLLER_PARAMS, True))
        
        self.AddExperimentCaseButton.clicked.connect(
            lambda: construct_experiment_case(self, self.ControllerComboBox.currentText(),self.ParamsBox,
                                              pickle_env_button.current_selection(), self.CaseNameTextEdit.text(),
                                              self.fullscan_list, geom, parse_advanced_params(self.AdvancedParamsGroupBox))
        )

        self.RunExperimentButton.clicked.connect(
            lambda: (self.RunExperimentButton.setEnabled(False),
                     self.start_exp.emit(self.experiment_case_list, parse_xcms_params(self.XCMSParamTab)))
        )
        self.ViewSummaryButton.clicked.connect(
            lambda: view_summary(self)
        )
        self.NewExperimentButton.clicked.connect(
            lambda: new_experiment(self)
        )

        self.CumulativeIntensityProportionRadioButton.clicked.connect(
            lambda: experiment_result_plot(self.canvas, self.experiment, 
                                           self.experiment_case_list, "cumulative_intensity_proportion")
        )

        self.CumulativeCoverageRadioButton.clicked.connect(
            lambda: experiment_result_plot(self.canvas, self.experiment, 
                                           self.experiment_case_list, "cumulative_coverage_proportion")
        )

    @qtc.pyqtSlot(Experiment, str)
    def set_experiment_and_summary(self, experiment, summary):
        task_completed_pop_up("ViMMS Experiment", "Experiment execution now complete!", self.ViewSummaryButton)
        self.RunExperimentButton.setEnabled(True)
        self.experiment = experiment
        self.summary = summary

    def check_mzml_file(self):
        if self.fullscan_upload_button.file_name == "":
            self.AddFullscanButton.setEnabled(False)
        else:
            self.AddFullscanButton.setEnabled(True)
