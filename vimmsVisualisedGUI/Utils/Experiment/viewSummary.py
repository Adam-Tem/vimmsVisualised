from PyQt5 import QtWidgets as qtw
from Graphing.ExperimentResultPlot import experiment_result_plot

def view_summary(self):
    count = len(self.experiment_case_list)
    self.SummaryInfoLabel.setText(self.summary)
    self.SummaryInfoLabel.setFixedHeight(170*count)
    self.SummaryScrollContents.setFixedHeight(170*count + 15)
    self.SummaryGroupBox.setHidden(False)
    self.SummaryGroupBox.move(0,100)
    experiment_result_plot(self.canvas, self.experiment, 
                           self.experiment_case_list, "cumulative_coverage_proportion")