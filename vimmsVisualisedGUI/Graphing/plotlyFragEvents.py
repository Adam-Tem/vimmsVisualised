from vimms.Common import path_or_mzml
from vimms.BoxVisualise import PlotPoints

from plotly.subplots import make_subplots
from plotly.offline import plot as pop

from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY

import os

def plotly_frag_events(exp_name, mzmls, colour_minm=None):

    fig = make_subplots(rows=len(mzmls), cols=1,
                        subplot_titles=[os.path.split(name)[-1] for name in mzmls])

    for i, mzml in enumerate(mzmls):
        mzml = path_or_mzml(mzml)
        pp = PlotPoints.from_mzml(mzml)
        data = pp.plotly_ms2s(colour_minm=colour_minm)
        data.name = os.path.basename(mzml.file_name)
        fig.add_trace(data, row=i+1, col=1)
        fig.update_yaxes(title_text="mz", row=i+1, col=1)
        fig.update_xaxes(title_text="Retention Time (seconds)", row=i+2, col=1)
    
    fig.update_layout(
        template = "plotly_white",
        title = f"{exp_name} Fragmentation Events",
        height = 300 * len(mzmls),
        showlegend=False
    )
    pop(fig,  filename= os.path.join(SAVE_DIRECTORY, "temp-plot.html"), auto_open=False)