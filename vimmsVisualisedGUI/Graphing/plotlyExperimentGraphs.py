from vimms.BoxVisualise import plotly_timing_hist, plotly_fragmentation_events
from Graphing.plotlyMzml import plotly_mzml
from vimms.Common import load_obj
import os
def plotly_experiment_graphs(plotly_figure, radio_buttons, exp_mzmls, exp_location, exp_name):


    if radio_buttons[0]:
        plotly_mzml(os.path.join(exp_location, exp_mzmls.currentText() + ".mzML"))
        
    elif radio_buttons[1]:
        pkl_file = load_obj([f for f in os.listdir(exp_location) if f.split(".")[-1] == "pkl"][0])
        timing_hist_plot = plotly_timing_hist([pkl_file.processing_times], exp_name)
        plotly_figure.set_html(timing_hist_plot.to_html(full_html=False))
    elif radio_buttons[2]:
        mzml_list = [exp_mzmls.itemText(idx) for idx in len(exp_mzmls.count())]
        frag_events_plot = plotly_fragmentation_events(exp_name, mzml_list)
        plotly_figure.set_html(frag_events_plot.to_html(full_html=False))