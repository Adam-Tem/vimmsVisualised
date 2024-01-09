from vimms.Roi import RoiBuilderParams, SmartRoiParams

from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParseParams import parse_params

def adjust_for_roi_params(self, include_smart_roi):

    roi_param_names = identify_params("roi_params")
    roi_params = parse_params(self, roi_param_names)
    roi = RoiBuilderParams(**roi_params)
    if include_smart_roi:
        smart_roi_param_names = identify_params("smartroi_params")
        smart_roi_params = parse_params(self, smart_roi_param_names)
        smart_roi = SmartRoiParams(**smart_roi_params)
        return roi, smart_roi
    return roi