from datetime import datetime
import json
import requests


# This function returns kp data in json format and converts the json data to a list.
def get_kp_json():
    try:
        kp_url = requests.get('https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json')
        kp_text = kp_url.text
        kp_data = json.loads(kp_text)
        return kp_data
    except requests.exceptions.ConnectionError:
        return 'No Data Available'


# This function returns bz data in json format and converts the json data to a list.
def get_bz_json():
    try:
        bz_url = requests.get('https://services.swpc.noaa.gov/products/solar-wind/mag-2-hour.json')
        bz_text = bz_url.text
        bz_data = json.loads(bz_text)
        # print(bz_data)
        return bz_data
    except requests.exceptions.ConnectionError:
        return 'No Data Available'


# This function returns the most recent kp measurement.
def get_kp():
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d')
    kp = get_kp_json()
    matching_dates = []
    for k in kp:
        if formatted_now == k[0][0:10]:
            matching_dates.append(k)
    if len(matching_dates) > 1:
        last_kp = matching_dates[-1]
        print(last_kp)
        print(last_kp[1])
        return last_kp[1]


# This function returns the most recent bz measurement.
def get_bz():
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d')
    bz = get_bz_json()
    matching_dates = []
    for k in bz:
        if formatted_now == k[0][0:10]:
            matching_dates.append(k)
    if len(matching_dates) > 1:
        last_bz = matching_dates[-1]
        print(last_bz)
        print(last_bz[3])
        return last_bz[3]
