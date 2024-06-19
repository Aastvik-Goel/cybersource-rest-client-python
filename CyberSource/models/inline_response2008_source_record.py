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


class InlineResponse2008SourceRecord(object):
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
        'token': 'str',
        'customer_id': 'str',
        'payment_instrument_id': 'str',
        'instrument_identifier_id': 'str',
        'card_number': 'str',
        'card_expiry_month': 'str',
        'card_expiry_year': 'str',
        'card_type': 'str'
    }

    attribute_map = {
        'token': 'token',
        'customer_id': 'customerId',
        'payment_instrument_id': 'paymentInstrumentId',
        'instrument_identifier_id': 'instrumentIdentifierId',
        'card_number': 'cardNumber',
        'card_expiry_month': 'cardExpiryMonth',
        'card_expiry_year': 'cardExpiryYear',
        'card_type': 'cardType'
    }

    def __init__(self, token=None, customer_id=None, payment_instrument_id=None, instrument_identifier_id=None, card_number=None, card_expiry_month=None, card_expiry_year=None, card_type=None):
        """
        InlineResponse2008SourceRecord - a model defined in Swagger
        """

        self._token = None
        self._customer_id = None
        self._payment_instrument_id = None
        self._instrument_identifier_id = None
        self._card_number = None
        self._card_expiry_month = None
        self._card_expiry_year = None
        self._card_type = None

        if token is not None:
          self.token = token
        if customer_id is not None:
          self.customer_id = customer_id
        if payment_instrument_id is not None:
          self.payment_instrument_id = payment_instrument_id
        if instrument_identifier_id is not None:
          self.instrument_identifier_id = instrument_identifier_id
        if card_number is not None:
          self.card_number = card_number
        if card_expiry_month is not None:
          self.card_expiry_month = card_expiry_month
        if card_expiry_year is not None:
          self.card_expiry_year = card_expiry_year
        if card_type is not None:
          self.card_type = card_type

    @property
    def token(self):
        """
        Gets the token of this InlineResponse2008SourceRecord.

        :return: The token of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this InlineResponse2008SourceRecord.

        :param token: The token of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._token = token

    @property
    def customer_id(self):
        """
        Gets the customer_id of this InlineResponse2008SourceRecord.

        :return: The customer_id of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this InlineResponse2008SourceRecord.

        :param customer_id: The customer_id of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._customer_id = customer_id

    @property
    def payment_instrument_id(self):
        """
        Gets the payment_instrument_id of this InlineResponse2008SourceRecord.

        :return: The payment_instrument_id of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._payment_instrument_id

    @payment_instrument_id.setter
    def payment_instrument_id(self, payment_instrument_id):
        """
        Sets the payment_instrument_id of this InlineResponse2008SourceRecord.

        :param payment_instrument_id: The payment_instrument_id of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._payment_instrument_id = payment_instrument_id

    @property
    def instrument_identifier_id(self):
        """
        Gets the instrument_identifier_id of this InlineResponse2008SourceRecord.

        :return: The instrument_identifier_id of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._instrument_identifier_id

    @instrument_identifier_id.setter
    def instrument_identifier_id(self, instrument_identifier_id):
        """
        Sets the instrument_identifier_id of this InlineResponse2008SourceRecord.

        :param instrument_identifier_id: The instrument_identifier_id of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._instrument_identifier_id = instrument_identifier_id

    @property
    def card_number(self):
        """
        Gets the card_number of this InlineResponse2008SourceRecord.

        :return: The card_number of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """
        Sets the card_number of this InlineResponse2008SourceRecord.

        :param card_number: The card_number of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._card_number = card_number

    @property
    def card_expiry_month(self):
        """
        Gets the card_expiry_month of this InlineResponse2008SourceRecord.

        :return: The card_expiry_month of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._card_expiry_month

    @card_expiry_month.setter
    def card_expiry_month(self, card_expiry_month):
        """
        Sets the card_expiry_month of this InlineResponse2008SourceRecord.

        :param card_expiry_month: The card_expiry_month of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._card_expiry_month = card_expiry_month

    @property
    def card_expiry_year(self):
        """
        Gets the card_expiry_year of this InlineResponse2008SourceRecord.

        :return: The card_expiry_year of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._card_expiry_year

    @card_expiry_year.setter
    def card_expiry_year(self, card_expiry_year):
        """
        Sets the card_expiry_year of this InlineResponse2008SourceRecord.

        :param card_expiry_year: The card_expiry_year of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._card_expiry_year = card_expiry_year

    @property
    def card_type(self):
        """
        Gets the card_type of this InlineResponse2008SourceRecord.

        :return: The card_type of this InlineResponse2008SourceRecord.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this InlineResponse2008SourceRecord.

        :param card_type: The card_type of this InlineResponse2008SourceRecord.
        :type: str
        """

        self._card_type = card_type

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
        if not isinstance(other, InlineResponse2008SourceRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
