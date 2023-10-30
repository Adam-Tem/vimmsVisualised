from vimms.Chemicals import ChemicalMixtureCreator
from vimms.ChemicalSamplers import *
from vimms.Common import save_obj

from Utils.Generate.SelectSamplers import *

def GenerateData(self):

    formula_sampler = select_formula_sampler(self.FormulaSamplerComboBox.currentText())
    rti_sampler = select_rti_sampler(self.RtiComboBox.currentText())
    chromo_sampler = select_chromo_sampler(self.ChromoComboBox.currentText())
    ms2_sampler = select_ms2_sampler(self.MS2ComboBox.currentText())
    
    adduct_cut_off = float(self.AdductPropTextEdit.text())
    cm = ChemicalMixtureCreator(formula_sampler, rti_sampler, chromo_sampler, ms2_sampler, adduct_cut_off)
    chemicals = cm.sample(int(self.ChemsToSampleTextEdit.text()), int(self.MS2LevelSpinBox.cleanText()))

    save_obj(chemicals,"generatedData.p")