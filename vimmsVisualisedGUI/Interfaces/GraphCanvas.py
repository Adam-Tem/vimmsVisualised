import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as fcqt

import numpy as np
from vimms.Common import path_or_mzml

class MplCanvas(fcqt):

    def __init__(self, parent):
        self.fig = plt.figure(figsize=(3,3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        super().__init__(figure=self.fig)
        self.setParent(parent)


    def updatePlot(self, minRT, maxRT, file_location, file_name):
        
        mzml = path_or_mzml(file_location)
        rt_vals = []
        charge_vals = []
        intensity_vals = []
        for scan in mzml.scans[minRT:maxRT]:
            rt = scan.rt_in_seconds
            row_intensity = []
            for mz, intensity in scan.peaks:
                row_intensity.append(intensity)
            
            intensity_vals.append(row_intensity)

        length = max(map(len, intensity_vals))
        convert = np.array([xi+[0]*(length-len(xi)) for xi in intensity_vals])

        normalized_arr = (convert - convert.min()) / (convert.max() - convert.min())
        
        plt.imshow(normalized_arr.T)
        plt.gca().set_aspect('equal')
        colorbar = plt.colorbar()
        colorbar.set_label('Intensity')
        plt.figure(figsize=(3, 3))
        self.fig.canvas.draw()