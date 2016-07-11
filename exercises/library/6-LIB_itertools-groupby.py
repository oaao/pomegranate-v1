import itertools
import operator

data = [
    {'type': 'a', 'v1': 'off', 'v2': '1'},
    {'type': 'b', 'v1': 'off', 'v2': '1'},
    {'type': 'c', 'v1': 'on', 'v2': '1'},
    {'type': 'b', 'v1': 'off', 'v2': '2'},
    {'type': 'a', 'v1': 'on', 'v2': '2'},
    {'type': 'a', 'v1': 'on', 'v2': '3'}
]

sorted_data = sorted(data, key=operator.itemgetter('type'))
grouped_data = itertools.groupby(sorted_data, lambda x: x['type'])

new_data = {}
for k,v in grouped_data:
    new_data[k] = list(v)

print(new_data)

# issue: ['type'] remains inside new dict because it wasn't popped; will shit up DB
# solution: try collections.defaultdict()