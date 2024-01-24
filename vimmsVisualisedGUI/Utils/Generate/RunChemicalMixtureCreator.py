from PyQt5 import QtWidgets as qtw

from vimms.Chemicals import ChemicalMixtureCreator
from vimms.Common import save_obj

from Utils.Generate.getAssociatedParamBox import get_associated_param_box
from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import *

def run_chemical_mixture_creator(param_box, adduct_prop, chems_to_sample, ms2_level, file_name):

<<<<<<< HEAD
=======
    global save_directory

>>>>>>> 84f8a4c4993f6138f7d9b613ad41a8f79e35b62d
    constructed_params = {}
    sampler_type = ""
    for child_constructor in param_box.findChildren(qtw.QComboBox):
        for sampler in SAMPLERS:
            if child_constructor.accessibleName() == sampler[0]:
                sampler_type = sampler

        selected_constructor = child_constructor.currentText()
        child_param_box = get_associated_param_box(param_box, selected_constructor)
        if selected_constructor != "---":
<<<<<<< HEAD
            param_names = identify_params(selected_constructor)
            params = parse_params(child_param_box, param_names)
            constructed_params[sampler_type[0]] = sampler_type[1][selected_constructor](**params)
    
=======
            param_names = identify_params(selected_constructor, sampler_type[1])
            params = parse_params(child_param_box, param_names)
            print("\n")
            print(sampler_type[0])
            print(sampler_type[1])
            print(selected_constructor)
            print("\n")
            constructed_params[sampler_type[0]] = sampler_type[1][selected_constructor](**params)

>>>>>>> 84f8a4c4993f6138f7d9b613ad41a8f79e35b62d
    cm = ChemicalMixtureCreator(**constructed_params, adduct_proportion_cutoff=adduct_prop)
    chemicals = cm.sample(int(chems_to_sample), int(ms2_level))
    save_obj(chemicals, SAVE_DIRECTORY + "/generated_data/" + file_name + ".p")