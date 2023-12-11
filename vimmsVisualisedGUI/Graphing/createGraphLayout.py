from PyQt5 import QtWidgets as qtw


from Graphing.GraphCanvas import MplCanvas, QNavBar

def create_graph_layout(self):
    layout = qtw.QVBoxLayout()
    self.canvas = MplCanvas()
    self.nav_bar = QNavBar(self.canvas)
    self.canvas.canvas_changed.connect(self.nav_bar.graph_change)
    layout.addWidget(self.nav_bar)
    layout.addWidget(self.canvas)
    self.CanvasGroupBox.setLayout(layout)