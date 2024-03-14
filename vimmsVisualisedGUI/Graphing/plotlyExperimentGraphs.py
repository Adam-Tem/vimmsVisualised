from Graphing.plotlyMzml import plotly_mzml
from Graphing.plotlyTimingHist import plotly_timing_hist
from Graphing.plotlyFragEvents import plotly_frag_events
from vimms.Common import load_obj
import os
def plotly_experiment_graphs(radio_buttons, exp_mzmls, exp_pkls, exp_location, exp_name):

    if radio_buttons[0]:
        plotly_mzml(os.path.join(exp_location, exp_mzmls.currentText() + ".mzML"))
        
    elif radio_buttons[1]:
        processing_times = [load_obj(os.path.join(exp_location, "pickle", 
                                    exp_pkls.currentText().split(" ")[0] + ".pkl")).processing_times]
        plotly_timing_hist(processing_times, exp_name)
    elif radio_buttons[2]:
        mzml_list = [os.path.join(exp_location, exp_mzmls.itemText(idx) + ".mzML") 
                     for idx in range(exp_mzmls.count())]
        plotly_frag_events(exp_name, mzml_list)