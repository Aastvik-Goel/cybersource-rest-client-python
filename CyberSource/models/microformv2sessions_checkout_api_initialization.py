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


class Microformv2sessionsCheckoutApiInitialization(object):
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
        'profile_id': 'str',
        'access_key': 'str',
        'reference_number': 'str',
        'transaction_uuid': 'str',
        'transaction_type': 'str',
        'currency': 'str',
        'amount': 'str',
        'locale': 'str',
        'override_custom_receipt_page': 'str',
        'unsigned_field_names': 'str'
    }

    attribute_map = {
        'profile_id': 'profile_id',
        'access_key': 'access_key',
        'reference_number': 'reference_number',
        'transaction_uuid': 'transaction_uuid',
        'transaction_type': 'transaction_type',
        'currency': 'currency',
        'amount': 'amount',
        'locale': 'locale',
        'override_custom_receipt_page': 'override_custom_receipt_page',
        'unsigned_field_names': 'unsigned_field_names'
    }

    def __init__(self, profile_id=None, access_key=None, reference_number=None, transaction_uuid=None, transaction_type=None, currency=None, amount=None, locale=None, override_custom_receipt_page=None, unsigned_field_names=None):
        """
        Microformv2sessionsCheckoutApiInitialization - a model defined in Swagger
        """

        self._profile_id = None
        self._access_key = None
        self._reference_number = None
        self._transaction_uuid = None
        self._transaction_type = None
        self._currency = None
        self._amount = None
        self._locale = None
        self._override_custom_receipt_page = None
        self._unsigned_field_names = None

        if profile_id is not None:
          self.profile_id = profile_id
        if access_key is not None:
          self.access_key = access_key
        if reference_number is not None:
          self.reference_number = reference_number
        if transaction_uuid is not None:
          self.transaction_uuid = transaction_uuid
        if transaction_type is not None:
          self.transaction_type = transaction_type
        if currency is not None:
          self.currency = currency
        if amount is not None:
          self.amount = amount
        if locale is not None:
          self.locale = locale
        if override_custom_receipt_page is not None:
          self.override_custom_receipt_page = override_custom_receipt_page
        if unsigned_field_names is not None:
          self.unsigned_field_names = unsigned_field_names

    @property
    def profile_id(self):
        """
        Gets the profile_id of this Microformv2sessionsCheckoutApiInitialization.

        :return: The profile_id of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """
        Sets the profile_id of this Microformv2sessionsCheckoutApiInitialization.

        :param profile_id: The profile_id of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._profile_id = profile_id

    @property
    def access_key(self):
        """
        Gets the access_key of this Microformv2sessionsCheckoutApiInitialization.

        :return: The access_key of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """
        Sets the access_key of this Microformv2sessionsCheckoutApiInitialization.

        :param access_key: The access_key of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._access_key = access_key

    @property
    def reference_number(self):
        """
        Gets the reference_number of this Microformv2sessionsCheckoutApiInitialization.

        :return: The reference_number of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """
        Sets the reference_number of this Microformv2sessionsCheckoutApiInitialization.

        :param reference_number: The reference_number of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._reference_number = reference_number

    @property
    def transaction_uuid(self):
        """
        Gets the transaction_uuid of this Microformv2sessionsCheckoutApiInitialization.

        :return: The transaction_uuid of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._transaction_uuid

    @transaction_uuid.setter
    def transaction_uuid(self, transaction_uuid):
        """
        Sets the transaction_uuid of this Microformv2sessionsCheckoutApiInitialization.

        :param transaction_uuid: The transaction_uuid of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._transaction_uuid = transaction_uuid

    @property
    def transaction_type(self):
        """
        Gets the transaction_type of this Microformv2sessionsCheckoutApiInitialization.

        :return: The transaction_type of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """
        Sets the transaction_type of this Microformv2sessionsCheckoutApiInitialization.

        :param transaction_type: The transaction_type of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._transaction_type = transaction_type

    @property
    def currency(self):
        """
        Gets the currency of this Microformv2sessionsCheckoutApiInitialization.

        :return: The currency of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Microformv2sessionsCheckoutApiInitialization.

        :param currency: The currency of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._currency = currency

    @property
    def amount(self):
        """
        Gets the amount of this Microformv2sessionsCheckoutApiInitialization.

        :return: The amount of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Microformv2sessionsCheckoutApiInitialization.

        :param amount: The amount of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._amount = amount

    @property
    def locale(self):
        """
        Gets the locale of this Microformv2sessionsCheckoutApiInitialization.

        :return: The locale of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this Microformv2sessionsCheckoutApiInitialization.

        :param locale: The locale of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._locale = locale

    @property
    def override_custom_receipt_page(self):
        """
        Gets the override_custom_receipt_page of this Microformv2sessionsCheckoutApiInitialization.

        :return: The override_custom_receipt_page of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._override_custom_receipt_page

    @override_custom_receipt_page.setter
    def override_custom_receipt_page(self, override_custom_receipt_page):
        """
        Sets the override_custom_receipt_page of this Microformv2sessionsCheckoutApiInitialization.

        :param override_custom_receipt_page: The override_custom_receipt_page of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._override_custom_receipt_page = override_custom_receipt_page

    @property
    def unsigned_field_names(self):
        """
        Gets the unsigned_field_names of this Microformv2sessionsCheckoutApiInitialization.

        :return: The unsigned_field_names of this Microformv2sessionsCheckoutApiInitialization.
        :rtype: str
        """
        return self._unsigned_field_names

    @unsigned_field_names.setter
    def unsigned_field_names(self, unsigned_field_names):
        """
        Sets the unsigned_field_names of this Microformv2sessionsCheckoutApiInitialization.

        :param unsigned_field_names: The unsigned_field_names of this Microformv2sessionsCheckoutApiInitialization.
        :type: str
        """



        self._unsigned_field_names = unsigned_field_names

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
        if not isinstance(other, Microformv2sessionsCheckoutApiInitialization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
