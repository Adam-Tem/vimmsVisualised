from PyQt5 import QtWidgets as qtw
from Utils.CustomWidgets import *

from vimms.Controller import TopNController, TopN_SmartRoiController
from vimms.Roi import RoiBuilderParams, SmartRoiParams
from vimms.ChemicalSamplers import *

CONTROLLERS = {"TopN Controller": TopNController, 
               "TopN Smart ROI Controller": TopN_SmartRoiController,           
               }

ROI_BUILDERS = {"roi_params": RoiBuilderParams,
               "smartroi_params": SmartRoiParams,
}


FORMULA_SAMPLERS = {"Even MZ Formula Sampler": EvenMZFormulaSampler,
               "Pick Everything Formula Sampler": PickEverythingFormulaSampler,
               "Uniform MZ Formula Sampler": UniformMZFormulaSampler,
               "MZML Formula Sampler": MZMLFormulaSampler,
               "Database Formula Sampler": DatabaseFormulaSampler,
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
                "Exact Match MS2 Sampler": ExactMatchMS2Sampler,
                "MZML MS2 Sampler": MZMLMS2Sampler}

SAMPLERS = [("formula_sampler", FORMULA_SAMPLERS),
            ("chromatogram_sampler", CHROMO_SAMPLERS),
            ("ms2_sampler", MS2_SAMPLERS),
            ("rt_and_intensity_sampler", RTI_SAMPLERS),]

CONTROLLER_PARAMS = {
    "ionisation_mode": [("ionisation_mode", QIonModeButton), ("Ionisation Mode:", qtw.QLabel)],
    "N": [("N", qtw.QSpinBox), ("# of Injections:", qtw.QLabel)],
    "isolation_width": [("isolation_width", qtw.QLineEdit), ("Isolation Width:", qtw.QLabel)],
    "mz_tol": [("mz_tol", qtw.QLineEdit), ("MZ Tolerance:", qtw.QLabel)],
    "rt_tol": [("rt_tol", qtw.QLineEdit), ("RT Tolerance:", qtw.QLabel)],
    "min_ms1_intensity": [("min_ms1_intensity", qtw.QLineEdit), ("Min MS1 Intensity:", qtw.QLabel)],
    "ms1_shift": [("ms1_shift", qtw.QLineEdit), ("MS1 Shift:", qtw.QLabel)],
    "initial_exclusion_list": [("initial_exclusion_list", qtw.QLineEdit), ("Initial Exclusion:", qtw.QLabel)],
    "advanced_params": [("advanced_params", qtw.QLineEdit), ("Advanced Params:", qtw.QLabel)],
    "force_N": [("force_N", qtw.QLineEdit), ("Force N:", qtw.QLabel)],
    "min_roi_length_for_fragmentation": [("min_roi_length_for_fragmentation", qtw.QLineEdit), ("Min Fragmention Length:", qtw.QLabel)],
    "exclusion_method": [("exclusion_method", qtw.QComboBox), ("Exclusion Method:", qtw.QLabel)],
    "exclusion_t_0": [("exclusion_t_0", qtw.QLineEdit), ("Exclusion T0:", qtw.QLabel)],
}

ROI_PARAMS = {
    "min_roi_length": [("min_roi_length", qtw.QLineEdit), ("Min ROI Length:", qtw.QLabel)],
    "min_roi_intensity": [("min_roi_intensity", qtw.QLineEdit), ("Min ROI Intensity:", qtw.QLabel)],
    "at_least_one_point_above": [("at_least_one_point_above", qtw.QLineEdit), ("At Least 1 Above:", qtw.QLabel)],
    "start_rt": [("start_rt", qtw.QLineEdit), ("Start RT:", qtw.QLabel)],
    "stop_rt": [("stop_rt", qtw.QLineEdit), ("Stop RT:", qtw.QLabel)],
    "max_gaps_allowed": [("max_gaps_allowed", qtw.QLineEdit), ("Max Gaps Allowed:", qtw.QLabel)],
}

SMART_ROI_PARAMS = {
    "initial_length_seconds": [("initial_length_seconds", qtw.QLineEdit), ("Initial Length (s):", qtw.QLabel)],
    "reset_length_seconds": [("reset_length_seconds", qtw.QLineEdit), ("Reset Length (s):", qtw.QLabel)],
    "intensity_increase_factor": [("intensity_increase_factor", qtw.QLineEdit), ("Intensity Increase Factor:", qtw.QLabel)],
    "dew": [("dew", qtw.QLineEdit), ("DEW:", qtw.QLabel)],
    "drop_perc": [("drop_perc", qtw.QLineEdit), ("Drop Percent:", qtw.QLabel)],
}

FORMULA_SAMPLER_PARAMS = {
    "database": [("database", qtw.QLineEdit), ("Database:", qtw.QLabel)],
    "min_mz": [("min_mz", qtw.QLineEdit), ("Min MZ:", qtw.QLabel)],
    "max_mz": [("max_mz", qtw.QLineEdit), ("Max MZ:",  qtw.QLabel)],
    "mzml_file_name": [("mzml_file_name", qtw.QLineEdit), ("MZML File:", qtw.QLabel)],
    "source_polarity": [("source_polarity", QIonModeButton), ("Source Polarity:", qtw.QLabel)],
}

RTI_SAMPLER_PARAMS = {
    "min_rt": [("min_rt", qtw.QLineEdit), ("Min RT:", qtw.QLabel)],
    "max_rt": [("max_rt", qtw.QLineEdit), ("Max RT:", qtw.QLabel)],
    "min_log_intensity": [("min_log_intensity", qtw.QLineEdit), ("Min Log Intensity:", qtw.QLabel)],
    "max_log_intensity": [("max_log_intensity", qtw.QLineEdit), ("Max Log Intensity", qtw.QLabel)],
    "mzml_file_name": [("mzml_file_name", qtw.QLineEdit), ("MZML File:", qtw.QLabel)],
    "n_intensity_bins": [("n_intensity_bins", qtw.QLineEdit), ("# Intensity Bins:", qtw.QLabel)],
   
    
}

CHROMO_SAMPLER_PARAMS = {
   "sigma": [("sigma", qtw.QLineEdit), ("Sigma:", qtw.QLabel)],
#    "mzml_file_name": [("mzml_file_name", QFileSelector), ("MZML File:", qtw.QLabel)],
}

MS2_SAMPLER_PARAMS = {
    "poiss_peak_mean": [("poiss_peak_mean", qtw.QLineEdit), ("Poiss Peak Mean:", qtw.QLabel)],
    "min_mz": [("min_mz", qtw.QLineEdit), ("Min MZ:", qtw.QLabel)],
    "min_proportion": [("min_proportion", qtw.QLineEdit), ("Min Proportion:", qtw.QLabel)],
    "max_proportion": [("max_proportion", qtw.QLineEdit), ("Max Proportion:", qtw.QLabel)],
    "n_frags": [("n_frags", qtw.QLineEdit), ("# Fragment Peaks:", qtw.QLabel)],
    "n_draws": [("n_draws", qtw.QLineEdit), ("# Draws:", qtw.QLabel)],
    "alpha": [("alpha", qtw.QLineEdit), ("Alpha:", qtw.QLabel)],
    "base": [("base", qtw.QComboBox), ("Base:", qtw.QLabel)],
    # "mgf_file": [("mgf_file", QFileSelector), ("MGF File:", qtw.QLabel)],
    "max_peaks": [("max_peaks", qtw.QLineEdit), ("Max Peaks:", qtw.QLabel)],
    # "replace": [("replace", QTFButton), ("Replace:", qtw.QLabel)],
    "id_field": [("id_field", qtw.QLineEdit), ("ID of MGF:", qtw.QLabel)],
    # "mzml_file": [("mzml_file", QFileSelector), ("MZML File:", qtw.QLabel)],
    "min_n_peaks": [("min_n_peaks", qtw.QLineEdit), ("Min # Peaks:", qtw.QLabel)],
    # "with_replacement": [("with_replacement", QTFButton), ("Replace:", qtw.QLabel)],
}