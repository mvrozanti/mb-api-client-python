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

parser = argparse.ArgumentParser(description='Interface for mercadobitcoin.com.br API')
group = parser.add_mutually_exclusive_group()
group.add_argument('-l', action='store_const', const='list_orders',         help='list orders')
group.add_argument('-i', action='store_const', const='get_account_info',    help='get account info')
group.add_argument('-o', metavar='order id',                                help='get order')
group.add_argument('-b', action='store_const', const='list_orderbook',      help='list orderbook')
# group.add_argument('-', action='store_const', const='place_buy_order',    help='get account info')
# group.add_argument('-', action='store_const', const='cancel_order',       help='get account info')
# group.add_argument('-', action='store_const', const='get_withdrawal',     help='get account info')
# group.add_argument('-', action='store_const', const='withdraw_coin',     help='get account info')

op=vars(parser.parse_args())
if len(op) == 0: print 'Needs at least one argument' or sys.exit(1)

params, tapi_method = None,filter(None,op.values())[0]

params = {
    'tapi_method' : tapi_method,
    'tapi_nonce' : str(int(time.time())),
    'coin_pair' : 'BRLBTC'
    }

if op['o'] != None: 
    params['order_id'] = params['tapi_method']
    params['tapi_method'] = 'get_order'

try:
    conn = httplib.HTTPSConnection(REQUEST_HOST)
    params = urllib.urlencode(params)
    params_string = REQUEST_PATH + '?' + params
    H = hmac.new(MB_TAPI_SECRET, digestmod=hashlib.sha512)
    H.update(params_string)
    tapi_mac = H.hexdigest()
    headers = { 'Content-type': 'application/x-www-form-urlencoded', 'TAPI-ID': MB_TAPI_ID, 'TAPI-MAC': tapi_mac }
    conn.request('POST', REQUEST_PATH, params, headers)
    response = conn.getresponse()
    response = response.read()
    response_json = json.loads(response, object_pairs_hook=OrderedDict)
    print "status: %s" % response_json['status_code']
    print json.dumps(response_json, indent=4)
finally:
    if conn: conn.close()
