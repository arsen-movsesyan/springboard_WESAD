import os
import re


DATA_PATH = '../data/'

VALUE_EXTRACT_KEYS = {
    "age": {
        'search_key': 'Age',
        'delimeter': ':'
    },
    "height": {
        'search_key': 'Height',
        'delimeter': ':'
    },
    "weight": {
        'search_key': 'Weight',
        'delimeter': ':'
    },
    "gender": {
        'search_key': 'Gender',
        'delimeter': ':'
    },
    "dominant_hand": {
        'search_key': 'Dominant',
        'delimeter': ':'
    },
    "coffee_today": {
        'search_key': 'Did you drink coffee today',
        'delimeter': '? '
    },
    "coffee_last_hour": {
        'search_key': 'Did you drink coffee within the last hour',
        'delimeter': '? '
    },
    "sport_today": {
        'search_key': 'Did you do any sports today',
        'delimeter': '? '
    },
    "smoker": {
        'search_key': 'Are you a smoker',
        'delimeter': '? '
    },
    "smoke_last_hour": {
        'search_key': 'Did you smoke within the last hour',
        'delimeter': '? '
    },
    "feel_ill_today": {
        'search_key': 'Do you feel ill today',
        'delimeter': '? '
    }
}


def get_subject_dirs():
    """
    Returns list of  tuples with path to subject directory and subject
    :return: [(path, subject),...]
    """
    ret = []
    for subject_directory in os.listdir(DATA_PATH):
        if re.match('^S[0-9]{1,2}$', subject_directory):
            ret.append((DATA_PATH + subject_directory + '/', subject_directory))
    return ret


def get_file_content_as_lines(data_path_tuple):
    """
    Filters out empty lines and those starts with '#'
    :param data_path_tuple: contains path to subject's directory and subject
    :return: list of lines
    """
    (data_path, subject) = data_path_tuple
    file_path = data_path + subject + '_readme.txt'
    with open(file_path, 'r') as readme:
        content = readme.read()
    return [i for i in content.split('\n') if not i.startswith('#') or i != '']


def get_key_value(item):
    """
    Determines parameter value which is predefined in VALUE_EXTRACT_KEYS
    :param item: single line
    :return: dictionary of parameter, definition and value
    {
        'param': 'smoker',
        'definition': 'Are you a smoker',
        'value': 'NO'
    }
    """
    for k in VALUE_EXTRACT_KEYS.keys():
        search_key = VALUE_EXTRACT_KEYS[k]['search_key']
        delimiter = VALUE_EXTRACT_KEYS[k]['delimeter']
        if item.startswith(search_key):
            d, v = item.split(delimiter)
            return dict(param=k, definition=d, value=v)
    return False


# Parsing and getting a list of dictionaries per subject
subjects = []
for src in get_subject_dirs():
    lines = get_file_content_as_lines(src)
    for line in lines:
        subject = get_key_value(line)
        if subject:
            subject['subject'] = src[1]
            subjects.append(subject)

print(subjects)

