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
from CyberSource.apis.create_new_webhooks_api import CreateNewWebhooksApi


class TestCreateNewWebhooksApi(unittest.TestCase):
    """ CreateNewWebhooksApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.create_new_webhooks_api.CreateNewWebhooksApi()

    def tearDown(self):
        pass

    def test_create_webhook_subscription(self):
        """
        Test case for create_webhook_subscription

        Create a Webhook
        """
        pass

    def test_find_products_to_subscribe(self):
        """
        Test case for find_products_to_subscribe

        Find Products You Can Subscribe To
        """
        pass

    def test_save_sym_egress_key(self):
        """
        Test case for save_sym_egress_key

        Create Webhook Security Keys
        """
        pass


if __name__ == '__main__':
    unittest.main()
