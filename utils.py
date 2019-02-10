import csv

def _get_list_from_csv(file_name):
    with open(file_name) as file:
        return [{key: value for key, value in row.items()} for row in
                         csv.DictReader(file, skipinitialspace=True, delimiter=';')]