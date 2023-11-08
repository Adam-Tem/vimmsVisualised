import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fcqt
from matplotlib.figure import Figure

class MplCanvas(fcqt):

    def __init__(self, parent = None):
        self.fig = Figure(figsize=(1, 1), layout="constrained")
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlabel("RT (s)")
        self.axes.set_ylabel("m/z")
        self.canvas = fcqt(self.fig)
        self.canvas.setParent(parent)

        
        super(MplCanvas, self).__init__(self.fig)