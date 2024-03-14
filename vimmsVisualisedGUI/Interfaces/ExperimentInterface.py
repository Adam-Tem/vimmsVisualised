from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtWebEngineCore import *

from vimms.Experiment import Experiment

from ExperimentPage import Ui_experimentForm

from Graphing.createGraphLayout import create_graph_layout
from Graphing.experimentResultPlot import experiment_result_plot
from Utils.checkValidInputs import check_valid_inputs
from Utils.Display.addLoadingWidget import add_loading_widget
from Utils.Display.displayParams import displayParams
from Utils.Display.inputErrorPopUp import input_error_pop_up
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Experiment.addFullscanToList import add_fullscan_to_list
from Utils.Experiment.constructExperimentCase import construct_experiment_case
from Utils.Experiment.newExperiment import new_experiment
from Utils.Experiment.removeFullscan import remove_option
from Utils.Experiment.viewSummary import view_summary
from Utils.Parameters.addElementsToComboBox import add_elements_to_combo_box
from Utils.Parameters.CustomWidgets import QMzmlUpload
from Utils.Parameters.loadParamState import load_param_state
from Utils.Parameters.ParamWidgets import *
from Utils.Parameters.parseAdvancedParams import parse_advanced_params
from Utils.Parameters.saveParamState import save_param_state
from Utils.Threads.workerThreads import ExperimentWorker
from Utils.PeakPicking.parsePeakPickingParams import parse_peak_picking_params
from Utils.PeakPicking.checkPeakPickingPaths import check_peak_picking_paths
from Utils.PeakPicking.assignMzmineTemplateSignal import assign_mzmine_template_signal

import json

class ExperimentPage(qtw.QWidget, Ui_experimentForm):

    start_exp = qtc.pyqtSignal(qtw.QLabel, list, str, str, dict)
    mzml_upload = qtc.pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.file_name = ""
        self.file_location = ""
        self.experiment = ""
        self.fullscan_list = []
        self.experiment_case_list = []
        self.experiment_name_list = []
        self.summary = ""
        self.r_install = ""
        self.mzmine_install = ""

        add_loading_widget(self.ExperimentLoadingLabel)
        add_elements_to_combo_box(self.ControllerComboBox, CONTROLLERS)
        
        create_graph_layout(self)
        self.worker = ExperimentWorker()
        self.worker_thread = qtc.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.start_exp.connect(self.worker.run)
        self.worker.experiment_finished.connect(self.set_experiment_and_summary)
           
        self.scrollArea.setWidget(self.ParamsBox)
        self.PeakPickingscrollArea.setWidget(self.PeakPickingParamsBox)
        self.AdvancedParamsScrollArea.setWidget(self.AdvancedParamsGroupBox)
        self.SummaryGroupBox.setHidden(True)

        self.fullscan_upload_button = QMzmlUpload(parent=self.MzmlUploadGroupBox)
        self.fullscan_upload_button.setObjectName("fullscan_upload_button")
        self.MzmlUploadGroupBox.setLayout(self.fullscan_upload_button.layout())
        self.fullscan_upload_button.file_upload.connect(self.check_mzml_file)

        self.exe_upload_btn = QExeUpload(parent=self.AddPathGroupBox)
        self.exe_upload_btn.setObjectName("exe_upload_button")
        self.ExeBtnGroupBox.setLayout(self.exe_upload_btn.layout())
        self.exe_upload_btn.file_upload.connect(self.check_install_paths)

        self.bat_upload_btn = QBatUpload(parent=self.AddPathGroupBox)
        self.bat_upload_btn.setObjectName("bat_upload_button")
        self.BatBtnGroupBox.setLayout(self.bat_upload_btn.layout())
        self.bat_upload_btn.file_upload.connect(self.check_install_paths)

        self.PeakPickingComboBox.currentIndexChanged.connect(self.check_install_paths)
        self.PeakPickingComboBox.currentIndexChanged.connect(self.check_run_exp_inputs)

        self.ControllerComboBox.currentIndexChanged.connect(self.check_case_inputs)
        self.CaseNameTextEdit.textChanged.connect(self.check_case_inputs)

        self.ExperimentTitleTextEdit.textChanged.connect(self.check_run_exp_inputs)

        
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

                                        self.fullscan_upload_button.file_name,
                                        self.fullscan_upload_button.file_location,
                                        os.getcwd(), self.NoOfInjectionsSpinBox.value()))

        self.AddFullscanButton.clicked.connect(self.check_case_inputs)
        
        
        self.InjectionUndoButton.clicked.connect(
            lambda: remove_option(self, self.FullscanNamesScrollArea, "fullscan"))
        self.InjectionUndoButton.clicked.connect(self.check_case_inputs)

        self.CaseUndoButton.clicked.connect(
            lambda: remove_option(self, self.ExperimentNamesScrollArea, "case")
        )
        self.CaseUndoButton.clicked.connect(self.check_run_exp_inputs)
        self.CaseUndoButton.clicked.connect(self.check_case_inputs)


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
                                  CONTROLLER_PARAMS, True))
        
        self.PeakPickingComboBox.currentIndexChanged.connect(
            lambda: (displayParams(self.PeakPickingParamsBox,
                                  self.PeakPickingComboBox.currentText(),
                                  "Peak Picking", True),
                                  assign_mzmine_template_signal(self)))
        
        self.AddExperimentCaseButton.clicked.connect(
            lambda: construct_experiment_case(self, self.ControllerComboBox.currentText(),self.ParamsBox,
                                              pickle_env_button.current_selection(), self.CaseNameTextEdit.text(),
                                              self.fullscan_list, parse_advanced_params(self.AdvancedParamsGroupBox)))

        self.AddExperimentCaseButton.clicked.connect(self.check_run_exp_inputs)
        self.AddExperimentCaseButton.clicked.connect(self.check_case_inputs)

        self.RunExperimentButton.clicked.connect(
            lambda: (self.RunExperimentButton.setEnabled(False),
                     self.AddExperimentCaseButton.setEnabled(False),
                     self.start_exp.emit(self.ExperimentLoadingLabel,
                                         self.experiment_case_list,
                                         self.ExperimentTitleTextEdit.text(),
                                         self.PeakPickingComboBox.currentText(),
                                          parse_peak_picking_params(self.PeakPickingComboBox.currentText(),
                                                            self.PeakPickingParamsBox))))

        self.ViewSummaryButton.clicked.connect(
            lambda: view_summary(self)
        )
        self.NewExperimentButton.clicked.connect(
            lambda: new_experiment(self)
        )

        self.CumulativeIntensityProportionRadioButton.clicked.connect(
            lambda: experiment_result_plot(self.canvas, self.experiment, 
                                           self.experiment_name_list, "cumulative_intensity_proportion")
        )

        self.CumulativeCoverageRadioButton.clicked.connect(
            lambda: experiment_result_plot(self.canvas, self.experiment, 
                                           self.experiment_name_list, "cumulative_coverage_proportion")
        )

    @qtc.pyqtSlot(Experiment, str)
    def set_experiment_and_summary(self, experiment, summary):
        if summary != "":
            task_completed_pop_up("ViMMS Experiment", "Experiment execution now complete!\nOutput saved to: results/experiment_results", 
                                  self.ViewSummaryButton)
            self.experiment = experiment
            self.summary = summary
        else:
            input_error_pop_up(self.RunExperimentButton)

    @qtc.pyqtSlot()
    def check_mzml_file(self):
        check_valid_inputs(self.AddFullscanButton, line_edits = [self.fullscan_upload_button.file_name])

    @qtc.pyqtSlot()
    def check_case_inputs(self):
        check_valid_inputs(self.AddExperimentCaseButton, 
                           line_edits = [self.CaseNameTextEdit.text()],
                           combo_boxes = [self.ControllerComboBox],
                           stored_required_lists = [self.fullscan_list],
                           stored_named_vals = [self.experiment_name_list])

    @qtc.pyqtSlot()
    def check_run_exp_inputs(self):
        check_valid_inputs(self.RunExperimentButton, 
                           line_edits=[self.ExperimentTitleTextEdit.text()],
                            combo_boxes= [self.PeakPickingComboBox],
                           stored_required_lists = [self.experiment_case_list],
                           stored_named_vals=[self.r_install, self.mzmine_install],
                           peak_picking_params=[self.PeakPickingComboBox.currentText(),
                                                self.PeakPickingParamsBox])
        

    @qtc.pyqtSlot()
    def check_install_paths(self):
        if not os.path.isfile(os.path.join(os.getcwd(), "userData.json")):
            with open(os.path.join(os.getcwd(), "userData.json"), 'w') as f:
                json.dump({"R": "", "MZMine": ""}, f)
        
        if self.PeakPickingComboBox.currentText() == "XCMS":
            check_peak_picking_paths(self, "R")
        elif self.PeakPickingComboBox.currentText() == "MZMine":
            check_peak_picking_paths(self, "MZMine")