# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'str',
        'category_code': 'str',
        'processor_raw_name': 'str'
    }

    attribute_map = {
        'category': 'category',
        'category_code': 'categoryCode',
        'processor_raw_name': 'processorRawName'
    }

    def __init__(self, category=None, category_code=None, processor_raw_name=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights - a model defined in Swagger
        """

        self._category = None
        self._category_code = None
        self._processor_raw_name = None

        if category is not None:
          self.category = category
        if category_code is not None:
          self.category_code = category_code
        if processor_raw_name is not None:
          self.processor_raw_name = processor_raw_name

    @property
    def category(self):
        """
        Gets the category of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        Categorization of response message from processor  Possible Values: - `APPROVED` - `ISSUER_WILL_NEVER_APPROVE` - `ISSUER_CANT_APPROVE_AT_THIS_TIME` - `ISSUER_CANT_APPROVE_WITH_THESE_DETAILS` - `GENERIC_ERROR` - `OTHERS` - `MATCH_NOT_FOUND` 

        :return: The category of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        Categorization of response message from processor  Possible Values: - `APPROVED` - `ISSUER_WILL_NEVER_APPROVE` - `ISSUER_CANT_APPROVE_AT_THIS_TIME` - `ISSUER_CANT_APPROVE_WITH_THESE_DETAILS` - `GENERIC_ERROR` - `OTHERS` - `MATCH_NOT_FOUND` 

        :param category: The category of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        :type: str
        """



        self._category = category

    @property
    def category_code(self):
        """
        Gets the category_code of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        Categorization Code of response message from processor  Possible Values: - `01` : Issuer Will Never Approve - `02` : Issuer Can't Approve at this Time - `03` : Issuer Can't Approve with these Details - `04` : Generic Error - `98` : Others - `99` : Payment Insights Response Category Match Not Found 

        :return: The category_code of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """
        Sets the category_code of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        Categorization Code of response message from processor  Possible Values: - `01` : Issuer Will Never Approve - `02` : Issuer Can't Approve at this Time - `03` : Issuer Can't Approve with these Details - `04` : Generic Error - `98` : Others - `99` : Payment Insights Response Category Match Not Found 

        :param category_code: The category_code of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        :type: str
        """



        self._category_code = category_code

    @property
    def processor_raw_name(self):
        """
        Gets the processor_raw_name of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        Raw name of the processor used for the transaction processing, especially useful during acquirer swing to see which processor transaction settled with 

        :return: The processor_raw_name of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        :rtype: str
        """
        return self._processor_raw_name

    @processor_raw_name.setter
    def processor_raw_name(self, processor_raw_name):
        """
        Sets the processor_raw_name of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        Raw name of the processor used for the transaction processing, especially useful during acquirer swing to see which processor transaction settled with 

        :param processor_raw_name: The processor_raw_name of this PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights.
        :type: str
        """



        self._processor_raw_name = processor_raw_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
