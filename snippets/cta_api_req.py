import requests

def make_req(bus_api_key):
    url = 'http://www.ctabustracker.com/bustime/api/v2/getpredictions'
    params = {
        'key': bus_api_key,
        'stpid': 5960,
        'format': 'json'
    }

    r = requests.get(url, params=params)
    return r.json()
