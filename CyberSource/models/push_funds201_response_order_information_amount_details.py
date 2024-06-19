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


class PushFunds201ResponseOrderInformationAmountDetails(object):
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
        'total_amount': 'str',
        'currency': 'str',
        'settlement_amount': 'str',
        'settlement_currency': 'str'
    }

    attribute_map = {
        'total_amount': 'totalAmount',
        'currency': 'currency',
        'settlement_amount': 'settlementAmount',
        'settlement_currency': 'settlementCurrency'
    }

    def __init__(self, total_amount=None, currency=None, settlement_amount=None, settlement_currency=None):
        """
        PushFunds201ResponseOrderInformationAmountDetails - a model defined in Swagger
        """

        self._total_amount = None
        self._currency = None
        self._settlement_amount = None
        self._settlement_currency = None

        if total_amount is not None:
          self.total_amount = total_amount
        self.currency = currency
        if settlement_amount is not None:
          self.settlement_amount = settlement_amount
        if settlement_currency is not None:
          self.settlement_currency = settlement_currency

    @property
    def total_amount(self):
        """
        Gets the total_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  Note For Visa Platform Conenct, FDC Compass, and Chase Paymentech processors, the maximum length for this field is 12 numbers.  Processor Amount Ranges: Visa Platform Connect: .01-9999999999.99  Mastercard Send: 1-9999999999.99  FDC Compass: .01- 9999999999.994  Chase Paymentech: .01-9999999999.99 

        :return: The total_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  Note For Visa Platform Conenct, FDC Compass, and Chase Paymentech processors, the maximum length for this field is 12 numbers.  Processor Amount Ranges: Visa Platform Connect: .01-9999999999.99  Mastercard Send: 1-9999999999.99  FDC Compass: .01- 9999999999.994  Chase Paymentech: .01-9999999999.99 

        :param total_amount: The total_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._total_amount = total_amount

    @property
    def currency(self):
        """
        Gets the currency of this PushFunds201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes 

        :return: The currency of this PushFunds201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PushFunds201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character ISO Standard Currency Codes 

        :param currency: The currency of this PushFunds201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._currency = currency

    @property
    def settlement_amount(self):
        """
        Gets the settlement_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder's account. This field is returned for OCT transactions. 

        :return: The settlement_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, settlement_amount):
        """
        Sets the settlement_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder's account. This field is returned for OCT transactions. 

        :param settlement_amount: The settlement_amount of this PushFunds201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._settlement_amount = settlement_amount

    @property
    def settlement_currency(self):
        """
        Gets the settlement_currency of this PushFunds201ResponseOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. This field is returned for OCT transactions. 

        :return: The settlement_currency of this PushFunds201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """
        Sets the settlement_currency of this PushFunds201ResponseOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. This field is returned for OCT transactions. 

        :param settlement_currency: The settlement_currency of this PushFunds201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._settlement_currency = settlement_currency

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
        if not isinstance(other, PushFunds201ResponseOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
