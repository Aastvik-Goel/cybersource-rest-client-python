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


class PtsV2PaymentsPost201Response1ProcessorInformation(object):
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
        'trade_number': 'str',
        'raw_response': 'str',
        'response_code': 'str',
        'seller_protection': 'PtsV2PaymentsPost201Response1ProcessorInformationSellerProtection',
        'avs': 'PtsV2PaymentsPost201Response1ProcessorInformationAvs'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'trade_number': 'tradeNumber',
        'raw_response': 'rawResponse',
        'response_code': 'responseCode',
        'seller_protection': 'sellerProtection',
        'avs': 'avs'
    }

    def __init__(self, transaction_id=None, trade_number=None, raw_response=None, response_code=None, seller_protection=None, avs=None):
        """
        PtsV2PaymentsPost201Response1ProcessorInformation - a model defined in Swagger
        """

        self._transaction_id = None
        self._trade_number = None
        self._raw_response = None
        self._response_code = None
        self._seller_protection = None
        self._avs = None

        if transaction_id is not None:
          self.transaction_id = transaction_id
        if trade_number is not None:
          self.trade_number = trade_number
        if raw_response is not None:
          self.raw_response = raw_response
        if response_code is not None:
          self.response_code = response_code
        if seller_protection is not None:
          self.seller_protection = seller_protection
        if avs is not None:
          self.avs = avs

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this PtsV2PaymentsPost201Response1ProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this value.  Returned by the authorization service.  #### PIN debit Transaction identifier generated by the processor.  Returned by PIN debit credit.  #### GPX Processor transaction ID.  #### Cielo For Cielo, this value is the non-sequential unit (NSU) and is supported for all transactions. The value is generated by Cielo or the issuing bank.  #### Comercio Latino For Comercio Latino, this value is the proof of sale or non-sequential unit (NSU) number generated by the acquirers Cielo and Rede, or the issuing bank.  #### CyberSource through VisaNet and GPN For details about this value for CyberSource through VisaNet and GPN, see \"Network Transaction Identifiers\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Moneris This value identifies the transaction on a host system. It contains the following information: - Terminal used to process the transaction - Shift during which the transaction took place - Batch number - Transaction number within the batch You must store this value. If you give the customer a receipt, display this value on the receipt.  **Example** For the value 66012345001069003: - Terminal ID = 66012345 - Shift number = 001 - Batch number = 069 - Transaction number = 003 

        :return: The transaction_id of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this PtsV2PaymentsPost201Response1ProcessorInformation.
        Network transaction identifier (TID). You can use this value to identify a specific transaction when you are discussing the transaction with your processor. Not all processors provide this value.  Returned by the authorization service.  #### PIN debit Transaction identifier generated by the processor.  Returned by PIN debit credit.  #### GPX Processor transaction ID.  #### Cielo For Cielo, this value is the non-sequential unit (NSU) and is supported for all transactions. The value is generated by Cielo or the issuing bank.  #### Comercio Latino For Comercio Latino, this value is the proof of sale or non-sequential unit (NSU) number generated by the acquirers Cielo and Rede, or the issuing bank.  #### CyberSource through VisaNet and GPN For details about this value for CyberSource through VisaNet and GPN, see \"Network Transaction Identifiers\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Moneris This value identifies the transaction on a host system. It contains the following information: - Terminal used to process the transaction - Shift during which the transaction took place - Batch number - Transaction number within the batch You must store this value. If you give the customer a receipt, display this value on the receipt.  **Example** For the value 66012345001069003: - Terminal ID = 66012345 - Shift number = 001 - Batch number = 069 - Transaction number = 003 

        :param transaction_id: The transaction_id of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def trade_number(self):
        """
        Gets the trade_number of this PtsV2PaymentsPost201Response1ProcessorInformation.
        The description for this field is not available.

        :return: The trade_number of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :rtype: str
        """
        return self._trade_number

    @trade_number.setter
    def trade_number(self, trade_number):
        """
        Sets the trade_number of this PtsV2PaymentsPost201Response1ProcessorInformation.
        The description for this field is not available.

        :param trade_number: The trade_number of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :type: str
        """

        self._trade_number = trade_number

    @property
    def raw_response(self):
        """
        Gets the raw_response of this PtsV2PaymentsPost201Response1ProcessorInformation.
        This field is set to the value of failure reason returned by the processor. 

        :return: The raw_response of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :rtype: str
        """
        return self._raw_response

    @raw_response.setter
    def raw_response(self, raw_response):
        """
        Sets the raw_response of this PtsV2PaymentsPost201Response1ProcessorInformation.
        This field is set to the value of failure reason returned by the processor. 

        :param raw_response: The raw_response of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :type: str
        """

        self._raw_response = raw_response

    @property
    def response_code(self):
        """
        Gets the response_code of this PtsV2PaymentsPost201Response1ProcessorInformation.
        This field is set to the value of response code returned by the processor. 

        :return: The response_code of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PtsV2PaymentsPost201Response1ProcessorInformation.
        This field is set to the value of response code returned by the processor. 

        :param response_code: The response_code of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :type: str
        """

        self._response_code = response_code

    @property
    def seller_protection(self):
        """
        Gets the seller_protection of this PtsV2PaymentsPost201Response1ProcessorInformation.

        :return: The seller_protection of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :rtype: PtsV2PaymentsPost201Response1ProcessorInformationSellerProtection
        """
        return self._seller_protection

    @seller_protection.setter
    def seller_protection(self, seller_protection):
        """
        Sets the seller_protection of this PtsV2PaymentsPost201Response1ProcessorInformation.

        :param seller_protection: The seller_protection of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :type: PtsV2PaymentsPost201Response1ProcessorInformationSellerProtection
        """

        self._seller_protection = seller_protection

    @property
    def avs(self):
        """
        Gets the avs of this PtsV2PaymentsPost201Response1ProcessorInformation.

        :return: The avs of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :rtype: PtsV2PaymentsPost201Response1ProcessorInformationAvs
        """
        return self._avs

    @avs.setter
    def avs(self, avs):
        """
        Sets the avs of this PtsV2PaymentsPost201Response1ProcessorInformation.

        :param avs: The avs of this PtsV2PaymentsPost201Response1ProcessorInformation.
        :type: PtsV2PaymentsPost201Response1ProcessorInformationAvs
        """

        self._avs = avs

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
        if not isinstance(other, PtsV2PaymentsPost201Response1ProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
