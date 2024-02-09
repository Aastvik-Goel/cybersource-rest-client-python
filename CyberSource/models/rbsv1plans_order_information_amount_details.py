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


class Rbsv1plansOrderInformationAmountDetails(object):
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
        'currency': 'str',
        'billing_amount': 'str',
        'setup_fee': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'billing_amount': 'billingAmount',
        'setup_fee': 'setupFee'
    }

    def __init__(self, currency=None, billing_amount=None, setup_fee=None):
        """
        Rbsv1plansOrderInformationAmountDetails - a model defined in Swagger
        """

        self._currency = None
        self._billing_amount = None
        self._setup_fee = None

        self.currency = currency
        self.billing_amount = billing_amount
        if setup_fee is not None:
          self.setup_fee = setup_fee

    @property
    def currency(self):
        """
        Gets the currency of this Rbsv1plansOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :return: The currency of this Rbsv1plansOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Rbsv1plansOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :param currency: The currency of this Rbsv1plansOrderInformationAmountDetails.
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")

        self._currency = currency

    @property
    def billing_amount(self):
        """
        Gets the billing_amount of this Rbsv1plansOrderInformationAmountDetails.
        Billing amount for the billing period. 

        :return: The billing_amount of this Rbsv1plansOrderInformationAmountDetails.
        :rtype: str
        """
        return self._billing_amount

    @billing_amount.setter
    def billing_amount(self, billing_amount):
        """
        Sets the billing_amount of this Rbsv1plansOrderInformationAmountDetails.
        Billing amount for the billing period. 

        :param billing_amount: The billing_amount of this Rbsv1plansOrderInformationAmountDetails.
        :type: str
        """
        if billing_amount is None:
            raise ValueError("Invalid value for `billing_amount`, must not be `None`")

        self._billing_amount = billing_amount

    @property
    def setup_fee(self):
        """
        Gets the setup_fee of this Rbsv1plansOrderInformationAmountDetails.
        Subscription setup fee 

        :return: The setup_fee of this Rbsv1plansOrderInformationAmountDetails.
        :rtype: str
        """
        return self._setup_fee

    @setup_fee.setter
    def setup_fee(self, setup_fee):
        """
        Sets the setup_fee of this Rbsv1plansOrderInformationAmountDetails.
        Subscription setup fee 

        :param setup_fee: The setup_fee of this Rbsv1plansOrderInformationAmountDetails.
        :type: str
        """

        self._setup_fee = setup_fee

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
        if not isinstance(other, Rbsv1plansOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other