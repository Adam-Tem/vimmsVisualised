def round_experiment_results(summary_string):

    results = summary_string.split("\n")
    output = ""
    for line in results:
        breakdown = line.split(":")
        if len(breakdown) == 2:
            output += breakdown[0] + ":"
            if "proportion" in breakdown[0]:
                rounded_result = round(float(breakdown[1][2:-1]), 3)
                output += " " + str(rounded_result) + "\n"
            else:
                output += " " + breakdown[1] + "\n"
        else:
            output += line + "\n"
    return output


