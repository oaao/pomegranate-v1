# correct asynchronous implementation of requests-futures
# as opposed to /exercises/2-LIB_requests-futures.py

import logging
import sys

import concurrent.futures as cf
from requests_futures.sessions import FuturesSession

TEST_URL = 'https://crest-tq.eveonline.com/market/10000002/orders/all/?page='

logging.basicConfig(
    stream=sys.stderr, level=logging.INFO,
    format='%(relativeCreated)s %(message)s',
    )

session = FuturesSession(max_workers=10)
futures = []

data = []

logging.info('Sending requests to CREST API')
for n in range(1, 20):
    try_url = TEST_URL + str(n)
    future = session.get(try_url)
    futures.append(future)

logging.info('Requests sent; awaiting responses')

for future in cf.as_completed(futures, timeout=15):
    res = future.result()
    if 'items' in res.json() and len(res.json()['items']) > 0:
        logging.info('OK: [%s items] %s' % (len(res.json()['items']), res.url))
        data.append(res.json()['items'])
    elif 'items' in res.json() and len(res.json()['items']) == 0:
        logging.info('ERROR: [data is empty] %s' % res.url)
    else:
        logging.info('ERROR: [unknown exception]')

logging.info('Process complete')

