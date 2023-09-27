import datetime

import requests


def is_prime(number: int):
    if number < 0 or number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_jakarta_weather():
    url = "https://api.openweathermap.org/data/2.5/forecast?lat=-6.208763&lon=106.845599&appid=29bcfb0c8db724e8dd1942a48dbb4938&units=metric"  # TODO: move the API KEY to environment variable

    payload = {}
    headers = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    except:
        return None


def format_date(epochmill: str):
    DATE_FORMAT = "%a, %d %b %Y"

    return datetime.datetime.fromtimestamp(epochmill).strftime(DATE_FORMAT)
