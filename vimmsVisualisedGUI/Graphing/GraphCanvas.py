import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fcqt
from matplotlib.figure import Figure

class MplCanvas(fcqt):

    def __init__(self, parent):
        self.fig = Figure(figsize=(3, 3))
        self.axes = self.fig.add_subplot(111)
        self.canvas = fcqt(self.fig)
        self.canvas.setParent(parent)
        super(MplCanvas, self).__init__(self.fig)