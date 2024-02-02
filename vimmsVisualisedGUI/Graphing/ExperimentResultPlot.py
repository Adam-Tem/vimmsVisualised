def experiment_result_plot(canvas, experiment, experiment_cases, graph_type):

    current_subplot = canvas.fig.get_axes()[0]
    canvas.fig.delaxes(current_subplot)
    canvas.axes = canvas.fig.add_subplot(111)
    canvas.axes.cla()
    markers = ["o" for _ in experiment_cases]

    layouts = {
        "cumulative_coverage_proportion" : {
            "title" : "Cumulative Coverage",
            "ylabel" : "Cumulative Coverage \nProportion",
        },
        
        "cumulative_intensity_proportion" : {
            "title" : "Cumulative Intensity \nProportion",
            "ylabel" : "Cumulative Intensity \nProportion",
        }
    }

    results_list = [eva.evaluation_report(min_intensity=0) for eva in experiment.evaluators]

    itr = zip(experiment.case_names, results_list, markers)
    
    for exp_name, results, m in itr:
        scores = results[graph_type]       
        xs = list(range(1, len(scores) + 1))
        
        canvas.axes.set_xlabel("Num. Runs", fontsize=7)
        canvas.axes.set_ylabel(layouts[graph_type]["ylabel"], fontsize=7)
        canvas.axes.set_title(layouts[graph_type]["title"], fontsize=8)
        canvas.axes.tick_params(labelsize=6)
        canvas.axes.plot(xs, scores, label=exp_name, marker=m)
    canvas.axes.legend((experiment_cases), loc="upper right", fontsize=6)
    ##fix this first the mora
    canvas.draw()