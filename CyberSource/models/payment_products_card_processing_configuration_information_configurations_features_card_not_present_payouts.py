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


class PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts(object):
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
        'reimbursement_code': 'str',
        'acquiring_institution_id': 'str',
        'business_application_id': 'str',
        'financial_institution_id': 'str',
        'merchant_aba_number': 'str',
        'network_order': 'str',
        'currencies': 'dict(str, PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayoutsCurrencies)',
        'merchant_id': 'str',
        'terminal_id': 'str'
    }

    attribute_map = {
        'reimbursement_code': 'reimbursementCode',
        'acquiring_institution_id': 'acquiringInstitutionId',
        'business_application_id': 'businessApplicationId',
        'financial_institution_id': 'financialInstitutionId',
        'merchant_aba_number': 'merchantAbaNumber',
        'network_order': 'networkOrder',
        'currencies': 'currencies',
        'merchant_id': 'merchantId',
        'terminal_id': 'terminalId'
    }

    def __init__(self, reimbursement_code=None, acquiring_institution_id=None, business_application_id=None, financial_institution_id=None, merchant_aba_number=None, network_order=None, currencies=None, merchant_id=None, terminal_id=None):
        """
        PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts - a model defined in Swagger
        """

        self._reimbursement_code = None
        self._acquiring_institution_id = None
        self._business_application_id = None
        self._financial_institution_id = None
        self._merchant_aba_number = None
        self._network_order = None
        self._currencies = None
        self._merchant_id = None
        self._terminal_id = None

        if reimbursement_code is not None:
          self.reimbursement_code = reimbursement_code
        if acquiring_institution_id is not None:
          self.acquiring_institution_id = acquiring_institution_id
        if business_application_id is not None:
          self.business_application_id = business_application_id
        if financial_institution_id is not None:
          self.financial_institution_id = financial_institution_id
        if merchant_aba_number is not None:
          self.merchant_aba_number = merchant_aba_number
        if network_order is not None:
          self.network_order = network_order
        if currencies is not None:
          self.currencies = currencies
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if terminal_id is not None:
          self.terminal_id = terminal_id

    @property
    def reimbursement_code(self):
        """
        Gets the reimbursement_code of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Applicable for VPC processors.

        :return: The reimbursement_code of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._reimbursement_code

    @reimbursement_code.setter
    def reimbursement_code(self, reimbursement_code):
        """
        Sets the reimbursement_code of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Applicable for VPC processors.

        :param reimbursement_code: The reimbursement_code of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._reimbursement_code = reimbursement_code

    @property
    def acquiring_institution_id(self):
        """
        Gets the acquiring_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        This code identifies the financial institution acting as the acquirer of this customer transaction. The acquirer is the member or system user that signed the merchant. This number is usually a Visa-assigned. Applicable for VPC processors.

        :return: The acquiring_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._acquiring_institution_id

    @acquiring_institution_id.setter
    def acquiring_institution_id(self, acquiring_institution_id):
        """
        Sets the acquiring_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        This code identifies the financial institution acting as the acquirer of this customer transaction. The acquirer is the member or system user that signed the merchant. This number is usually a Visa-assigned. Applicable for VPC processors.

        :param acquiring_institution_id: The acquiring_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._acquiring_institution_id = acquiring_institution_id

    @property
    def business_application_id(self):
        """
        Gets the business_application_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Transaction type. List of supported identifiers documented in the Developer Guide. Applicable for GPX (gpx) and VPC processors.

        :return: The business_application_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._business_application_id

    @business_application_id.setter
    def business_application_id(self, business_application_id):
        """
        Sets the business_application_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Transaction type. List of supported identifiers documented in the Developer Guide. Applicable for GPX (gpx) and VPC processors.

        :param business_application_id: The business_application_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._business_application_id = business_application_id

    @property
    def financial_institution_id(self):
        """
        Gets the financial_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Applicable for GPX (gpx) and VPC processors.

        :return: The financial_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._financial_institution_id

    @financial_institution_id.setter
    def financial_institution_id(self, financial_institution_id):
        """
        Sets the financial_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Applicable for GPX (gpx) and VPC processors.

        :param financial_institution_id: The financial_institution_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._financial_institution_id = financial_institution_id

    @property
    def merchant_aba_number(self):
        """
        Gets the merchant_aba_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Routing Number to identify banks within the United States. Applicable for VPC processors.

        :return: The merchant_aba_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._merchant_aba_number

    @merchant_aba_number.setter
    def merchant_aba_number(self, merchant_aba_number):
        """
        Sets the merchant_aba_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Routing Number to identify banks within the United States. Applicable for VPC processors.

        :param merchant_aba_number: The merchant_aba_number of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._merchant_aba_number = merchant_aba_number

    @property
    def network_order(self):
        """
        Gets the network_order of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Order of the networks in which Visa should make routing decisions. Applicable for VPC processors.

        :return: The network_order of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._network_order

    @network_order.setter
    def network_order(self, network_order):
        """
        Sets the network_order of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Order of the networks in which Visa should make routing decisions. Applicable for VPC processors.

        :param network_order: The network_order of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._network_order = network_order

    @property
    def currencies(self):
        """
        Gets the currencies of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Three-character [ISO 4217 ALPHA-3 Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)

        :return: The currencies of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: dict(str, PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayoutsCurrencies)
        """
        return self._currencies

    @currencies.setter
    def currencies(self, currencies):
        """
        Sets the currencies of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Three-character [ISO 4217 ALPHA-3 Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)

        :param currencies: The currencies of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: dict(str, PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayoutsCurrencies)
        """

        self._currencies = currencies

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Merchant ID assigned by an acquirer or a processor. Should not be overridden by any other party.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>Barclays</td><td>cnp, hybrid</td><td>No</td><td>1</td><td>11</td><td>^[0-9]+$</td></tr> </table> 

        :return: The merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        Merchant ID assigned by an acquirer or a processor. Should not be overridden by any other party.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>Barclays</td><td>cnp, hybrid</td><td>No</td><td>1</td><td>11</td><td>^[0-9]+$</td></tr> </table> 

        :param merchant_id: The merchant_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def terminal_id(self):
        """
        Gets the terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        The 'Terminal Id' aka TID, is an identifier used for with your payments processor. Depending on the processor and payment acceptance type this may also be the default Terminal ID used for Card Present and Virtual Terminal transactions.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>Barclays</td><td>cnp, hybrid</td><td>No</td><td>1</td><td>255</td><td>^[0-9:&#92;-]+$</td></tr> </table> 

        :return: The terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """
        Sets the terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        The 'Terminal Id' aka TID, is an identifier used for with your payments processor. Depending on the processor and payment acceptance type this may also be the default Terminal ID used for Card Present and Virtual Terminal transactions.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>Barclays</td><td>cnp, hybrid</td><td>No</td><td>1</td><td>255</td><td>^[0-9:&#92;-]+$</td></tr> </table> 

        :param terminal_id: The terminal_id of this PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts.
        :type: str
        """

        self._terminal_id = terminal_id

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
        if not isinstance(other, PaymentProductsCardProcessingConfigurationInformationConfigurationsFeaturesCardNotPresentPayouts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
