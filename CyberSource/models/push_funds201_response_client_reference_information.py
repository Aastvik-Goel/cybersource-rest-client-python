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


class PushFunds201ResponseClientReferenceInformation(object):
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
        'code': 'str',
        'submit_local_date_time': 'str'
    }

    attribute_map = {
        'code': 'code',
        'submit_local_date_time': 'submitLocalDateTime'
    }

    def __init__(self, code=None, submit_local_date_time=None):
        """
        PushFunds201ResponseClientReferenceInformation - a model defined in Swagger
        """

        self._code = None
        self._submit_local_date_time = None

        if code is not None:
          self.code = code
        if submit_local_date_time is not None:
          self.submit_local_date_time = submit_local_date_time

    @property
    def code(self):
        """
        Gets the code of this PushFunds201ResponseClientReferenceInformation.
        Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction. 

        :return: The code of this PushFunds201ResponseClientReferenceInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this PushFunds201ResponseClientReferenceInformation.
        Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction. 

        :param code: The code of this PushFunds201ResponseClientReferenceInformation.
        :type: str
        """

        self._code = code

    @property
    def submit_local_date_time(self):
        """
        Gets the submit_local_date_time of this PushFunds201ResponseClientReferenceInformation.
        Date and time at your physical location.  Format: YYYYMMDDhhmmss, where YYYY = year, MM = month, DD = day, hh = hour, mm = minutes ss = seconds 

        :return: The submit_local_date_time of this PushFunds201ResponseClientReferenceInformation.
        :rtype: str
        """
        return self._submit_local_date_time

    @submit_local_date_time.setter
    def submit_local_date_time(self, submit_local_date_time):
        """
        Sets the submit_local_date_time of this PushFunds201ResponseClientReferenceInformation.
        Date and time at your physical location.  Format: YYYYMMDDhhmmss, where YYYY = year, MM = month, DD = day, hh = hour, mm = minutes ss = seconds 

        :param submit_local_date_time: The submit_local_date_time of this PushFunds201ResponseClientReferenceInformation.
        :type: str
        """

        self._submit_local_date_time = submit_local_date_time

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
        if not isinstance(other, PushFunds201ResponseClientReferenceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
