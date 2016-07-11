import requests

url_base = "https://crest-tq.eveonline.com/market/"
url_orders = "/orders/all/"


def eval_200(resp):
    if len(resp.json()['items']) > 0:
        return "Valid ID; contains %s items." % len(resp.json()['items'])
    else:
        return "Invalid ID."


def eval_329(resp):
    return "Rate limit exceeded."


def eval_404(resp):
    return "Path not found."


def eval_500(resp):
    return "Internal Server Error: " + resp.json()['message']


http_evals = {
    200: eval_200,
    329: eval_329,
    404: eval_404,
    500: eval_500
}


def test_responses(resps, evals):
    for case in resps:
        r = requests.get(url_base + case + url_orders)
        code_info = evals[r.status_code](r)
        print("TEST INPUT: %s" % case)
        print("%s --- %s\n" % (r, code_info))

inputs = ["a", "2147483648", "2147483647", "10000002"]

test_responses(inputs, http_evals)

# redo using raise_for_status() method for requests objects
