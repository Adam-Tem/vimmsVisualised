from Graphing.ScatterPlot import scatter_plot
from Graphing.ThreeDBarPlot import three_d_bar_plot


def select_graph_to_plot(canvas, file_location, file_name, combo_box_text, min_rt, max_rt, lower_scan, upper_scan):

    match combo_box_text:

        case "Scatter Plot":
            scatter_plot(canvas, file_location, file_name, min_rt, max_rt)
        case "3d Bar Plot":
            print("Here 2")
            three_d_bar_plot(canvas, file_location, file_name, min_rt, max_rt, lower_scan, upper_scan)
    