from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from ExtractGeneratePage import Ui_ExtractGenerateForm

from Utils.ChangePage import *
from Utils.ExtractData import *
from vimmsVisualisedGUI.Utils.UploadFile import *
from Utils.Display.displayParams import *
from Utils.Parameters.ParamWidgets import *
from Utils.Generate.RunChemicalMixtureCreator import run_chemical_mixture_creator

class ExtractGeneratePage(qtw.QWidget, Ui_ExtractGenerateForm):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.fileName = ""
        self.fileLocation = ""
        self.min_intensity = 0

        self.ExtractHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        
        self.SelectFileButton.clicked.connect(lambda: upload_file(self, "mzml"))

        self.MinIntensityEdit.setText(str(self.min_intensity))

        self.ExtractDataButton.clicked.connect(lambda: extract_data(self, int(self.MinIntensityEdit.text()), self.fileLocation, self.fileName.split(".")[0]))
        self.GenerateDataButton.clicked.connect(lambda: run_chemical_mixture_creator(self))
        self.scrollArea.setWidgetResizable(True)

        self.FormulaSamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.FormulaSamplerParamBox,self.FormulaSamplerComboBox.currentText(),
                                  [False, ""], FORMULA_SAMPLERS, FORMULA_SAMPLER_PARAMS))
        self.RTISamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.RTISamplerParamBox,self.RTISamplerComboBox.currentText(),
                                  [False, ""], RTI_SAMPLERS, RTI_SAMPLER_PARAMS))
        self.ChromoSamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ChromoSamplerParamBox,self.ChromoSamplerComboBox.currentText(),
                                  [False, ""], CHROMO_SAMPLERS, CHROMO_SAMPLER_PARAMS))
        self.MS2SamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.MS2SamplerParamBox,self.MS2SamplerComboBox.currentText(),
                                  [False, ""], MS2_SAMPLERS, MS2_SAMPLER_PARAMS))
        