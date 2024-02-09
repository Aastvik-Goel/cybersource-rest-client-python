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
class ReportDownloadsApi(object):
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



    def download_report(self, report_date, report_name, **kwargs):
        """
        Download a Report
        Download a report using the unique report name and date. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download_report(report_date, report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date report_date: Valid date on which to download the report in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**  yyyy-mm-dd For reports that span multiple days, this value would be the end date of the report in the time zone of the report subscription. Example 1: If your report start date is 2020-03-06 and the end date is 2020-03-09, the reportDate passed in the query is 2020-03-09. Example 2: If your report runs from midnight to midnight on 2020-03-09, the reportDate passed in the query is 2020-03-10  (required)
        :param str report_name: Name of the report to download (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `download_report` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.download_report_with_http_info(report_date, report_name, **kwargs)
        else:
            (data) = self.download_report_with_http_info(report_date, report_name, **kwargs)
            return data

    def download_report_with_http_info(self, report_date, report_name, **kwargs):
        """
        Download a Report
        Download a report using the unique report name and date. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.download_report_with_http_info(report_date, report_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date report_date: Valid date on which to download the report in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format.[Rfc Date Format](https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14)  **Example date format:**  yyyy-mm-dd For reports that span multiple days, this value would be the end date of the report in the time zone of the report subscription. Example 1: If your report start date is 2020-03-06 and the end date is 2020-03-09, the reportDate passed in the query is 2020-03-09. Example 2: If your report runs from midnight to midnight on 2020-03-09, the reportDate passed in the query is 2020-03-10  (required)
        :param str report_name: Name of the report to download (required)
        :param str organization_id: Valid Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_date', 'report_name', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_date' is set
        if ('report_date' not in params) or (params['report_date'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `report_date` when calling `download_report`")
            raise ValueError("Missing the required parameter `report_date` when calling `download_report`")
        # verify the required parameter 'report_name' is set
        if ('report_name' not in params) or (params['report_name'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `report_name` when calling `download_report`")
            raise ValueError("Missing the required parameter `report_name` when calling `download_report`")

        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `download_report`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `download_report`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))
        if 'report_date' in params:
            query_params.append(('reportDate', params['report_date']))
        if 'report_name' in params:
            query_params.append(('reportName', params['report_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/xml', 'text/csv'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/report-downloads', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)