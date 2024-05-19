#!/usr/bin/python3
'''
Log Parsing
'''


import sys


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
counter = 0

try:
    for line in sys.stdin:
        data = line.split()
        if len(data) > 4:
            file_size += int(data[-1])
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
            counter += 1
            if counter == 10:
                print("File size: {}".format(file_size))
                for key in sorted(status_codes.keys()):
                    if status_codes[key] != 0:
                        print("{}: {}".format(key, status_codes[key]))
                counter = 0
except Exception:
    pass
finally:
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))
