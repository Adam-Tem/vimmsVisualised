from Graphing.experimentResultPlot import experiment_result_plot
from Utils.Experiment.roundExperimentResults import round_experiment_results

def view_summary(self):
    count = len(self.experiment_case_list)
    self.SummaryInfoLabel.setText(round_experiment_results(self.summary))
    self.SummaryInfoLabel.setFixedHeight(180*count*len(self.fullscan_list))
    self.SummaryScrollContents.setFixedHeight(180*count*len(self.fullscan_list) + 15)
    self.SummaryGroupBox.setHidden(False)
    self.SummaryGroupBox.move(0,100)
    experiment_result_plot(self.canvas, self.experiment, 
                           self.experiment_name_list, "cumulative_coverage_proportion")