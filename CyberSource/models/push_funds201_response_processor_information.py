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


class PushFunds201ResponseProcessorInformation(object):
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
        'transaction_id': 'int',
        'response_code': 'str',
        'approval_code': 'str',
        'system_trace_audit_number': 'str',
        'response_code_source': 'str',
        'retrieval_reference_number': 'str'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'response_code': 'responseCode',
        'approval_code': 'approvalCode',
        'system_trace_audit_number': 'systemTraceAuditNumber',
        'response_code_source': 'responseCodeSource',
        'retrieval_reference_number': 'retrievalReferenceNumber'
    }

    def __init__(self, transaction_id=None, response_code=None, approval_code=None, system_trace_audit_number=None, response_code_source=None, retrieval_reference_number=None):
        """
        PushFunds201ResponseProcessorInformation - a model defined in Swagger
        """

        self._transaction_id = None
        self._response_code = None
        self._approval_code = None
        self._system_trace_audit_number = None
        self._response_code_source = None
        self._retrieval_reference_number = None

        if transaction_id is not None:
          self.transaction_id = transaction_id
        if response_code is not None:
          self.response_code = response_code
        if approval_code is not None:
          self.approval_code = approval_code
        if system_trace_audit_number is not None:
          self.system_trace_audit_number = system_trace_audit_number
        if response_code_source is not None:
          self.response_code_source = response_code_source
        if retrieval_reference_number is not None:
          self.retrieval_reference_number = retrieval_reference_number

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this PushFunds201ResponseProcessorInformation.
        Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor. 

        :return: The transaction_id of this PushFunds201ResponseProcessorInformation.
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this PushFunds201ResponseProcessorInformation.
        Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor. 

        :param transaction_id: The transaction_id of this PushFunds201ResponseProcessorInformation.
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def response_code(self):
        """
        Gets the response_code of this PushFunds201ResponseProcessorInformation.
        Transaction status from the processor. 

        :return: The response_code of this PushFunds201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PushFunds201ResponseProcessorInformation.
        Transaction status from the processor. 

        :param response_code: The response_code of this PushFunds201ResponseProcessorInformation.
        :type: str
        """

        self._response_code = response_code

    @property
    def approval_code(self):
        """
        Gets the approval_code of this PushFunds201ResponseProcessorInformation.
        Issuer-generated approval code for the transaction. 

        :return: The approval_code of this PushFunds201ResponseProcessorInformation.
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """
        Sets the approval_code of this PushFunds201ResponseProcessorInformation.
        Issuer-generated approval code for the transaction. 

        :param approval_code: The approval_code of this PushFunds201ResponseProcessorInformation.
        :type: str
        """

        self._approval_code = approval_code

    @property
    def system_trace_audit_number(self):
        """
        Gets the system_trace_audit_number of this PushFunds201ResponseProcessorInformation.
        System audit number. Returned by authorization and incremental authorization services.  Visa Platform Connect  System trace number that must be printed on the customer’s receipt. 

        :return: The system_trace_audit_number of this PushFunds201ResponseProcessorInformation.
        :rtype: str
        """
        return self._system_trace_audit_number

    @system_trace_audit_number.setter
    def system_trace_audit_number(self, system_trace_audit_number):
        """
        Sets the system_trace_audit_number of this PushFunds201ResponseProcessorInformation.
        System audit number. Returned by authorization and incremental authorization services.  Visa Platform Connect  System trace number that must be printed on the customer’s receipt. 

        :param system_trace_audit_number: The system_trace_audit_number of this PushFunds201ResponseProcessorInformation.
        :type: str
        """

        self._system_trace_audit_number = system_trace_audit_number

    @property
    def response_code_source(self):
        """
        Gets the response_code_source of this PushFunds201ResponseProcessorInformation.
        Used by Visa only and contains the response source/reason code that identifies the source of the response decision. 

        :return: The response_code_source of this PushFunds201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code_source

    @response_code_source.setter
    def response_code_source(self, response_code_source):
        """
        Sets the response_code_source of this PushFunds201ResponseProcessorInformation.
        Used by Visa only and contains the response source/reason code that identifies the source of the response decision. 

        :param response_code_source: The response_code_source of this PushFunds201ResponseProcessorInformation.
        :type: str
        """

        self._response_code_source = response_code_source

    @property
    def retrieval_reference_number(self):
        """
        Gets the retrieval_reference_number of this PushFunds201ResponseProcessorInformation.
        Unique reference number returned by the processor that identifies the transaction at the network.  Supported by Mastercard Send 

        :return: The retrieval_reference_number of this PushFunds201ResponseProcessorInformation.
        :rtype: str
        """
        return self._retrieval_reference_number

    @retrieval_reference_number.setter
    def retrieval_reference_number(self, retrieval_reference_number):
        """
        Sets the retrieval_reference_number of this PushFunds201ResponseProcessorInformation.
        Unique reference number returned by the processor that identifies the transaction at the network.  Supported by Mastercard Send 

        :param retrieval_reference_number: The retrieval_reference_number of this PushFunds201ResponseProcessorInformation.
        :type: str
        """

        self._retrieval_reference_number = retrieval_reference_number

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
        if not isinstance(other, PushFunds201ResponseProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
