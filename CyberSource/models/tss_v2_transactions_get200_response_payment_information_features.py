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


class TssV2TransactionsGet200ResponsePaymentInformationFeatures(object):
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
        'account_funding_source': 'str',
        'account_funding_source_sub_type': 'str',
        'card_product': 'str',
        'message_type': 'str',
        'acceptance_level': 'str',
        'card_platform': 'str',
        'combo_card': 'str'
    }

    attribute_map = {
        'account_funding_source': 'accountFundingSource',
        'account_funding_source_sub_type': 'accountFundingSourceSubType',
        'card_product': 'cardProduct',
        'message_type': 'messageType',
        'acceptance_level': 'acceptanceLevel',
        'card_platform': 'cardPlatform',
        'combo_card': 'comboCard'
    }

    def __init__(self, account_funding_source=None, account_funding_source_sub_type=None, card_product=None, message_type=None, acceptance_level=None, card_platform=None, combo_card=None):
        """
        TssV2TransactionsGet200ResponsePaymentInformationFeatures - a model defined in Swagger
        """

        self._account_funding_source = None
        self._account_funding_source_sub_type = None
        self._card_product = None
        self._message_type = None
        self._acceptance_level = None
        self._card_platform = None
        self._combo_card = None

        if account_funding_source is not None:
          self.account_funding_source = account_funding_source
        if account_funding_source_sub_type is not None:
          self.account_funding_source_sub_type = account_funding_source_sub_type
        if card_product is not None:
          self.card_product = card_product
        if message_type is not None:
          self.message_type = message_type
        if acceptance_level is not None:
          self.acceptance_level = acceptance_level
        if card_platform is not None:
          self.card_platform = card_platform
        if combo_card is not None:
          self.combo_card = combo_card

    @property
    def account_funding_source(self):
        """
        Gets the account_funding_source of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the account funding source. Possible values:   - `CREDIT`   - `DEBIT`   - `PREPAID`   - `DEFERRED DEBIT`   - `CHARGE` 

        :return: The account_funding_source of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :rtype: str
        """
        return self._account_funding_source

    @account_funding_source.setter
    def account_funding_source(self, account_funding_source):
        """
        Sets the account_funding_source of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the account funding source. Possible values:   - `CREDIT`   - `DEBIT`   - `PREPAID`   - `DEFERRED DEBIT`   - `CHARGE` 

        :param account_funding_source: The account_funding_source of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :type: str
        """



        self._account_funding_source = account_funding_source

    @property
    def account_funding_source_sub_type(self):
        """
        Gets the account_funding_source_sub_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of prepaid card. Possible values:   - `Reloadable`   - `Non-reloadable` 

        :return: The account_funding_source_sub_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :rtype: str
        """
        return self._account_funding_source_sub_type

    @account_funding_source_sub_type.setter
    def account_funding_source_sub_type(self, account_funding_source_sub_type):
        """
        Sets the account_funding_source_sub_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of prepaid card. Possible values:   - `Reloadable`   - `Non-reloadable` 

        :param account_funding_source_sub_type: The account_funding_source_sub_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :type: str
        """



        self._account_funding_source_sub_type = account_funding_source_sub_type

    @property
    def card_product(self):
        """
        Gets the card_product of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of issuer product. Example values:   - Visa Classic   - Visa Signature   - Visa Infinite 

        :return: The card_product of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :rtype: str
        """
        return self._card_product

    @card_product.setter
    def card_product(self, card_product):
        """
        Sets the card_product of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of issuer product. Example values:   - Visa Classic   - Visa Signature   - Visa Infinite 

        :param card_product: The card_product of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :type: str
        """



        self._card_product = card_product

    @property
    def message_type(self):
        """
        Gets the message_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of BIN based authentication. Possible values:   - `S`: Single Message   - `D`: Dual Message 

        :return: The message_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :rtype: str
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """
        Sets the message_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of BIN based authentication. Possible values:   - `S`: Single Message   - `D`: Dual Message 

        :param message_type: The message_type of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :type: str
        """



        self._message_type = message_type

    @property
    def acceptance_level(self):
        """
        Gets the acceptance_level of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the acceptance level of the PAN. Possible values:   - `0` : Normal   - `1` : Monitor   - `2` : Refuse   - `3` : Not Allowed   - `4` : Private   - `5` : Test 

        :return: The acceptance_level of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :rtype: str
        """
        return self._acceptance_level

    @acceptance_level.setter
    def acceptance_level(self, acceptance_level):
        """
        Sets the acceptance_level of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the acceptance level of the PAN. Possible values:   - `0` : Normal   - `1` : Monitor   - `2` : Refuse   - `3` : Not Allowed   - `4` : Private   - `5` : Test 

        :param acceptance_level: The acceptance_level of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :type: str
        """



        self._acceptance_level = acceptance_level

    @property
    def card_platform(self):
        """
        Gets the card_platform of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of card platform. Possible values:   - `BUSINESS`   - `CONSUMER`   - `COMMERCIAL`   - `GOVERNMENT` 

        :return: The card_platform of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :rtype: str
        """
        return self._card_platform

    @card_platform.setter
    def card_platform(self, card_platform):
        """
        Sets the card_platform of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field contains the type of card platform. Possible values:   - `BUSINESS`   - `CONSUMER`   - `COMMERCIAL`   - `GOVERNMENT` 

        :param card_platform: The card_platform of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :type: str
        """



        self._card_platform = card_platform

    @property
    def combo_card(self):
        """
        Gets the combo_card of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field indicates the type of combo card. Possible values:   - 0 (Not a combo card)   - 1 (Credit and Prepaid Combo card)   - 2 (Credit and Debit Combo card) 

        :return: The combo_card of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :rtype: str
        """
        return self._combo_card

    @combo_card.setter
    def combo_card(self, combo_card):
        """
        Sets the combo_card of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        This field indicates the type of combo card. Possible values:   - 0 (Not a combo card)   - 1 (Credit and Prepaid Combo card)   - 2 (Credit and Debit Combo card) 

        :param combo_card: The combo_card of this TssV2TransactionsGet200ResponsePaymentInformationFeatures.
        :type: str
        """



        self._combo_card = combo_card

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
        if not isinstance(other, TssV2TransactionsGet200ResponsePaymentInformationFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
