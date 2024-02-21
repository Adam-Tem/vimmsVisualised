from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from ExtractGeneratePage import Ui_ExtractGenerateForm

from Utils.Display.displayParams import *
from Utils.Display.inputErrorPopUp import input_error_pop_up
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Extract.ExtractData import *
from Utils.Parameters.addElementsToComboBox import add_elements_to_combo_box
from Utils.Parameters.ParamWidgets import *
from Utils.UploadFile import *
from Utils.checkValidInputs import check_valid_inputs
from Utils.Threads.workerThreads import ExtractWorker, GenerateWorker

class ExtractGeneratePage(qtw.QWidget, Ui_ExtractGenerateForm):

    start_extract = qtc.pyqtSignal(qtw.QGroupBox, str, str, str)
    start_generate = qtc.pyqtSignal(qtw.QGroupBox, str, str, int, str)
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.ExtractHomeButton.setIcon(qtg.QIcon("Images/home.png"))

        self.extract_upload_button = QMzmlUpload(parent=self.MzmlUploadGroupBox)
        self.extract_upload_button.setObjectName("extract_upload_button")
        self.MzmlUploadGroupBox.setLayout(self.extract_upload_button.layout())
        self.extract_upload_button.file_upload.connect(self.check_extract_inputs)
        self.ExtractFileNameTextEdit.textChanged.connect(self.check_extract_inputs)

        self.FormulaSamplerComboBox.currentIndexChanged.connect(self.check_generate_inputs)
        self.RTISamplerComboBox.currentIndexChanged.connect(self.check_generate_inputs)
        self.ChromoSamplerComboBox.currentIndexChanged.connect(self.check_generate_inputs)
        self.MS2SamplerComboBox.currentIndexChanged.connect(self.check_generate_inputs)
        self.ChemsToSampleTextEdit.textChanged.connect(self.check_generate_inputs)
        self.AdductPropTextEdit.textChanged.connect(self.check_generate_inputs)
        self.GenerateFileNameTextEdit.textChanged.connect(self.check_generate_inputs)

        add_elements_to_combo_box(self.FormulaSamplerComboBox, FORMULA_SAMPLERS)
        add_elements_to_combo_box(self.ChromoSamplerComboBox, CHROMO_SAMPLERS)
        add_elements_to_combo_box(self.MS2SamplerComboBox, MS2_SAMPLERS)
        add_elements_to_combo_box(self.RTISamplerComboBox, RTI_SAMPLERS)

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

        self.ExtractDataButton.clicked.connect(lambda: (
                                        self.ExtractDataButton.setEnabled(False),

                                        self.start_extract.emit(self.ExtractParamBox, 
                                        self.extract_upload_button.file_name, 
                                        self.ExtractFileNameTextEdit.text(),
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
                                  FORMULA_SAMPLER_PARAMS, False))
        self.RTISamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.RTISamplerParamBox,self.RTISamplerComboBox.currentText(),
                                  RTI_SAMPLER_PARAMS, False))
        self.ChromoSamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.ChromoSamplerParamBox,self.ChromoSamplerComboBox.currentText(),
                                  CHROMO_SAMPLER_PARAMS, False))
        self.MS2SamplerComboBox.currentIndexChanged.connect(
            lambda: displayParams(self.MS2SamplerParamBox,self.MS2SamplerComboBox.currentText(),
                                  MS2_SAMPLER_PARAMS, False))
        
        self.tabWidget.tabBarClicked.connect(lambda: displayParams(self.ExtractParamBox, "roi_params",
                                  ROI_PARAMS, False))
        
    @qtc.pyqtSlot(str)
    def notify_extract_generate_finish(self, action):
        if action == "Extracted":
            task_completed_pop_up("ViMMS Extraction",
                                  "Current extraction now complete!\nOutput saved to: results/extracted_data",
                                  self.ExtractDataButton)
        elif action == "Extraction Failed":
            input_error_pop_up(self.ExtractDataButton)
        elif action == "Generated":
            task_completed_pop_up("ViMMS Generation",
                                  "Current generation now complete!\nOutput saved to: results/generated_data",
                                  self.GenerateDataButton)
        elif action == "Generation Failed":
            input_error_pop_up(self.GenerateDataButton)

    @qtc.pyqtSlot()
    def check_extract_inputs(self):
        check_valid_inputs(self.ExtractDataButton, line_edits = [self.extract_upload_button.file_name,
                                                self.ExtractFileNameTextEdit.text()])

    
    @qtc.pyqtSlot()
    def check_generate_inputs(self):
        check_valid_inputs(self.GenerateDataButton, line_edits = [self.AdductPropTextEdit.text(), 
                                                    self.ChemsToSampleTextEdit.text(),
                                                    self.GenerateFileNameTextEdit.text()],
                                                   combo_boxes = self.findChildren(qtw.QComboBox))