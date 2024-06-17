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


class Ptsv2paymentsidrefundsPaymentInformation(object):
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
        'card': 'Ptsv2paymentsidrefundsPaymentInformationCard',
        'bank': 'Ptsv2paymentsidrefundsPaymentInformationBank',
        'tokenized_card': 'Ptsv2paymentsPaymentInformationTokenizedCard',
        'fluid_data': 'Ptsv2paymentsPaymentInformationFluidData',
        'customer': 'Ptsv2paymentsPaymentInformationCustomer',
        'payment_instrument': 'Ptsv2paymentsPaymentInformationPaymentInstrument',
        'instrument_identifier': 'Ptsv2paymentsPaymentInformationInstrumentIdentifier',
        'shipping_address': 'Ptsv2paymentsPaymentInformationShippingAddress',
        'legacy_token': 'Ptsv2paymentsPaymentInformationLegacyToken',
        'payment_type': 'Ptsv2paymentsidrefundsPaymentInformationPaymentType',
        'e_wallet': 'Ptsv2paymentsidrefundsPaymentInformationEWallet'
    }

    attribute_map = {
        'card': 'card',
        'bank': 'bank',
        'tokenized_card': 'tokenizedCard',
        'fluid_data': 'fluidData',
        'customer': 'customer',
        'payment_instrument': 'paymentInstrument',
        'instrument_identifier': 'instrumentIdentifier',
        'shipping_address': 'shippingAddress',
        'legacy_token': 'legacyToken',
        'payment_type': 'paymentType',
        'e_wallet': 'eWallet'
    }

    def __init__(self, card=None, bank=None, tokenized_card=None, fluid_data=None, customer=None, payment_instrument=None, instrument_identifier=None, shipping_address=None, legacy_token=None, payment_type=None, e_wallet=None):
        """
        Ptsv2paymentsidrefundsPaymentInformation - a model defined in Swagger
        """

        self._card = None
        self._bank = None
        self._tokenized_card = None
        self._fluid_data = None
        self._customer = None
        self._payment_instrument = None
        self._instrument_identifier = None
        self._shipping_address = None
        self._legacy_token = None
        self._payment_type = None
        self._e_wallet = None

        if card is not None:
          self.card = card
        if bank is not None:
          self.bank = bank
        if tokenized_card is not None:
          self.tokenized_card = tokenized_card
        if fluid_data is not None:
          self.fluid_data = fluid_data
        if customer is not None:
          self.customer = customer
        if payment_instrument is not None:
          self.payment_instrument = payment_instrument
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier
        if shipping_address is not None:
          self.shipping_address = shipping_address
        if legacy_token is not None:
          self.legacy_token = legacy_token
        if payment_type is not None:
          self.payment_type = payment_type
        if e_wallet is not None:
          self.e_wallet = e_wallet

    @property
    def card(self):
        """
        Gets the card of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The card of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsidrefundsPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Ptsv2paymentsidrefundsPaymentInformation.

        :param card: The card of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsidrefundsPaymentInformationCard
        """



        self._card = card

    @property
    def bank(self):
        """
        Gets the bank of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The bank of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsidrefundsPaymentInformationBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this Ptsv2paymentsidrefundsPaymentInformation.

        :param bank: The bank of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsidrefundsPaymentInformationBank
        """



        self._bank = bank

    @property
    def tokenized_card(self):
        """
        Gets the tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationTokenizedCard
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """
        Sets the tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.

        :param tokenized_card: The tokenized_card of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationTokenizedCard
        """



        self._tokenized_card = tokenized_card

    @property
    def fluid_data(self):
        """
        Gets the fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationFluidData
        """
        return self._fluid_data

    @fluid_data.setter
    def fluid_data(self, fluid_data):
        """
        Sets the fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.

        :param fluid_data: The fluid_data of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationFluidData
        """



        self._fluid_data = fluid_data

    @property
    def customer(self):
        """
        Gets the customer of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The customer of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this Ptsv2paymentsidrefundsPaymentInformation.

        :param customer: The customer of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationCustomer
        """



        self._customer = customer

    @property
    def payment_instrument(self):
        """
        Gets the payment_instrument of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The payment_instrument of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationPaymentInstrument
        """
        return self._payment_instrument

    @payment_instrument.setter
    def payment_instrument(self, payment_instrument):
        """
        Sets the payment_instrument of this Ptsv2paymentsidrefundsPaymentInformation.

        :param payment_instrument: The payment_instrument of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationPaymentInstrument
        """



        self._payment_instrument = payment_instrument

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The instrument_identifier of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationInstrumentIdentifier
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this Ptsv2paymentsidrefundsPaymentInformation.

        :param instrument_identifier: The instrument_identifier of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationInstrumentIdentifier
        """



        self._instrument_identifier = instrument_identifier

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The shipping_address of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this Ptsv2paymentsidrefundsPaymentInformation.

        :param shipping_address: The shipping_address of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationShippingAddress
        """



        self._shipping_address = shipping_address

    @property
    def legacy_token(self):
        """
        Gets the legacy_token of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The legacy_token of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationLegacyToken
        """
        return self._legacy_token

    @legacy_token.setter
    def legacy_token(self, legacy_token):
        """
        Sets the legacy_token of this Ptsv2paymentsidrefundsPaymentInformation.

        :param legacy_token: The legacy_token of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationLegacyToken
        """



        self._legacy_token = legacy_token

    @property
    def payment_type(self):
        """
        Gets the payment_type of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The payment_type of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsidrefundsPaymentInformationPaymentType
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """
        Sets the payment_type of this Ptsv2paymentsidrefundsPaymentInformation.

        :param payment_type: The payment_type of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsidrefundsPaymentInformationPaymentType
        """



        self._payment_type = payment_type

    @property
    def e_wallet(self):
        """
        Gets the e_wallet of this Ptsv2paymentsidrefundsPaymentInformation.

        :return: The e_wallet of this Ptsv2paymentsidrefundsPaymentInformation.
        :rtype: Ptsv2paymentsidrefundsPaymentInformationEWallet
        """
        return self._e_wallet

    @e_wallet.setter
    def e_wallet(self, e_wallet):
        """
        Sets the e_wallet of this Ptsv2paymentsidrefundsPaymentInformation.

        :param e_wallet: The e_wallet of this Ptsv2paymentsidrefundsPaymentInformation.
        :type: Ptsv2paymentsidrefundsPaymentInformationEWallet
        """



        self._e_wallet = e_wallet

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
        if not isinstance(other, Ptsv2paymentsidrefundsPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
