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


class Ptsv2paymentsPaymentInformationDirectDebitMandate(object):
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
        'clearing_date': 'str'
    }

    attribute_map = {
        'clearing_date': 'clearingDate'
    }

    def __init__(self, clearing_date=None):
        """
        Ptsv2paymentsPaymentInformationDirectDebitMandate - a model defined in Swagger
        """

        self._clearing_date = None

        if clearing_date is not None:
          self.clearing_date = clearing_date

    @property
    def clearing_date(self):
        """
        Gets the clearing_date of this Ptsv2paymentsPaymentInformationDirectDebitMandate.
        This is the date on which the SEPA DD should be executed. Debit date: the day on which the payer's account is debited. 

        :return: The clearing_date of this Ptsv2paymentsPaymentInformationDirectDebitMandate.
        :rtype: str
        """
        return self._clearing_date

    @clearing_date.setter
    def clearing_date(self, clearing_date):
        """
        Sets the clearing_date of this Ptsv2paymentsPaymentInformationDirectDebitMandate.
        This is the date on which the SEPA DD should be executed. Debit date: the day on which the payer's account is debited. 

        :param clearing_date: The clearing_date of this Ptsv2paymentsPaymentInformationDirectDebitMandate.
        :type: str
        """

        self._clearing_date = clearing_date

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
        if not isinstance(other, Ptsv2paymentsPaymentInformationDirectDebitMandate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other