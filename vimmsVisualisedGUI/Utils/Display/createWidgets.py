from Utils.Display.identifyParams import identifyParams
from Utils.Parameters.ParamWidgets import *

def createWidgets(selected_controller):

    params = identifyParams(selected_controller)
    inline_constructors = {"roi_params": ROI_PARAMS, "smartroi_params": SMART_ROI_PARAMS}
    widgets = []
    for param in params:
        try:
            widgets.append(PARAM_WIDGETS[param])
        except:
            inline_constructor_params = identifyParams(param)
            for inline_param in inline_constructor_params:
                if inline_param not in params:
                    widgets.append(inline_constructors[param][inline_param])
    return widgets