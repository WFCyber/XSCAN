import base64
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def Fofa(query, fields='host', page='1', size=100, all=0):
    url = 'https://fofa.info/api/v1/search/all'
    params = {
        "email": config['fofa']['email'],
        "key": config['fofa']['key'],
        "query": query,
        "fields": fields,
        "page": page,
        "size": size,
        "full": all
    }
    x = requests.get(url, params=params)
    return x
