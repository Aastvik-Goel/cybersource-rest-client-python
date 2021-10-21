# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
import CyberSource.logging.log_factory as LogFactory


class AsymmetricKeyManagementApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config)
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.api_client.mconfig.log_config)



    def create_p12_keys(self, create_p12_keys_request, **kwargs):
        """
        Create one or more PKCS#12 keys
        'Create one or more PKCS#12 keys' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_p12_keys(create_p12_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateP12KeysRequest create_p12_keys_request: (required)
        :return: KmsV2KeysAsymPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_p12_keys` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_p12_keys_with_http_info(create_p12_keys_request, **kwargs)
        else:
            (data) = self.create_p12_keys_with_http_info(create_p12_keys_request, **kwargs)
            return data

    def create_p12_keys_with_http_info(self, create_p12_keys_request, **kwargs):
        """
        Create one or more PKCS#12 keys
        'Create one or more PKCS#12 keys' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_p12_keys_with_http_info(create_p12_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateP12KeysRequest create_p12_keys_request: (required)
        :return: KmsV2KeysAsymPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_p12_keys_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_p12_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_p12_keys_request' is set
        if ('create_p12_keys_request' not in params) or (params['create_p12_keys_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_p12_keys_request` when calling `create_p12_keys`")
            raise ValueError("Missing the required parameter `create_p12_keys_request` when calling `create_p12_keys`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_p12_keys_request' in params:
            body_params = params['create_p12_keys_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/kms/v2/keys-asym', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KmsV2KeysAsymPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_bulk_p12_keys(self, delete_bulk_p12_keys_request, **kwargs):
        """
        Delete one or more PKCS#12 keys
        'Delete one or more PKCS#12 keys' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bulk_p12_keys(delete_bulk_p12_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeleteBulkP12KeysRequest delete_bulk_p12_keys_request: (required)
        :return: KmsV2KeysAsymDeletesPost200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `delete_bulk_p12_keys` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_bulk_p12_keys_with_http_info(delete_bulk_p12_keys_request, **kwargs)
        else:
            (data) = self.delete_bulk_p12_keys_with_http_info(delete_bulk_p12_keys_request, **kwargs)
            return data

    def delete_bulk_p12_keys_with_http_info(self, delete_bulk_p12_keys_request, **kwargs):
        """
        Delete one or more PKCS#12 keys
        'Delete one or more PKCS#12 keys' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bulk_p12_keys_with_http_info(delete_bulk_p12_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeleteBulkP12KeysRequest delete_bulk_p12_keys_request: (required)
        :return: KmsV2KeysAsymDeletesPost200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delete_bulk_p12_keys_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bulk_p12_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delete_bulk_p12_keys_request' is set
        if ('delete_bulk_p12_keys_request' not in params) or (params['delete_bulk_p12_keys_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `delete_bulk_p12_keys_request` when calling `delete_bulk_p12_keys`")
            raise ValueError("Missing the required parameter `delete_bulk_p12_keys_request` when calling `delete_bulk_p12_keys`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delete_bulk_p12_keys_request' in params:
            body_params = params['delete_bulk_p12_keys_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/kms/v2/keys-asym/deletes', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KmsV2KeysAsymDeletesPost200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_p12_key_details(self, key_id, **kwargs):
        """
        Retrieves PKCS#12 key details
        Retrieves keys details by providing the key id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_p12_key_details(key_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key_id: Key ID.  (required)
        :return: KmsV2KeysAsymGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_p12_key_details` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_p12_key_details_with_http_info(key_id, **kwargs)
        else:
            (data) = self.get_p12_key_details_with_http_info(key_id, **kwargs)
            return data

    def get_p12_key_details_with_http_info(self, key_id, **kwargs):
        """
        Retrieves PKCS#12 key details
        Retrieves keys details by providing the key id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_p12_key_details_with_http_info(key_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key_id: Key ID.  (required)
        :return: KmsV2KeysAsymGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_p12_key_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params) or (params['key_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `key_id` when calling `get_p12_key_details`")
            raise ValueError("Missing the required parameter `key_id` when calling `get_p12_key_details`")


        collection_formats = {}

        path_params = {}
        if 'key_id' in params:
            path_params['keyId'] = params['key_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/kms/v2/keys-asym/{key_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KmsV2KeysAsymGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
