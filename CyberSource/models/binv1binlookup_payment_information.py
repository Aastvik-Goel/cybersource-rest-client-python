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


class Binv1binlookupPaymentInformation(object):
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
        'card': 'Binv1binlookupPaymentInformationCard',
        'customer': 'GetAllSubscriptionsResponsePaymentInformationCustomer',
        'payment_instrument': 'Ptsv2paymentsPaymentInformationPaymentInstrument',
        'instrument_identifier': 'Ptsv2paymentsPaymentInformationInstrumentIdentifier'
    }

    attribute_map = {
        'card': 'card',
        'customer': 'customer',
        'payment_instrument': 'paymentInstrument',
        'instrument_identifier': 'instrumentIdentifier'
    }

    def __init__(self, card=None, customer=None, payment_instrument=None, instrument_identifier=None):
        """
        Binv1binlookupPaymentInformation - a model defined in Swagger
        """

        self._card = None
        self._customer = None
        self._payment_instrument = None
        self._instrument_identifier = None

        if card is not None:
          self.card = card
        if customer is not None:
          self.customer = customer
        if payment_instrument is not None:
          self.payment_instrument = payment_instrument
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier

    @property
    def card(self):
        """
        Gets the card of this Binv1binlookupPaymentInformation.

        :return: The card of this Binv1binlookupPaymentInformation.
        :rtype: Binv1binlookupPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Binv1binlookupPaymentInformation.

        :param card: The card of this Binv1binlookupPaymentInformation.
        :type: Binv1binlookupPaymentInformationCard
        """

        self._card = card

    @property
    def customer(self):
        """
        Gets the customer of this Binv1binlookupPaymentInformation.

        :return: The customer of this Binv1binlookupPaymentInformation.
        :rtype: GetAllSubscriptionsResponsePaymentInformationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this Binv1binlookupPaymentInformation.

        :param customer: The customer of this Binv1binlookupPaymentInformation.
        :type: GetAllSubscriptionsResponsePaymentInformationCustomer
        """

        self._customer = customer

    @property
    def payment_instrument(self):
        """
        Gets the payment_instrument of this Binv1binlookupPaymentInformation.

        :return: The payment_instrument of this Binv1binlookupPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationPaymentInstrument
        """
        return self._payment_instrument

    @payment_instrument.setter
    def payment_instrument(self, payment_instrument):
        """
        Sets the payment_instrument of this Binv1binlookupPaymentInformation.

        :param payment_instrument: The payment_instrument of this Binv1binlookupPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationPaymentInstrument
        """

        self._payment_instrument = payment_instrument

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this Binv1binlookupPaymentInformation.

        :return: The instrument_identifier of this Binv1binlookupPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationInstrumentIdentifier
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this Binv1binlookupPaymentInformation.

        :param instrument_identifier: The instrument_identifier of this Binv1binlookupPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationInstrumentIdentifier
        """

        self._instrument_identifier = instrument_identifier

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
        if not isinstance(other, Binv1binlookupPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
