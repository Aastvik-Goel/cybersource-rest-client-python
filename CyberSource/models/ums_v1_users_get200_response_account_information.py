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


class UmsV1UsersGet200ResponseAccountInformation(object):
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
        'user_name': 'str',
        'role_id': 'str',
        'permissions': 'list[str]',
        'status': 'str',
        'created_time': 'datetime',
        'last_access_time': 'datetime',
        'language_preference': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'user_name': 'userName',
        'role_id': 'roleId',
        'permissions': 'permissions',
        'status': 'status',
        'created_time': 'createdTime',
        'last_access_time': 'lastAccessTime',
        'language_preference': 'languagePreference',
        'timezone': 'timezone'
    }

    def __init__(self, user_name=None, role_id=None, permissions=None, status=None, created_time=None, last_access_time=None, language_preference=None, timezone=None):
        """
        UmsV1UsersGet200ResponseAccountInformation - a model defined in Swagger
        """

        self._user_name = None
        self._role_id = None
        self._permissions = None
        self._status = None
        self._created_time = None
        self._last_access_time = None
        self._language_preference = None
        self._timezone = None

        if user_name is not None:
          self.user_name = user_name
        if role_id is not None:
          self.role_id = role_id
        if permissions is not None:
          self.permissions = permissions
        if status is not None:
          self.status = status
        if created_time is not None:
          self.created_time = created_time
        if last_access_time is not None:
          self.last_access_time = last_access_time
        if language_preference is not None:
          self.language_preference = language_preference
        if timezone is not None:
          self.timezone = timezone

    @property
    def user_name(self):
        """
        Gets the user_name of this UmsV1UsersGet200ResponseAccountInformation.

        :return: The user_name of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this UmsV1UsersGet200ResponseAccountInformation.

        :param user_name: The user_name of this UmsV1UsersGet200ResponseAccountInformation.
        :type: str
        """



        self._user_name = user_name

    @property
    def role_id(self):
        """
        Gets the role_id of this UmsV1UsersGet200ResponseAccountInformation.

        :return: The role_id of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """
        Sets the role_id of this UmsV1UsersGet200ResponseAccountInformation.

        :param role_id: The role_id of this UmsV1UsersGet200ResponseAccountInformation.
        :type: str
        """



        self._role_id = role_id

    @property
    def permissions(self):
        """
        Gets the permissions of this UmsV1UsersGet200ResponseAccountInformation.

        :return: The permissions of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this UmsV1UsersGet200ResponseAccountInformation.

        :param permissions: The permissions of this UmsV1UsersGet200ResponseAccountInformation.
        :type: list[str]
        """



        self._permissions = permissions

    @property
    def status(self):
        """
        Gets the status of this UmsV1UsersGet200ResponseAccountInformation.
        Valid values: - active - inactive - locked - disabled - forgotpassword - deleted 

        :return: The status of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UmsV1UsersGet200ResponseAccountInformation.
        Valid values: - active - inactive - locked - disabled - forgotpassword - deleted 

        :param status: The status of this UmsV1UsersGet200ResponseAccountInformation.
        :type: str
        """



        self._status = status

    @property
    def created_time(self):
        """
        Gets the created_time of this UmsV1UsersGet200ResponseAccountInformation.

        :return: The created_time of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """
        Sets the created_time of this UmsV1UsersGet200ResponseAccountInformation.

        :param created_time: The created_time of this UmsV1UsersGet200ResponseAccountInformation.
        :type: datetime
        """



        self._created_time = created_time

    @property
    def last_access_time(self):
        """
        Gets the last_access_time of this UmsV1UsersGet200ResponseAccountInformation.

        :return: The last_access_time of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """
        Sets the last_access_time of this UmsV1UsersGet200ResponseAccountInformation.

        :param last_access_time: The last_access_time of this UmsV1UsersGet200ResponseAccountInformation.
        :type: datetime
        """



        self._last_access_time = last_access_time

    @property
    def language_preference(self):
        """
        Gets the language_preference of this UmsV1UsersGet200ResponseAccountInformation.

        :return: The language_preference of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: str
        """
        return self._language_preference

    @language_preference.setter
    def language_preference(self, language_preference):
        """
        Sets the language_preference of this UmsV1UsersGet200ResponseAccountInformation.

        :param language_preference: The language_preference of this UmsV1UsersGet200ResponseAccountInformation.
        :type: str
        """



        self._language_preference = language_preference

    @property
    def timezone(self):
        """
        Gets the timezone of this UmsV1UsersGet200ResponseAccountInformation.

        :return: The timezone of this UmsV1UsersGet200ResponseAccountInformation.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this UmsV1UsersGet200ResponseAccountInformation.

        :param timezone: The timezone of this UmsV1UsersGet200ResponseAccountInformation.
        :type: str
        """



        self._timezone = timezone

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
        if not isinstance(other, UmsV1UsersGet200ResponseAccountInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
