from parsers.dir_parser import SubjectDirectory
from collections import OrderedDict
import numpy as np


class QuestParser(SubjectDirectory):
    parse_file_suffix = '_quest.csv'

    @staticmethod
    def get_questionary_lists(questionary_set, in_lines, limit=None):

        def validate(arr):
            def try_catch(element):
                try:
                    return int(element)
                except (TypeError, ValueError):
                    return np.nan

            if arr is None:
                return np.nan
            if not isinstance(arr, list):
                return try_catch(arr)
            ret = []
            for el in arr:
                ret.append(try_catch(el))
            return ret

        ret_set = [None for i in range(6)]
        l = 0
        for in_line in in_lines:
            if in_line.startswith(questionary_set):
                ret_set[l] = in_line.split(';')[1:limit]
                l += 1
        return list(map(validate, ret_set))

    @classmethod
    def parse_ordered_dictionary(cls, lines):
        subj_name = lines[0].split(';')[1]
        order_dict = OrderedDict(
            {cond: dict(
            start=None,
            end=None,
            panas=None,
            stai=None,
            dim=None,
            sssg=None) for cond in lines[1].split(';')[1:6]})
        starts = [start for start in lines[2].split(';')[1:6]]
        ends = lines[3].split(';')[1:6]

        panases = cls.get_questionary_lists('# PANAS', lines)
        stais = cls.get_questionary_lists('# STAI', lines, 7)
        dims = cls.get_questionary_lists('# DIM', lines, 3)
        sssqs = [None for i in range(6)]
        for line in lines:
            if line.startswith('# SSSQ'):
                sssqs = line.split(';')[1:6]

        for i, item in enumerate(order_dict):
            order_dict[item]['start'] = starts[i]
            order_dict[item]['end'] = ends[i]
            order_dict[item]['panas'] = panases[i]
            order_dict[item]['stai'] = stais[i]
            order_dict[item]['dim'] = dims[i]
            order_dict[item]['sssq'] = sssqs[i]
        return {'subject': subj_name, 'values': order_dict}

    def parse(self):
        self.subjects = []
        for src in self.directories:
            per_subject_lines = self.get_file_content_as_lines(src)
            ordered_dict = self.parse_ordered_dictionary(per_subject_lines)
            self.subjects.append(ordered_dict)


class Questionary(object):

    questionary_items = []
    questionary_feelings = {}
    my_name = None

    def __init__(self, order, q_period, q_item):
        self.order_dict = order
        self.q_period = q_period
        self.q_item = q_item
        self.answer = None
        self._parse()

    def _parse(self):
        item_index = self.questionary_items.index(self.q_item)
        value_index = self.order_dict[self.q_period][self.my_name][item_index]
        self.answer = self.questionary_feelings[value_index]

    def response(self):
        return self.answer

    def response_pretty(self):
        return 'At {} period feels {} {} for {} questionary'.format(
            self.q_period,
            self.answer,
            self.q_item,
            self.my_name)


class Panas(Questionary):

    my_name = 'panas'
    questionary_feelings = {
        '1': 'Not at all',
        '2': 'A little bit',
        '3': 'Somewhat',
        '4': 'Very much',
        '5': 'Extremely'
    }

    questionary_items = [
        'Active',
        'Distressed',
        'Interested',
        'Inspired',
        'Annoyed',
        'Strong',
        'Guilty',
        'Scared',
        'Hostile',
        'Excited',
        'Proud',
        'Irritable',
        'Enthusiastic',
        'Ashamed',
        'Alert',
        'Nervous',
        'Determined',
        'Attentive',
        'Jittery',
        'Afraid',
        'Stressed',
        'Frustrated',
        'Happy',
        '(Angry)',
        '(Irritated)',
        'Sad'
    ]


class Stai(Questionary):

    my_name = 'stai'

    questionary_feelings = {
        '1': 'Not at all',
        '2': 'Somewhat',
        '3': 'Moderately so',
        '4': 'Very much so'
    }

    questionary_items = [
        'I feel at ease',
        'I feel nervous',
        'I am jittery',
        'I am relaxed',
        'I am worried',
        'I feel pleasant'
    ]


class Dim(Questionary):

    my_name = 'dim'

    questionary_feelings = {str(k): str(v) for k,v in enumerate(range(1,10))}

    questionary_items = [
        'Valence',
        'Arousal'
    ]


# for src in get_subject_dirs():
#     per_subject_lines = get_file_content_as_lines(src)
#     ordered_dict = parse_ordered_dictionary(per_subject_lines)
#     p = Panas(ordered_dict, 'Base', 'Happy')
#     s = Stai(ordered_dict, 'Base', 'I am jittery')
#     d = Dim(ordered_dict, 'Base', 'Arousal')
#     print('Subject ' + src[1], d.response_pretty())

q = QuestParser()
# q.parse()

for s in q.get_subjects():
    print(s)
