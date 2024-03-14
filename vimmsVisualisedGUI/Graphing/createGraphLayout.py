from PyQt5 import QtWidgets as qtw
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navBar

from Graphing.graphCanvas import MplCanvas

def create_graph_layout(self):
    layout = qtw.QVBoxLayout()
    self.canvas = MplCanvas()
    self.nav_bar = navBar(self.canvas)
    layout.addWidget(self.nav_bar)
    layout.addWidget(self.canvas)
    self.CanvasGroupBox.setLayout(layout)