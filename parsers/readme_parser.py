from parsers.dir_parser import SubjectDirectory


class ReadmeParser(SubjectDirectory):
    parse_file_suffix = '_readme.txt'

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

    def get_key_value(self, item):
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
        for k in self.VALUE_EXTRACT_KEYS.keys():
            search_key = self.VALUE_EXTRACT_KEYS[k]['search_key']
            delimiter = self.VALUE_EXTRACT_KEYS[k]['delimeter']
            if item.startswith(search_key):
                d, v = item.split(delimiter)
                return dict(param=k, definition=d, value=v)
        return False

    def parse(self):
        self.subjects = []
        for src in self.directories:
            subject = dict(subject=src[1], params=[])
            lines = self.get_file_content_as_lines(src)
            for line in lines:
                subject_info = self.get_key_value(line)
                if subject_info:
                    subject['subject'] = src[1]
                    subject['params'].append(subject_info)
            self.subjects.append(subject)


rp = ReadmeParser()
rp.parse()

for subj in rp.get_subjects():
    print(subj)
