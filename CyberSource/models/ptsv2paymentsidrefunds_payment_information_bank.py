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


class Ptsv2paymentsidrefundsPaymentInformationBank(object):
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
        'account': 'Ptsv2paymentsidrefundsPaymentInformationBankAccount',
        'routing_number': 'str',
        'iban': 'str',
        'swift_code': 'str'
    }

    attribute_map = {
        'account': 'account',
        'routing_number': 'routingNumber',
        'iban': 'iban',
        'swift_code': 'swiftCode'
    }

    def __init__(self, account=None, routing_number=None, iban=None, swift_code=None):
        """
        Ptsv2paymentsidrefundsPaymentInformationBank - a model defined in Swagger
        """

        self._account = None
        self._routing_number = None
        self._iban = None
        self._swift_code = None

        if account is not None:
          self.account = account
        if routing_number is not None:
          self.routing_number = routing_number
        if iban is not None:
          self.iban = iban
        if swift_code is not None:
          self.swift_code = swift_code

    @property
    def account(self):
        """
        Gets the account of this Ptsv2paymentsidrefundsPaymentInformationBank.

        :return: The account of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :rtype: Ptsv2paymentsidrefundsPaymentInformationBankAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Ptsv2paymentsidrefundsPaymentInformationBank.

        :param account: The account of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :type: Ptsv2paymentsidrefundsPaymentInformationBankAccount
        """

        self._account = account

    @property
    def routing_number(self):
        """
        Gets the routing_number of this Ptsv2paymentsidrefundsPaymentInformationBank.
        Bank routing number. This is also called the _transit number_. 

        :return: The routing_number of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """
        Sets the routing_number of this Ptsv2paymentsidrefundsPaymentInformationBank.
        Bank routing number. This is also called the _transit number_. 

        :param routing_number: The routing_number of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :type: str
        """

        self._routing_number = routing_number

    @property
    def iban(self):
        """
        Gets the iban of this Ptsv2paymentsidrefundsPaymentInformationBank.
        International Bank Account Number (IBAN) for the bank account. For some countries you can provide this number instead of the traditional bank account information. You can use this field only when scoring a direct debit transaction. 

        :return: The iban of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """
        Sets the iban of this Ptsv2paymentsidrefundsPaymentInformationBank.
        International Bank Account Number (IBAN) for the bank account. For some countries you can provide this number instead of the traditional bank account information. You can use this field only when scoring a direct debit transaction. 

        :param iban: The iban of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :type: str
        """

        self._iban = iban

    @property
    def swift_code(self):
        """
        Gets the swift_code of this Ptsv2paymentsidrefundsPaymentInformationBank.
        Bank's SWIFT code. You can use this field only when scoring a direct debit transaction. Required only for crossborder transactions. 

        :return: The swift_code of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :rtype: str
        """
        return self._swift_code

    @swift_code.setter
    def swift_code(self, swift_code):
        """
        Sets the swift_code of this Ptsv2paymentsidrefundsPaymentInformationBank.
        Bank's SWIFT code. You can use this field only when scoring a direct debit transaction. Required only for crossborder transactions. 

        :param swift_code: The swift_code of this Ptsv2paymentsidrefundsPaymentInformationBank.
        :type: str
        """

        self._swift_code = swift_code

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
        if not isinstance(other, Ptsv2paymentsidrefundsPaymentInformationBank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
