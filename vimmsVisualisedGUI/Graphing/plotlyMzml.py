from vimms.Common import path_or_mzml
from vimms.BoxVisualise import PlotPoints

from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY

from plotly import graph_objects as go
from plotly.offline import plot as pop
import os

def plotly_mzml(mzml, draw_minm=0.0, colour_minm=None, show_precursors=False):
    fig = go.Figure()
    mzml = path_or_mzml(mzml)
    if len(mzml.scans) > 0:
        pp = PlotPoints.from_mzml(mzml)
        fig.add_trace(
            pp.plotly_ms1s(
                draw_minm=draw_minm, 
                colour_minm=colour_minm, 
                show_precursors=show_precursors
            )
        )
    fig.update_layout(
        template="plotly_white",
        title = os.path.basename(mzml.file_name),
        xaxis_title="Retention Time",
        yaxis_title="m/z"
    )
    pop(fig, filename= os.path.join(SAVE_DIRECTORY, "temp-plot.html"), auto_open=False)
