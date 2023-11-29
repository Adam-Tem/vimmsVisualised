from PyQt5 import QtWidgets as qtw

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as navBar
from Graphing.GraphCanvas import MplCanvas

from Graphing.ExperimentResultPlot import experiment_result_plot


def view_summary(self):
    self.SummaryGroupBox.setHidden(False)
    self.SummaryGroupBox.move(0,100)
    self.SummaryInfoLabel.setText(self.summary)
    canvas = MplCanvas()
    nav_bar = navBar(canvas)
    experiment_result_plot(self, canvas, self.experiment, self.experiment_case_list, self.fullscan_list)
    layout = qtw.QVBoxLayout()
    layout.addWidget(nav_bar)
    layout.addWidget(canvas)
    self.CanvasGroupBox.setLayout(layout)


    