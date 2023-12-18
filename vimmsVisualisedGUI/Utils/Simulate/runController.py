from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Environment import Environment
from vimms.Common import load_obj, set_log_level_warning, set_log_level_debug
from vimms.Controller.base import AdvancedParams
from vimms.Roi import RoiBuilderParams, SmartRoiParams

from Utils.CustomWidgets import *
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import CONTROLLERS, SAVE_DIRECTORY, ROI_BUILDERS
from Utils.Parameters.ParamWidgets import CONTROLLERS_WITH_ROI_PARAMS,CONTROLLERS_WITH_SMART_ROI_PARAMS

def run_controller(controller_name, file_location, min_rt, max_rt, param_box, 
                   output_filename , advanced_params):

    param_names = identify_params(controller_name, CONTROLLERS)
    params = parse_params(param_box, param_names)

    if controller_name in CONTROLLERS_WITH_ROI_PARAMS:
        roi_param_names = identify_params("roi_params", ROI_BUILDERS)
        roi_params = parse_params(param_box, roi_param_names)
        params["roi_params"] = RoiBuilderParams(**roi_params)

    if controller_name in CONTROLLERS_WITH_SMART_ROI_PARAMS:
        smartroi_param_names = identify_params("smartroi_params", ROI_BUILDERS)
        smartroi_params = parse_params(param_box, smartroi_param_names)
        params["smartroi_params"] = SmartRoiParams(**smartroi_params)
    
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
