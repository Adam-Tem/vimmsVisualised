from PyQt5 import QtCore as qtc
from vimms.Experiment import Experiment

from Utils.Experiment.runExperiment import run_experiment

class ExperimentWorker(qtc.QObject):
    experiment_finished = qtc.pyqtSignal(Experiment, str)

    @qtc.pyqtSlot(list, dict)
    def run(self, experiment_cases, xcms_params):
        experiment, summary = run_experiment(experiment_cases, xcms_params)
        self.experiment_finished.emit(experiment, summary)