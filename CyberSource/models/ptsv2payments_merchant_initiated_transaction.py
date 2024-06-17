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


class Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction(object):
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
        'reason': 'str',
        'previous_transaction_id': 'str',
        'original_authorized_amount': 'str'
    }

    attribute_map = {
        'reason': 'reason',
        'previous_transaction_id': 'previousTransactionId',
        'original_authorized_amount': 'originalAuthorizedAmount'
    }

    def __init__(self, reason=None, previous_transaction_id=None, original_authorized_amount=None):
        """
        Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction - a model defined in Swagger
        """

        self._reason = None
        self._previous_transaction_id = None
        self._original_authorized_amount = None

        if reason is not None:
          self.reason = reason
        if previous_transaction_id is not None:
          self.previous_transaction_id = previous_transaction_id
        if original_authorized_amount is not None:
          self.original_authorized_amount = original_authorized_amount

    @property
    def reason(self):
        """
        Gets the reason of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Reason for the merchant-initiated transaction or incremental authorization. Possible values: - `1`: Resubmission - `2`: Delayed charge - `3`: Reauthorization for split shipment - `4`: No show - `5`: Account top up This field is required only for the five kinds of transactions in the preceding list. This field is supported only for merchant-initiated transactions and incremental authorizations.  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR0 - Position: 160-163 - Field: Message Reason Code  #### All Processors For details, see `subsequent_auth_reason` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The reason of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Reason for the merchant-initiated transaction or incremental authorization. Possible values: - `1`: Resubmission - `2`: Delayed charge - `3`: Reauthorization for split shipment - `4`: No show - `5`: Account top up This field is required only for the five kinds of transactions in the preceding list. This field is supported only for merchant-initiated transactions and incremental authorizations.  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR0 - Position: 160-163 - Field: Message Reason Code  #### All Processors For details, see `subsequent_auth_reason` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param reason: The reason of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :type: str
        """



        self._reason = reason

    @property
    def previous_transaction_id(self):
        """
        Gets the previous_transaction_id of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Network transaction identifier that was returned in the payment response field _processorInformation.transactionID_ in the reply message for either the original merchant-initiated payment in the series or the previous merchant-initiated payment in the series.  If the current payment request includes a token instead of an account number, the following time limits apply for the value of this field: - For a **resubmission**, the transaction ID must be less than 14 days old. - For a **delayed charge** or **reauthorization**, the transaction ID must be less than 30 days old.  **NOTE**: The value for this field does not correspond to any data in the TC 33 capture file5. This field is supported only for Visa transactions on CyberSource through VisaNet. 

        :return: The previous_transaction_id of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :rtype: str
        """
        return self._previous_transaction_id

    @previous_transaction_id.setter
    def previous_transaction_id(self, previous_transaction_id):
        """
        Sets the previous_transaction_id of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Network transaction identifier that was returned in the payment response field _processorInformation.transactionID_ in the reply message for either the original merchant-initiated payment in the series or the previous merchant-initiated payment in the series.  If the current payment request includes a token instead of an account number, the following time limits apply for the value of this field: - For a **resubmission**, the transaction ID must be less than 14 days old. - For a **delayed charge** or **reauthorization**, the transaction ID must be less than 30 days old.  **NOTE**: The value for this field does not correspond to any data in the TC 33 capture file5. This field is supported only for Visa transactions on CyberSource through VisaNet. 

        :param previous_transaction_id: The previous_transaction_id of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :type: str
        """



        self._previous_transaction_id = previous_transaction_id

    @property
    def original_authorized_amount(self):
        """
        Gets the original_authorized_amount of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Amount of the original authorization.  This field is supported only for Apple Pay, Google Pay, and Samsung Pay transactions with Discover on FDC Nashville Global and Chase Paymentech.  See \"Recurring Payments,\" and \"Subsequent Authorizations,\" field description in the [Payment Network Tokenization Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/tokenization_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :return: The original_authorized_amount of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :rtype: str
        """
        return self._original_authorized_amount

    @original_authorized_amount.setter
    def original_authorized_amount(self, original_authorized_amount):
        """
        Sets the original_authorized_amount of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        Amount of the original authorization.  This field is supported only for Apple Pay, Google Pay, and Samsung Pay transactions with Discover on FDC Nashville Global and Chase Paymentech.  See \"Recurring Payments,\" and \"Subsequent Authorizations,\" field description in the [Payment Network Tokenization Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/tokenization_SCMP_API/html/wwhelp/wwhimpl/js/html/wwhelp.htm) 

        :param original_authorized_amount: The original_authorized_amount of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction.
        :type: str
        """



        self._original_authorized_amount = original_authorized_amount

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
        if not isinstance(other, Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
