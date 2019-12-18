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
from CyberSource.apis.download_xsd_api import DownloadXSDApi


class TestDownloadXSDApi(unittest.TestCase):
    """ DownloadXSDApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.download_xsd_api.DownloadXSDApi()

    def tearDown(self):
        pass

    def test_get_xsdv2(self):
        """
        Test case for get_xsdv2

        Download XSD for report
        """
        pass


if __name__ == '__main__':
    unittest.main()