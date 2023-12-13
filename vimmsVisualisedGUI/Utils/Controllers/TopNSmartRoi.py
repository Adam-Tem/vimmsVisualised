from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import TopN_SmartRoiController
from vimms.Environment import Environment
from vimms.Common import load_obj, set_log_level_warning, set_log_level_debug
from vimms.Roi import RoiBuilderParams, SmartRoiParams
from vimms.Controller.base import AdvancedParams

from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.ParamWidgets import ROI_BUILDERS, CONTROLLERS
import os

def runTopNSmartRoiController(self, main_page, advanced_params):

    min_rt = int(main_page.min_rt.text())
    max_rt = int(main_page.max_rt.text())

    roi_param_names = identify_params("roi_params", ROI_BUILDERS)
    
    roi_params = parse_params(self, roi_param_names)

    smartroi_param_names = identify_params("smartroi_params", ROI_BUILDERS)
    smartroi_params = parse_params(self, smartroi_param_names)
    if "drop_perc" in smartroi_params:
        smartroi_params["drop_perc"] = smartroi_params["drop_perc"] / 100

    topN_smartroi_param_names = identify_params("TopN Smart ROI Controller", CONTROLLERS)
    topN_smartroi_param_names.remove("roi_params")
    topN_smartroi_param_names.remove("smartroi_params")
    params = parse_params(self, topN_smartroi_param_names)

    roi = RoiBuilderParams(**roi_params)
    smartroi = SmartRoiParams(**smartroi_params)
    params["advanced_params"] = AdvancedParams(**advanced_params)
    dataset = load_obj(main_page.file_location)
    mass_spec = IndependentMassSpectrometer(params["ionisation_mode"], dataset)
    controller = TopN_SmartRoiController(**params, roi_params=roi, smartroi_params=smartroi)
    
    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)

    set_log_level_warning()
    env.run()
    set_log_level_debug()
    mzml_filename = main_page.OutputFileTextEdit.text() + ".mzML"
    out_dir = os.path.join(os.getcwd(), 'results')
    env.write_mzML(out_dir, mzml_filename)
