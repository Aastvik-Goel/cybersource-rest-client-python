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


class UpdatePGPKeysRequest1(object):
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
        'organization_id': 'str',
        'status': 'str',
        'expiration_date': 'str',
        'version': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'organization_id': 'organizationId',
        'status': 'status',
        'expiration_date': 'expirationDate',
        'version': 'version',
        'comment': 'comment'
    }

    def __init__(self, organization_id=None, status=None, expiration_date=None, version=None, comment=None):
        """
        UpdatePGPKeysRequest1 - a model defined in Swagger
        """

        self._organization_id = None
        self._status = None
        self._expiration_date = None
        self._version = None
        self._comment = None

        if organization_id is not None:
          self.organization_id = organization_id
        if status is not None:
          self.status = status
        if expiration_date is not None:
          self.expiration_date = expiration_date
        if version is not None:
          self.version = version
        if comment is not None:
          self.comment = comment

    @property
    def organization_id(self):
        """
        Gets the organization_id of this UpdatePGPKeysRequest1.
        Organization Id

        :return: The organization_id of this UpdatePGPKeysRequest1.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this UpdatePGPKeysRequest1.
        Organization Id

        :param organization_id: The organization_id of this UpdatePGPKeysRequest1.
        :type: str
        """



        self._organization_id = organization_id

    @property
    def status(self):
        """
        Gets the status of this UpdatePGPKeysRequest1.
        Only inactive status is applicable for SCMP_API. Only status as inactive needs to be provided to deactivate scmp.

        :return: The status of this UpdatePGPKeysRequest1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdatePGPKeysRequest1.
        Only inactive status is applicable for SCMP_API. Only status as inactive needs to be provided to deactivate scmp.

        :param status: The status of this UpdatePGPKeysRequest1.
        :type: str
        """



        self._status = status

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this UpdatePGPKeysRequest1.
        Expiration Date. Required field to update the SCMP_API key

        :return: The expiration_date of this UpdatePGPKeysRequest1.
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this UpdatePGPKeysRequest1.
        Expiration Date. Required field to update the SCMP_API key

        :param expiration_date: The expiration_date of this UpdatePGPKeysRequest1.
        :type: str
        """



        self._expiration_date = expiration_date

    @property
    def version(self):
        """
        Gets the version of this UpdatePGPKeysRequest1.
        Version. Required field to update the SCMP_API key

        :return: The version of this UpdatePGPKeysRequest1.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpdatePGPKeysRequest1.
        Version. Required field to update the SCMP_API key

        :param version: The version of this UpdatePGPKeysRequest1.
        :type: str
        """



        self._version = version

    @property
    def comment(self):
        """
        Gets the comment of this UpdatePGPKeysRequest1.
        Comment. Optional field. Can be provided along with Expiration Date and Version

        :return: The comment of this UpdatePGPKeysRequest1.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this UpdatePGPKeysRequest1.
        Comment. Optional field. Can be provided along with Expiration Date and Version

        :param comment: The comment of this UpdatePGPKeysRequest1.
        :type: str
        """



        self._comment = comment

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
        if not isinstance(other, UpdatePGPKeysRequest1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
