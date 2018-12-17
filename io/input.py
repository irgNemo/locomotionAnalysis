import csv;

class Input:
    'Input file class'

    def __init__(self, path_file):
        print("Constructor...");
        self.path_file = path_file; 

    def headerFrequencies(self):
        with open(self.path_file) as csv_file:
            for line in csv_file
               print(line); 
