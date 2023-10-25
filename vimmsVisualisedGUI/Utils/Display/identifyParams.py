from Utils.Parameters.ParamWidgets import CONTROLLERS

import inspect

def identifyParams(selected_controller):

    param_names = []
    try:
        params = inspect.signature(CONTROLLERS[selected_controller].__init__).parameters
        
        for val in params:
            if val != "self":
                param_names.append(val)
    except:
        pass
    return param_names