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


class TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting(object):
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
        'name': 'str',
        'response_code': 'str',
        'reason_code': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'name': 'name',
        'response_code': 'responseCode',
        'reason_code': 'reasonCode',
        'sequence': 'sequence'
    }

    def __init__(self, name=None, response_code=None, reason_code=None, sequence=None):
        """
        TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting - a model defined in Swagger
        """

        self._name = None
        self._response_code = None
        self._reason_code = None
        self._sequence = None

        if name is not None:
          self.name = name
        if response_code is not None:
          self.response_code = response_code
        if reason_code is not None:
          self.reason_code = reason_code
        if sequence is not None:
          self.sequence = sequence

    @property
    def name(self):
        """
        Gets the name of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        Name of the Processor. 

        :return: The name of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        Name of the Processor. 

        :param name: The name of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :type: str
        """

        self._name = name

    @property
    def response_code(self):
        """
        Gets the response_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  **Important** Do not use this field to evaluate the result of the authorization.  #### PIN debit Response value that is returned by the processor or bank. **Important** Do not use this field to evaluate the results of the transaction request.  Returned by PIN debit credit, PIN debit purchase, and PIN debit reversal.  #### AIBMS If this value is `08`, you can accept the transaction if the customer provides you with identification.  #### Atos This value is the response code sent from Atos and it might also include the response code from the bank. Format: `aa,bb` with the two values separated by a comma and where: - `aa` is the two-digit error message from Atos. - `bb` is the optional two-digit error message from the bank.  #### Comercio Latino This value is the status code and the error or response code received from the processor separated by a colon. Format: [status code]:E[error code] or [status code]:R[response code] Example `2:R06`  #### JCN Gateway Processor-defined detail error code. The associated response category code is in the `processorInformation.responseCategoryCode` field. String (3) 

        :return: The response_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  **Important** Do not use this field to evaluate the result of the authorization.  #### PIN debit Response value that is returned by the processor or bank. **Important** Do not use this field to evaluate the results of the transaction request.  Returned by PIN debit credit, PIN debit purchase, and PIN debit reversal.  #### AIBMS If this value is `08`, you can accept the transaction if the customer provides you with identification.  #### Atos This value is the response code sent from Atos and it might also include the response code from the bank. Format: `aa,bb` with the two values separated by a comma and where: - `aa` is the two-digit error message from Atos. - `bb` is the optional two-digit error message from the bank.  #### Comercio Latino This value is the status code and the error or response code received from the processor separated by a colon. Format: [status code]:E[error code] or [status code]:R[response code] Example `2:R06`  #### JCN Gateway Processor-defined detail error code. The associated response category code is in the `processorInformation.responseCategoryCode` field. String (3) 

        :param response_code: The response_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :type: str
        """

        self._response_code = response_code

    @property
    def reason_code(self):
        """
        Gets the reason_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        Indicates the reason why a request succeeded or failed and possible action to take if a request fails.  For details, see the appendix of reason codes in the documentation for the relevant payment method. 

        :return: The reason_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """
        Sets the reason_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        Indicates the reason why a request succeeded or failed and possible action to take if a request fails.  For details, see the appendix of reason codes in the documentation for the relevant payment method. 

        :param reason_code: The reason_code of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :type: str
        """

        self._reason_code = reason_code

    @property
    def sequence(self):
        """
        Gets the sequence of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        The order in which the transaction was routed to the processor 

        :return: The sequence of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        Sets the sequence of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        The order in which the transaction was routed to the processor 

        :param sequence: The sequence of this TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting.
        :type: str
        """

        self._sequence = sequence

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
        if not isinstance(other, TssV2TransactionsGet200ResponseProcessorInformationMultiProcessorRouting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
