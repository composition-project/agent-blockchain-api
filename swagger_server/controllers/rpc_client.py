import datetime
import os
import json
import requests
import logging, sys
from requests.auth import HTTPBasicAuth

from swagger_server import conf

cfg = conf.read_configuration()

def multichain(method, params):
    return json_rpc_send(os.getenv('RPC_HOST', cfg.get('multichain', 'rpc_host')),
                         os.getenv('RPC_PORT', cfg.get('multichain', 'rpc_port')),
                         os.getenv('RPC_USERNAME', cfg.get('multichain', 'rpc_username')),
                         os.getenv('RPC_PASSWORD', cfg.get('multichain', 'rpc_password')),
                         method, params)

def json_rpc_send(host, port, user, password, method, params):
    url = 'http://' + host + ':' + str(port)

    payload = {}
    payload['id'] = str(datetime.datetime.now())
    payload['method'] = method
    payload['params'] = params

    headers = {'content-type': 'application/json'}

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug('josn_rpc_send %r', payload)

    req = requests.post(url, data=json.dumps(payload), headers=headers,
                        auth=HTTPBasicAuth(user, password))
    return req.text

