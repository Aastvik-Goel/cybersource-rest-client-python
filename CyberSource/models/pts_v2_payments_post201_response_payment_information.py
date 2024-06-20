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


class PtsV2PaymentsPost201ResponsePaymentInformation(object):
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
        'card': 'PtsV2PaymentsPost201ResponsePaymentAccountInformationCard',
        'tokenized_card': 'PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard',
        'account_features': 'PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures',
        'bank': 'PtsV2PaymentsPost201ResponsePaymentInformationBank',
        'customer': 'Ptsv2paymentsPaymentInformationCustomer',
        'payment_instrument': 'Ptsv2paymentsPaymentInformationPaymentInstrument',
        'instrument_identifier': 'PtsV2PaymentsPost201ResponsePaymentInformationInstrumentIdentifier',
        'shipping_address': 'Ptsv2paymentsPaymentInformationShippingAddress',
        'scheme': 'str',
        'bin': 'str',
        'account_type': 'str',
        'issuer': 'str',
        'bin_country': 'str',
        'e_wallet': 'PtsV2PaymentsPost201ResponsePaymentInformationEWallet'
    }

    attribute_map = {
        'card': 'card',
        'tokenized_card': 'tokenizedCard',
        'account_features': 'accountFeatures',
        'bank': 'bank',
        'customer': 'customer',
        'payment_instrument': 'paymentInstrument',
        'instrument_identifier': 'instrumentIdentifier',
        'shipping_address': 'shippingAddress',
        'scheme': 'scheme',
        'bin': 'bin',
        'account_type': 'accountType',
        'issuer': 'issuer',
        'bin_country': 'binCountry',
        'e_wallet': 'eWallet'
    }

    def __init__(self, card=None, tokenized_card=None, account_features=None, bank=None, customer=None, payment_instrument=None, instrument_identifier=None, shipping_address=None, scheme=None, bin=None, account_type=None, issuer=None, bin_country=None, e_wallet=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInformation - a model defined in Swagger
        """

        self._card = None
        self._tokenized_card = None
        self._account_features = None
        self._bank = None
        self._customer = None
        self._payment_instrument = None
        self._instrument_identifier = None
        self._shipping_address = None
        self._scheme = None
        self._bin = None
        self._account_type = None
        self._issuer = None
        self._bin_country = None
        self._e_wallet = None

        if card is not None:
          self.card = card
        if tokenized_card is not None:
          self.tokenized_card = tokenized_card
        if account_features is not None:
          self.account_features = account_features
        if bank is not None:
          self.bank = bank
        if customer is not None:
          self.customer = customer
        if payment_instrument is not None:
          self.payment_instrument = payment_instrument
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier
        if shipping_address is not None:
          self.shipping_address = shipping_address
        if scheme is not None:
          self.scheme = scheme
        if bin is not None:
          self.bin = bin
        if account_type is not None:
          self.account_type = account_type
        if issuer is not None:
          self.issuer = issuer
        if bin_country is not None:
          self.bin_country = bin_country
        if e_wallet is not None:
          self.e_wallet = e_wallet

    @property
    def card(self):
        """
        Gets the card of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The card of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: PtsV2PaymentsPost201ResponsePaymentAccountInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param card: The card of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: PtsV2PaymentsPost201ResponsePaymentAccountInformationCard
        """

        self._card = card

    @property
    def tokenized_card(self):
        """
        Gets the tokenized_card of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The tokenized_card of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """
        Sets the tokenized_card of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param tokenized_card: The tokenized_card of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: PtsV2PaymentsPost201ResponsePaymentInformationTokenizedCard
        """

        self._tokenized_card = tokenized_card

    @property
    def account_features(self):
        """
        Gets the account_features of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The account_features of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures
        """
        return self._account_features

    @account_features.setter
    def account_features(self, account_features):
        """
        Sets the account_features of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param account_features: The account_features of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: PtsV2PaymentsPost201ResponsePaymentInformationAccountFeatures
        """

        self._account_features = account_features

    @property
    def bank(self):
        """
        Gets the bank of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The bank of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: PtsV2PaymentsPost201ResponsePaymentInformationBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param bank: The bank of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: PtsV2PaymentsPost201ResponsePaymentInformationBank
        """

        self._bank = bank

    @property
    def customer(self):
        """
        Gets the customer of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The customer of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param customer: The customer of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: Ptsv2paymentsPaymentInformationCustomer
        """

        self._customer = customer

    @property
    def payment_instrument(self):
        """
        Gets the payment_instrument of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The payment_instrument of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationPaymentInstrument
        """
        return self._payment_instrument

    @payment_instrument.setter
    def payment_instrument(self, payment_instrument):
        """
        Sets the payment_instrument of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param payment_instrument: The payment_instrument of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: Ptsv2paymentsPaymentInformationPaymentInstrument
        """

        self._payment_instrument = payment_instrument

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The instrument_identifier of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: PtsV2PaymentsPost201ResponsePaymentInformationInstrumentIdentifier
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param instrument_identifier: The instrument_identifier of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: PtsV2PaymentsPost201ResponsePaymentInformationInstrumentIdentifier
        """

        self._instrument_identifier = instrument_identifier

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The shipping_address of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param shipping_address: The shipping_address of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: Ptsv2paymentsPaymentInformationShippingAddress
        """

        self._shipping_address = shipping_address

    @property
    def scheme(self):
        """
        Gets the scheme of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Subtype of card account. This field can contain one of the following values: - Maestro International - Maestro UK Domestic - MasterCard Credit - MasterCard Debit - Visa Credit - Visa Debit - Visa Electron  **Note** Additional values may be present. 

        :return: The scheme of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """
        Sets the scheme of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Subtype of card account. This field can contain one of the following values: - Maestro International - Maestro UK Domestic - MasterCard Credit - MasterCard Debit - Visa Credit - Visa Debit - Visa Electron  **Note** Additional values may be present. 

        :param scheme: The scheme of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: str
        """

        self._scheme = scheme

    @property
    def bin(self):
        """
        Gets the bin of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Credit card BIN (the first six digits of the credit card).Derived either from the `cc_bin` request field or from the first six characters of the `customer_cc_num` field. 

        :return: The bin of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """
        Sets the bin of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Credit card BIN (the first six digits of the credit card).Derived either from the `cc_bin` request field or from the first six characters of the `customer_cc_num` field. 

        :param bin: The bin of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: str
        """

        self._bin = bin

    @property
    def account_type(self):
        """
        Gets the account_type of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Type of payment card account. This field can refer to a credit card, debit card, or prepaid card account type. 

        :return: The account_type of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Type of payment card account. This field can refer to a credit card, debit card, or prepaid card account type. 

        :param account_type: The account_type of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: str
        """

        self._account_type = account_type

    @property
    def issuer(self):
        """
        Gets the issuer of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Name of the bank or entity that issued the card account. 

        :return: The issuer of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Name of the bank or entity that issued the card account. 

        :param issuer: The issuer of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: str
        """

        self._issuer = issuer

    @property
    def bin_country(self):
        """
        Gets the bin_country of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Country (two-digit country code) associated with the BIN of the customer's card used for the payment. Returned if the information is available. Use this field for additional information when reviewing orders. This information is also displayed in the details page of the CyberSource Business Center. 

        :return: The bin_country of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._bin_country

    @bin_country.setter
    def bin_country(self, bin_country):
        """
        Sets the bin_country of this PtsV2PaymentsPost201ResponsePaymentInformation.
        Country (two-digit country code) associated with the BIN of the customer's card used for the payment. Returned if the information is available. Use this field for additional information when reviewing orders. This information is also displayed in the details page of the CyberSource Business Center. 

        :param bin_country: The bin_country of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: str
        """

        self._bin_country = bin_country

    @property
    def e_wallet(self):
        """
        Gets the e_wallet of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :return: The e_wallet of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :rtype: PtsV2PaymentsPost201ResponsePaymentInformationEWallet
        """
        return self._e_wallet

    @e_wallet.setter
    def e_wallet(self, e_wallet):
        """
        Sets the e_wallet of this PtsV2PaymentsPost201ResponsePaymentInformation.

        :param e_wallet: The e_wallet of this PtsV2PaymentsPost201ResponsePaymentInformation.
        :type: PtsV2PaymentsPost201ResponsePaymentInformationEWallet
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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
