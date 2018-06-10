#!/usr/bin/env python
import argparse
import hashlib
import hmac
import httplib
import json
import urllib
import os
import time
from collections import OrderedDict

MB_TAPI_ID = os.environ['MERCADO_BTC_ID']
MB_TAPI_SECRET = os.environ['MERCADO_BTC_PASS']
REQUEST_HOST = 'www.mercadobitcoin.net'
REQUEST_PATH = '/tapi/v3/'
NONCE = str(int(time.time()))

parser = argparse.ArgumentParser(description='Interface for mercadobitcoin.com.br API')
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', action='store_const', const='list_orders', help='list orders')
# parser.add_argument('-l', action='store_true', help='list orders')
# parser.add_argument('-l', action='store_true', help='list orders')
# parser.add_argument('-l', action='store_true', help='list orders')
parsed_args = parser.parse_args()

params, tapi_method = None,None
print 'l' in parsed_args
print vars(parsed_args)
params = {
        'tapi_method': 'list_orders',
        'NONCE': NONCE,
        'coin_pair': 'BRLBTC'
        }
# if parsed_args.l: 
    # list orders 
#     # list orders 
#     params = {
#             'tapi_method': 'list_system_messages',
#             'NONCE': NONCE,
#             'coin_pair': 'BRLBTC'
#             }
# 
#     try:
#         conn = httplib.HTTPSConnection(REQUEST_HOST)
#     params = urllib.urlencode(params)
#     params_string = REQUEST_PATH + '?' + params
#     H = hmac.new(MB_TAPI_SECRET, digestmod=hashlib.sha512)
#     H.update(params_string)
#     tapi_mac = H.hexdigest()
#     conn.request("POST", REQUEST_PATH, params, { 'Content-type': 'application/x-www-form-urlencoded', 'TAPI-ID': MB_TAPI_ID, 'TAPI-MAC': tapi_mac })
#     response = conn.getresponse()
#     response = response.read()
#     response_json = json.loads(response, object_pairs_hook=OrderedDict)
#     print "status: %s" % response_json['status_code']
#     print json.dumps(response_json, indent=4)
# finally:
#     if conn: conn.close()
