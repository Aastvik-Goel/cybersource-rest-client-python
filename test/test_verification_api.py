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
from CyberSource.apis.verification_api import VerificationApi


class TestVerificationApi(unittest.TestCase):
    """ VerificationApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.verification_api.VerificationApi()

    def tearDown(self):
        pass

    def test_validate_export_compliance(self):
        """
        Test case for validate_export_compliance

        Validate export compliance
        """
        pass

    def test_verify_customer_address(self):
        """
        Test case for verify_customer_address

        Verify customer address
        """
        pass


if __name__ == '__main__':
    unittest.main()
