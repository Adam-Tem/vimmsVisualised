from vimms.Experiment import ExperimentCase

from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Experiment.controllerStringConversion import controller_string_conversion
from Utils.Parameters.ParamWidgets import *
from Utils.Experiment.updateLabel import update_label

def construct_experiment_case(self, controller_type, params_box, pickle_env, case_name, fullscan_list, geom):
    
    param_dict = parse_params(params_box, CONTROLLER_PARAMS)
    if controller_type == "TopN Smart ROI Controller":
        roi_param_names = identify_params("roi_params", ROI_BUILDERS)
        roi_params = parse_params(self, roi_param_names)
        roi = RoiBuilderParams(**roi_params)
        param_dict["roi_params"] = roi
    
    print(param_dict)
    adjusted_controller_name = controller_string_conversion(controller_type)
    experiment_case = ExperimentCase(adjusted_controller_name, fullscan_list, param_dict, case_name,
                                     pickle_env= pickle_env, grid_base=geom)
    
    self.experiment_case_list.append(experiment_case)
    text_label = self.ExperimentNamesScrollArea.findChild(qtw.QLabel, "ExperimentNamesLabel")
    scroll_area_contents = self.ExperimentNamesScrollArea.findChild(qtw.QWidget, "ScrollContents_2")
    update_label(scroll_area_contents, text_label, case_name, "experiment_case")