from Utils.Parameters.ParamWidgets import ROI_BUILDERS

def docstring_tooltip_parsing(constructor_name, constructor_type):

    constructor = constructor_type[constructor_name]
    docstring_param_desc = constructor.__init__.__doc__.split("\n")
    found_args = False
    param_desc_dict = {}
    for line in docstring_param_desc:
        if "Args:" in line:
            found_args = True
            continue
        if found_args:
            param_and_desc = line.split(":")
            if param_and_desc[0].strip() == "roi_params":
                roi_params = docstring_tooltip_parsing("roi_params", ROI_BUILDERS)
                param_desc_dict.update(roi_params)
            elif param_and_desc[0].strip() == "smartroi_params":
                smartroi_params = docstring_tooltip_parsing("smartroi_params", ROI_BUILDERS) 
                param_desc_dict.update(smartroi_params)
            elif param_and_desc[0].strip() == "advanced_params":
                print("Yep")
            if len(param_and_desc) == 2:
                param = param_and_desc[0].strip()
                desc = param_and_desc[1].strip()
                param_desc_dict[param] = desc
            else:
                param_desc_dict[param] = desc +" "+param_and_desc[0].strip()

    return param_desc_dict