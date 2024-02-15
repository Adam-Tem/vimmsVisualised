from PyQt5 import QtWidgets as qtw
from Utils.Parameters.CustomWidgets import *

from vimms.Controller import *
from vimms.Roi import RoiBuilderParams, SmartRoiParams
from vimms.BoxManager import BoxManager, BoxConverter, BoxSplitter
from vimms.Box import BoxGrid
from vimms.ChemicalSamplers import *
from vimms.Common import ROI_EXCLUSION_DEW, GRID_CONTROLLER_SCORING_PARAMS

import copy

R_INSTALL = os.path.join("C:\\","Program Files","R","R-4.3.2","bin","Rscript.exe")

MIN_MZ = 0
MAX_MZ = 100000
CONTROLLERS = {"TopN Controller": TopNController, 
               "TopN ROI Controller": TopN_RoiController, 
               "TopN Smart ROI Controller": TopN_SmartRoiController,
               "TopNEX Controller": TopNEXController,
               "Hard ROI Exclusion Controller": HardRoIExcludeController,
               "Intensity ROI Exclusion Controller": IntensityRoIExcludeController,
               "Non Overlap Controller": NonOverlapController,
               "Intensity Non Overlap Controller": IntensityNonOverlapController,
               }

CONTROLLERS_WITH_ROI_PARAMS = ["TopN Smart ROI Controller", 
                               "TopN ROI Controller",
                               "TopNEX Controller",
                               "Hard ROI Exclusion Controller",
                               "Intensity ROI Exclusion Controller",
                               "Non Overlap Controller",
                               "Intensity Non Overlap Controller"]


CONTROLLERS_WITH_SMART_ROI_PARAMS = copy.copy(CONTROLLERS_WITH_ROI_PARAMS)
CONTROLLERS_WITH_SMART_ROI_PARAMS.remove("TopN ROI Controller")

CONTROLLERS_WITH_BOX_GRID = copy.copy(CONTROLLERS_WITH_SMART_ROI_PARAMS)
CONTROLLERS_WITH_BOX_GRID.remove("TopN Smart ROI Controller")



FORMULA_SAMPLERS = {"Even MZ Formula Sampler": EvenMZFormulaSampler,
               "Uniform MZ Formula Sampler": UniformMZFormulaSampler,
               "MZML Formula Sampler": MZMLFormulaSampler,
}

RTI_SAMPLERS = {"Uniform RT & Intensity": UniformRTAndIntensitySampler,
                "MZML RT & Intensity": MZMLRTandIntensitySampler,
}

CHROMO_SAMPLERS = {"Gaussian Chromatogram Sampler": GaussianChromatogramSampler,
                   "Constant Chromatogram Sampler": ConstantChromatogramSampler,
                   "MZML Chromatogram Sampler": MZMLChromatogramSampler,
}

MS2_SAMPLERS = {"Uniform MS2 Sampler": UniformMS2Sampler,
                "Fixed MS2 Sampler": FixedMS2Sampler,
                "MGF MS2 Sampler": MGFMS2Sampler,
                "MZML MS2 Sampler": MZMLMS2Sampler,
                "CRPM MS2 Sampler": CRPMS2Sampler}

SAMPLERS = [("formula_sampler", FORMULA_SAMPLERS),
            ("chromatogram_sampler", CHROMO_SAMPLERS),
            ("ms2_sampler", MS2_SAMPLERS),
            ("rt_and_intensity_sampler", RTI_SAMPLERS),]

CONTROLLER_PARAMS = {
    "ionisation_mode": [("ionisation_mode", QIonModeButton), ("Ionisation Mode:", qtw.QLabel)],
    "N": [("N", qtw.QSpinBox), ("N:", qtw.QLabel)],
    "isolation_width": [("isolation_width", qtw.QLineEdit), ("Isolation Width:", qtw.QLabel)],
    "mz_tol": [("mz_tol", qtw.QLineEdit), ("MZ Tolerance:", qtw.QLabel)],
    "rt_tol": [("rt_tol", qtw.QLineEdit), ("RT Tolerance:", qtw.QLabel)],
    "min_ms1_intensity": [("min_ms1_intensity", qtw.QLineEdit), ("Min MS1 Intensity:", qtw.QLabel)],
    "ms1_shift": [("ms1_shift", qtw.QLineEdit), ("MS1 Shift:", qtw.QLabel), 0],
    # "initial_exclusion_list": [("initial_exclusion_list", qtw.QLineEdit), ("Initial Exclusion:", qtw.QLabel)],
    "force_N": [("force_N", QBooleanButton), ("Force N:", qtw.QLabel), False],
    "min_roi_length_for_fragmentation": [("min_roi_length_for_fragmentation", qtw.QLineEdit), ("Min Frag. Length:", qtw.QLabel), 0],
    "exclusion_method": [("exclusion_method", qtw.QComboBox), ("Exclusion Method:", qtw.QLabel), ROI_EXCLUSION_DEW],
    "exclusion_t_0": [("exclusion_t_0", qtw.QLineEdit), ("Exclusion T0:", qtw.QLabel)],
    "register_all_roi": [("register_all_roi", QBooleanButton), ("Register all ROI:", qtw.QLabel), False],
    "scoring_params": [("scoring_params", QScoringParams), ("Scoring Params:", qtw.QLabel), GRID_CONTROLLER_SCORING_PARAMS],
    "dsda_state": [("dsda_state", qtw.QLineEdit), ("DSDA State:", qtw.QLabel)],
    "mzml_name": [("mzml_name", qtw.QLineEdit), ("MZML Name:", qtw.QLabel)],
    "task_filter": [("task_filter", qtw.QLineEdit), ("Task Filter:", qtw.QLabel)],
    "schedule": [("schedule", qtw.QLineEdit), ("Schedule:", qtw.QLabel)],
    "expected_rts": [("expected_rts", qtw.QLineEdit), ("Expected RTs:", qtw.QLabel)],
}

ROI_PARAMS = {
    "min_roi_length": [("min_roi_length", qtw.QLineEdit), ("Min ROI Length:", qtw.QLabel), 0],
    "min_roi_intensity": [("min_roi_intensity", qtw.QLineEdit), ("Min ROI Intensity:", qtw.QLabel), 0],
    "at_least_one_point_above": [("at_least_one_point_above", qtw.QLineEdit), ("At Least 1 Above:", qtw.QLabel), 0],
    "start_rt": [("start_rt", qtw.QLineEdit), ("Start RT:", qtw.QLabel), 0],
    "stop_rt": [("stop_rt", qtw.QLineEdit), ("Stop RT:", qtw.QLabel), 100000],
    "max_gaps_allowed": [("max_gaps_allowed", qtw.QLineEdit), ("Max Gaps Allowed:", qtw.QLabel), 0],
    "mz_tol": [("mz_tol", qtw.QLineEdit), ("MZ Tolerance:", qtw.QLabel), 10]
}

SMART_ROI_PARAMS = {
    "initial_length_seconds": [("initial_length_seconds", qtw.QLineEdit), ("Initial Length (s):", qtw.QLabel), 5],
    "reset_length_seconds": [("reset_length_seconds", qtw.QLineEdit), ("Reset Length (s):", qtw.QLabel), 1000000],
    "intensity_increase_factor": [("intensity_increase_factor", qtw.QLineEdit), ("Intensity Increase Factor:", qtw.QLabel), 10],
    "dew": [("dew", qtw.QLineEdit), ("DEW:", qtw.QLabel), 15],
    "drop_perc": [("drop_perc", qtw.QLineEdit), ("Drop Percent:", qtw.QLabel), 0.1],
}

BOX_PARAMS = {
    "delete_rois": [("delete_rois", QBooleanButton), ("Delete RoIs:", qtw.QLabel), True], 
    "min_rt": [("min_rt", qtw.QLineEdit), ("Min RT:", qtw.QLabel), 0],
    "max_rt": [("max_rt", qtw.QLineEdit), ("Max RT:", qtw.QLabel), 1440],
    "rt_box_size": [("rt_box_size", qtw.QLineEdit), ("RT Box Size:", qtw.QLabel), 50],
    "min_mz": [("min_mz", qtw.QLineEdit), ("Min MZ:", qtw.QLabel), 0],
    "max_mz": [("max_mz", qtw.QLineEdit), ("max_mz", qtw.QLabel), 2000],
    "mz_box_size": [("mz_box_size", qtw.QLineEdit), ("MZ Box Size:", qtw.QLabel), 1],
    "ignore": [("ignore", QBooleanButton), ("Ignore:", qtw.QLabel), False],
    "unique": [("unique", QBooleanButton), ("Unique:", qtw.QLabel), True],
    "min_rt_width": [("min_rt_width", qtw.QLineEdit), ("Min RT Width:", qtw.QLabel), 1E-07],
    "min_mz_width": [("min_mz_width", qtw.QLineEdit), ("Min MZ Width:", qtw.QLabel), 1E-07],
    "split": [("split", QBooleanButton ), ("Split:", qtw.QLabel), False]
}

INLINE_PARAMS = ROI_PARAMS | SMART_ROI_PARAMS | BOX_PARAMS

BOX_CONSTRUCTORS = {
    "box_geometry": BoxGrid,
    "box_converter": BoxConverter,
    "box_splitter": BoxSplitter
}

INLINE_CONSTRUCTORS = {
    "roi_params": RoiBuilderParams,
    "smartroi_params": SmartRoiParams,
    "grid": BoxManager,
} | BOX_CONSTRUCTORS


FORMULA_SAMPLER_PARAMS = {
    "min_mz": [("min_mz", qtw.QLineEdit), ("Min MZ:", qtw.QLabel), MIN_MZ],
    "max_mz": [("max_mz", qtw.QLineEdit), ("Max MZ:",  qtw.QLabel), MAX_MZ],
    "mzml_file_name": [("mzml_file_name", QMzmlUpload), ("MZML File:", qtw.QLabel)],
    "source_polarity": [("source_polarity", QIonModeButton), ("Source Polarity:", qtw.QLabel), POSITIVE],
}

RTI_SAMPLER_PARAMS = {
    "min_rt": [("min_rt", qtw.QLineEdit), ("Min RT:", qtw.QLabel), 0],
    "max_rt": [("max_rt", qtw.QLineEdit), ("Max RT:", qtw.QLabel), 1600],
    "min_log_intensity": [("min_log_intensity", qtw.QLineEdit), ("Min Log Intensity:", qtw.QLabel), 10000],
    "max_log_intensity": [("max_log_intensity", qtw.QLineEdit), ("Max Log Intensity", qtw.QLabel), 10000000],
    "mzml_file_name": [("mzml_file_name", QMzmlUpload), ("MZML File:", qtw.QLabel)],
    "n_intensity_bins": [("n_intensity_bins", qtw.QLineEdit), ("# Intensity Bins:", qtw.QLabel), 10],
   
    
}

CHROMO_SAMPLER_PARAMS = {
   "sigma": [("sigma", qtw.QLineEdit), ("Sigma:", qtw.QLabel), 10],
   "mzml_file_name": [("mzml_file_name", QMzmlUpload), ("MZML File:", qtw.QLabel)],
}

MS2_SAMPLER_PARAMS = {
    "poiss_peak_mean": [("poiss_peak_mean", qtw.QLineEdit), ("Poiss Peak Mean:", qtw.QLabel), 10],
    "min_mz": [("min_mz", qtw.QLineEdit), ("Min MZ:", qtw.QLabel), MIN_MZ_MS2],
    "min_proportion": [("min_proportion", qtw.QLineEdit), ("Min Proportion:", qtw.QLabel), 0.1],
    "max_proportion": [("max_proportion", qtw.QLineEdit), ("Max Proportion:", qtw.QLabel), 0.8],
    "n_frags": [("n_frags", qtw.QLineEdit), ("# Fragment Peaks:", qtw.QLabel), 2],
    "n_draws": [("n_draws", qtw.QLineEdit), ("# Draws:", qtw.QLabel), 1000],
    "alpha": [("alpha", qtw.QLineEdit), ("Alpha:", qtw.QLabel), 1],
    "base": [("base", qtw.QLabel), ("Base:", qtw.QLabel), "uniform"],
    "mgf_file": [("mgf_file", QMgfUpload), ("MGF File:", qtw.QLabel)],
    "max_peaks": [("max_peaks", qtw.QLineEdit), ("Max Peaks:", qtw.QLabel), 0],
    "replace": [("replace", QBooleanButton), ("Replace:", qtw.QLabel), False],
    "id_field": [("id_field", qtw.QLabel), ("ID of MGF:", qtw.QLabel), "SPECTRUMID"],
    "mzml_file": [("mzml_file", QMzmlUpload), ("MZML File:", qtw.QLabel)],
    "min_n_peaks": [("min_n_peaks", qtw.QLineEdit), ("Min # Peaks:", qtw.QLabel), 1],
    "with_replacement": [("with_replacement", QBooleanButton), ("Replace:", qtw.QLabel), False],
}

XCMS_PARAMS = {
    "ppm": [("ppm", qtw.QLineEdit), ("PPM:", qtw.QLabel), 15],
    "pwlower": [("pwlower", qtw.QLineEdit), ("Min Peak Width:", qtw.QLabel), 15],
    "pwupper": [("pwupper", qtw.QLineEdit), ("Max Peak Width:", qtw.QLabel), 80],
    "snthresh": [("snthresh", qtw.QLineEdit), ("Signal to Noise Thresh.:", qtw.QLabel), 5],
    "noise": [("noise", qtw.QLineEdit), ("Noise:", qtw.QLabel), 1000],
    "prefilterlower": [("prefilterlower", qtw.QLineEdit), ("Pre Filter Min:", qtw.QLabel), 3],
    "prefilterupper": [("prefilterupper",qtw.QLineEdit ), ("Pre Filter Max:", qtw.QLabel), 500], 
}

MZMINE_PARAMS = {
    "mzmine_template": [("mzmine_template", QXMLUpload), ("MZMine Template:", qtw.QLabel)],
}

PARSE_AS_INT = ["n_intensity_bins", "n_frags", "n_draws"]
PARSE_AS_LOG = ["min_log_intensity", "max_log_intensity"]

SAVE_DIRECTORY =  os.path.join(os.path.abspath(os.getcwd()), 'results')


ALL_CONSTRUCTORS = CONTROLLERS | INLINE_CONSTRUCTORS | FORMULA_SAMPLERS | MS2_SAMPLERS | CHROMO_SAMPLERS | RTI_SAMPLERS
                    