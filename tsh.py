import json


def parse_person(file):
    """Processes data for one person from file input

    First checks if end of file is reached. If not, patient
    information is read in order. The TSH data is sorted and
    the information is outputted in a json file

    Args:
        file: reference to file being read

    Returns:
        boolean: whether the processing is successful
    """
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
    """Determines the diagnosis given a list of tsh values

    "hyperthyroidism" as defined by any of their tests results being less than
    1.0, "hypothyroidism" as defined by any of their test results being
    greater than 4.0, or "normal thyroid function" as defined by all of their
    test results being between 1.0 and 4.0, inclusive.
    No single patient will have test results both above 4.0 and below 1.0,
    hence will only meet one of the diagnoses above.

    Args:
        tsh_list (list): list of TSH values in str or numeric format

    Returns:
        str: the diagnosis
    """
    tsh_num = [float(x) for x in tsh_list]
    if min(tsh_num) < 1:
        return "hyperthyroidism"
    elif max(tsh_num) > 4:
        return "hypothyroidism"
    else:
        return "normal thyroid function"


def write_json(name, age, gender, tsh_list):
    """Stores the information of a single patient in a json format output

    Args:
        name (list): [first name, last name] format
        age (str): age of the patient
        gender (str): gender of the patient
        tsh_list (list): the pateint's TSH values

    Returns:

    """
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


def main():
    """Main method of the program

    Returns:

    """
    filename = "test_data.txt"
    f = open(filename, "r")
    while parse_person(f):
        pass
    f.close()


if __name__ == '__main__':
    main()
