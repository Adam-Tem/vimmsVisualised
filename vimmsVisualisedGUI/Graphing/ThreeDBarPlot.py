import numpy as np
from vimms.Common import path_or_mzml

def three_d_bar_plot(canvas, file_location, file_name, min_rt, max_rt, lower_scan, upper_scan):

    current_subplot = canvas.fig.get_axes()[0]
    canvas.fig.delaxes(current_subplot)
    canvas.axes = canvas.fig.add_subplot(111, projection='3d')

    canvas.axes.cla()
    mzml = path_or_mzml(file_location)
    
    for scan in mzml.scans[int(float(lower_scan)):int(float(upper_scan))]:
        rt = scan.rt_in_seconds
        for mz, intensity in scan.peaks:
            canvas.axes.plot(np.array([mz, mz]), np.array([rt, rt]), np.array([0, intensity]), color="black")

        canvas.axes.set(
            title=f"3d Plot of {file_name}",
            xlabel="m/z",
            ylabel="Retention Time",
            zlabel="Intensity",
            zlim=[0, None],
        )
    canvas.axes.autoscale()
    canvas.axes.set_ylim([float(min_rt),float(max_rt)])
    canvas.draw()