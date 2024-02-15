from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from SimulatePage import Ui_SimulateForm

from Utils.UploadFile import *

from Utils.Display.setCharge import *
from Utils.Display.displayParams import *
from Utils.Display.inputErrorPopUp import input_error_pop_up
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Index.indexP import index_p
from Utils.Parameters.addElementsToComboBox import add_elements_to_combo_box
from Utils.Parameters.CustomWidgets import PUpload, QParamRangeSlider
from Utils.Parameters.ParamWidgets import CONTROLLER_PARAMS, CONTROLLERS
from Utils.Parameters.loadParamState import load_param_state
from Utils.Parameters.saveParamState import save_param_state
from Utils.Parameters.parseAdvancedParams import parse_advanced_params
from Utils.checkValidInputs import check_valid_inputs
from Utils.Threads.workerThreads import SimulateWorker

class SimulatePage(qtw.QWidget, Ui_SimulateForm):

    start_sim = qtc.pyqtSignal(str, str, int, int, qtw.QGroupBox, str, dict)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        
        self.SimulateHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.LoadParamsButton.setIcon(qtg.QIcon("Images/folder.svg"))
        self.SaveParamsButton.setIcon(qtg.QIcon("Images/save.png"))

        self.scrollArea.setWidget(self.ParamsBox)

        add_elements_to_combo_box(self.ControllerComboBox, CONTROLLERS)

        self.p_upload_button = PUpload(parent=self.PUploadGroupBox)
        self.p_upload_button.setObjectName("p_upload_button")
        self.PUploadGroupBox.setLayout(self.p_upload_button.layout())
        self.p_upload_button.file_upload.connect(self.check_simulate_inputs)
        self.p_upload_button.file_upload.connect(self.set_slider_ranges)
        self.OutputFileTextEdit.textChanged.connect(self.check_simulate_inputs)
        self.ControllerComboBox.currentIndexChanged.connect(self.check_simulate_inputs)

        self.rt_input = QParamRangeSlider(parent=self.RTSliderGroupBox)

        self.worker = SimulateWorker()
        self.worker_thread = qtc.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.start_sim.connect(self.worker.run)
        self.worker.simulation_finished.connect(self.notify_sim_finish)

        self.ControllerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ParamsBox,self.ControllerComboBox.currentText(), 
             CONTROLLER_PARAMS,True))
        
        self.SaveParamsButton.clicked.connect(
            lambda: save_param_state(self,
                                     self.ControllerComboBox.currentText())
        )

        self.LoadParamsButton.clicked.connect(
            lambda: load_param_state(self)
        )
        
        self.SimulateButton.clicked.connect(
            lambda: (self.SimulateButton.setEnabled(False),
                     self.start_sim.emit(self.ControllerComboBox.currentText(), 
                                         self.p_upload_button.file_location,
                                         self.rt_input.min_val_input.text(), 
                                         self.rt_input.max_val_input.text(),self.ParamsBox,
                                        self.OutputFileTextEdit.text(),
                                        parse_advanced_params(self.AdvancedParamsGroupBox),
                                        ))
        )

    @qtc.pyqtSlot(str)
    def notify_sim_finish(self, notification_msg):
        if notification_msg == "Simulated":
            task_completed_pop_up(self, "ViMMS Simulation", "Current simulation now complete!",
                                  self.SimulateButton)
        else:
            input_error_pop_up(self.SimulateButton)

    @qtc.pyqtSlot()
    def check_simulate_inputs(self):
        check_valid_inputs(self.SimulateButton, line_edits = [self.p_upload_button.file_name, 
                                                                 self.OutputFileTextEdit.text()],
                                                   combo_boxes = self.findChildren(qtw.QComboBox))
        
    @qtc.pyqtSlot()
    def set_slider_ranges(self):
            if self.p_upload_button.file_name != "":
                min_val, max_val = index_p(self.p_upload_button.file_location)
                self.rt_input.set_vals(min_val, max_val)
            else:
                self.rt_input.disable_slider()