from vimms.Chemicals import ChemicalMixtureCreator
from vimms.ChemicalSamplers import *

def GenerateData(self):

    formula_sampler = ""
    for i in range(1,6):
        button = getattr(self, "FormulaRadioButton" + str(i)) 
        if button.isChecked():
            formula_sampler = button.text()

    match formula_sampler:
        case "Pick Everything Formula Sampler":
            formula_sampler = PickEverythingFormulaSampler()
        case "Uniform MZ Formula Sampler":
            formula_sampler = UniformMZFormulaSampler()
        case "Even MZ Formula Sampler":
            formula_sampler = EvenMZFormulaSampler()
        case "MZML Formula Sampler":
            formula_sampler = MZMLFormulaSampler()
        case "Database Formula Sampler":
            formula_sampler = DatabaseFormulaSampler()

    match self.RTIComboBox.currentText():
        case "Uniform RT & Intensity":
            rti_sampler = UniformRTAndIntensitySampler()
        case "MZML RT & Intensity":
            rti_sampler = MZMLFormulaSampler()

    match self.ChromoComboBox.currentText():
        case "Gaussian":
            chrom_sampler = GaussianChromatogramSampler()
        case "Constant":
            chrom_sampler = ConstantChromatogram()
        case "MZML":
            chrom_sampler = MZMLChromatogramSampler()
    
    match self.MS2ComboBox.currentText():
        case "Uniform":
            ms2_sampler = UniformMS2Sampler()
        case "Fixed":
            ms2_sampler = FixedMS2Sampler()
        case "CRPM":
            ms2_sampler = CRPMS2Sampler()
        case "MGF":
            ms2_sampler = MGFMS2Sampler()
        case "Exact Match":
            ms2_sampler = ExactMatchMS2Sampler()
        case "MZML":
            ms2_sampler = MZMLMS2Sampler()

    adduct_cut_off = float(self.AdductPropTextEdit.text())
    cm = ChemicalMixtureCreator(formula_sampler, rti_sampler, chrom_sampler, ms2_sampler, adduct_cut_off)
    chemicals = cm.sample(int(self.ChemsToSampleTextEdit.text()), int(self.MS2LevelSpinBox.cleanText()))

    with open("generatedData.p", "w") as outfile:
        for chemical in chemicals:
            outfile.write(str(chemical) + "\n")