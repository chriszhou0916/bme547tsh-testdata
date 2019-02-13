import json


def parse_person(file):
    name = file.readline()
    if name == "END":
        return False
    first_last = name.split()
    age = file.readline()
    gender = file.readline()
    tsh_line = file.readline().strip()
    tsh_list = tsh_line.split(',')
    # remove "TSH" label
    tsh_list.pop(0)
    print(sorted(tsh_list))


filename = "test_data.txt"
f = open(filename, "r")
parse_person(f)
