# read and process raw data, store processed data

# using config(?) and io_db, calculate the following and store its end-result data to db:
# - raw profitability ("hypothetical")
# - competitiveness of orders per typeID per hub
# - END-RESULT [DB]: competition-factored profitability ("actual")
# - END-RESULT [DB]: per-orderID update behaviours

import config
import io_http
import arrow
# remove specific dependency:
import requests


def group_dictvalue(raw_list, dictvalue):
    new_dict = {}
    for i in raw_list:
        new_key = i.pop(dictvalue)
        if new_key in new_dict:
            new_dict[new_key].append(i)
        else:
            new_dict[new_key] = [i]
    return new_dict


def market_import(hub_spec):
    data_configs = config.market_configs(hub_spec)
    hub_regionid = str(data_configs[0])
    url_base = io_http.url_format(hub_regionid, 'orders')
    url_market = url_base + '?page='
    data_pages = requests.get(url_base).json()['pageCount']
    url_set = [url_market + str(x) for x in range(1, data_pages+1)]
    data_res = io_http.url_async(url_set, data_pages)
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


def market_context(raw_list, configs):
    data_distilled = raw_list
    hub_regionid = str(configs[0])
    type_ids = data_distilled.keys()
    url_context = io_http.url_format(hub_regionid, 'context')
    url_set = [url_context + str(x) + '/history/' for x in type_ids]
    data_res = io_http.url_async(url_set, len(type_ids))
    # need to restructure this so the typeID is preserved
    # data_context = [x for i in data_res for x in i['items']]
    # make a new list that contains:
    # - pricing/volume info
    # add to dict such that {'typeid': [[orders],[context]]
    data_contextualised = {}
    return data_contextualised
