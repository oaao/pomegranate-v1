import time
import requests
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
import json


def market_configs():
    region = {
        'jita': [10000002, 60003760],
        'amarr': [10000043, 60008494],
        'dodixie': [10000032, 60011866],
        'hek': [10000042, 60005686],
        'rens': [10000030, 60004588]
    }
    hub_choice = region['jita']
    return hub_choice


def url_format(region_spec):
    url_base = 'https://crest-tq.eveonline.com/market/' + region_spec + '/orders/all/'
    return url_base


def market_import():
    data_configs = market_configs()
    hub_regionid = str(data_configs[0])
    url_base = url_format(hub_regionid)
    url_market = url_base + '?page='
    t0 = time.time()
    data_pages = requests.get(url_base).json()['pageCount']
    url_set = [url_market + str(x) for x in range(1, data_pages+1)]
    print(url_set[0])
    print("--- %s seconds ---\n" % (time.time() - t0))
    t1 = time.time()
    session = FuturesSession(executor=ThreadPoolExecutor(max_workers=data_pages))
    data_res = (session.get(x).result().json() for x in url_set)
    data_items = [x for i in data_res for x in i['items']]
    print("--- %s seconds ---\n" % (time.time() - t1))
    '''for pages in range(1, data_pages+1, 1):
        data_append = requests.get(url_base + '?page=' + str(pages)).json()
        data_items += data_append['items']'''
    return data_items, data_configs

orders_raw, orders_config = market_import()
with open("json" + str(time.time()) + ".txt", "w") as f_output:
    json.dump(orders_raw, f_output, indent=4)
