def round_experiment_results(summary_string):

    results = summary_string.split("\n")
    output = ""
    for line in results:
        breakdown = line.split(":")
        if len(breakdown) == 2:
            output += breakdown[0] + ":"
            if "proportion" in breakdown[0]:
                rounded_results = []
                for value in breakdown[1][2:-1].split(","):
                    rounded_results.append(str(round(float(value.strip()), 3)))
                output += " " + ",".join(rounded_results)
            else:
                output += " " + breakdown[1]
            output += "\n"
        else:
            output += line + "\n"
    return output