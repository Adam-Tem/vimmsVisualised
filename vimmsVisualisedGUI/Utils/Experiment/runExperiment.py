from vimms.Experiment import Experiment
from Utils.PeakPicking.loadPeakPickingParams import load_peak_picking_param
from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY
import os

def run_experiment(experiment_cases, experiment_title, pp_type, passed_pp_params):

    experiment = Experiment()
    current_folder = os.getcwd()

    experiment.add_cases(experiment_cases)
    if not os.path.isdir(os.path.join(SAVE_DIRECTORY, "experiment_results")):
        os.mkdir(os.path.join(SAVE_DIRECTORY, "experiment_results"))
    if not os.path.isdir(os.path.join(SAVE_DIRECTORY, "experiment_results", experiment_title)):
        os.mkdir(os.path.join(SAVE_DIRECTORY, "experiment_results", experiment_title))
    out_dir = os.path.join(current_folder, SAVE_DIRECTORY, "experiment_results", experiment_title)
    num_of_workers = len(experiment_cases)
    scan_duration_dict = {1: 0.59, 2: 0.19}
    experiment.run_experiment(out_dir=out_dir, num_workers=num_of_workers, scan_duration_dict=scan_duration_dict)
    pp_params = load_peak_picking_param(pp_type, passed_pp_params)

    experiment.evaluate(pp_params=pp_params, num_workers=num_of_workers, force_peak_picking=True, aligned_names="test_0_xcms_aligned.csv")
    summary = experiment.summarise()
    return experiment, summary