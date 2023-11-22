from vimms.Experiment import Experiment
from vimms.PeakPicking import XCMSScriptParams

import os

def run_experiment(experiment_cases):

    experiment = Experiment()
    current_folder = os.getcwd()

    experiment.add_cases(experiment_cases)
    if not os.path.isdir(os.path.join(current_folder, "experiment_results")):
        os.mkdir(os.path.join(current_folder, "experiment_results"))
    
    out_dir = os.path.join(current_folder, "experiment_results")
    num_of_workers = len(experiment_cases)
    scan_duration_dict = {1: 0.59, 2: 0.19}
    experiment.run_experiment(out_dir=out_dir, num_workers=num_of_workers, scan_duration_dict=scan_duration_dict)
    pp_params = XCMSScriptParams(
    xcms_r_script = os.path.join(current_folder, "xcms_script.R"), 
    ppm = 15,
    pwlower = 15,
    pwupper = 80,
    snthresh = 5,
    noise = 1000,
    prefilterlower = 3,
    prefilterupper = 500,
    rscript_exe= os.path.join("C:\\","Program Files","R","R-4.3.2","bin","Rscript.exe")
)

    experiment.evaluate(pp_params=pp_params, num_workers=num_of_workers, force_peak_picking=True, aligned_names="test_0_xcms_aligned.csv")
    experiment.get_reports(min_intensities=[1000]*len(experiment_cases))
    experiment.rank_cases(min_intensities=[1000]*len(experiment_cases), num_workers=num_of_workers)
    experiment.summarise(num_workers=num_of_workers, min_intensities=[1000]*len(experiment_cases))