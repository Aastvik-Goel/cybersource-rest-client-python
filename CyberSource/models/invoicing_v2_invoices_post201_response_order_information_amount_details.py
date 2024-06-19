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


class InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails(object):
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
        'total_amount': 'str',
        'currency': 'str',
        'balance_amount': 'str',
        'discount_amount': 'str',
        'discount_percent': 'float',
        'sub_amount': 'float',
        'minimum_partial_amount': 'float',
        'tax_details': 'Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails',
        'freight': 'Invoicingv2invoicesOrderInformationAmountDetailsFreight'
    }

    attribute_map = {
        'total_amount': 'totalAmount',
        'currency': 'currency',
        'balance_amount': 'balanceAmount',
        'discount_amount': 'discountAmount',
        'discount_percent': 'discountPercent',
        'sub_amount': 'subAmount',
        'minimum_partial_amount': 'minimumPartialAmount',
        'tax_details': 'taxDetails',
        'freight': 'freight'
    }

    def __init__(self, total_amount=None, currency=None, balance_amount=None, discount_amount=None, discount_percent=None, sub_amount=None, minimum_partial_amount=None, tax_details=None, freight=None):
        """
        InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails - a model defined in Swagger
        """

        self._total_amount = None
        self._currency = None
        self._balance_amount = None
        self._discount_amount = None
        self._discount_percent = None
        self._sub_amount = None
        self._minimum_partial_amount = None
        self._tax_details = None
        self._freight = None

        if total_amount is not None:
          self.total_amount = total_amount
        if currency is not None:
          self.currency = currency
        if balance_amount is not None:
          self.balance_amount = balance_amount
        if discount_amount is not None:
          self.discount_amount = discount_amount
        if discount_percent is not None:
          self.discount_percent = discount_percent
        if sub_amount is not None:
          self.sub_amount = sub_amount
        if minimum_partial_amount is not None:
          self.minimum_partial_amount = minimum_partial_amount
        if tax_details is not None:
          self.tax_details = tax_details
        if freight is not None:
          self.freight = freight

    @property
    def total_amount(self):
        """
        Gets the total_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. For details, see: - \"Authorization Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Capture Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Credit Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. For details, see \"Zero Amount Authorizations,\" \"Credit Information for Specific Processors\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Card Present Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.  #### Invoicing Required for creating a new invoice.  #### PIN Debit Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. For details, see `grand_total_amount` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in \"Authorization Information for Specific Processors\" of the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC for First Data Not used. 

        :return: The total_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. For details, see: - \"Authorization Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Capture Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Credit Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. For details, see \"Zero Amount Authorizations,\" \"Credit Information for Specific Processors\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Card Present Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.  #### Invoicing Required for creating a new invoice.  #### PIN Debit Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. For details, see `grand_total_amount` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in \"Authorization Information for Specific Processors\" of the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC for First Data Not used. 

        :param total_amount: The total_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._total_amount = total_amount

    @property
    def currency(self):
        """
        Gets the currency of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :return: The currency of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :param currency: The currency of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._currency = currency

    @property
    def balance_amount(self):
        """
        Gets the balance_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Remaining balance on the account.  Returned by authorization service.  #### PIN debit Remaining balance on the prepaid card.  Returned by PIN debit purchase. 

        :return: The balance_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._balance_amount

    @balance_amount.setter
    def balance_amount(self, balance_amount):
        """
        Sets the balance_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Remaining balance on the account.  Returned by authorization service.  #### PIN debit Remaining balance on the prepaid card.  Returned by PIN debit purchase. 

        :param balance_amount: The balance_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._balance_amount = balance_amount

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Total discount amount applied to the order. 

        :return: The discount_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Total discount amount applied to the order. 

        :param discount_amount: The discount_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: str
        """

        self._discount_amount = discount_amount

    @property
    def discount_percent(self):
        """
        Gets the discount_percent of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        The total discount percentage applied to the invoice.

        :return: The discount_percent of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: float
        """
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        """
        Sets the discount_percent of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        The total discount percentage applied to the invoice.

        :param discount_percent: The discount_percent of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: float
        """

        self._discount_percent = discount_percent

    @property
    def sub_amount(self):
        """
        Gets the sub_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Sub-amount of the invoice.

        :return: The sub_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: float
        """
        return self._sub_amount

    @sub_amount.setter
    def sub_amount(self, sub_amount):
        """
        Sets the sub_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        Sub-amount of the invoice.

        :param sub_amount: The sub_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: float
        """

        self._sub_amount = sub_amount

    @property
    def minimum_partial_amount(self):
        """
        Gets the minimum_partial_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        The minimum partial amount required to pay the invoice.

        :return: The minimum_partial_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: float
        """
        return self._minimum_partial_amount

    @minimum_partial_amount.setter
    def minimum_partial_amount(self, minimum_partial_amount):
        """
        Sets the minimum_partial_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        The minimum partial amount required to pay the invoice.

        :param minimum_partial_amount: The minimum_partial_amount of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: float
        """

        self._minimum_partial_amount = minimum_partial_amount

    @property
    def tax_details(self):
        """
        Gets the tax_details of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.

        :return: The tax_details of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails
        """
        return self._tax_details

    @tax_details.setter
    def tax_details(self, tax_details):
        """
        Sets the tax_details of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.

        :param tax_details: The tax_details of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails
        """

        self._tax_details = tax_details

    @property
    def freight(self):
        """
        Gets the freight of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.

        :return: The freight of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :rtype: Invoicingv2invoicesOrderInformationAmountDetailsFreight
        """
        return self._freight

    @freight.setter
    def freight(self, freight):
        """
        Sets the freight of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.

        :param freight: The freight of this InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails.
        :type: Invoicingv2invoicesOrderInformationAmountDetailsFreight
        """

        self._freight = freight

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
        if not isinstance(other, InvoicingV2InvoicesPost201ResponseOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
