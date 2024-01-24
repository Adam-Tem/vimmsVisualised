from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as fcqt
from PyQt5.QtWebEngineWidgets import QWebEngineView

from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY
from matplotlib.figure import Figure


def seeError(num, val):
    print("Hello")
    print(num, val)

def start():
    print("started")

def sc():
    print("sc")


class MplCanvas(fcqt):
    canvas_changed = qtc.pyqtSignal()

    def __init__(self, parent = None):
        self.fig = Figure(figsize=(4, 1), layout="constrained")
        self.fig.set_constrained_layout_pads(w_pad = 0.3, h_pad = 0.2)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlabel("RT (s)")
        self.axes.set_ylabel("m/z")
        self.canvas = fcqt(self.fig)
        self.canvas.setParent(parent)

        super(MplCanvas, self).__init__(self.fig)

import os    
class PlotlyCanvas(QWebEngineView):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.resize(400,315)

    def update_plot(self):
        self.setUrl(qtc.QUrl.fromLocalFile(os.path.join(SAVE_DIRECTORY, "temp-plot.html")))