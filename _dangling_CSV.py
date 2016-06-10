import csv
from os import path

base_dir = path.dirname(path.realpath('__file__'))


def csv_makedict(f_dir, f_name, k, v, enc):
    with open(path.join(f_dir, f_name), mode='r', encoding=enc) as csv_input:
        csv_read = csv.reader(csv_input)
        csv_dict = {rows[k]: rows[v] for rows in csv_read}
        return csv_dict

context_namelist = csv_makedict('resources', 'invTypes_small.csv', 0, 2, 'utf-8')
