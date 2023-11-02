from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

from VisualisePage import Ui_VisualiseForm
from Interfaces.GraphCanvas import MplCanvas
from Utils.UploadFile import upload_file

class VisualisePage(qtw.QWidget, Ui_VisualiseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        self.file_name = ""
        self.file_location = ""

        self.static_graph = MplCanvas(self.InteractTab)

        self.VisualiseHomeButton.setIcon(qtg.QIcon("Images/home.png"))
        self.SelectFileButton.clicked.connect(lambda: upload_file(self, "mzml"))
        self.VisualiseButton.clicked.connect(lambda: self.static_graph.scatterPlot(file_name=self.file_name, file_location=self.file_location))