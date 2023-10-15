from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import TopNController
from vimms.Environment import Environment
from vimms.Common import POSITIVE, NEGATIVE, load_obj, set_log_level_warning, set_log_level_debug

from Utils.LoadingWidget import *
from Utils.CheckInput import *
from CustomWidgets import *

import inspect
import os

def runTopNController(self):

    min_rt = 0
    max_rt = 100
    params = []
    for child in self.ParamsBox.findChildren(qtw.QWidget):
        if type(child) == QIonModeButton:
            if child.text() == "positive":
                params.append(POSITIVE)
            else:
                params.append(NEGATIVE)
            continue
        if child.text() == "Simulate":
            continue
        if len(child.text()) > 0 and type(child) != qtw.QLabel:
            params.append(float(child.text()))

    dataset = load_obj(self.fileLocation)

    mass_spec = IndependentMassSpectrometer(params[0], dataset)
    controller = TopNController(*params)
    print("hello?", inspect.signature(controller.__init__).parameters)

    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)

    set_log_level_warning()
    env.run()
    set_log_level_debug()
    mzml_filename = 'topn_controller.mzML'
    out_dir = os.path.join(os.getcwd(), 'results')
    env.write_mzML(out_dir, mzml_filename)