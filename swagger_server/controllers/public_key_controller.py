import connexion
import six

from swagger_server.models.public_key import PublicKey  # noqa: E501
from swagger_server import util

from swagger_server.controllers import multichain_client
from flask import Response
import json

import logging, sys

def add_public_key(body):  # noqa: E501
    """Add a new PublicKey (to the multichain stream)

     # noqa: E501

    :param body: PublicKey that should to be added to the blockchain
    :type body: dict | bytes

    :rtype: PublicKey
    """
    if connexion.request.is_json:
        json_body = connexion.request.get_json()
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug('add_public_key %r', json_body)
        body = PublicKey.from_dict(json_body)  # noqa: E501
        logging.debug('add_public_key', body)
        logging.debug('add_public_key',dir(body))
        indexkeys = []
        indexkeys.append('pki_name:'+body.public_keyname)
        indexkeys.append('pki_company_id:'+body.company_id)
        indexkeys.append('pki_agent_id:'+body.agent_id)
        multichain_client.publish("PKI",indexkeys, json_body)
        return Response(status=201, mimetype='application/json')
    else:
        return Response(status=405, mimetype='application/json')


def extract_time(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        print(int(json['blocktime']))
        return int(json['blocktime'])
    except KeyError:
        return 9999999999999;




def get_public_key(agentid=None, companyid=None):  # noqa: E501
    """Find PublicKeys by agent and/or company ID

    Returns a list of PublicKeys # noqa: E501

    :param agentid: Required to filter PublicKeys by agent.
    :type agentid: str
    :param companyid: Required to filter PublicKeys by company.
    :type companyid: str

    :rtype: PublicKey
    """
    keys = []
    if agentid is not None and agentid!='' and agentid != 'false':
        keys.append('pki_agent_id:'+agentid)
    if companyid is not None and companyid!='' and companyid != 'false':
        keys.append('pki_company_id:'+companyid)

    result = multichain_client.liststreamqueryitems ("PKI", keys)
    print(result)
    print('SORT')
    #print(type(result))
    j_result = json.loads(result);
    print(j_result)
    print(type(j_result))
    if j_result["error"] is None:
        if len(j_result["result"])>0:
            sortedjson = j_result["result"].sort(key=extract_time, reverse=True)
            print(sortedjson)
            return sortedjson
            #[0]["data"]["json"]
            #return j_result["result"][0]["data"]["json"]
        else:
            return Response(status=404, mimetype='application/json')
    else:
        return Response(status=500, mimetype='application/json')
