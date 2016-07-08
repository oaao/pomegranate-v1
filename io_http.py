# handle all HTTP / CREST API work:
# input validation, correctly navigating CREST endpoints, rate limiting, async retrieval

import requests
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession


def url_format(region_id, req_type):
    url_parent = 'https://crest-tq.eveonline.com/market/'
    if req_type is 'orders':
        url_result = url_parent + region_id + '/orders/all/'
    elif req_type is 'context':
        url_result = url_parent + region_id + '/inventory/types/'
    return url_result


def url_async(url_list, worker_limit):
    if worker_limit > 10:
        worker_limit = 10
    session = FuturesSession(executor=ThreadPoolExecutor(max_workers=worker_limit))
    response = (session.get(x).result().json() for x in url_list)
    return response
