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


class PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds(object):
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
        'acquirer_country_code': 'int',
        'acquiring_bin': 'int',
        'allow_crypto_currency_purchase': 'bool',
        'financial_institution_id': 'str',
        'network_order': 'str',
        'national_reimbursement_fee': 'str',
        'originator_business_application_id': 'str',
        'originator_pseudo_aba_number': 'str',
        'processor_account': 'list[PaymentsProductsPayoutsConfigurationInformationConfigurationsProcessorAccount]'
    }

    attribute_map = {
        'acquirer_country_code': 'acquirerCountryCode',
        'acquiring_bin': 'acquiringBIN',
        'allow_crypto_currency_purchase': 'allowCryptoCurrencyPurchase',
        'financial_institution_id': 'financialInstitutionId',
        'network_order': 'networkOrder',
        'national_reimbursement_fee': 'nationalReimbursementFee',
        'originator_business_application_id': 'originatorBusinessApplicationId',
        'originator_pseudo_aba_number': 'originatorPseudoAbaNumber',
        'processor_account': 'processorAccount'
    }

    def __init__(self, acquirer_country_code=None, acquiring_bin=None, allow_crypto_currency_purchase=None, financial_institution_id=None, network_order=None, national_reimbursement_fee=None, originator_business_application_id=None, originator_pseudo_aba_number=None, processor_account=None):
        """
        PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds - a model defined in Swagger
        """

        self._acquirer_country_code = None
        self._acquiring_bin = None
        self._allow_crypto_currency_purchase = None
        self._financial_institution_id = None
        self._network_order = None
        self._national_reimbursement_fee = None
        self._originator_business_application_id = None
        self._originator_pseudo_aba_number = None
        self._processor_account = None

        self.acquirer_country_code = acquirer_country_code
        self.acquiring_bin = acquiring_bin
        if allow_crypto_currency_purchase is not None:
          self.allow_crypto_currency_purchase = allow_crypto_currency_purchase
        if financial_institution_id is not None:
          self.financial_institution_id = financial_institution_id
        if network_order is not None:
          self.network_order = network_order
        if national_reimbursement_fee is not None:
          self.national_reimbursement_fee = national_reimbursement_fee
        self.originator_business_application_id = originator_business_application_id
        if originator_pseudo_aba_number is not None:
          self.originator_pseudo_aba_number = originator_pseudo_aba_number
        self.processor_account = processor_account

    @property
    def acquirer_country_code(self):
        """
        Gets the acquirer_country_code of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The acquirer_country_code of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: int
        """
        return self._acquirer_country_code

    @acquirer_country_code.setter
    def acquirer_country_code(self, acquirer_country_code):
        """
        Sets the acquirer_country_code of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param acquirer_country_code: The acquirer_country_code of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: int
        """



        self._acquirer_country_code = acquirer_country_code

    @property
    def acquiring_bin(self):
        """
        Gets the acquiring_bin of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The acquiring_bin of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: int
        """
        return self._acquiring_bin

    @acquiring_bin.setter
    def acquiring_bin(self, acquiring_bin):
        """
        Sets the acquiring_bin of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param acquiring_bin: The acquiring_bin of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: int
        """



        self._acquiring_bin = acquiring_bin

    @property
    def allow_crypto_currency_purchase(self):
        """
        Gets the allow_crypto_currency_purchase of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        This configuration allows a transaction to be flagged for cryptocurrency funds transfer.

        :return: The allow_crypto_currency_purchase of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: bool
        """
        return self._allow_crypto_currency_purchase

    @allow_crypto_currency_purchase.setter
    def allow_crypto_currency_purchase(self, allow_crypto_currency_purchase):
        """
        Sets the allow_crypto_currency_purchase of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        This configuration allows a transaction to be flagged for cryptocurrency funds transfer.

        :param allow_crypto_currency_purchase: The allow_crypto_currency_purchase of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: bool
        """



        self._allow_crypto_currency_purchase = allow_crypto_currency_purchase

    @property
    def financial_institution_id(self):
        """
        Gets the financial_institution_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The financial_institution_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: str
        """
        return self._financial_institution_id

    @financial_institution_id.setter
    def financial_institution_id(self, financial_institution_id):
        """
        Sets the financial_institution_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param financial_institution_id: The financial_institution_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: str
        """



        self._financial_institution_id = financial_institution_id

    @property
    def network_order(self):
        """
        Gets the network_order of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The network_order of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: str
        """
        return self._network_order

    @network_order.setter
    def network_order(self, network_order):
        """
        Sets the network_order of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param network_order: The network_order of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: str
        """



        self._network_order = network_order

    @property
    def national_reimbursement_fee(self):
        """
        Gets the national_reimbursement_fee of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The national_reimbursement_fee of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: str
        """
        return self._national_reimbursement_fee

    @national_reimbursement_fee.setter
    def national_reimbursement_fee(self, national_reimbursement_fee):
        """
        Sets the national_reimbursement_fee of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param national_reimbursement_fee: The national_reimbursement_fee of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: str
        """



        self._national_reimbursement_fee = national_reimbursement_fee

    @property
    def originator_business_application_id(self):
        """
        Gets the originator_business_application_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The originator_business_application_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: str
        """
        return self._originator_business_application_id

    @originator_business_application_id.setter
    def originator_business_application_id(self, originator_business_application_id):
        """
        Sets the originator_business_application_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param originator_business_application_id: The originator_business_application_id of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: str
        """



        self._originator_business_application_id = originator_business_application_id

    @property
    def originator_pseudo_aba_number(self):
        """
        Gets the originator_pseudo_aba_number of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The originator_pseudo_aba_number of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: str
        """
        return self._originator_pseudo_aba_number

    @originator_pseudo_aba_number.setter
    def originator_pseudo_aba_number(self, originator_pseudo_aba_number):
        """
        Sets the originator_pseudo_aba_number of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param originator_pseudo_aba_number: The originator_pseudo_aba_number of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: str
        """



        self._originator_pseudo_aba_number = originator_pseudo_aba_number

    @property
    def processor_account(self):
        """
        Gets the processor_account of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :return: The processor_account of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :rtype: list[PaymentsProductsPayoutsConfigurationInformationConfigurationsProcessorAccount]
        """
        return self._processor_account

    @processor_account.setter
    def processor_account(self, processor_account):
        """
        Sets the processor_account of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        TBD

        :param processor_account: The processor_account of this PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds.
        :type: list[PaymentsProductsPayoutsConfigurationInformationConfigurationsProcessorAccount]
        """



        self._processor_account = processor_account

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
        if not isinstance(other, PaymentsProductsPayoutsConfigurationInformationConfigurationsPushfunds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
