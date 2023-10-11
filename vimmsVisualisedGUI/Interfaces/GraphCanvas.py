import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fcqt
import numpy as np
from vimms.Common import path_or_mzml

import os
class MplCanvas(fcqt):

    def __init__(self, parent):
        self.fig = plt.figure(figsize=(3,3), dpi=100)
        self.ax = self.fig.add_subplot(111, projection="3d")
        super().__init__(figure=self.fig)
        self.setParent(parent)

        x = [1,2,3]
        y = [3,2,1]
        z = [1,2,3]

        self.ax.plot(x, y, z)

    def updatePlot(self, minRT, maxRT, file_location, file_name):
        
        mzml = path_or_mzml(file_location)
        min_mz = 10000
        max_mz = -1
        scaled_rt_min = 10000
        scaled_rt_max = -1
        for scan in mzml.scans[minRT:maxRT]:
            rt = scan.rt_in_seconds
            if rt < scaled_rt_min:
                scaled_rt_min = rt
            if rt > scaled_rt_max:
                scaled_rt_max = rt
            for mz, intensity in scan.peaks:
                if mz < min_mz:
                    min_mz = mz
                if mz > max_mz:
                    max_mz = mz
                self.ax.plot(np.array([mz, mz]), np.array([rt, rt]), np.array([0, intensity]), color="black")

        self.ax.set(
            title="Visualised mzML",
            ylabel="Retention Time",
            xlabel="m/z",
            zlabel="Intensity",
            zlim=[0, None],
            xlim=[min_mz, max_mz],
            ylim=[scaled_rt_min, scaled_rt_max]
            )
        self.fig.canvas.draw()