from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw

import traceback
from vimms.Experiment import Experiment

from Graphing.graphCanvas import MplCanvas
from Graphing.SelectGraphToPlot import select_graph_to_plot
from Graphing.plotlyExperimentGraphs import plotly_experiment_graphs
from Utils.Simulate.runController import run_controller
from Utils.Experiment.runExperiment import run_experiment
from Utils.Extract.ExtractData import extract_data
from Utils.Generate.RunChemicalMixtureCreator import run_chemical_mixture_creator

class ExperimentWorker(qtc.QObject):
    experiment_finished = qtc.pyqtSignal(Experiment, str)

    @qtc.pyqtSlot(qtw.QLabel, list, str, str, dict)
    def run(self, loading_label, experiment_cases, experiment_title, pp_type, pp_params):
        try:
            loading_label.show()
            experiment, summary = run_experiment(experiment_cases, experiment_title, pp_type, pp_params)
            loading_label.hide()
            self.experiment_finished.emit(experiment, summary)
        except Exception as e:
            loading_label.hide()
            self.experiment_finished.emit(Experiment(), "")

class SimulateWorker(qtc.QObject):
    simulation_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QLabel, str, str, qtw.QGroupBox, str, dict)
    def run(self, loading_label, controller_name, file_location, param_box, output_filename, advanced_params):
        try:
            loading_label.show()
            run_controller(controller_name, file_location, param_box , output_filename, advanced_params)
            loading_label.hide()
            self.simulation_finished.emit("Simulated")
        except:
            loading_label.hide()
            self.simulation_finished.emit("Simulation Failed")

class ExtractWorker(qtc.QObject):
    extract_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QLabel, qtw.QGroupBox, str, str, str)
    def run(self, loading_label, param_box, file_name, file_save_name, save_directory):
        try:
            loading_label.show()
            extract_data(param_box, file_name, file_save_name, save_directory)
            loading_label.hide()
            self.extract_finished.emit("Extracted")
        except:
            loading_label.hide()
            self.extract_finished.emit("Extraction Failed")
           

class GenerateWorker(qtc.QObject):
    generate_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QLabel, qtw.QPushButton, qtw.QGroupBox, str, str, int, str)
    def run(self, loading_label, button, param_box, adduct_prop, chems_to_sample, ms2_level, file_save_name):
        try:
            loading_label.move(button.x(), button.y())
            loading_label.show()
            run_chemical_mixture_creator(param_box, adduct_prop, chems_to_sample, ms2_level, file_save_name)
            loading_label.hide()
            self.generate_finished.emit("Generated")
        except:
            loading_label.hide()
            self.generate_finished.emit("Generation Failed")

class MzmlGraphWorker(qtc.QObject):
    graphing_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QLabel, MplCanvas, str, str, str, str, str, str, str)
    def run(self, loading_label, canvas, file_location, file_name, combo_box_text, min_rt, max_rt, lower_scan, upper_scan):
        try:
            loading_label.show()
            select_graph_to_plot(canvas, file_location, file_name, combo_box_text, min_rt, max_rt, lower_scan, upper_scan)
            loading_label.hide()
            self.graphing_finished.emit("Graphing finished")
        except:
            loading_label.hide()
            self.graphing_finished.emit("Graphing failed")

class ExpGraphWorker(qtc.QObject):
    graphing_finished = qtc.pyqtSignal(str)

    @qtc.pyqtSlot(qtw.QLabel, list, qtw.QComboBox, qtw.QComboBox, str, str)
    def run(self, loading_label, radio_buttons, exp_mzmls, exp_pkls, exp_location, exp_name):
        try:
            loading_label.show()
            plotly_experiment_graphs(radio_buttons, exp_mzmls, exp_pkls, exp_location, exp_name)
            loading_label.hide()
            self.graphing_finished.emit("Graphing finished")
        except:
            loading_label.hide()
            self.graphing_finished.emit("Graphing failed")