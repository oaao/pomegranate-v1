import time
import requests
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
import arrow
import json
import csv
from os import path

base_dir = path.dirname(path.realpath('__file__'))


def market_configs(hub_spec):
    region = {
        'jita': [10000002, 60003760],
        'amarr': [10000043, 60008494],
        'dodixie': [10000032, 60011866],
        'hek': [10000042, 60005686],
        'rens': [10000030, 60004588]
    }
    hub_choice = region[hub_spec]
    return hub_choice


def url_format(region_spec):
    url_base = 'https://crest-tq.eveonline.com/market/' + region_spec + '/orders/all/'
    return url_base


def url_async(url_list, worker_limit):
    if worker_limit > 10:
        worker_limit = 10
    session = FuturesSession(executor=ThreadPoolExecutor(max_workers=worker_limit))
    response = (session.get(x).result().json() for x in url_list)
    return response


def group_dictvalue(raw_list, dictvalue):
    new_dict = {}
    for i in raw_list:
        new_key = i.pop(dictvalue)
        if new_key in new_dict:
            new_dict[new_key].append(i)
        else:
            new_dict[new_key] = [i]
    return new_dict


def csv_makedict(f_dir, f_name, k, v, enc):
    with open(path.join(f_dir, f_name), mode='r', encoding=enc) as csv_input:
        csv_read = csv.reader(csv_input)
        csv_dict = {rows[k]: rows[v] for rows in csv_read}
        return csv_dict


def market_import(hub_spec):
    data_configs = market_configs(hub_spec)
    hub_regionid = str(data_configs[0])
    url_base = url_format(hub_regionid)
    url_market = url_base + '?page='
    data_pages = requests.get(url_base).json()['pageCount']
    url_set = [url_market + str(x) for x in range(1, data_pages+1)]
    data_res = url_async(url_set, data_pages)
    data_items = [x for i in data_res for x in i['items']]
    return data_items, data_configs


def market_distill(raw_list, configs):
    data_total = raw_list
    hub_stationid = configs[1]
    data_hubonly = [x for x in data_total if hub_stationid == x['stationID']]
    data_timestamp = data_hubonly
    for i in range(0, len(data_hubonly)):
        order_time = arrow.get(data_hubonly[i]['issued'])
        data_timestamp[i]['issued'] = order_time.timestamp
    sort_choice = 'type'
    data_grouped_type = group_dictvalue(data_timestamp, sort_choice)
    data_grouped_buysell = {}
    sort_choice = 'buy'
    for k,v in data_grouped_type.items():
        buysell_grouped = group_dictvalue(v, sort_choice)
        data_grouped_buysell[k] = [buysell_grouped]
    sort_choice = 'stationID'
    data_grouped_station = {}
    for k,v in data_grouped_buysell.items():
        for order_pair in v:
            for order_type, order in order_pair.items():
                for attribute in order:
                    id_subgroup = attribute.pop(sort_choice)
        data_grouped_station[k] = {id_subgroup: v}
    return data_grouped_station


def market_context(raw_list):
    context_namelist = csv_makedict('resources', 'invTypes_small.csv', 0, 2, 'utf-8')
    # take out the station value from each
    # make a new list that contains:
    # - name that corresponds w/ ID
    # - station id
    # - pricing/volume info
    # add to dict such that {'typeid': [[orders],[context]]
    data_contextualised = ''
    return data_contextualised


def write_json(data_input):
    print('WRITE_JSON: Writing JSON to file.')
    with open(path.join('json', "orderbook_" + str(time.time()) + ".txt"), "w") as f_output:
        json.dump(data_input, f_output, indent=4)


def write_db():
    # write data structure to database
    pass


orders_raw, orders_config = market_import('rens')
orders_structured = market_distill(orders_raw, orders_config)
orders_contextualised = market_context(orders_structured)

write_json(orders_structured)
