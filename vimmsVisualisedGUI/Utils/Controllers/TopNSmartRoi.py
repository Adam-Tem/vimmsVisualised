from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import TopN_SmartRoiController
from vimms.Environment import Environment
from vimms.Common import POSITIVE, NEGATIVE, load_obj, set_log_level_warning, set_log_level_debug
from vimms.Roi import RoiBuilderParams, SmartRoiParams

from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParseParams import parse_params
import os

def runTopNSmartRoiController(self):

    min_rt = int(self.min_rt.text())
    max_rt = int(self.max_rt.text())

    roi_param_names = identify_params("roi_params")
    
    roi_params = parse_params(self, roi_param_names)

    smartroi_param_names = identify_params("smartroi_params")
    smartroi_params = parse_params(self, smartroi_param_names)
    if "drop_perc" in smartroi_params:
        smartroi_params["drop_perc"] = smartroi_params["drop_perc"] / 100

    topN_smartroi_param_names = identify_params("TopN Smart ROI Controller")
    topN_smartroi_param_names.remove("roi_params")
    topN_smartroi_param_names.remove("smartroi_params")
    kwargs = parse_params(self, topN_smartroi_param_names)

    roi = RoiBuilderParams(**roi_params)
    smartroi = SmartRoiParams(**smartroi_params)

    dataset = load_obj(self.fileLocation)
    mass_spec = IndependentMassSpectrometer(POSITIVE, dataset)
    controller = TopN_SmartRoiController(**kwargs, roi_params=roi, smartroi_params=smartroi)
    
    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)

    set_log_level_warning()
    env.run()
    set_log_level_debug()
    mzml_filename = 'topNSmartROI_controller.mzML'
    out_dir = os.path.join(os.getcwd(), 'results')
    env.write_mzML(out_dir, mzml_filename)
