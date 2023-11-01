


def get_associated_param_box(self, constructor_name):

    if "Formula" in constructor_name:
        return self.FormulaSamplerParamBox
    elif "Intensity" in constructor_name:
        return self.RTISamplerParamBox
    elif "Chromatogram" in constructor_name:
        return self.ChromoSamplerParamBox
    else:
        return self.MS2SamplerParamBox