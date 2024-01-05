from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from VisualisePage import Ui_VisualiseForm
from Graphing.GraphCanvas import MplCanvas
from Graphing.createGraphLayout import create_graph_layout
from Utils.checkValidInputs import check_valid_inputs
from Utils.Display.inputErrorPopUp import input_error_pop_up
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Index.indexMzml import index_mzml
from Utils.Parameters.CustomWidgets import QMzmlUpload, QParamRangeSlider
from Utils.Threads.workerThreads import GraphWorker

class VisualisePage(qtw.QWidget, Ui_VisualiseForm):

    mzml_upload = qtc.pyqtSignal()
    update_visual = qtc.pyqtSignal(MplCanvas, str, str, str, str, str, str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        create_graph_layout(self)

        self.rt_input = QParamRangeSlider(parent=self.RTSliderGroupBox)
        self.scan_input = QParamRangeSlider(parent=self.ScanSliderGroupBox)
        self.scan_input.range_slider.setSingleStep(1)
        self.scan_input.range_slider.setPageStep(1)
        self.mzml_to_visualise_button = QMzmlUpload(parent=self)
        self.mzml_to_visualise_button.setObjectName("mzml_to_visualise_button")
        self.MzmlUploadGroupBox.setLayout(self.mzml_to_visualise_button.layout())
        self.mzml_to_visualise_button.file_upload.connect(self.check_visual_inputs)
        self.mzml_to_visualise_button.file_upload.connect(self.set_slider_ranges)
        self.GraphTypeComboBox.currentIndexChanged.connect(self.check_visual_inputs)
        self.GraphTypeComboBox.currentIndexChanged.connect(self.set_slider_ranges)

        self.VisualiseHomeButton.setIcon(qtg.QIcon("Images/home.png"))

        self.worker = GraphWorker()
        self.worker_thread = qtc.QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.update_visual.connect(self.worker.run)
        self.worker.graphing_finished.connect(self.set_new_graph)

        self.VisualiseButton.clicked.connect(
            lambda: (self.VisualiseButton.setEnabled(False),
                     self.update_visual.emit(self.canvas,
                                             self.mzml_to_visualise_button.file_location,
                                             self.mzml_to_visualise_button.file_name,
                                              self.GraphTypeComboBox.currentText(),
                                             self.rt_input.min_val_input.text(),
                                             self.rt_input.max_val_input.text(),
                                             self.scan_input.min_val_input.text(),
                                             self.scan_input.max_val_input.text()))
        )

    @qtc.pyqtSlot()
    def check_visual_inputs(self):
        check_valid_inputs(self.VisualiseButton, line_edits = [self.mzml_to_visualise_button.file_name],
                           combo_boxes = self.findChildren(qtw.QComboBox))
        
    @qtc.pyqtSlot()
    def set_slider_ranges(self):
        if self.GraphTypeComboBox.currentText() != "---":
            if self.mzml_to_visualise_button.file_name != "":
                min_val, max_val, scans = index_mzml(self.mzml_to_visualise_button.file_location, "rt")
                self.rt_input.set_vals(min_val, max_val)
                if self.GraphTypeComboBox.currentText() == "3d Bar Plot":
                    self.scan_input.set_vals(0, scans)
                else:
                    self.scan_input.disable_slider()
            else:
                self.rt_input.disable_slider()
                self.scan_input.disable_slider()
        else:
            self.rt_input.disable_slider()
            self.scan_input.disable_slider()
        
    @qtc.pyqtSlot(str)
    def set_new_graph(self, response):
        if response == "Graphing finished":
            task_completed_pop_up("ViMMS Visual", "Graph visualisation update now complete!", 
                                  self.VisualiseButton)
        else:
            input_error_pop_up(self.VisualiseButton)