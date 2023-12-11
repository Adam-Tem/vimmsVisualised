from PyQt5 import QtCore as qtc

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as fcqt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navBar
from matplotlib.figure import Figure

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

class QNavBar(navBar):
    @qtc.pyqtSlot()
    def graph_change():
        pass