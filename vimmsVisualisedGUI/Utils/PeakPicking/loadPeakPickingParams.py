from vimms.PeakPicking import XCMSScriptParams, MZMineParams

import json
import os

def load_peak_picking_param(pp_type, passed_pp_params):
    with open('userData.json', 'r') as file:
        installs = json.load(file)
    
    if pp_type == "XCMS":
        return XCMSScriptParams(
    xcms_r_script = os.path.join(os.getcwd(), "xcms_script.R"), 
    rscript_exe= installs["R"],
    **passed_pp_params
    )
    else:
        return MZMineParams(
            **passed_pp_params,
            mzmine_exe=installs["MZMine"]
        )