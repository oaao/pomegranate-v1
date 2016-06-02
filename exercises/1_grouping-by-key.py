data = [{'type': 'a', 'v1': '1', 'v2': '1'},
           {'type': 'b', 'v1': '1', 'v2': '1'},
           {'type': 'c', 'v1': '1', 'v2': '1'},
           {'type': 'b', 'v1': '2', 'v2': '2'},
           {'type': 'a', 'v1': '2', 'v2': '2'},
           {'type': 'a', 'v1': '3', 'v2': '3'}]


def sort_types(my_list):
    new_dict = {}
    for i in my_list:
        new_key = i.pop('type')
        if new_key in new_dict:
            new_dict[new_key].append(i)
        else:
            new_dict[new_key] = [i]
    return new_dict


def print_dict(my_list):
    for i in my_list:
        print(i, my_list[i])


new_data = sort_types(data)
print_dict(new_data)
print(new_data)
