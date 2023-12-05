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


class PtsV2PayoutsPost201ResponseProcessorInformation(object):
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
        'approval_code': 'str',
        'response_code': 'str',
        'transaction_id': 'str',
        'system_trace_audit_number': 'str',
        'response_code_source': 'str'
    }

    attribute_map = {
        'approval_code': 'approvalCode',
        'response_code': 'responseCode',
        'transaction_id': 'transactionId',
        'system_trace_audit_number': 'systemTraceAuditNumber',
        'response_code_source': 'responseCodeSource'
    }

    def __init__(self, approval_code=None, response_code=None, transaction_id=None, system_trace_audit_number=None, response_code_source=None):
        """
        PtsV2PayoutsPost201ResponseProcessorInformation - a model defined in Swagger
        """

        self._approval_code = None
        self._response_code = None
        self._transaction_id = None
        self._system_trace_audit_number = None
        self._response_code_source = None

        if approval_code is not None:
          self.approval_code = approval_code
        if response_code is not None:
          self.response_code = response_code
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if system_trace_audit_number is not None:
          self.system_trace_audit_number = system_trace_audit_number
        if response_code_source is not None:
          self.response_code_source = response_code_source

    @property
    def approval_code(self):
        """
        Gets the approval_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Issuer-generated approval code for the transaction.

        :return: The approval_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """
        Sets the approval_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Issuer-generated approval code for the transaction.

        :param approval_code: The approval_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :type: str
        """

        self._approval_code = approval_code

    @property
    def response_code(self):
        """
        Gets the response_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Transaction status from the processor.

        :return: The response_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Transaction status from the processor.

        :param response_code: The response_code of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :type: str
        """

        self._response_code = response_code

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor. 

        :return: The transaction_id of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Network transaction identifier (TID). This value can be used to identify a specific transaction when you are discussing the transaction with your processor. 

        :param transaction_id: The transaction_id of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def system_trace_audit_number(self):
        """
        Gets the system_trace_audit_number of this PtsV2PayoutsPost201ResponseProcessorInformation.
        This field is returned only for **American Express Direct** and **CyberSource through VisaNet**. Returned by authorization and incremental authorization services.  #### American Express Direct  System trace audit number (STAN). This value identifies the transaction and is useful when investigating a chargeback dispute.  #### CyberSource through VisaNet  System trace number that must be printed on the customer's receipt. 

        :return: The system_trace_audit_number of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._system_trace_audit_number

    @system_trace_audit_number.setter
    def system_trace_audit_number(self, system_trace_audit_number):
        """
        Sets the system_trace_audit_number of this PtsV2PayoutsPost201ResponseProcessorInformation.
        This field is returned only for **American Express Direct** and **CyberSource through VisaNet**. Returned by authorization and incremental authorization services.  #### American Express Direct  System trace audit number (STAN). This value identifies the transaction and is useful when investigating a chargeback dispute.  #### CyberSource through VisaNet  System trace number that must be printed on the customer's receipt. 

        :param system_trace_audit_number: The system_trace_audit_number of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :type: str
        """

        self._system_trace_audit_number = system_trace_audit_number

    @property
    def response_code_source(self):
        """
        Gets the response_code_source of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Used by Visa only and contains the response source/reason code that identifies the source of the response decision. 

        :return: The response_code_source of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code_source

    @response_code_source.setter
    def response_code_source(self, response_code_source):
        """
        Sets the response_code_source of this PtsV2PayoutsPost201ResponseProcessorInformation.
        Used by Visa only and contains the response source/reason code that identifies the source of the response decision. 

        :param response_code_source: The response_code_source of this PtsV2PayoutsPost201ResponseProcessorInformation.
        :type: str
        """

        self._response_code_source = response_code_source

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
        if not isinstance(other, PtsV2PayoutsPost201ResponseProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
