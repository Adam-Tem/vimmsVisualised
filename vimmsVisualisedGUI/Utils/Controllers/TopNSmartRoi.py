from vimms.MassSpec import IndependentMassSpectrometer
from vimms.Controller import TopN_SmartRoiController
from vimms.Environment import Environment
from vimms.Common import POSITIVE, NEGATIVE, load_obj, set_log_level_warning, set_log_level_debug
from vimms.Roi import RoiBuilderParams, SmartRoiParams

import os

def runTopNSmartRoiController(self):

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
    min_rt = int(self.RTMinTextEdit.text())
    max_rt = int(self.RTMaxTextEdit.text())

    roi_params = RoiBuilderParams(int(self.MZTolTextEdit.text()), int(self.MinROILengthTextEdit.text()),
                                int(self.MinROIIntTextEdit.text()), int(self.OnePointAboveTextEdit.text()),
                                int(self.StartRTTextEdit.text()), int(self.StopRTTextEdit.text()),
                                int(self.MaxGapsTextEdit.text()))
    
    smartroi_params = SmartRoiParams(int(self.InitialLengthTextEdit.text()), int(self.ResetLengthTextEdit.text()),
                                int(self.IntFacTextEdit.text()), int(self.DEWTextEdit.text()),
                                float(self.DropPercentTextEdit.text())/100)

    mass_spec = IndependentMassSpectrometer(POSITIVE, dataset)
    controller = TopN_SmartRoiController(charge, isolation_window, n, mz_tol, rt_tol, 
                                     min_ms1_intensity, roi_params, smartroi_params)
    
    env = Environment(mass_spec, controller, min_rt, max_rt, progress_bar=True)

    set_log_level_warning()
    env.run()
    set_log_level_debug()
    mzml_filename = 'topNSmartROI_controller.mzML'
    out_dir = os.path.join(os.getcwd(), 'results')
    env.write_mzML(out_dir, mzml_filename)
