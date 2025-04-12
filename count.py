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
