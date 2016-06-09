# example dict
data = [
    {'type': 'a', 'v1': 'off', 'v2': '1'},
    {'type': 'b', 'v1': 'off', 'v2': '1'},
    {'type': 'c', 'v1': 'on', 'v2': '1'},
    {'type': 'b', 'v1': 'off', 'v2': '2'},
    {'type': 'a', 'v1': 'on', 'v2': '2'},
    {'type': 'a', 'v1': 'on', 'v2': '3'}
]


def sort_types(my_list, my_key):
    new_dict = {}
    for i in my_list:
        new_key = i.pop(my_key)
        if new_key in new_dict:
            new_dict[new_key].append(i)
        else:
            new_dict[new_key] = [i]
    return new_dict


def print_dict(my_list):
    for i in my_list:
        print(i, my_list[i])

sort_param = 'type'
data_sorted_type = sort_types(data, sort_param)

data_sorted_subtype = {}
sort_subtype_param = 'v1'

for k,v in data_sorted_type.items():
    sorted_subtype_value = sort_types(v, sort_subtype_param)
    data_sorted_subtype[k] = [sorted_subtype_value]

print(data_sorted_subtype)
