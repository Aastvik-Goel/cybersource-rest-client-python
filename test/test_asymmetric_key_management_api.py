# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.asymmetric_key_management_api import AsymmetricKeyManagementApi


class TestAsymmetricKeyManagementApi(unittest.TestCase):
    """ AsymmetricKeyManagementApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.asymmetric_key_management_api.AsymmetricKeyManagementApi()

    def tearDown(self):
        pass

    def test_create_p12_keys(self):
        """
        Test case for create_p12_keys

        Create one or more PKCS12 keys
        """
        pass

    def test_delete_bulk_p12_keys(self):
        """
        Test case for delete_bulk_p12_keys

        Delete one or more PKCS12 keys
        """
        pass

    def test_get_p12_key_details(self):
        """
        Test case for get_p12_key_details

        Retrieves PKCS12 key details
        """
        pass

    def test_update_asym_key(self):
        """
        Test case for update_asym_key

        Activate or De-activate Asymmetric Key
        """
        pass


if __name__ == '__main__':
    unittest.main()
