#!/usr/bin/env python

from IO import Input;
import Utilities;

def main():
    print("Searching csv files");
    paths = Utilities.get_csv_filenames("./todosLosAngulos", "**/*.csv");
    print("Listing " + str(len(paths)) + " files \n");
    input_list = [];
    for path in paths:
        input_obj = Input(str(path));
        input_obj.compute_metadata();
        input_list.append(input_obj);

    #print_filename_list(input_list);
    #print("----------------------------------");
    #print_segment_list(input_list);
    print("----------------------------------");
    print_subject_list(input_list);

def print_filename_list(file_obj_list):
    for file_obj in file_obj_list:
        print(file_obj.get_path());

def print_segment_list(obj_list):
    for obj in obj_list:
        print(obj.get_segment());

def print_subject_list(obj_list):
    for obj in obj_list:
        print(obj.get_subject_ids());

def print_condition_list(obj_list):
    for obj in obj_list:
        print(obj.get_segment());

if __name__ == '__main__':
    main();
