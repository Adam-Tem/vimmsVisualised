from Utils.Parameters.ParamWidgets import ALL_CONSTRUCTORS

import inspect

def identify_params(selected_constructor):

    param_names = []
    try:
        params = inspect.signature(ALL_CONSTRUCTORS[selected_constructor].__init__).parameters
        for val in params:
            if val != "self" and val != "args" and val != "kwargs" and val != "advanced_params":
                param_names.append(val)
    except:
        pass
    return param_names