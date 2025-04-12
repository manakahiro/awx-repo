#
#
import os
import configparser
import requests
import datetime
import dateutil.parser
conf = configparser.ConfigParser()
conf.read("Token.ini")
base = conf["DEFAULT"]["BaseURL"]
token = conf["DEFAULT"]["Token"]

print( base )
print( sum( [x for x in range(1, 100 + 1)] ))

headers = { 'Authorization' : f'Bearer {token}' }

r = requests.get(base + "/api/v2/jobs/?order_by=-created&page_size=5", headers = headers)

if r.ok:
    print( r.text )
