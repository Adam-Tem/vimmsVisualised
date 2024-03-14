from PyQt5 import QtWidgets as qtw

def get_associated_param_box(param_box, constructor_name):

    if "Formula" in constructor_name:
        return param_box.findChild(qtw.QGroupBox, "FormulaSamplerParamBox")
    elif "Intensity" in constructor_name:
        return param_box.findChild(qtw.QGroupBox, "RTISamplerParamBox")
    elif "Chromatogram" in constructor_name:
        return param_box.findChild(qtw.QGroupBox, "ChromoSamplerParamBox")
    else:
        return param_box.findChild(qtw.QGroupBox, "MS2SamplerParamBox")