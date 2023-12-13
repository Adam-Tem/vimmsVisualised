from vimms.Experiment import ExperimentCase

from Utils.Parameters.ParamWidgets import *
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.adjustForROIParams import adjust_for_roi_params
from Utils.Experiment.controllerStringConversion import controller_string_conversion
from Utils.Experiment.updateLabel import add_to_label

def construct_experiment_case(self, controller_type, params_box, pickle_env, case_name, fullscan_list, geom, advanced_params):
    
    param_dict = parse_params(params_box, CONTROLLER_PARAMS)
    param_dict["advanced_params"] = advanced_params
    include_smart_roi = False
    if controller_type in CONTROLLERS_WITH_ROI_PARAMS:
        if controller_type in CONTROLLERS_WITH_SMART_ROI_PARAMS:
            include_smart_roi = True
            roi, smart_roi = adjust_for_roi_params(self, include_smart_roi)
            param_dict["smartroi_params"] = smart_roi
        else:
            roi = adjust_for_roi_params(self, include_smart_roi)
        param_dict["roi_params"] = roi
    print(param_dict["advanced_params"].ms1_max_it)
    adjusted_controller_name = controller_string_conversion(controller_type)
    experiment_case = ExperimentCase(adjusted_controller_name, fullscan_list, param_dict, case_name,
                                     pickle_env= pickle_env, grid_base=geom)
    
    self.experiment_case_list.append(experiment_case)
    text_label = self.ExperimentNamesScrollArea.findChild(qtw.QLabel, "ExperimentNamesLabel")
    scroll_area_contents = self.ExperimentNamesScrollArea.findChild(qtw.QWidget, "ScrollContents_2")
    add_to_label(scroll_area_contents, text_label, case_name, "experiment_case")
    self.CaseUndoButton.setEnabled(True)