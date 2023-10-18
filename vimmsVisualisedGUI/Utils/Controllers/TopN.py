from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import TopNController
from vimms.Environment import Environment
from vimms.Common import POSITIVE, NEGATIVE, load_obj, set_log_level_warning, set_log_level_debug

from Utils.LoadingWidget import *
from Utils.CheckInput import *
from Utils.Parameters.ParseParams import parseParams
from Utils.CustomWidgets import *
from Utils.Display.identifyParams import identifyParams

import os

def runTopNController(self):

    min_rt = 0
    max_rt = 100
    param_names = identifyParams("TopN Controller")
    params = parseParams(self, param_names)
    
    dataset = load_obj(self.fileLocation)
    mass_spec = IndependentMassSpectrometer(params["ionisation_mode"], dataset)
    controller = TopNController(**params)
    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)

    set_log_level_warning()
    env.run()
    set_log_level_debug()
    mzml_filename = 'topn_controller.mzML'
    out_dir = os.path.join(os.getcwd(), 'results')
    env.write_mzML(out_dir, mzml_filename)