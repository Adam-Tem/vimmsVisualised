from PyQt5 import QtCore as qtc
from vimms.Experiment import Experiment

from Utils.Experiment.runExperiment import run_experiment

class ExperimentWorker(qtc.QObject):
    experiment_finished = qtc.pyqtSignal(Experiment, str)

    @qtc.pyqtSlot(list)
    def run(self, experiment_cases):
        experiment, summary = run_experiment(experiment_cases)
        self.experiment_finished.emit(experiment, summary)