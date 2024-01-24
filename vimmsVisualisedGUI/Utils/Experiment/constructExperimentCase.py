from vimms.Experiment import ExperimentCase

from Utils.Parameters.ParamWidgets import *
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.constructObjectParams import construct_object_params
from Utils.Experiment.controllerStringConversion import controller_string_conversion
from Utils.Experiment.updateLabel import add_to_label

def construct_experiment_case(self, controller_type, params_box, pickle_env,
                              case_name, fullscan_list, advanced_params):
    
    param_dict = parse_params(params_box, CONTROLLER_PARAMS)
    param_dict["advanced_params"] = AdvancedParams(**advanced_params)
    if controller_type in CONTROLLERS_WITH_ROI_PARAMS:
        param_dict["roi_params"] = construct_object_params("roi_params", params_box)

    if controller_type in CONTROLLERS_WITH_SMART_ROI_PARAMS:
        param_dict["smartroi_params"] = construct_object_params("smartroi_params", params_box)
    
    if controller_type in CONTROLLERS_WITH_BOX_GRID:
        param_dict["grid"] = construct_object_params("grid", params_box)

    adjusted_controller_name = controller_string_conversion(controller_type)
    experiment_case = ExperimentCase(adjusted_controller_name, fullscan_list, param_dict, case_name,
                                     pickle_env= pickle_env)
    
    self.experiment_name_list.append(case_name)
    self.experiment_case_list.append(experiment_case)
    text_label = self.ExperimentNamesScrollArea.findChild(qtw.QLabel, "ExperimentNamesLabel")
    scroll_area_contents = self.ExperimentNamesScrollArea.findChild(qtw.QWidget, "ScrollContents_2")
    add_to_label(scroll_area_contents, text_label, case_name, "experiment_case")
    self.CaseUndoButton.setEnabled(True)