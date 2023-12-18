from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from SimulatePage import Ui_SimulateForm

from vimmsVisualisedGUI.Utils.UploadFile import *

from Utils.setCharge import *
from Utils.Display.displayParams import *
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.LoadingWidget import *
from Utils.Parameters.ParamWidgets import CONTROLLER_PARAMS, CONTROLLERS
from Utils.Parameters.loadParamState import load_param_state
from Utils.Parameters.saveParamState import save_param_state
from Utils.Parameters.parseAdvancedParams import parse_advanced_params
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

        self.worker = SimulateWorker()
        self.worker_thread = qtc.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.start_sim.connect(self.worker.run)
        self.worker.simulation_finished.connect(self.notify_sim_finish)

        self.SelectFileButton.clicked.connect(lambda: upload_file(self, "p"))
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
                                         int(self.min_rt.text()), int(self.max_rt.text()),self.ParamsBox,
                                        self.OutputFileTextEdit.text(),
                                        parse_advanced_params(self.AdvancedParamsGroupBox),
                                        ))
        )

    @qtc.pyqtSlot()
    def notify_sim_finish(self):
        self.SimulateButton.setEnabled(True)
        task_completed_pop_up("ViMMS Simulation", "Current simulation now complete!")