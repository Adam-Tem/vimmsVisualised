from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from VisualisePage import Ui_VisualiseForm
from Graphing.SelectGraphToPlot import select_graph_to_plot
from Graphing.createGraphLayout import create_graph_layout
from Utils.Parameters.CustomWidgets import QMzmlUpload

class VisualisePage(qtw.QWidget, Ui_VisualiseForm):

    mzml_upload = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        create_graph_layout(self)

        self.mzml_to_visualise_button = QMzmlUpload(parent=self)
        self.mzml_to_visualise_button.setObjectName("mzml_to_visualise_button")
        self.MzmlUploadGroupBox.setLayout(self.mzml_to_visualise_button.layout())
        self.mzml_to_visualise_button.mzml_upload.connect(self.check_mzml_file)

        self.VisualiseHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.VisualiseButton.clicked.connect(lambda: select_graph_to_plot(self, 
                                                                          self.GraphTypeComboBox.currentText()))
    @qtc.pyqtSlot(str)
    def check_mzml_file(self, file_name):
        if file_name == "":
            self.VisualiseButton.setEnabled(False)
        else:
            self.VisualiseButton.setEnabled(True)