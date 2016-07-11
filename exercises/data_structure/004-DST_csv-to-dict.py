# Will open the EVE SDE invTypes.csv and
# create a dictionary matching typeID (L11"rows[0]") to its name (L11"rows[2]").

import csv
from os import path

exercises_dir = path.dirname(path.realpath('__file__'))
res_dir = path.abspath(path.realpath(path.join(exercises_dir, '../../resources')))

with open(path.join(res_dir, 'invTypes.csv'), mode='r', encoding="utf8") as csv_input:
    csv_read = csv.reader(csv_input)
    new_dict = {rows[0]: rows[2] for rows in csv_read}

# Should return 'Arkonor'.
print(new_dict['22'])
