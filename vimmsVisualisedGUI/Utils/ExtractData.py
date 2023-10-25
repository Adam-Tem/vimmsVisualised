from vimms.Common import  save_obj, POSITIVE, load_obj
from vimms.Roi import RoiBuilderParams
from vimms.Chemicals import ChemicalMixtureFromMZML
import os
def extract_data(self, min_roi_intensity, file_location, file_name):
            rp = RoiBuilderParams(min_roi_intensity)
            cm = ChemicalMixtureFromMZML(file_location, roi_params=rp)
            dataset = cm.sample(None, 2)
            save_location = os.path.dirname(os.path.abspath(file_location)) + "/ExtracctedData"
            out_name = os.path.join(save_location, file_name + '.p')
            save_obj(dataset, out_name)
            self.ExtractCompleteLabel.setText("Extraction Complete! Find result in Extracted Data folder.")
            self.ExtractCompleteLabel.setStyleSheet("background-color: green; color: white;")