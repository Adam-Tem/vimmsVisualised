from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from VisualisePage import Ui_VisualiseForm
from Graphing.graphCanvas import MplCanvas, PlotlyCanvas
from Graphing.createGraphLayout import create_graph_layout
from Utils.checkValidInputs import check_valid_inputs
from Utils.Display.addLoadingWidget import add_loading_widget
from Utils.Display.inputErrorPopUp import input_error_pop_up
from Utils.Display.taskedCompletedPopUp import task_completed_pop_up
from Utils.Index.indexMzml import index_mzml
from Utils.Index.indexExperiment import index_experiment
from Utils.Parameters.CustomWidgets import QMzmlUpload, QFolderUpload, QParamRangeSlider
from Utils.Threads.workerThreads import MzmlGraphWorker, ExpGraphWorker

class VisualisePage(qtw.QWidget, Ui_VisualiseForm):

    mzml_upload = qtc.pyqtSignal()
    update_mzml_visual = qtc.pyqtSignal(qtw.QLabel, MplCanvas, str, str, str, str, str, str, str)
    update_exp_visual = qtc.pyqtSignal(qtw.QLabel, list, qtw.QComboBox, qtw.QComboBox, str, str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        create_graph_layout(self)

        self.exp_figure = PlotlyCanvas(self.PlotlyCanvasGroupBox)
        self.exp_figure.show()

        self.rt_input = QParamRangeSlider(parent=self.RTSliderGroupBox)
        self.scan_input = QParamRangeSlider(parent=self.ScanSliderGroupBox)
        self.scan_input.range_slider.setSingleStep(1)
        self.scan_input.range_slider.setPageStep(1)
        
        self.current_tab_btn = self.MzmlVisualiseButton
        self.VisualisationTabs.currentChanged.connect(self.tab_changed)

        self.mzml_to_visualise_button = QMzmlUpload(parent=self)
        self.mzml_to_visualise_button.setObjectName("mzml_to_visualise_button")
        self.MzmlUploadGroupBox.setLayout(self.mzml_to_visualise_button.layout())

        self.exp_to_visualise_button = QFolderUpload(parent=self)
        self.exp_to_visualise_button.setObjectName("exp_to_visualise_button")
        self.ExpUploadGroupBox.setLayout(self.exp_to_visualise_button.layout())

        self.mzml_to_visualise_button.file_upload.connect(self.check_visual_inputs)
        self.mzml_to_visualise_button.file_upload.connect(self.set_slider_ranges)
        self.GraphTypeComboBox.currentIndexChanged.connect(self.check_visual_inputs)
        self.GraphTypeComboBox.currentIndexChanged.connect(self.set_slider_ranges)

        self.exp_to_visualise_button.file_upload.connect(self.index_experiment)

        self.ExpMzmlComboBox.currentIndexChanged.connect(self.check_visual_inputs)
        self.ExpMzmlRadioButton.clicked.connect(self.check_visual_inputs)
        self.TimingHistRadioButton.clicked.connect(self.check_visual_inputs)
        self.FragEventsRadioButton.clicked.connect(self.check_visual_inputs)

        self.VisualiseHomeButton.setIcon(qtg.QIcon("Images/home.png"))

        add_loading_widget(self.MzmlLoadingLabel)
        add_loading_widget(self.ExperimentLoadingLabel)

        self.VisualisationTabs.setStyleSheet("QTabWidget::pane { background-color: lightblue; }")

        self.mzml_worker = MzmlGraphWorker()
        self.mzml_worker_thread = qtc.QThread()
        self.mzml_worker.moveToThread(self.mzml_worker_thread)
        self.mzml_worker_thread.start()
        self.update_mzml_visual.connect(self.mzml_worker.run)
        self.mzml_worker.graphing_finished.connect(self.set_new_graph)

        self.exp_worker = ExpGraphWorker()
        self.exp_worker_thread = qtc.QThread()
        self.exp_worker.moveToThread(self.exp_worker_thread)
        self.exp_worker_thread.start()
        self.update_exp_visual.connect(self.exp_worker.run)
        self.exp_worker.graphing_finished.connect(self.set_new_graph)


        self.MzmlVisualiseButton.clicked.connect(
            lambda: (self.MzmlVisualiseButton.setEnabled(False),
                     self.update_mzml_visual.emit(self.MzmlLoadingLabel, self.canvas,
                                             self.mzml_to_visualise_button.file_location,
                                             self.mzml_to_visualise_button.file_name,
                                              self.GraphTypeComboBox.currentText(),
                                             self.rt_input.min_val_input.text(),
                                             self.rt_input.max_val_input.text(),
                                             self.scan_input.min_val_input.text(),
                                             self.scan_input.max_val_input.text()))
        )

        self.ExpVisualiseButton.clicked.connect(
            lambda: (self.ExpVisualiseButton.setEnabled(False),
                    self.update_exp_visual.emit(
                        self.ExperimentLoadingLabel,
                        [self.ExpMzmlRadioButton.isChecked(),
                         self.TimingHistRadioButton.isChecked(),
                         self.FragEventsRadioButton.isChecked()],
                         self.ExpMzmlComboBox,
                         self.ExpPklComboBox,
                         self.exp_to_visualise_button.file_location,
                         self.exp_to_visualise_button.file_name
                    )
                     )
        )

    @qtc.pyqtSlot()
    def check_visual_inputs(self):
            if self.VisualisationTabs.currentIndex() == 0:
                check_valid_inputs(self.current_tab_btn, 
                                   line_edits = [self.mzml_to_visualise_button.file_name],
                           combo_boxes = self.mzmlTab.findChildren(qtw.QComboBox))
            else:
                check_valid_inputs(self.current_tab_btn, 
                                   line_edits = [self.exp_to_visualise_button.file_name],
                           combo_boxes = self.experimentTab.findChildren(qtw.QComboBox))

        
    @qtc.pyqtSlot()
    def set_slider_ranges(self):
        if self.GraphTypeComboBox.currentText() != "---":
            if self.mzml_to_visualise_button.file_name != "":
                min_val, max_val, scans = index_mzml(self.mzml_to_visualise_button.file_location)
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

    @qtc.pyqtSlot()
    def index_experiment(self):
        index_experiment(self, self.exp_to_visualise_button.file_location)
        
    @qtc.pyqtSlot(str)
    def set_new_graph(self, response):
            
        if response == "Graphing finished":
            task_completed_pop_up("ViMMS Visual", "Graph visualisation update now complete!", 
                                    self.current_tab_btn)
            self.exp_figure.update_plot()
        else:
            input_error_pop_up(self.current_tab_btn)

    @qtc.pyqtSlot()
    def tab_changed(self):
        if self.VisualisationTabs.currentIndex() == 0:
            self.current_tab_btn = self.MzmlVisualiseButton
        else:
            self.current_tab_btn = self.ExpVisualiseButton