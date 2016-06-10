import pprint

data = {
        'b':
            [
                {'off': [{'v2': '1', 'popme': 'x'}, {'v2': '2', 'popme': 'y'}]}
            ],
        'c':
            [
                {'on': [{'v2': '1', 'popme': 'x'}]}
            ],
        'a': [
                {'off': [{'v2': '1', 'popme': 'x'}],
                 'on': [{'v2': '2', 'popme': 'y'}, {'v2': '3', 'popme': 'y'}]}
            ]
}


def sort_types(my_list, my_key):
    new_dict = {}
    for i in my_list:
        new_key = i.pop(my_key)
        if new_key in new_dict:
            new_dict[new_key].append(i)
        else:
            new_dict[new_key] = [i]
    return new_dict

data_manual = data
data_pop_m = {}
for k,v in data_manual.items():
    new_pop = ''
    for i in v:
        for x, y in i.items():
            for val in y:
                new_pop = val.pop('popme')
    data_pop_m[k] = [{new_pop: v}, {'a descriptor': new_pop}]

for k,v in data_pop_m.items():
    print(k)
    for i in v:
        pprint.pprint(i)
