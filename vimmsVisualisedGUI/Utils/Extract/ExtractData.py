from vimms.Common import  save_obj, POSITIVE, load_obj
from vimms.Roi import RoiBuilderParams
from vimms.Chemicals import ChemicalMixtureFromMZML
import os

from Utils.Parameters.ParamWidgets import ROI_BUILDERS

from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParseParams import parse_params
def extract_data(param_box,file_location, file_name, file_save_name):
            
            param_names = identify_params(RoiBuilderParams, ROI_BUILDERS)
            params = parse_params(param_box, param_names)
            roi = RoiBuilderParams(**params)
            cm = ChemicalMixtureFromMZML(mzml_file_name=file_name, roi_params=roi)
            dataset = cm.sample(None, 2)
            save_location = os.path.dirname(os.path.abspath(file_location)) + "/ExtracctedData"
            out_name = os.path.join(save_location, file_save_name + '.p')
            save_obj(dataset, out_name)