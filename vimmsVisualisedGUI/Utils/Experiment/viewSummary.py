from PyQt5 import QtWidgets as qtw
from Graphing.ExperimentResultPlot import experiment_result_plot

def view_summary(self):
    self.SummaryGroupBox.setHidden(False)
    self.SummaryGroupBox.move(0,100)
    self.SummaryInfoLabel.setText(self.summary)
    experiment_result_plot(self.canvas, self.experiment, 
                           self.experiment_case_list, "cumulative_coverage_proportion")