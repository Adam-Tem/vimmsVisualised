from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

from vimms.Experiment import Experiment

from Utils.Simulate.runController import run_controller
from Utils.Experiment.runExperiment import run_experiment
from Utils.Extract.ExtractData import extract_data
from Utils.Generate.RunChemicalMixtureCreator import run_chemical_mixture_creator

class ExperimentWorker(qtc.QObject):
    experiment_finished = qtc.pyqtSignal(Experiment, str)

    @qtc.pyqtSlot(list, dict)
    def run(self, experiment_cases, xcms_params):
        try:
            experiment, summary = run_experiment(experiment_cases, xcms_params)
            self.experiment_finished.emit(experiment, summary)
        except:
            self.experiment_finished.emit(Experiment(), "")

class SimulateWorker(qtc.QObject):
    simulation_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(str, str, int, int, qtw.QGroupBox, str, dict)
    def run(self, controller_name, file_location, min_rt, max_rt, param_box, output_filename, advanced_params):
        try:
            run_controller(controller_name, file_location, int(min_rt), int(max_rt), param_box , output_filename, advanced_params)
            self.simulation_finished.emit("Simulated")
        except:
            self.simulation_finished.emit("Simulation Failed")

class ExtractWorker(qtc.QObject):
    extract_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QGroupBox, str, str, str, str)
    def run(self, param_box, file_location, file_name, file_save_name, save_directory):
        try:
            extract_data(param_box, file_location, file_name, file_save_name, save_directory)
            self.extract_finished.emit("Extracted")
        except:
            self.extract_finished.emit("Extraction Failed")
           

class GenerateWorker(qtc.QObject):
    generate_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QGroupBox, str, str, int, str)
    def run(self, param_box, adduct_prop, chems_to_sample, ms2_level, file_save_name):
        try:
            run_chemical_mixture_creator(param_box, adduct_prop, chems_to_sample, ms2_level, file_save_name)
            self.generate_finished.emit("Generated")
        except:
            self.generate_finished.emit("Generation Failed")