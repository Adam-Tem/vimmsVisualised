from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import *

def create_widgets(selected_constructor, potential_params):

    if type(potential_params) == dict:
        params = identify_params(selected_constructor)
    elif type(potential_params) == str:
        if selected_constructor == "XCMS":
            return XCMS_PARAMS.values()
        elif selected_constructor == "MZMine":
            return MZMINE_PARAMS.values()
        else:
            return []

    widgets = []
    for param in params:
        if param not in INLINE_CONSTRUCTORS.keys():
            try:
                widgets.append(potential_params[param])
            except:
                pass
        else:
            widgets = widgets + create_widgets(param, INLINE_PARAMS)
    return widgets