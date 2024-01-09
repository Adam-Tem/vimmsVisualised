from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import *

def create_widgets(selected_constructor, potential_params):

    params = identify_params(selected_constructor)

    widgets = []
    for param in params:
        if param not in INLINE_CONSTRUCTORS.keys():
            try:
                ##ONLY HERE FOR FIXED DISTANCE PARAMS ATM.
                widgets.append(potential_params[param])
            except:
                pass
        else:
            widgets = widgets + create_widgets(param, INLINE_PARAMS)
    return widgets


