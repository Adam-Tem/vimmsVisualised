from vimms.Controller import TopNController

import inspect

def identifyParams(selected_controller):
    try:
        string_to_constructor = {"TopN Controller": TopNController, }

        params = inspect.signature(string_to_constructor[selected_controller].__init__).parameters
        param_names = []

        for val in params:
            if val != "self":
                param_names.append(val)
    except:
        param_names = []
    return param_names

