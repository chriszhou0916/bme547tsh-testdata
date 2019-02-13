import json


def parse_person(file):
    name = file.readline().strip()
    if name == "END":
        return False
    first_last = name.split()
    age = file.readline().strip()
    gender = file.readline().strip()
    tsh_line = file.readline().strip()
    tsh_list = tsh_line.split(',')
    # remove "TSH" label
    tsh_list.pop(0)
    tsh_list.sort()
    write_json(first_last, age, gender, tsh_list)
    return True


def diagnose(tsh_list):
    tsh_num = [float(x) for x in tsh_list]
    if min(tsh_num) < 1:
        return "hyperthyroidism"
    elif max(tsh_num) > 4:
        return "hypothyroidism"
    else:
        return "normal thyroid function"


def write_json(name, age, gender, tsh_list):
    info_dict = {
        "First Name": name[0],
        "Last Name": name[1],
        "Age": age,
        "Gender": gender,
        "Diagnosis": diagnose(tsh_list),
        "TSH": tsh_list
    }
    write_filename = "{}-{}.json".format(name[0], name[1])
    out = open(write_filename, "w")
    json.dump(info_dict, out)
    out.close()


filename = "test_data.txt"
f = open(filename, "r")
while parse_person(f):
    pass
f.close()
