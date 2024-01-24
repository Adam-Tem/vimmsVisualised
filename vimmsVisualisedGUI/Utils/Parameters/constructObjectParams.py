from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.ParamWidgets import INLINE_CONSTRUCTORS

def construct_object_params(object_name, param_box):

    object_param_names = identify_params(object_name)
    
    object_params = parse_params(param_box, object_param_names)
    for param in object_param_names:
        if param in INLINE_CONSTRUCTORS:
            object_params[param] = construct_object_params(param, param_box)

    return INLINE_CONSTRUCTORS[object_name](**object_params)