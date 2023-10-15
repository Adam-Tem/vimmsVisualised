from PyQt5 import QtWidgets as qtw
from CustomWidgets import *

### ADD EXTRA PARAM TO EACH LIST, THAT WILL BE THE ASSOCIATED LABEL WITH 
### THAT INPUT VALUE. WORK OUT A WAY TO CONSTRUCT THIS IN THE FOR LOOP.
### WILL NEED TO ADD A MODIFICATION FOR WHEN IT IS ADVANCED PARAMS,
### ROI PARAMS, ETC.
PARAM_WIDGETS = {
    "ionisation_mode": [("IonModeButton", QIonModeButton), ("Ionisation Mode:", qtw.QLabel)],
    "N": [("NInput", qtw.QSpinBox), ("# of Injections:", qtw.QLabel)],
    "isolation_width": [("IsoWidthInput", qtw.QLineEdit), ("Isolation Width:", qtw.QLabel)],
    "mz_tol": [("MZToleranceInput", qtw.QLineEdit), ("MZ Tolerance:", qtw.QLabel)],
    "rt_tol": [("RTToleranceInput", qtw.QLineEdit), ("RT Tolerance", qtw.QLabel)],
    "min_ms1_intensity": [("MinMS1IntInput", qtw.QLineEdit), ("Min MS1 Intensity:", qtw.QLabel)],
    "ms1_shift": [("MS1ShiftInput", qtw.QLineEdit), ("MS1 Shift:", qtw.QLabel)],
    "initial_exclusion_list": [("InitialExclListInput", qtw.QLineEdit), ("Initial Exclusion:", qtw.QLabel)],
    "advanced_params": [("AdvancedParamsInput", qtw.QLineEdit), ("Advanced Params:", qtw.QLabel)],
    "force_N": [("ForceNInput", qtw.QLineEdit), ("Force N:", qtw.QLabel)]
}