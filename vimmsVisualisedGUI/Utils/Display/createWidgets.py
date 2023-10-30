from Utils.Display.identifyParams import identifyParams
from Utils.Parameters.ParamWidgets import *

def createWidgets(selected_constructor, potential_constructors, potential_params):

    params = identifyParams(selected_constructor, potential_constructors)
    inline_constructors = {"roi_params": ROI_PARAMS, "smartroi_params": SMART_ROI_PARAMS}
    widgets = []
    for param in params:
        try:
            widgets.append(potential_params[param])
        except:
            inline_constructor_params = identifyParams(param, ROI_BUILDERS)

            for inline_param in inline_constructor_params:
                if inline_param not in params:
                    widgets.append(inline_constructors[param][inline_param])
    return widgets