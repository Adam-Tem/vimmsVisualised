from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from SimulatePage import Ui_SimulateForm

from vimmsVisualisedGUI.Utils.UploadFile import *

from vimmsVisualisedGUI.Utils.Display.setCharge import *
from Utils.Display.displayParams import *
from Utils.Display.inputErrorPopUp import input_error_pop_up
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Parameters.CustomWidgets import PUpload
from Utils.Parameters.ParamWidgets import CONTROLLER_PARAMS, CONTROLLERS
from Utils.Parameters.loadParamState import load_param_state
from Utils.Parameters.saveParamState import save_param_state
from Utils.Parameters.parseAdvancedParams import parse_advanced_params
from Utils.checkValidInputs import check_valid_inputs
from vimmsVisualisedGUI.Utils.Threads.workerThreads import SimulateWorker

class SimulatePage(qtw.QWidget, Ui_SimulateForm):

    start_sim = qtc.pyqtSignal(str, str, int, int, qtw.QGroupBox, str, dict)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.file_name = ""
        self.file_location = ""
        
        self.SimulateHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.LoadParamsButton.setIcon(qtg.QIcon("Images/folder.svg"))
        self.SaveParamsButton.setIcon(qtg.QIcon("Images/save.png"))

        self.simulate_upload_button = PUpload(parent=self.PUploadGroupBox)
        self.simulate_upload_button.setObjectName("simulate_upload_button")
        self.PUploadGroupBox.setLayout(self.simulate_upload_button.layout())
        self.simulate_upload_button.file_upload.connect(self.check_simulate_inputs)
        self.OutputFileTextEdit.textChanged.connect(self.check_simulate_inputs)
        self.min_rt.textChanged.connect(self.check_simulate_inputs)
        self.max_rt.textChanged.connect(self.check_simulate_inputs)
        self.ControllerComboBox.currentIndexChanged.connect(self.check_simulate_inputs)

        self.worker = SimulateWorker()
        self.worker_thread = qtc.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.start_sim.connect(self.worker.run)
        self.worker.simulation_finished.connect(self.notify_sim_finish)

        self.ControllerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ParamsBox,self.ControllerComboBox.currentText(), 
             CONTROLLERS, CONTROLLER_PARAMS,True))
        
        self.SaveParamsButton.clicked.connect(
            lambda: save_param_state(self,
                                     self.ControllerComboBox.currentText())
        )

        self.LoadParamsButton.clicked.connect(
            lambda: load_param_state(self)
        )
        
        self.SimulateButton.clicked.connect(
            lambda: (self.SimulateButton.setEnabled(False),
                     self.start_sim.emit(self.ControllerComboBox.currentText(), self.file_location,
                                         self.min_rt.text(), self.max_rt.text(),self.ParamsBox,
                                        self.OutputFileTextEdit.text(),
                                        parse_advanced_params(self.AdvancedParamsGroupBox),
                                        ))
        )

    @qtc.pyqtSlot(str)
    def notify_sim_finish(self, notification_msg):
        if notification_msg == "Simulated":
            task_completed_pop_up("ViMMS Simulation", "Current simulation now complete!",
                                  self.SimulateButton)
        else:
            input_error_pop_up(self.SimulateButton)

    @qtc.pyqtSlot()
    def check_simulate_inputs(self):
        check_valid_inputs(self.SimulateButton, line_edits = [self.simulate_upload_button.file_name, 
                                                                 self.OutputFileTextEdit.text(),
                                                                 self.min_rt.text(), self.max_rt.text()],
                                                   combo_boxes = self.findChildren(qtw.QComboBox))
