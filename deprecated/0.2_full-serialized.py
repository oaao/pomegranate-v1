import requests
import time
import arrow
import json

c_str = lambda x: "{:,}".format(x)


def market_configs():
    region = {
        'jita': [10000002, 60003760],
        'amarr': [10000043, 60008494],
        'dodixie': [10000032, 60011866],
        'hek': [10000042, 60005686],
        'rens': [10000030, 60004588]
    }
    hub_select = ''
    '''while hub_select not in region:
        hub_select = input('Jita, Amarr, Dodixie, Hek, Rens?\n').lower()
    hub_choice = region.get(hub_select)'''
    hub_choice = region['jita']
    return hub_choice


def url_format(region_spec):
    url_base = 'https://crest-tq.eveonline.com/market/' + region_spec + '/orders/all/'
    return url_base


def group_dictvalue(raw_list, dictvalue):
    new_dict = {}
    for i in raw_list:
        new_key = i.pop(dictvalue)
        if new_key in new_dict:
            new_dict[new_key].append(i)
        else:
            new_dict[new_key] = [i]
    return new_dict


def market_import():
    t0 = time.time()
    data_configs = market_configs()
    hub_regionid = str(data_configs[0])
    url_market = url_format(hub_regionid)
    print('\nMARKET_IMPORT: Trying: %s' % url_market)
    data_items = []
    data_pages = requests.get(url_market).json()['pageCount']
    print('MARKET_IMPORT: %s pages found.' % (str(data_pages)))
    for pages in range(1, data_pages+1, 1):
        data_append = requests.get(url_market + '?page=' + str(pages)).json()
        data_items += data_append['items']
    print('MARKET_IMPORT: %s total entries combined.' % (c_str(len(data_items))))
    print("--- %s seconds ---\n" % (time.time() - t0))
    return data_items, data_configs


def market_distill(raw_list, configs):
    t_hub = time.time()
    print('MARKET_DISTILL: Purging all non-hub orders.')
    data_total = raw_list
    hub_stationid = configs[1]
    data_hubonly = [x for x in data_total if hub_stationid == x['stationID']]
    print('MARKET_DISTILL: %s total entries, %s entries purged.'
          % (c_str(len(data_hubonly)), c_str(len(raw_list) - len(data_hubonly))))
    print("--- %s seconds ---\n" % (time.time() - t_hub))
    t_timestamp = time.time()
    print('MARKET_DISTILL: Converting order times to integer timestamps with Arrow.')
    data_timestamp = data_hubonly
    for i in range(0, len(data_hubonly)):
        order_time = arrow.get(data_hubonly[i]['issued'])
        data_timestamp[i]['issued'] = order_time.timestamp
    print('MARKET_DISTILL: %s total entries updated.' % (c_str(len(data_timestamp))))
    print("--- %s seconds ---\n" % (time.time() - t_timestamp))
    sort_choice = 'type'
    t_typesort = time.time()
    data_typesort = group_dictvalue(data_timestamp, sort_choice)
    print('MARKET_DISTILL: %s total entries grouped by %s items.'
          % (c_str(len(data_timestamp)), c_str(len(data_typesort))))
    print("--- %s seconds ---\n" % (time.time() - t_typesort))
    # group by buys, sells (or database?)
    # add a name field for each id
    return data_typesort

t0 = time.time()
orders_raw, orders_config = market_import()
orders_structured = market_distill(orders_raw, orders_config)[17464]
t_p_json = time.time()
print('MARKET_PRINT: Writing JSON to file.')
with open("structured_json_concurrent.txt", "w") as f_output:
    json.dump(orders_structured, f_output)
print("--- %s seconds ---\n" % (time.time() - t_p_json))
t_p_raw = time.time()
print('MARKET_PRINT: Writing as-string Python data to file.')
with open("structured_raw.txt", "w") as f_output:
    f_output.write(str(orders_structured))
print("--- %s seconds ---\n" % (time.time() - t_p_raw))
# print('EXAMPLE_PRINT: Orders for Massive Scordite')
# print(orders_structured[17464])
print("--- %s seconds ---\n" % (time.time() - t0))
