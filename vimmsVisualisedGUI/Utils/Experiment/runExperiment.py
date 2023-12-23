from vimms.Experiment import Experiment
from vimms.PeakPicking import XCMSScriptParams
from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY
import os

def run_experiment(experiment_cases, xcms_params):

    experiment = Experiment()
    current_folder = os.getcwd()

    experiment.add_cases(experiment_cases)
    if not os.path.isdir(os.path.join(SAVE_DIRECTORY, "experiment_results")):
        os.mkdir(os.path.join(SAVE_DIRECTORY, "experiment_results"))
    
    out_dir = os.path.join(current_folder, SAVE_DIRECTORY, "experiment_results")
    num_of_workers = len(experiment_cases)
    scan_duration_dict = {1: 0.59, 2: 0.19}
    experiment.run_experiment(out_dir=out_dir, num_workers=num_of_workers, scan_duration_dict=scan_duration_dict)
    print(xcms_params)
    pp_params = XCMSScriptParams(
    xcms_r_script = os.path.join(current_folder, "xcms_script.R"), 
    rscript_exe= os.path.join("C:\\","Program Files","R","R-4.3.2","bin","Rscript.exe"),
    **xcms_params
)
    experiment.evaluate(pp_params=pp_params, num_workers=num_of_workers, force_peak_picking=True, aligned_names="test_0_xcms_aligned.csv")
    summary = experiment.summarise()
    return experiment, summary