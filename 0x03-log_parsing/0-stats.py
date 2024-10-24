#!/usr/bin/python3

<<<<<<< HEAD
'''
Method to print

'''

=======
"""
method to print
"""
>>>>>>> eafcb17d1cafd5a13a68f70614b23ef9958c322e
import sys


def printer(dict_sc, TFile_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        TFile_size: total of the file
    Returns:
        None
    """

    print("File size: {}".format(TFile_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


TFile_size = 0
code = 0
c = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            c += 1

            if c <= 10:
                TFile_size += int(parsed_line[0])
                code = parsed_line[1]

                if code in dict_sc.keys():
                    dict_sc[code] += 1

            if c == 10:
                printer(dict_sc, TFile_size)
                c = 0

finally:
    printer(dict_sc, TFile_size)