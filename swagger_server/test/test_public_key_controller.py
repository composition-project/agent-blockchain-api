# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.public_key import PublicKey  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPublicKeyController(BaseTestCase):
    """PublicKeyController integration test stubs"""

    def test_add_public_key(self):
        """Test case for add_public_key

        Add a new PublicKey (to the multichain stream)
        """
        body = PublicKey()
        response = self.client.open(
            '/v0_9_1/PublicKeys',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_public_key(self):
        """Test case for get_public_key

        Find PublicKeys by agent and/or company ID
        """
        query_string = [('agentid', 'false'),
                        ('companyid', 'false')]
        response = self.client.open(
            '/v0_9_1/PublicKeys',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
