#!/usr/bin/env python

import requests

def get_me_some_chuck(url):
    response = requests.get(url)
    json = response.json()
    quote = json['value']

    print(quote)

if __name__ == '__main__':
    get_me_some_chuck("https://api.chucknorris.io/jokes/random")