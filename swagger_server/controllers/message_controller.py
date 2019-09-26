import connexion
import six

from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


from swagger_server.controllers import multichain_client
from flask import Response
import json

def add_message(agentIdPath, body):  # noqa: E501
    """Add a new message (to the agent&#39;s multichain stream)

    Adds a new Message  # noqa: E501

    :param agentIdPath: ID of marketplace agent
    :type agentIdPath: str
    :param body: Message that should to be added to the blockchain
    :type body: dict | bytes

    :rtype: Message
    """
    if connexion.request.is_json:
        json_body = connexion.request.get_json()
        body = Message.from_dict(json_body)  # noqa: E501
        body.indexkeys.append('id:'+body.id)
        json_body['indexkeys'].append('id:'+json_body['id'])
        multichain_client.publish(agentIdPath,body.indexkeys, json_body)
        return Response(status=201, mimetype='application/json')
    else:
        return Response(status=405, mimetype='application/json')



def add_stream(agentIdPath):  # noqa: E501
    """Add a new message stream (the agent&#39;s multichain stream)

    Adds a new Message Stream for the agent. This must be performed before adding or querying for messages. # noqa: E501

    :param agentIdPath: ID of marketplace agent
    :type agentIdPath: str

    :rtype: Message
    """
    return multichain_client.createstream(agentIdPath)


def get_message(agentIdPath, messageIdPath):  # noqa: E501
    """Find Message by agent

    Returns the Message with the given messageId # noqa: E501

    :param agentIdPath: ID of marketplace agent
    :type agentIdPath: str
    :param messageIdPath: ID of message
    :type messageIdPath: str

    :rtype: Message
    """
    keys = ["id:"+messageIdPath]
    result = multichain_client.liststreamqueryitems (agentIdPath, keys, verbose)
    print(result)
    print(type(result))
    j_result = json.loads(result);
    print(j_result)
    print(type(j_result))
    if j_result["error"] is None:
        if len(j_result["result"])>0:
            return j_result["result"][0]["data"]["json"]
        else:
            return Response(status=404, mimetype='application/json')
    else:
        return Response(status=500, mimetype='application/json')


def get_messages(agentIdPath, keys=None):  # noqa: E501
    """Find Messages by agent

    Returns a list of Messages for this agent # noqa: E501

    :param agentIdPath: ID of marketplace agent
    :type agentIdPath: str
    :param keys: The keys to use as filter.
    :type keys: List[str]

    :rtype: Message
    """
     verbose = False
    print(keys)
    print(type(keys))
    result = multichain_client.liststreamqueryitems (agentIdPath, keys, verbose)
    print(result)
    print(type(result))
    j_result = json.loads(result);
    print(j_result)
    print(type(j_result))
    if j_result["error"] is None:
         if len(j_result["result"])>0:
            return [o["data"]["json"] for o in j_result["result"]]
        else:
            return []
    else:
        return Response(status=500, mimetype='application/json')

