#!/usr/bin/env python

from IO import Input;
import Utilities;

def main():
    print("Searching csv files");
    directory_path = "./todosLosAngulos";
    file_searching_pattern = "**/*.csv";
    paths = Utilities.get_csv_filenames(directory_path, file_searching_pattern);
    db_path = "locomotionAnalysis.db";
    #print("Listing " + str(len(paths)) + " files \n");
    
    input_list = [];
    # Create object Input based on csv files
    for path in paths:
        input_obj = Input(str(path));
        input_obj.compute_metadata();
        input_list.append(input_obj);
    
    input_obj = input_list[0];
    print(input_obj.get_path());
    input_obj.insert_steps_into_db(db_path);
    print("------------------------------");
    
    # Insert steps into db
    #for input_obj in input_list:
    #    print(input_obj.get_path());
    #    input_obj.insert_steps_into_db(db_path);
    #    print("------------------------------");

def print_obj_list(obj_list):
    for obj in obj_list:
        print(obj.get_data_position());


if __name__ == '__main__':
    main();
