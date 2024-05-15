#!/usr/bin/python3
'''
Log Parsing
'''


import sys


status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_dict = {code: 0 for code in status_codes}
file_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        if len(data) > 2:
            if data[-2] in status_dict:
                status_dict[data[-2]] += 1
            file_size += int(data[-1])
        if counter == 10:
            print('File size: {}'.format(file_size))
            for key, value in status_dict.items():
                if value:
                    print('{}: {}'.format(key, value))
            counter = 0
except KeyboardInterrupt:
    print('File size: {}'.format(file_size))
    for key, value in status_dict.items():
        if value:
            print('{}: {}'.format(key, value))
    exit()
print('File size: {}'.format(file_size))
for key, value in status_dict.items():
    if value:
        print('{}: {}'.format(key, value))
