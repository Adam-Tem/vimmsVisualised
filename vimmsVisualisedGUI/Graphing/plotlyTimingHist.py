from plotly.subplots import make_subplots
from plotly import graph_objects as go
from plotly.offline import plot as pop

from Utils.Parameters.ParamWidgets import SAVE_DIRECTORY

import os

def plotly_timing_hist(processing_times, title, binsize=None):
    fig = make_subplots(rows=1, cols=len(processing_times))
    
    for i, run_times in enumerate(processing_times):
        fig.add_trace(
            go.Histogram(
                x=run_times,
                xbins={
                    "size": binsize
                },
                name=f"Injection {i}",
            ),
            row=1,
            col=i+1
        )

    fig.update_layout(
        template="plotly_white",
        title_text=f"{title} Scan Timings",
        xaxis_title_text="Processing Time (secs)",
        yaxis_title_text="Count",
    )
    pop(fig, filename= os.path.join(SAVE_DIRECTORY, "temp-plot.html"), auto_open=False)