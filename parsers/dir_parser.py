import os
import re


class SubjectDirectory(object):
    DATA_PATH = '../data/'
    directories = []
    subjects = None
    parse_file_suffix = None

    def __init__(self):
        self._get_subject_dirs()

    def _get_subject_dirs(self):
        for subject_directory in os.listdir(self.DATA_PATH):
            if re.match('^S[0-9]{1,2}$', subject_directory):
                self.directories.append((self.DATA_PATH + subject_directory + '/', subject_directory))

    def get_file_content_as_lines(self, data_path_tuple):
        """
        Filters out empty lines and those starts with '#'
        :param data_path_tuple: contains path to subject's directory and subject
        :return: list of lines
        """
        (data_path, subject) = data_path_tuple
        file_path = data_path + subject + self.parse_file_suffix
        with open(file_path, 'r') as readme:
            content = readme.read()
        return [i for i in content.split('\n') if not i.startswith('#') or i != '']

    def get_subjects(self):
        if self.subjects is None:
            self.parse()
        return self.subjects

    def parse(self):
        raise NotImplementedError('`parse()` must be implemented.')
