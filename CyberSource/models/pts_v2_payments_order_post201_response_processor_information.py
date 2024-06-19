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


class PtsV2PaymentsOrderPost201ResponseProcessorInformation(object):
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
        'seller_protection': 'PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection',
        'avs': 'PtsV2PaymentsPost201Response1ProcessorInformationAvs',
        'transaction_id': 'str',
        'response_details': 'str'
    }

    attribute_map = {
        'seller_protection': 'sellerProtection',
        'avs': 'avs',
        'transaction_id': 'transactionId',
        'response_details': 'responseDetails'
    }

    def __init__(self, seller_protection=None, avs=None, transaction_id=None, response_details=None):
        """
        PtsV2PaymentsOrderPost201ResponseProcessorInformation - a model defined in Swagger
        """

        self._seller_protection = None
        self._avs = None
        self._transaction_id = None
        self._response_details = None

        if seller_protection is not None:
          self.seller_protection = seller_protection
        if avs is not None:
          self.avs = avs
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if response_details is not None:
          self.response_details = response_details

    @property
    def seller_protection(self):
        """
        Gets the seller_protection of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.

        :return: The seller_protection of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :rtype: PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection
        """
        return self._seller_protection

    @seller_protection.setter
    def seller_protection(self, seller_protection):
        """
        Sets the seller_protection of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.

        :param seller_protection: The seller_protection of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :type: PtsV2PaymentsOrderPost201ResponseProcessorInformationSellerProtection
        """

        self._seller_protection = seller_protection

    @property
    def avs(self):
        """
        Gets the avs of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.

        :return: The avs of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :rtype: PtsV2PaymentsPost201Response1ProcessorInformationAvs
        """
        return self._avs

    @avs.setter
    def avs(self, avs):
        """
        Sets the avs of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.

        :param avs: The avs of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :type: PtsV2PaymentsPost201Response1ProcessorInformationAvs
        """

        self._avs = avs

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this value.  Returned by the authorization service.  #### PIN debit Transaction identifier generated by the processor.  Returned by PIN debit credit.  #### GPX Processor transaction ID.  #### Cielo For Cielo, this value is the non-sequential unit (NSU) and is supported for all transactions. The value is generated by Cielo or the issuing bank.  #### Comercio Latino For Comercio Latino, this value is the proof of sale or non-sequential unit (NSU) number generated by the acquirers Cielo and Rede, or the issuing bank.  #### CyberSource through VisaNet and GPN For details about this value for CyberSource through VisaNet and GPN, see \"Network Transaction Identifiers\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Moneris This value identifies the transaction on a host system. It contains the following information: - Terminal used to process the transaction - Shift during which the transaction took place - Batch number - Transaction number within the batch You must store this value. If you give the customer a receipt, display this value on the receipt.  **Example** For the value 66012345001069003: - Terminal ID = 66012345 - Shift number = 001 - Batch number = 069 - Transaction number = 003 

        :return: The transaction_id of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this value.  Returned by the authorization service.  #### PIN debit Transaction identifier generated by the processor.  Returned by PIN debit credit.  #### GPX Processor transaction ID.  #### Cielo For Cielo, this value is the non-sequential unit (NSU) and is supported for all transactions. The value is generated by Cielo or the issuing bank.  #### Comercio Latino For Comercio Latino, this value is the proof of sale or non-sequential unit (NSU) number generated by the acquirers Cielo and Rede, or the issuing bank.  #### CyberSource through VisaNet and GPN For details about this value for CyberSource through VisaNet and GPN, see \"Network Transaction Identifiers\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Moneris This value identifies the transaction on a host system. It contains the following information: - Terminal used to process the transaction - Shift during which the transaction took place - Batch number - Transaction number within the batch You must store this value. If you give the customer a receipt, display this value on the receipt.  **Example** For the value 66012345001069003: - Terminal ID = 66012345 - Shift number = 001 - Batch number = 069 - Transaction number = 003 

        :param transaction_id: The transaction_id of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def response_details(self):
        """
        Gets the response_details of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        This field might contain information about a decline. This field is supported only for **CyberSource through VisaNet**. 

        :return: The response_details of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_details

    @response_details.setter
    def response_details(self, response_details):
        """
        Sets the response_details of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        This field might contain information about a decline. This field is supported only for **CyberSource through VisaNet**. 

        :param response_details: The response_details of this PtsV2PaymentsOrderPost201ResponseProcessorInformation.
        :type: str
        """

        self._response_details = response_details

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
        if not isinstance(other, PtsV2PaymentsOrderPost201ResponseProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
