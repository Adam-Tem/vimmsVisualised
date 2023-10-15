from Utils.Display.identifyParams import identifyParams
from Utils.Controllers.Parameters.ParamWidgets import PARAM_WIDGETS

def createWidgets(selected_controller):

    params = identifyParams(selected_controller)
    widgets = []
    for param in params:
        widgets.append(PARAM_WIDGETS[param])
    return widgets