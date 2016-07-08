import csv
import json
import time
from os import path

base_dir = path.dirname(path.realpath('__file__'))


def csv_makedict(f_dir, f_name, k_col, v_col, enc):
    with open(path.join(f_dir, f_name), mode='r', encoding=enc) as csv_input:
        csv_read = csv.reader(csv_input)
        csv_dict = {rows[k_col]: rows[v_col] for rows in csv_read}
        return csv_dict

# context_namelist = csv_makedict('resources', 'invTypes_small.csv', k_col=0, v_col=2, enc='utf-8')


def write_json(data_input, ind):
    with open(path.join('json', "orderbook_" + str(time.time()) + ".txt"), "w") as f_output:
        json.dump(data_input, f_output, indent=4)
