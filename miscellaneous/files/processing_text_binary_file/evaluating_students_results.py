from os import strerror
from collections import defaultdict

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, line_cnt, message, value):
        self.line_cnt = line_cnt
        self.message = message
        self.value = value

        # Call base class constructor
        # super().__init__(f"Error in line '{self.line_cnt}': {self.message} (Got: {value})")
    
    def __str__(self):
        return f"Error in line '{self.line_cnt}': {self.message} (Got: {self.value})"       

class FileEmpty(StudentsDataException):
    def __init__(self):    
        super().__init__('This file is empty')

file_name = input('Please input the file name: ')
try: 

    f = open(file_name, 'r')
    if f.read() == "": 
        raise FileEmpty()
    
    f.seek(0)
    line = f.readline() 
    dict = defaultdict(list)
    line_cnt = 1
    while line != "": 
        line_lst = line.split()
        if len(line_lst) != 3: 
            raise BadLine(line_cnt, "Data line got less or more than 3 fields, please recheck", len(line_lst))
        key = line_lst[0] + " " + line_lst[1]
        try:
            value = float(line_lst[2])
        except:
            raise BadLine(line_cnt, "Invalid data input for score", line_lst[2])
        dict[key].append(value)
        line_cnt += 1
        line = f.readline() 
    
    for key in dict: 
        print(key, sum(dict[key])) 

except FileEmpty as e: 
    print(e)
except BadLine as e:
    print(e)
except IOError as e: 
    print("I/O error occurred:", strerror(e.errno))



