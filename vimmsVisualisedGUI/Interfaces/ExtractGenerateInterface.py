from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from ExtractGeneratePage import Ui_ExtractGenerateForm

from Utils.Display.displayParams import *
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Extract.ExtractData import *
from Utils.Parameters.ParamWidgets import *
from Utils.UploadFile import *
from Utils.Threads.workerThreads import ExtractWorker, GenerateWorker

class ExtractGeneratePage(qtw.QWidget, Ui_ExtractGenerateForm):

    start_extract = qtc.pyqtSignal(qtw.QGroupBox, str, str, str, str)
    start_generate = qtc.pyqtSignal(qtw.QGroupBox, str, str, int, str)
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.file_name = ""
        self.file_location = ""

        self.ExtractHomeButton.setIcon(qtg.QIcon("Images/home.png"))

        self.extract_worker = ExtractWorker()
        self.generate_worker = GenerateWorker()
        self.worker_thread_1 = qtc.QThread()
        self.worker_thread_2 = qtc.QThread()
        self.extract_worker.moveToThread(self.worker_thread_1)
        self.generate_worker.moveToThread(self.worker_thread_2)
        self.worker_thread_1.start()
        self.worker_thread_2.start()
        self.start_extract.connect(self.extract_worker.run)
        self.start_generate.connect(self.generate_worker.run)
        self.extract_worker.extract_finished.connect(self.notify_extract_generate_finish)
        self.generate_worker.generate_finished.connect(self.notify_extract_generate_finish)

        self.SelectFileButton.clicked.connect(lambda: upload_file(self, "mzml"))

        self.ExtractDataButton.clicked.connect(lambda: (
                                        self.ExtractDataButton.setEnabled(False),
                                        self.start_extract.emit(self.ExtractParamBox, self.file_location,
                                        self.file_name, self.ExtractFileNameTextEdit.text(),
                                        SAVE_DIRECTORY))
                                        )
        
        self.GenerateDataButton.clicked.connect(lambda: (
                                        self.GenerateDataButton.setEnabled(False),
                                        self.start_generate.emit(
                                        self.ParamBox, self.AdductPropTextEdit.text(), 
                                        self.ChemsToSampleTextEdit.text(),
                                        self.MS2LevelSpinBox.value(), self.GenerateFileNameTextEdit.text())))
        self.scrollArea.setWidgetResizable(True)

        self.FormulaSamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.FormulaSamplerParamBox,self.FormulaSamplerComboBox.currentText(),
                                  FORMULA_SAMPLERS, FORMULA_SAMPLER_PARAMS, False))
        self.RTISamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.RTISamplerParamBox,self.RTISamplerComboBox.currentText(),
                                  RTI_SAMPLERS, RTI_SAMPLER_PARAMS, False))
        self.ChromoSamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ChromoSamplerParamBox,self.ChromoSamplerComboBox.currentText(),
                                  CHROMO_SAMPLERS, CHROMO_SAMPLER_PARAMS, False))
        self.MS2SamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.MS2SamplerParamBox,self.MS2SamplerComboBox.currentText(),
                                  MS2_SAMPLERS, MS2_SAMPLER_PARAMS, False))
        
        self.tabWidget.tabBarClicked.connect(lambda: displayParams(self.ExtractParamBox, "roi_params",
                                  ROI_BUILDERS, ROI_PARAMS, False))
        
    @qtc.pyqtSlot(str)
    def notify_extract_generate_finish(self, action):
        if action == "Extracted":
            self.ExtractDataButton.setEnabled(True)
            task_completed_pop_up("ViMMS Extraction", "Current extraction now complete!")
        else:
            self.GenerateDataButton.setEnabled(True)
            task_completed_pop_up("ViMMS Generation", "Current generation now complete!")
        