from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from VisualisePage import Ui_VisualiseForm
from Graphing.GraphCanvas import MplCanvas
from Graphing.SelectGraphToPlot import select_graph_to_plot
from Utils.UploadFile import upload_file

class VisualisePage(qtw.QWidget, Ui_VisualiseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.file_name = ""
        self.file_location = ""

        self.canvas = MplCanvas(self.CanvasGroupBox)

        self.VisualiseHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.SelectFileButton.clicked.connect(lambda: upload_file(self, "mzml"))
        self.VisualiseButton.clicked.connect(lambda: select_graph_to_plot(self, self.GraphTypeComboBox.currentText()))