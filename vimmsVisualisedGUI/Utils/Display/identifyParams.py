from vimms.Controller import TopNController, TopN_SmartRoiController
from vimms.Roi import RoiBuilderParams, SmartRoiParams

import inspect

def identifyParams(selected_controller):

    param_names = []
    try:
        string_to_constructor = {"TopN Controller": TopNController, 
                                 "TopN Smart ROI Controller": TopN_SmartRoiController,
                                 "roi_params": RoiBuilderParams,
                                 "smartroi_params": SmartRoiParams,}
        params = inspect.signature(string_to_constructor[selected_controller].__init__).parameters
        
        for val in params:
            if val != "self":
                param_names.append(val)
    except:
        pass
    return param_names

