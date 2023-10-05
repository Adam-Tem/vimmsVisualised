from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import TopNController
from vimms.Environment import Environment
from vimms.Common import POSITIVE, NEGATIVE, load_obj, set_log_level_warning, set_log_level_debug

import os

def RunTopNController(self):

    dataset = load_obj(self.fileLocation)

    charge = self.IonModeButton.text()
    if self.IonModeButton.text() == "positive":
        charge = POSITIVE
    else:
        charge = NEGATIVE

    isolation_window = int(self.IsolWidthTextEdit.text())
    n = int(self.NoOfInjectionsSpinBox.text())
    rt_tol = int(self.RTTolTextEdit.text())
    mz_tol = int(self.MZTolTextEdit.text())
    min_ms1_intensity = float(self.MinMS1TextEdit.text())
    min_rt = int(self.RTRangeMinTextEdit.text())
    max_rt = int(self.RTRangeMaxTextEdit.text())

    mass_spec = IndependentMassSpectrometer(charge, dataset)
    controller = TopNController(charge, n, isolation_window, mz_tol, rt_tol, min_ms1_intensity)

    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)
    set_log_level_warning()
    env.run()

    set_log_level_debug()
    mzml_filename = 'topn_controller.mzML'
    out_dir = os.path.join(os.getcwd(), 'results')
    env.write_mzML(out_dir, mzml_filename)