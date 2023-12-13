import inspect

def identify_params(selected_constructor, potential_constructors):

    param_names = []
    try:
        params = inspect.signature(potential_constructors[selected_constructor].__init__).parameters
        
        for val in params:
            if val != "self" and val != "args" and val != "kwargs" and val != "advanced_params":
                param_names.append(val)
    except:
        pass
    return param_names