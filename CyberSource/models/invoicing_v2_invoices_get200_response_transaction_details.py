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


class InvoicingV2InvoicesGet200ResponseTransactionDetails(object):
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
        'transaction_id': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'amount': 'amount'
    }

    def __init__(self, transaction_id=None, amount=None):
        """
        InvoicingV2InvoicesGet200ResponseTransactionDetails - a model defined in Swagger
        """

        self._transaction_id = None
        self._amount = None

        if transaction_id is not None:
          self.transaction_id = transaction_id
        if amount is not None:
          self.amount = amount

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        Payer auth Transaction identifier.

        :return: The transaction_id of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        Payer auth Transaction identifier.

        :param transaction_id: The transaction_id of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def amount(self):
        """
        Gets the amount of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. For details, see: - \"Authorization Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Capture Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Credit Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. For details, see \"Zero Amount Authorizations,\" \"Credit Information for Specific Processors\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Card Present Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.  #### Invoicing Required for creating a new invoice.  #### PIN Debit Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. For details, see `grand_total_amount` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in \"Authorization Information for Specific Processors\" of the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC for First Data Not used. 

        :return: The amount of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. For details, see: - \"Authorization Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Capture Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Credit Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. For details, see \"Zero Amount Authorizations,\" \"Credit Information for Specific Processors\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Card Present Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.  #### Invoicing Required for creating a new invoice.  #### PIN Debit Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. For details, see `grand_total_amount` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in \"Authorization Information for Specific Processors\" of the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC for First Data Not used. 

        :param amount: The amount of this InvoicingV2InvoicesGet200ResponseTransactionDetails.
        :type: str
        """

        self._amount = amount

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
        if not isinstance(other, InvoicingV2InvoicesGet200ResponseTransactionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
