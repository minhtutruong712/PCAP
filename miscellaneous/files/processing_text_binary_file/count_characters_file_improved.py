from os import strerror
from collections import Counter 
import re

src_file_name = input('Please input the source file name: ')
list_char = []

try:
    tf = open(src_file_name, 'rt')
    line = tf.readline()
    while line != "": 
        line = line.lower()
        print(line)
        for char in line:
            if char != " " and char != "\n":
                list_char.append(char) 
        line = tf.readline()


    # count characters
    char_count = Counter(list_char)
    
    # sort keys by frequency 
    sorted_data = sorted(char_count, key=lambda x: char_count[x], reverse=True)

    # send to destination file name
    m = re.match(r'(.+)(\..+)', src_file_name)
    dest_file_name = m.group(1) + ".hist" + m.group(2)
    df = open(dest_file_name, 'wt')

    result = [key + " - > " + str(char_count[key]) for key in sorted_data]

    for r in result:
        df.write(r + "\n")

    
    df.close()
    tf.close()


except IOError as e: 
    print("I/O error occurred:", strerror(e.errno))




