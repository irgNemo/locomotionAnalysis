#!/usr/bin/env python

from pathlib import Path;

"""
get_csv_filenames list all the paths of files with an specific extension

Parameters:
    root directory

Returns:
    Dictionary with all paths with a csv file
"""
def get_csv_filenames(directory_path, file_type_expression):
   p = Path(directory_path);
   return list(p.glob(file_type_expression));

