import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fcqt
from matplotlib.figure import Figure

import numpy as np
from vimms.Common import path_or_mzml
from vimms.BoxVisualise import PlotPoints
import math
class MplCanvas(fcqt):

    def __init__(self, parent):
        self.fig = Figure(figsize=(6, 2))
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlabel(xlabel="RT (Seconds)", fontsize= 64) 
        self.canvas = fcqt(self.fig)
        self.canvas.setParent(parent)
        super(MplCanvas, self).__init__(self.fig)

    def scatterPlot(self, file_location = None, file_name = None, min_rt = None, max_rt = None):
        
        self.axes.cla()
        pp = PlotPoints.from_mzml(file_location)
        pp.mpl_add_ms2s(self.axes)
        self.axes.set(
            title=f"{file_name} Fragmentation Events", 
            ylabel="m/z",
        )
        self.canvas.draw()