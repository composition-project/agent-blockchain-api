# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.message import Message  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMessageController(BaseTestCase):
    """MessageController integration test stubs"""

    def test_add_message(self):
        """Test case for add_message

        Add a new message (to the agent's multichain stream)
        """
        body = Message()
        response = self.client.open(
            '/v0_9_1/{agentIdPath}/Messages'.format(agentIdPath='agentIdPath_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_stream(self):
        """Test case for add_stream

        Add a new message stream (the agent's multichain stream)
        """
        response = self.client.open(
            '/v0_9_1/{agentIdPath}'.format(agentIdPath='agentIdPath_example'),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_message(self):
        """Test case for get_message

        Find Message by agent
        """
        response = self.client.open(
            '/v0_9_1/{agentIdPath}/Messages/{messageIdPath}'.format(agentIdPath='agentIdPath_example', messageIdPath='messageIdPath_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_messages(self):
        """Test case for get_messages

        Find Messages by agent
        """
        query_string = [('keys', 'keys_example')]
        response = self.client.open(
            '/v0_9_1/{agentIdPath}/Messages'.format(agentIdPath='agentIdPath_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
