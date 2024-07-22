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

from ..utilities.tracking.sdk_tracker import SdkTracker
class BinLookupApi(object):
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



    def get_account_info(self, create_bin_lookup_request, **kwargs):
        """
        BIN Lookup API
        The BIN Lookup Service is a versatile business tool that provides card network agnostic solution designed to ensure frictionless transaction experience by utilizing up-to-date Bank Identification Number (BIN) attributes sourced from multiple global and regional data sources. This service helps to improve authorization rates by helping to route transactions to the best-suited card network, minimizes fraud through card detail verification and aids in regulatory compliance by identifying card properties. The service is flexible and provides businesses  with a flexible choice of inputs such as primary account number (PAN), network token from major networks which includes device PAN (DPAN), and all types of tokens generated via CyberSource Token Management Service (TMS). Currently, the range of available credentials is contingent on the networks enabled for the business entity. Therefore, the network information specified in this documentation is illustrative and subject to personalized offerings for each reseller or merchant. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_info(create_bin_lookup_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateBinLookupRequest create_bin_lookup_request: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.

        DISCLAIMER:
                Cybersource may allow Customer to access, use, and/or test a Cybersource product or service that may still be in development or has not been market-tested ("Beta Product") solely for the purpose of evaluating the functionality or marketability of the Beta Product (a "Beta Evaluation"). Notwithstanding any language to the contrary, the following terms shall apply with respect to Customer's participation in any Beta Evaluation (and the Beta Product(s)) accessed thereunder): The Parties will enter into a separate form agreement detailing the scope of the Beta Evaluation, requirements, pricing, the length of the beta evaluation period ("Beta Product Form"). Beta Products are not, and may not become, Transaction Services and have not yet been publicly released and are offered for the sole purpose of internal testing and non-commercial evaluation. Customer's use of the Beta Product shall be solely for the purpose of conducting the Beta Evaluation. Customer accepts all risks arising out of the access and use of the Beta Products. Cybersource may, in its sole discretion, at any time, terminate or discontinue the Beta Evaluation. Customer acknowledges and agrees that any Beta Product may still be in development and that Beta Product is provided "AS IS" and may not perform at the level of a commercially available service, may not operate as expected and may be modified prior to release. CYBERSOURCE SHALL NOT BE RESPONSIBLE OR LIABLE UNDER ANY CONTRACT, TORT (INCLUDING NEGLIGENCE), OR OTHERWISE RELATING TO A BETA PRODUCT OR THE BETA EVALUATION (A) FOR LOSS OR INACCURACY OF DATA OR COST OF PROCUREMENT OF SUBSTITUTE GOODS, SERVICES OR TECHNOLOGY, (B) ANY CLAIM, LOSSES, DAMAGES, OR CAUSE OF ACTION ARISING IN CONNECTION WITH THE BETA PRODUCT; OR (C) FOR ANY INDIRECT, INCIDENTAL OR CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, LOSS OF REVENUES AND LOSS OF PROFITS.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_account_info` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_info_with_http_info(create_bin_lookup_request, **kwargs)
        else:
            (data) = self.get_account_info_with_http_info(create_bin_lookup_request, **kwargs)
            return data

    def get_account_info_with_http_info(self, create_bin_lookup_request, **kwargs):
        """
        BIN Lookup API
        The BIN Lookup Service is a versatile business tool that provides card network agnostic solution designed to ensure frictionless transaction experience by utilizing up-to-date Bank Identification Number (BIN) attributes sourced from multiple global and regional data sources. This service helps to improve authorization rates by helping to route transactions to the best-suited card network, minimizes fraud through card detail verification and aids in regulatory compliance by identifying card properties. The service is flexible and provides businesses  with a flexible choice of inputs such as primary account number (PAN), network token from major networks which includes device PAN (DPAN), and all types of tokens generated via CyberSource Token Management Service (TMS). Currently, the range of available credentials is contingent on the networks enabled for the business entity. Therefore, the network information specified in this documentation is illustrative and subject to personalized offerings for each reseller or merchant. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_info_with_http_info(create_bin_lookup_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateBinLookupRequest create_bin_lookup_request: (required)
        :return: InlineResponse2011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_bin_lookup_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_bin_lookup_request' is set
        if ('create_bin_lookup_request' not in params) or (params['create_bin_lookup_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_bin_lookup_request` when calling `get_account_info`")
            raise ValueError("Missing the required parameter `create_bin_lookup_request` when calling `get_account_info`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_bin_lookup_request' in params:
            body_params = params['create_bin_lookup_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'create_bin_lookup_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/bin/v1/binlookup', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2011',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
