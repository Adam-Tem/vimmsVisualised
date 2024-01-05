from pymzml import run

def index_mzml(file_location, range_required):
    min_rt = float('inf')
    max_rt = float('-inf')

    with run.Reader(file_location) as reader:
        for spectrum in reader:
            rt = spectrum.scan_time_in_minutes() * 60
            min_rt = min(min_rt, rt)
            max_rt = max(max_rt, rt)
        scans = sum(1 for scan in reader)

        return min_rt, max_rt, scans