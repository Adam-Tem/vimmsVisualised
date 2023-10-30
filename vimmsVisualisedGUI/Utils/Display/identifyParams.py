import inspect

def identifyParams(selected_constructor, potential_constructors):

    param_names = []
    try:
        params = inspect.signature(potential_constructors[selected_constructor].__init__).parameters
        
        for val in params:
            if val != "self":
                param_names.append(val)
    except:
        pass
    return param_names