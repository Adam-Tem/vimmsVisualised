from Graphing.ScatterPlot import scatter_plot
from Graphing.ThreeDBarPlot import three_d_bar_plot


def select_graph_to_plot(self, combo_box_text):

    match combo_box_text:

        case "Scatter Plot":
            scatter_plot(self.canvas, self.file_location, self.file_name,) #min_rt, max_rt)
        case "3d Bar Plot":
            three_d_bar_plot(self.canvas, self.file_location, self.file_name,) #min_rt, max_rt)
    