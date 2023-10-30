from Utils.Controllers.TopN import runTopNController
from Utils.Controllers.TopNSmartRoi import runTopNSmartRoiController

def controllerSelection(param_box, controller):

    main_page = param_box.parent()
    match controller:
        case "TopN Controller":
            runTopNController(param_box, main_page)
            
        case "TopN Smart ROI Controller":
            runTopNSmartRoiController(param_box, main_page)