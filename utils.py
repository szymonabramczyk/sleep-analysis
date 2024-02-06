def get_file_path_motion(subject_id):
    return 'data/motion/' + str(subject_id) + '_acceleration.txt'

def get_file_path_steps(subject_id):
    return 'data/steps/' + str(subject_id) + '_steps.txt'

def get_file_path_labels(subject_id):
    return 'data/labels/' + str(subject_id) + '_labeled_sleep.txt'

def get_file_path_hr(subject_id):
    return 'data/heart_rate/' + str(subject_id) + '_heartrate.txt'

def generate_bins(min_value, max_value, interval):
    bins = []
    current_value = min_value-interval
    if current_value < 0:
        current_value = 0
    while current_value <= max_value:
        bins.append(current_value)
        current_value += interval
    bins.append(current_value)
    return bins