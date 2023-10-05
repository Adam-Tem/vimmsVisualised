from vimms.Common import path_or_mzml

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

path_to_file = os.path.join(os.getcwd(), "small_mzml.mzml")
def plot_mzml_2d(scan, title=None):
    fig, ax = plt.subplots(1, 1)
    
    for mz, intensity in scan.peaks:
        ax.plot(np.array([mz, mz]), np.array([0, intensity]), color="black")
    
    ax.set(
        title=title,
        xlabel="m/z", 
        ylabel="Intensity",
        ylim=[0, None]
    )
    fig.set_size_inches(18.5, 10.5)
    return fig

def plot_mzml_3d(ax, mzml, scan_lower, scan_upper, title=""):
    for scan in mzml.scans[scan_lower:scan_upper]:
        rt = scan.rt_in_seconds
        for mz, intensity in scan.peaks:
            ax.plot(np.array([mz, mz]), np.array([rt, rt]), np.array([0, intensity]), color="black")

        ax.set(
            title=title,
            ylabel="Retention Time",
            xlabel="m/z",
            zlabel="Intensity",
            zlim=[0, None],
        )

mzml = path_or_mzml(path_to_file)
# scan = max((s for s in mzml.scans), key=lambda s: len(s.peaks))
# print(f"scan rt: {scan.rt_in_seconds}")
# title = f"topN on Chromatograms Sampled from HMDB - at {round(scan.rt_in_seconds, 2)} secs"
# fig = plot_mzml_2d(scan, title=title)



scan_ranges = [(250, 260)]
for scan_lower, scan_upper in scan_ranges:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_mzml_3d(
        ax,
        mzml, 
        scan_lower, 
        scan_upper, 
        title=f"topN Chromatograms Sampled from HMDB - MS1 Scans {scan_lower} to {scan_upper}"
    )

    ax.autoscale()
    fig.set_size_inches(18.5, 10.5)

plt.show(block=True)
fig.show()

