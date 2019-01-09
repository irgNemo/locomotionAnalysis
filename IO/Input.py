import csv;
import re;
from re import search, findall, UNICODE;
import sqlite3;


class Input:
    'Input file class'
    db_connection = None; 

    def __init__(self, path):
        self._path = path; # path to the file read.
        self._segment = None; # Segment to be analyzed
        self._treatment = None; # List with the treatment of each subject
        self._subject_ids = None; # List with subjects id
        self._step_number = None; # List with the step numbers in the file 
        self._data_position = None; # Position of the begining of the data in the file
        self._time_elapsed = None; # List with time elapsed since alteration of the data in the file
        self._status = None; # Control or Altered 

    def compute_metadata(self):
        self.set_subject_ids([]);
        with open(self.get_path()) as csv_file:
            line = csv_file.readline();
            cnt = 0;
            while line:
                if cnt == 0:
                    self.set_segment(re.search("(\w|\s)+", line, UNICODE).group(0));
                    match_obj = re.search('(control)?\s*([\s+\w+]+)', line.lower(), UNICODE);
                    if match_obj: 
                        status = match_obj.group(1) if match_obj.group(1) else 'altered';
                        self.set_status(status);
                        self.set_segment(match_obj.group(2));
                    else:
                        print("Warning: there is no match with the segment header");
                if cnt == 1:
                    subject_parsed = re.findall('(R[0-9 ])-([ A-Za-z]{2,3})(,\s*([0-9]+\s+dpl))?', line);
                    subject_ids = [];
                    treatment = [];
                    time_elapsed = [];
                    for subject_tuple in subject_parsed:
                        subject_ids.append(subject_tuple[0]);
                        treatment.append(subject_tuple[1]);
                        time_elapsed.append(subject_tuple[3]);
                    self.set_subject_ids(subject_ids);
                    self.set_treatment(treatment);
                    self.set_time_elapsed(time_elapsed);
                if cnt == 2:
                    step_list = re.findall('[a-zA-Z]+\s+([0-9]+)',line);
                    self.set_step_number(step_list);
                    self.set_data_position(csv_file.tell());
                    break;
                line = csv_file.readline();
                cnt += 1;

    def insert_steps_into_db(self, db_path_name):
        Input.db_connection = self.get_connection(db_path_name);
        cursor = Input.db_connection.cursor();
        with open(self.get_path()) as cvs_file:
            cvs_file.seek(self.get_data_position());
            for line in cvs_file:
                subject_cnt = -1;
                treatment_cnt = -1; 
                elapsed_time_cnt = -1;
                for cnt,angle in enumerate(line.strip().split(',')):
                    if (self.get_status() == 'control'):
                        if (cnt % 3) == 0:
                            subject_cnt += 1;
                            elapsed_time_cnt +=1;
                            treatment_cnt += 1;
                        elif (self.get_status() == 'altered'):
                            if (cnt % 6) == 0:
                                subject_cnt += 1;
                                elapsed_time_cnt += 1;
                                treatment_cnt += 1;
                    segment = self.get_segment();
                    subject = self.get_subject_ids()[subject_cnt];
                    treatment = self.get_treatment()[treatment_cnt];
                    time_elapsed = self.get_time_elapsed()[elapsed_time_cnt];
                    status = self.get_status();
                    step = self.get_step_number()[cnt];
                    insert_tuple = (segment, subject, treatment, time_elapsed, step, angle, status);
                    insert_statement = 'INSERT INTO step (id_segment, id_subject, id_treatment, time_elapsed, step_number, angle, status) values (?,?,?,?,?,?,?)' + str(insert_tuple)
                    print(insert_statement);
             #print(self.get_status(), cnt, subject_cnt, treatment_cnt, elapsed_time_cnt);


    def get_connection(self, db_path_name):
        if not Input.db_connection:
            Input.db_connection = sqlite3.connect(db_path_name);
        return Input.db_connection;

    def get_status(self):
        return self._status;

    def set_status(self, status):
        self._status = status;

    def get_metadata(self):
        if(not self.get_segment() or not self.get_subject_ids() or not self.get_step_number()):
            self.compute_metadata();
        return (self.get_segment(), self.get_subject_ids(), self.get_step_number());

    def get_step_number(self):
        return self._step_number;

    def set_step_number(self, step_number):
        self._step_number = step_number;

    def get_data_position(self):
        return self._data_position;

    def set_data_position(self, position):
        self._data_position = position;

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

    def set_treatment(self, treatment):
        self._treatment = treatment;

    def get_treatment(self):
        return self._treatment;

    def get_time_elapsed(self):
        return self._time_elapsed;

    def set_time_elapsed(self, time_elapsed):
        self._time_elapsed = time_elapsed;
