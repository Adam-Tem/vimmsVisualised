from PyQt5 import QtWidgets as qtw

from vimms.Chemicals import ChemicalMixtureCreator
from vimms.Common import save_obj

from Utils.Parameters.ParseParams import parse_params
from Utils.Parameters.identifyParams import identify_params
from Utils.Parameters.ParamWidgets import *
from Utils.Generate.getAssociatedParamBox import get_associated_param_box

def run_chemical_mixture_creator(self):
    param_space = self.ParamBox
    constructed_params = {}
    sampler_types = []
    ## Just find a way to iterate over all the boxes in order.
    ## Just make a function that checks to see if a certain part of the string
    ## is in the constructor combobox text and return the right param_box.
    
    for child_constructor, sampler_type in zip(param_space.findChildren(qtw.QComboBox), 
                                               SAMPLERS):
        
        selected_constructor = child_constructor.currentText()
        child_param_box = get_associated_param_box(self, selected_constructor)
        if selected_constructor != "---":
            param_names = identify_params(selected_constructor, sampler_type[1])
            params = parse_params(child_param_box, param_names)
            print(params)
            constructed_params[sampler_type[0]] = sampler_type[1][selected_constructor](**params)

    cm = ChemicalMixtureCreator(**constructed_params, adduct_proportion_cutoff=self.AdductPropTextEdit.text())
    chemicals = cm.sample(int(self.ChemsToSampleTextEdit.text()), int(self.MS2LevelSpinBox.cleanText()))
    save_obj(chemicals,"generatedData.p")
    ## get spin box constructors.
    ####Use identify params?
    ## construct from params.
    ## pass to mixture creator.

    