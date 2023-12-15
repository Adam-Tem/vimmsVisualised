from Utils.Controllers.TopN import runTopNController
from Utils.Controllers.TopNSmartRoi import runTopNSmartRoiController

def controller_selection(param_box, controller, advanced_params):

    main_page = param_box.parent().parent().parent().parent()
    match controller:
        case "TopN Controller":
            runTopNController(param_box, main_page, advanced_params)
            
        case "TopN Smart ROI Controller":
            runTopNSmartRoiController(param_box, main_page, advanced_params)