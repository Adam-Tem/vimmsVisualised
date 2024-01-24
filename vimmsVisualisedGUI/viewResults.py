from vimms.BoxVisualise import plotly_mzml, plotly_timing_hist, plotly_fragmentation_events
from vimms.Common import load_obj
import os
def view_results(file):
    plotly_mzml(file)

    
def read_pickle(pkl_file):

    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "results", "experiment_results", pkl_file)
    print(file_path)
    # data = load_obj(file_path)
    # plotly_timing_hist([data.processing_times], "Test")
    plotly_fragmentation_events("Hello", file_path)
read_pickle("aaa_0.mzML")



# view_results("small_mzml.mzML")