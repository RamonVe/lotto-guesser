from datetime import datetime
import json
import requests


# This function returns kp data in json format and converts the json data to a list.
def get_kp_json():
    try:
        kp_url = requests.get('https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json', timeout=5)
        kp_text = kp_url.text
        kp_data = json.loads(kp_text)
        return kp_data
    except requests.exceptions.Timeout:
        return ['']


# This function returns bz data in json format and converts the json data to a list.
def get_bz_json():
    try:
        bz_url = requests.get('https://services.swpc.noaa.gov/products/solar-wind/mag-1-day.json', timeout=5)
        bz_text = bz_url.text
        bz_data = json.loads(bz_text)
        return bz_data
    except requests.exceptions.Timeout:
        return ['']


# This function returns the most recent kp measurement.
# Sometimes the data will not be returned.
# There is a null check to return string Try Later.
def get_kp():
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d')
    kp = get_kp_json()
    matching_dates = []
    for k in kp:
        if k == '':
            return 'Try Later'
        if formatted_now == k[0][0:10]:
            matching_dates.append(k)
    if len(matching_dates) > 1:
        last_kp = matching_dates[-1]
        return last_kp[1]


# This function returns the most recent bz measurement.
# Sometimes the data will not be returned.
# There is a null check to return string Try Later.
def get_bz():
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d')
    bz = get_bz_json()
    matching_dates = []
    for b in bz:
        if b == '':
            return 'Try Again'
        if formatted_now == b[0][0:10]:
            matching_dates.append(b)
    if len(matching_dates) > 1:
        last_bz = matching_dates[-1]
        return last_bz[1]


print(get_kp())
print(get_bz())