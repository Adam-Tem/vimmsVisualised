from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from vimms.Experiment import Experiment

from Utils.Controllers.controllerSelection import controller_selection
from Utils.Experiment.runExperiment import run_experiment
from Utils.Extract.ExtractData import extract_data
from Utils.Generate.RunChemicalMixtureCreator import run_chemical_mixture_creator

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

class ExtractWorker(qtc.QObject):
    extract_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QGroupBox, str, str, str, str)
    def run(self, param_box, file_location, file_name, file_save_name, save_directory):
        extract_data(param_box, file_location, file_name, file_save_name, save_directory)
        self.extract_finished.emit("Extracted")

class GenerateWorker(qtc.QObject):
    generate_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QGroupBox, str, str, int, str)
    def run(self, param_box, adduct_prop, chems_to_sample, ms2_level, file_save_name):
       run_chemical_mixture_creator(param_box, adduct_prop, chems_to_sample, ms2_level, file_save_name)
       self.generate_finished.emit("Generated")