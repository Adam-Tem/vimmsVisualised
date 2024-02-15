from vimms.Common import  save_obj
from vimms.Roi import RoiBuilderParams
from vimms.Chemicals import ChemicalMixtureFromMZML
import os

from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParseParams import parse_params
def extract_data(param_box,  file_name, file_save_name, save_directory):
            
            param_names = identify_params(RoiBuilderParams)
            params = parse_params(param_box, param_names)
            roi = RoiBuilderParams(**params)
            cm = ChemicalMixtureFromMZML(mzml_file_name=file_name, roi_params=roi)
            dataset = cm.sample(None, 2)
            save_location = os.path.join(save_directory, "extracted_data")
            out_name = os.path.join(save_location, file_save_name + '.p')
            save_obj(dataset, out_name)