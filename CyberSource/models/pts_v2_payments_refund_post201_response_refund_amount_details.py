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


class PtsV2PaymentsRefundPost201ResponseRefundAmountDetails(object):
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
        'refund_amount': 'str',
        'credit_amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'refund_amount': 'refundAmount',
        'credit_amount': 'creditAmount',
        'currency': 'currency'
    }

    def __init__(self, refund_amount=None, credit_amount=None, currency=None):
        """
        PtsV2PaymentsRefundPost201ResponseRefundAmountDetails - a model defined in Swagger
        """

        self._refund_amount = None
        self._credit_amount = None
        self._currency = None

        if refund_amount is not None:
          self.refund_amount = refund_amount
        if credit_amount is not None:
          self.credit_amount = credit_amount
        if currency is not None:
          self.currency = currency

    @property
    def refund_amount(self):
        """
        Gets the refund_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        Total amount of the refund.

        :return: The refund_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        :rtype: str
        """
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, refund_amount):
        """
        Sets the refund_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        Total amount of the refund.

        :param refund_amount: The refund_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        :type: str
        """

        self._refund_amount = refund_amount

    @property
    def credit_amount(self):
        """
        Gets the credit_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        Amount that was credited to the cardholder's account.  Returned by PIN debit credit. 

        :return: The credit_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        :rtype: str
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """
        Sets the credit_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        Amount that was credited to the cardholder's account.  Returned by PIN debit credit. 

        :param credit_amount: The credit_amount of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        :type: str
        """

        self._credit_amount = credit_amount

    @property
    def currency(self):
        """
        Gets the currency of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency.  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :return: The currency of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency.  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :param currency: The currency of this PtsV2PaymentsRefundPost201ResponseRefundAmountDetails.
        :type: str
        """

        self._currency = currency

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
        if not isinstance(other, PtsV2PaymentsRefundPost201ResponseRefundAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
