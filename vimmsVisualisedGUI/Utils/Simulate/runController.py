from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Environment import Environment
from vimms.Common import load_obj, set_log_level_warning, set_log_level_debug
from vimms.Controller.base import AdvancedParams

from Utils.Parameters.constructObjectParams import construct_object_params
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import *

import os

def run_controller(controller_name, file_location, min_rt, max_rt, param_box, 
                   output_filename , advanced_params):

    param_names = identify_params(controller_name)
    params = parse_params(param_box, param_names)

    if controller_name in CONTROLLERS_WITH_ROI_PARAMS:
        params["roi_params"] = construct_object_params("roi_params", param_box)

    if controller_name in CONTROLLERS_WITH_SMART_ROI_PARAMS:
        params["smartroi_params"] = construct_object_params("smartroi_params", param_box)
    
    if controller_name in CONTROLLERS_WITH_BOX_GRID:
        params["grid"] = construct_object_params("grid", param_box)
    
    params["advanced_params"] = AdvancedParams(**advanced_params)

    dataset = load_obj(file_location)
    mass_spec = IndependentMassSpectrometer(params["ionisation_mode"], dataset)
    controller = CONTROLLERS[controller_name](**params)
    
    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)

    set_log_level_warning()
    env.run()
    set_log_level_debug()
    mzml_filename = output_filename + ".mzML"
    out_dir = os.path.join(SAVE_DIRECTORY, 'simulations')
    env.write_mzML(out_dir, mzml_filename)