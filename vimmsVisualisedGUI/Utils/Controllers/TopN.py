from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import TopNController
from vimms.Environment import Environment
from vimms.Common import load_obj, set_log_level_warning, set_log_level_debug
from vimms.Controller.base import AdvancedParams

from Utils.LoadingWidget import *
from Utils.CheckInput import *
from Utils.CustomWidgets import *
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import CONTROLLERS

import os

def runTopNController(param_box, main_page, advanced_params):

    min_rt = int(main_page.min_rt.text())
    max_rt = int(main_page.max_rt.text())
    param_names = identify_params("TopN Controller", CONTROLLERS)
    params = parse_params(param_box, param_names)
    params["advanced_params"] = AdvancedParams(**advanced_params)
    print(main_page.file_location)
    dataset = load_obj(main_page.file_location)
    mass_spec = IndependentMassSpectrometer(params["ionisation_mode"], dataset)
    controller = TopNController(**params)
    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)

    set_log_level_warning()
    env.run()
    set_log_level_debug()
    mzml_filename =  main_page.OutputFileTextEdit.text() + ".mzML"
    out_dir = os.path.join(os.getcwd(), 'results')
    env.write_mzML(out_dir, mzml_filename)