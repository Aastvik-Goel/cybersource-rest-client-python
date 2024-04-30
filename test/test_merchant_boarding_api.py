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
from CyberSource.apis.merchant_boarding_api import MerchantBoardingApi


class TestMerchantBoardingApi(unittest.TestCase):
    """ MerchantBoardingApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.merchant_boarding_api.MerchantBoardingApi()

    def tearDown(self):
        pass

    def test_get_registration(self):
        """
        Test case for get_registration

        Gets all the information on a boarding registration
        """
        pass

    def test_post_registration(self):
        """
        Test case for post_registration

        Create a boarding registration
        """
        pass


if __name__ == '__main__':
    unittest.main()
