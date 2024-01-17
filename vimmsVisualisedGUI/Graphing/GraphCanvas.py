from PyQt5 import QtCore as qtc
from PyQt5 import QtWidgets as qtw
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as fcqt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage

from matplotlib.figure import Figure

from plotly import graph_objects as go
from plotly.subplots import make_subplots
from plotly import graph_objects as go
from plotly.offline import plot as pop

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

class PlotlyCanvas(qtw.QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.view = QWebEngineView(self) 
        self.page = QWebEnginePage(self)
        self.view.settings().setDefaultTextEncoding("utf-8")
        self.graph_layout = qtw.QVBoxLayout()
        self.graph = make_subplots(rows=1, cols=1)
        self.scatter = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
        self.graph.add_trace(self.scatter)
        self.page.setHtml(self.graph.to_html())
        self.view.setPage(self.page)
        self.graph_layout.addWidget(self.view)
        self.resize(200,200)
        

    def update_html(self):
        self.view.setHtml(self.graph.to_html(include_plotlyjs='cdn', full_html=False))

    def new_graph(self, graph):
        self.graph = graph
        self.update_html()