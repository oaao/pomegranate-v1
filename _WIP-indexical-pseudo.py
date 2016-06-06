import requests
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
import arrow
import json

# uncomment for console logging; comma-separates thousands
# c_str = lambda x: "{:,}".format(x)

# introduce classes


def group_dictvalue(raw, dictvalue):
    # group items in a dict by a key
    pass


def market_configs():
    # specify regional parameters
    pass


def url_format(spec):
    # determine API URL as per given parameters
    pass


def url_workers(workers):
    # parallelize connections
    pass


def market_importorders():
    # execute API pulls for orderbook
    pass


def market_importcontext():
    # execute API pulls for historical data, to be used after distillation
    pass


def market_distill():
    # purge unwanted orders, format by type, split buy/sell, and affix historical data
    pass


def db_write():
    # write python data structure to db
    pass
