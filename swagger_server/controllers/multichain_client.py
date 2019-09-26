import json
from swagger_server.controllers.rpc_client import *

def get_info():
    return multichain('getinfo', [])


# publish       stream key data-hex
# {"method":"publish","params":["agent001",["foo","key4"],{"json":{"name":"John Doe","city":"London"}}],"id":"69787723-1544172981","chain_name":"CompositionChain"}
def publish(agentIdPath,indexkeys,body):
    options = []
    options.append(agentIdPath)
    options.append(indexkeys)
    thedata = {}
    thedata["json"]=body
    options.append(thedata)
    return multichain('publish', options)

def createstream(agentIdPath):
    options = []
    options.append(agentIdPath)
    options.append(False)
    return multichain('create', options)

def liststreamitems(agentIdPath, verbose = False, count=10, start=-10, localordering=False):
    options = []
    options.append(agentIdPath)
    options.append(bool(verbose))
    options.append(int(count))
    options.append(int(start))
    options.append(bool(localordering))
    return multichain('liststreamitems', options)

# liststreamqueryitems stream1 '{"keys":["key4","key5"]}'
def liststreamqueryitems(agentIdPath, keys, verbose = False):
    options = []
    options.append(agentIdPath)
    keyobject = {}
    keyobject['keys'] = keys
    options.append(keyobject)
    options.append(bool(verbose))
    return multichain('liststreamqueryitems', options)

# def send_asset_with_data(address, asset, qty, data):
    # options = []
    # options.append(address)
    # _asset = {}
    # _asset[asset] = float(qty)
    # options.append(_asset)
    # options.append(data.encode("hex"))

    # return multichain('sendwithdata', options)

# def publish(stream, key, data):
    # options = []
    # options.append(stream)
    # options.append(key)
    # options.append(data.encode("hex"))

    # return multichain("publish", options)

# def publish_from(address, stream, key, data):
    # options = []
    # options.append(address)
    # options.append(stream)
    # options.append(key)
    # options.append(data.encode("hex"))

    # return multichain("publishfrom", options)
