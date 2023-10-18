from PyQt5 import QtWidgets as qtw
from Utils.CustomWidgets import *

### ADD EXTRA PARAM TO EACH LIST, THAT WILL BE THE ASSOCIATED LABEL WITH 
### THAT INPUT VALUE. WORK OUT A WAY TO CONSTRUCT THIS IN THE FOR LOOP.
### WILL NEED TO ADD A MODIFICATION FOR WHEN IT IS ADVANCED PARAMS,
### ROI PARAMS, ETC.
PARAM_WIDGETS = {
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