from vimms.BoxVisualise import mpl_results_plot, mpl_set_figure_style
from Graphing.GraphCanvas import MplCanvas
import matplotlib.pyplot as plt
def experiment_result_plot(self, canvas, experiment, experiment_cases, fullscan_list):

    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3], [4, 5, 6])

    current_subplot = canvas.fig.get_axes()[0]
    canvas.fig.delaxes(current_subplot)
    fig, axes = mpl_results_plot(
    experiment_cases,
    experiment.evaluators,
    markers = ["o" for _ in experiment_cases],
    min_intensity = 0
    )
    fig.show()
    print(fig, axes)
    canvas.axes = axes[0]
    canvas.figure = fig
    
    # mpl_set_figure_style(
    #     canvas.fig,
    #     figure_sizes = (4, 4),
    # )

    # for ax in canvas.axes:
    #     ax.set_xticks([x for x in range(1, len(fullscan_list) + 1)])

    #canvas.draw()
