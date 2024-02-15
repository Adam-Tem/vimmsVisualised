from Utils.Parameters.ParamWidgets import *

def check_controller_params(constructor_params, possible_params, param_box):
    all_params_created = True
    for param in constructor_params:
        if param in possible_params.keys():
            if param_box.findChild(qtw.QWidget, param):
                continue  
            else:
                if param == "roi_params":
                    all_params_created = check_controller_params(constructor_params, 
                                                                    ROI_PARAMS, param_box)
                    if not all_params_created:
                        return all_params_created
                    
                elif param == "smartroi_params":
                    all_params_created = check_controller_params(constructor_params, 
                                                                    SMART_ROI_PARAMS, param_box)
                    if not all_params_created:
                        return all_params_created
                else:
                    all_params_created = False
                
    return all_params_created