from vimms.ChemicalSamplers import *

def select_formula_sampler(selection):
    match selection:
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
    
    return formula_sampler

def select_rti_sampler(selection):
    match selection:
        case "Uniform RT & Intensity":
            rti_sampler = UniformRTAndIntensitySampler()
        case "MZML RT & Intensity":
            rti_sampler = MZMLRTandIntensitySampler()
    
    return rti_sampler

def select_chromo_sampler(selection):
    match selection:
        case "Gaussian":
            chrom_sampler = GaussianChromatogramSampler()
        case "Constant":
            chrom_sampler = ConstantChromatogram()
        case "MZML":
            chrom_sampler = MZMLChromatogramSampler()
    
    return chrom_sampler

def select_ms2_sampler(selection):
    match selection:
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

    return ms2_sampler