import csv;
import re;
from re import search, findall, UNICODE;
class Input:
    'Input file class'

    def __init__(self, path):
        self.set_path(path);
        self.set_segment(None);
        self.set_subject_ids(None);
        self.set_subject_steps(None);

    def compute_metadata(self):
        self.set_subject_ids([]);
        with open(self.get_path()) as csv_file:
            for cnt, line in enumerate(csv_file):
                if cnt == 3:
                    break;
                if cnt == 0:
                    self.set_segment(re.search("(\w|\s)+", line, UNICODE).group(0)); 
                if cnt == 1:
                    self.set_subject_ids(re.findall('(R[0-9 ]-[ A-Za-z]{2,3})(,\s*([0-9]+\s+dpl))?', line));
                if cnt == 2:
                    self.set_subject_steps(line.strip().split(','));
    
    def get_metadata(self):
        if(not self.get_segment() or not self.get_subject_ids() or not self.get__subject_steps()):
            self.compute_metadata();
        return (self.get_segment(), self.get_subject_ids(), self.get_subject_steps());

    def get_path(self):
        return self._path;

    def set_path(self, path):
        self._path = path;

    def get_segment(self):
        return self._segment;

    def set_segment(self, segment):
        self._segment = segment;

    def get_subject_ids(self):
        return self._subject_ids;

    def set_subject_ids(self, subject_ids):
        self._subject_ids = subject_ids;

    def get_subject_steps(self):
        return self._subject_steps;

    def set_subject_steps(self, subject_steps):
        self._subject_steps = subject_steps;
