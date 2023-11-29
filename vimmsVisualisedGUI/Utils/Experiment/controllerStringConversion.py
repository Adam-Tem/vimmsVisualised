

def controller_string_conversion(controller_name):
    match controller_name:
        case "TopN Controller":
            return "topn"
        case "TopN ROI Controller":
            return "topn_roi"
        case "TopN Exclusion Controller":
            return "topn_exclusion"
        case "topNEX Controller":
            return "topnex"
        case "Hard Roi Exclusion Controller":
            return "hard_roi_exclusion"
        case "Intensity Roi Exclusion Controller":
            return "intensity_roi_exclusion"
        case "Non Overlap Controller":
            return "non_overlap"
        case "Intensity Non Overlap Controller":
            return "intensity_non_overlap"
        case "DSDA Controller":
            return "dsda"
        case "Matching Controller":
            return "matching"
        