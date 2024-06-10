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


class PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails(object):
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
        'settlement_amount': 'str',
        'settlement_currency': 'str',
        'exchange_rate': 'str',
        'foreign_amount': 'str',
        'foreign_currency': 'str'
    }

    attribute_map = {
        'settlement_amount': 'settlementAmount',
        'settlement_currency': 'settlementCurrency',
        'exchange_rate': 'exchangeRate',
        'foreign_amount': 'foreignAmount',
        'foreign_currency': 'foreignCurrency'
    }

    def __init__(self, settlement_amount=None, settlement_currency=None, exchange_rate=None, foreign_amount=None, foreign_currency=None):
        """
        PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails - a model defined in Swagger
        """

        self._settlement_amount = None
        self._settlement_currency = None
        self._exchange_rate = None
        self._foreign_amount = None
        self._foreign_currency = None

        if settlement_amount is not None:
          self.settlement_amount = settlement_amount
        if settlement_currency is not None:
          self.settlement_currency = settlement_currency
        if exchange_rate is not None:
          self.exchange_rate = exchange_rate
        if foreign_amount is not None:
          self.foreign_amount = foreign_amount
        if foreign_currency is not None:
          self.foreign_currency = foreign_currency

    @property
    def settlement_amount(self):
        """
        Gets the settlement_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder's account. This field is returned for OCT transactions. 

        :return: The settlement_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, settlement_amount):
        """
        Sets the settlement_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency field. It contains the transaction amount (field 4), converted to the Currency used to bill the cardholder's account. This field is returned for OCT transactions. 

        :param settlement_amount: The settlement_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._settlement_amount = settlement_amount

    @property
    def settlement_currency(self):
        """
        Gets the settlement_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. This field is returned for OCT transactions. 

        :return: The settlement_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """
        Sets the settlement_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. This field is returned for OCT transactions. 

        :param settlement_currency: The settlement_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._settlement_currency = settlement_currency

    @property
    def exchange_rate(self):
        """
        Gets the exchange_rate of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        Exchange rate returned by the DCC service. Includes a decimal point and a maximum of 4 decimal places.  For details, see `exchange_rate` request-level field description in the [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf) 

        :return: The exchange_rate of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """
        Sets the exchange_rate of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        Exchange rate returned by the DCC service. Includes a decimal point and a maximum of 4 decimal places.  For details, see `exchange_rate` request-level field description in the [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf) 

        :param exchange_rate: The exchange_rate of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._exchange_rate = exchange_rate

    @property
    def foreign_amount(self):
        """
        Gets the foreign_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        Set this field to the converted amount that was returned by the DCC provider. For processor-specific information, see the `foreign_amount` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The foreign_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._foreign_amount

    @foreign_amount.setter
    def foreign_amount(self, foreign_amount):
        """
        Sets the foreign_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        Set this field to the converted amount that was returned by the DCC provider. For processor-specific information, see the `foreign_amount` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param foreign_amount: The foreign_amount of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._foreign_amount = foreign_amount

    @property
    def foreign_currency(self):
        """
        Gets the foreign_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        Set this field to the converted amount that was returned by the DCC provider. 

        :return: The foreign_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """
        Sets the foreign_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        Set this field to the converted amount that was returned by the DCC provider. 

        :param foreign_currency: The foreign_currency of this PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._foreign_currency = foreign_currency

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
        if not isinstance(other, PtsV2PaymentsRefundPost201ResponseOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other