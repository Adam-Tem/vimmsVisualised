from vimms.Common import load_obj

def index_p(file_location):
    data = load_obj(file_location)
    min_rt = data[0].rt
    max_rt = data[0].rt
    for chemical in data:
        max_rt = max(max_rt, chemical.rt)
        min_rt = min(min_rt, chemical.rt)
    
    return min_rt, max_rt