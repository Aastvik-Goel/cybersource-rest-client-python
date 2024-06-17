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


class Ptsv1pushfundstransferSenderInformationPersonalIdentification(object):
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
        'id': 'str',
        'personal_id_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'personal_id_type': 'personalIdType',
        'type': 'type'
    }

    def __init__(self, id=None, personal_id_type=None, type=None):
        """
        Ptsv1pushfundstransferSenderInformationPersonalIdentification - a model defined in Swagger
        """

        self._id = None
        self._personal_id_type = None
        self._type = None

        if id is not None:
          self.id = id
        if personal_id_type is not None:
          self.personal_id_type = personal_id_type
        if type is not None:
          self.type = type

    @property
    def id(self):
        """
        Gets the id of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        Visa Platform Connect(35) This tag will contain an acquirer-populated value associated with the API : senderInformation.personalIdType which will identify the personal ID type of the sender.  Mastercard Send(80) 

        :return: The id of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        Visa Platform Connect(35) This tag will contain an acquirer-populated value associated with the API : senderInformation.personalIdType which will identify the personal ID type of the sender.  Mastercard Send(80) 

        :param id: The id of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        :type: str
        """



        self._id = id

    @property
    def personal_id_type(self):
        """
        Gets the personal_id_type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        Visa Platform Connect This tag will denote whether the tax ID is a business or individual tax ID when personal ID Type contains the value of TXIN (Tax identification).  The valid values are: • B (Business) • I (Individual) 

        :return: The personal_id_type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        :rtype: str
        """
        return self._personal_id_type

    @personal_id_type.setter
    def personal_id_type(self, personal_id_type):
        """
        Sets the personal_id_type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        Visa Platform Connect This tag will denote whether the tax ID is a business or individual tax ID when personal ID Type contains the value of TXIN (Tax identification).  The valid values are: • B (Business) • I (Individual) 

        :param personal_id_type: The personal_id_type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        :type: str
        """



        self._personal_id_type = personal_id_type

    @property
    def type(self):
        """
        Gets the type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        This tag will contain the type of sender identification. The valid values are:  Visa Platform Connect: - `BTHD`: (Date of birth) - `CUID`: (Customer identification (unspecified)) - `NTID`: (National identification) - `PASN`: (Passport number) - `DRLN`: (Driver license) - `TXIN`: (Tax identification) - `CPNY`: (Company registration number) - `PRXY`: (Proxy identification) - `SSNB`: (Social security number) - `ARNB`: (Alien registration number) - `LAWE`: (Law enforcement identification) - `MILI`: (Military identification) - `TRVL`: (Travel identification (non-passport)) - `EMAL`: (Email) - `PHON`: (Phone number)  Mastercard Send: - `CUID`: (Customer identification (unspecified)) - `NTID`: (National identification) - `PASN`: (Passport number) - `DRLN`: (Driver license) - `TXIN`: (Tax identification) - `SSNB`: (Social security number) - `ARNB`: (Alien registration number) - `EIDN`: (Employer Identification Number) - `IDNB`: (Identity Card Number) 

        :return: The type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        This tag will contain the type of sender identification. The valid values are:  Visa Platform Connect: - `BTHD`: (Date of birth) - `CUID`: (Customer identification (unspecified)) - `NTID`: (National identification) - `PASN`: (Passport number) - `DRLN`: (Driver license) - `TXIN`: (Tax identification) - `CPNY`: (Company registration number) - `PRXY`: (Proxy identification) - `SSNB`: (Social security number) - `ARNB`: (Alien registration number) - `LAWE`: (Law enforcement identification) - `MILI`: (Military identification) - `TRVL`: (Travel identification (non-passport)) - `EMAL`: (Email) - `PHON`: (Phone number)  Mastercard Send: - `CUID`: (Customer identification (unspecified)) - `NTID`: (National identification) - `PASN`: (Passport number) - `DRLN`: (Driver license) - `TXIN`: (Tax identification) - `SSNB`: (Social security number) - `ARNB`: (Alien registration number) - `EIDN`: (Employer Identification Number) - `IDNB`: (Identity Card Number) 

        :param type: The type of this Ptsv1pushfundstransferSenderInformationPersonalIdentification.
        :type: str
        """



        self._type = type

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
        if not isinstance(other, Ptsv1pushfundstransferSenderInformationPersonalIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
