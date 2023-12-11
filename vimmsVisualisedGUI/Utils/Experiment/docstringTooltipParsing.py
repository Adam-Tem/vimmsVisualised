from Utils.Parameters.ParamWidgets import CONTROLLERS

def docstring_tooltip_parsing(controller_name):

    controller_object = CONTROLLERS[controller_name]
    docstring_param_desc = controller_object.__init__.__doc__.split("\n")
    found_args = False
    param_desc_dict = {}
    for line in docstring_param_desc:
        if "Args:" in line:
            found_args = True
            continue
        if found_args:
            param_and_desc = line.split(":")
            if len(param_and_desc) == 2:
                param = param_and_desc[0].strip()
                desc = param_and_desc[1].strip()
                param_desc_dict[param] = desc
            else:
                param_desc_dict[param] = desc +" "+param_and_desc[0].strip()

    return param_desc_dict