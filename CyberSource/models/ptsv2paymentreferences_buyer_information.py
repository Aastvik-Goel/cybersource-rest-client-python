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


class Ptsv2paymentreferencesBuyerInformation(object):
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
        'date_of_birth': 'str',
        'gender': 'str',
        'language': 'str',
        'note_to_seller': 'str',
        'personal_identification': 'list[Ptsv2paymentsidcapturesBuyerInformationPersonalIdentification]'
    }

    attribute_map = {
        'date_of_birth': 'dateOfBirth',
        'gender': 'gender',
        'language': 'language',
        'note_to_seller': 'noteToSeller',
        'personal_identification': 'personalIdentification'
    }

    def __init__(self, date_of_birth=None, gender=None, language=None, note_to_seller=None, personal_identification=None):
        """
        Ptsv2paymentreferencesBuyerInformation - a model defined in Swagger
        """

        self._date_of_birth = None
        self._gender = None
        self._language = None
        self._note_to_seller = None
        self._personal_identification = None

        if date_of_birth is not None:
          self.date_of_birth = date_of_birth
        if gender is not None:
          self.gender = gender
        if language is not None:
          self.language = language
        if note_to_seller is not None:
          self.note_to_seller = note_to_seller
        if personal_identification is not None:
          self.personal_identification = personal_identification

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this Ptsv2paymentreferencesBuyerInformation.
        Recipient's date of birth. **Format**: `YYYYMMDD`.  This field is a `pass-through`, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see `recipient_date_of_birth` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The date_of_birth of this Ptsv2paymentreferencesBuyerInformation.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this Ptsv2paymentreferencesBuyerInformation.
        Recipient's date of birth. **Format**: `YYYYMMDD`.  This field is a `pass-through`, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see `recipient_date_of_birth` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param date_of_birth: The date_of_birth of this Ptsv2paymentreferencesBuyerInformation.
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def gender(self):
        """
        Gets the gender of this Ptsv2paymentreferencesBuyerInformation.
        Customer's gender. Possible values are F (female), M (male),O (other).

        :return: The gender of this Ptsv2paymentreferencesBuyerInformation.
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this Ptsv2paymentreferencesBuyerInformation.
        Customer's gender. Possible values are F (female), M (male),O (other).

        :param gender: The gender of this Ptsv2paymentreferencesBuyerInformation.
        :type: str
        """

        self._gender = gender

    @property
    def language(self):
        """
        Gets the language of this Ptsv2paymentreferencesBuyerInformation.
        language setting of the user

        :return: The language of this Ptsv2paymentreferencesBuyerInformation.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Ptsv2paymentreferencesBuyerInformation.
        language setting of the user

        :param language: The language of this Ptsv2paymentreferencesBuyerInformation.
        :type: str
        """

        self._language = language

    @property
    def note_to_seller(self):
        """
        Gets the note_to_seller of this Ptsv2paymentreferencesBuyerInformation.
        Note to the recipient of the funds in this transaction

        :return: The note_to_seller of this Ptsv2paymentreferencesBuyerInformation.
        :rtype: str
        """
        return self._note_to_seller

    @note_to_seller.setter
    def note_to_seller(self, note_to_seller):
        """
        Sets the note_to_seller of this Ptsv2paymentreferencesBuyerInformation.
        Note to the recipient of the funds in this transaction

        :param note_to_seller: The note_to_seller of this Ptsv2paymentreferencesBuyerInformation.
        :type: str
        """

        self._note_to_seller = note_to_seller

    @property
    def personal_identification(self):
        """
        Gets the personal_identification of this Ptsv2paymentreferencesBuyerInformation.

        :return: The personal_identification of this Ptsv2paymentreferencesBuyerInformation.
        :rtype: list[Ptsv2paymentsidcapturesBuyerInformationPersonalIdentification]
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """
        Sets the personal_identification of this Ptsv2paymentreferencesBuyerInformation.

        :param personal_identification: The personal_identification of this Ptsv2paymentreferencesBuyerInformation.
        :type: list[Ptsv2paymentsidcapturesBuyerInformationPersonalIdentification]
        """

        self._personal_identification = personal_identification

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
        if not isinstance(other, Ptsv2paymentreferencesBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other