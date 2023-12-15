from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from vimms.Experiment import Experiment

from Utils.Experiment.runExperiment import run_experiment
from Utils.Controllers.controllerSelection import controller_selection

class ExperimentWorker(qtc.QObject):
    experiment_finished = qtc.pyqtSignal(Experiment, str)

    @qtc.pyqtSlot(list, dict)
    def run(self, experiment_cases, xcms_params):
        experiment, summary = run_experiment(experiment_cases, xcms_params)
        self.experiment_finished.emit(experiment, summary)

class SimulateWorker(qtc.QObject):
    simulation_finished = qtc.pyqtSignal()

    @qtc.pyqtSlot(qtw.QGroupBox, str, dict)
    def run(self, param_box, controller, advanced_params):
        controller_selection(param_box, controller, advanced_params)
        self.simulation_finished.emit()