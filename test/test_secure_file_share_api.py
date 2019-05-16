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
from CyberSource.apis.secure_file_share_api import SecureFileShareApi


class TestSecureFileShareApi(unittest.TestCase):
    """ SecureFileShareApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.secure_file_share_api.SecureFileShareApi()

    def tearDown(self):
        pass

    def test_get_file(self):
        """
        Test case for get_file

        Download a file with file identifier
        """
        pass

    def test_get_file_detail(self):
        """
        Test case for get_file_detail

        Get list of files
        """
        pass


if __name__ == '__main__':
    unittest.main()