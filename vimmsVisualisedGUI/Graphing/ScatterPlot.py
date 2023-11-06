from vimms.BoxVisualise import PlotPoints

def scatter_plot(canvas, file_location = None, file_name = None, min_rt = None, max_rt = None):
        
    current_subplot = canvas.fig.get_axes()[0]
    canvas.fig.delaxes(current_subplot)
    canvas.axes = canvas.fig.add_subplot(111)
    canvas.axes.cla()
    pp = PlotPoints.from_mzml(file_location)
    pp.mpl_add_ms2s(canvas.axes)
    canvas.axes.set(
        title=f"{file_name} Fragmentation Events", 
        ylabel="m/z",
    )
    canvas.canvas.draw()