data = {'1':
            [
                {
                    "stationid": 1001,
                    "buy": False,
                    "price": 11.0
                },
                {
                    "stationid": 1001,
                    "buy": True,
                    "price": 1.0
                }
            ],
        '2':
            [
                {
                    "stationid": 2002,
                    "buy": False,
                    "price": 22.0
                },
                {
                    "stationid": 2002,
                    "buy": True,
                    "price": 2.0
                }
            ]
        }


def group_dictvalue(raw_list, dictvalue):
    new_dict = {}
    for i in raw_list:
        new_key = i.pop(dictvalue)
        if new_key in new_dict:
            new_dict[new_key].append(i)
        else:
            new_dict[new_key] = [i]
    return new_dict

data_keys = []
data_values = []
for k, v in data.items():
    for i in v:
        #print(i)
        x = i.pop('buy')
        data_keys.append(x)
        y = i
        data_keys.append(y)
        #print(x, y)
        #d = {x: i for (x, i) in data.items()}
        #print(d)
        '''v1 = [{'buy': x}, [i for i in v]]
        a = {'buy': x}
        b = [i for i in v]
        print(b)
        #data_temp.append({k: v1})'''


'''for i in data_temp:
    #print(i)
    #print(i.items())
    for k, v in i.items():
        #print(k)
        #print(v)
        for n in v:
            print(n)'''



