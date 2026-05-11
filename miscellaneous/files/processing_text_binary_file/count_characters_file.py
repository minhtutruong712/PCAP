from os import strerror
from collections import Counter 

file_name = input('Please input the file name: ')
list_char = []

try:
    tf = open(file_name, 'rt')
    line = tf.readline()
    while line != "": 
        line = line.lower()
        print(line)
        for char in line:
            if char != " " and char != "\n":
                list_char.append(char) 
        line = tf.readline()
    
    char_count = Counter(list_char)

    
    
    for key in char_count: 
        print(key, '- >', char_count[key])

except IOError as e: 
    print("I/O error occurred:", strerror(e.errno))




