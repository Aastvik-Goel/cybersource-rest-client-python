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


class InlineResponse2012KeyInformation(object):
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
        'provider': 'str',
        'tenant': 'str',
        'organization_id': 'str',
        'client_key_id': 'str',
        'key_id': 'str',
        'key': 'str',
        'key_type': 'str',
        'status': 'str',
        'expiration_date': 'str',
        'message': 'str',
        'error_information': 'InlineResponse2012KeyInformationErrorInformation'
    }

    attribute_map = {
        'provider': 'provider',
        'tenant': 'tenant',
        'organization_id': 'organizationId',
        'client_key_id': 'clientKeyId',
        'key_id': 'keyId',
        'key': 'key',
        'key_type': 'keyType',
        'status': 'status',
        'expiration_date': 'expirationDate',
        'message': 'message',
        'error_information': 'errorInformation'
    }

    def __init__(self, provider=None, tenant=None, organization_id=None, client_key_id=None, key_id=None, key=None, key_type=None, status=None, expiration_date=None, message=None, error_information=None):
        """
        InlineResponse2012KeyInformation - a model defined in Swagger
        """

        self._provider = None
        self._tenant = None
        self._organization_id = None
        self._client_key_id = None
        self._key_id = None
        self._key = None
        self._key_type = None
        self._status = None
        self._expiration_date = None
        self._message = None
        self._error_information = None

        if provider is not None:
          self.provider = provider
        if tenant is not None:
          self.tenant = tenant
        if organization_id is not None:
          self.organization_id = organization_id
        if client_key_id is not None:
          self.client_key_id = client_key_id
        if key_id is not None:
          self.key_id = key_id
        if key is not None:
          self.key = key
        if key_type is not None:
          self.key_type = key_type
        if status is not None:
          self.status = status
        if expiration_date is not None:
          self.expiration_date = expiration_date
        if message is not None:
          self.message = message
        if error_information is not None:
          self.error_information = error_information

    @property
    def provider(self):
        """
        Gets the provider of this InlineResponse2012KeyInformation.
        Provider name 

        :return: The provider of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this InlineResponse2012KeyInformation.
        Provider name 

        :param provider: The provider of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._provider = provider

    @property
    def tenant(self):
        """
        Gets the tenant of this InlineResponse2012KeyInformation.
        Tenant name 

        :return: The tenant of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this InlineResponse2012KeyInformation.
        Tenant name 

        :param tenant: The tenant of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._tenant = tenant

    @property
    def organization_id(self):
        """
        Gets the organization_id of this InlineResponse2012KeyInformation.
        Organization Id 

        :return: The organization_id of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this InlineResponse2012KeyInformation.
        Organization Id 

        :param organization_id: The organization_id of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def client_key_id(self):
        """
        Gets the client_key_id of this InlineResponse2012KeyInformation.
        Client key Id 

        :return: The client_key_id of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._client_key_id

    @client_key_id.setter
    def client_key_id(self, client_key_id):
        """
        Sets the client_key_id of this InlineResponse2012KeyInformation.
        Client key Id 

        :param client_key_id: The client_key_id of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._client_key_id = client_key_id

    @property
    def key_id(self):
        """
        Gets the key_id of this InlineResponse2012KeyInformation.
        Key Serial Number 

        :return: The key_id of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this InlineResponse2012KeyInformation.
        Key Serial Number 

        :param key_id: The key_id of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._key_id = key_id

    @property
    def key(self):
        """
        Gets the key of this InlineResponse2012KeyInformation.
        Value of the key 

        :return: The key of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this InlineResponse2012KeyInformation.
        Value of the key 

        :param key: The key of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._key = key

    @property
    def key_type(self):
        """
        Gets the key_type of this InlineResponse2012KeyInformation.
        Type of the key 

        :return: The key_type of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this InlineResponse2012KeyInformation.
        Type of the key 

        :param key_type: The key_type of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._key_type = key_type

    @property
    def status(self):
        """
        Gets the status of this InlineResponse2012KeyInformation.
        The status of the key 

        :return: The status of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InlineResponse2012KeyInformation.
        The status of the key 

        :param status: The status of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._status = status

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this InlineResponse2012KeyInformation.
        The expiration time in UTC. `Format: YYYY-MM-DDThh:mm:ssZ` Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :return: The expiration_date of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this InlineResponse2012KeyInformation.
        The expiration time in UTC. `Format: YYYY-MM-DDThh:mm:ssZ` Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC. 

        :param expiration_date: The expiration_date of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def message(self):
        """
        Gets the message of this InlineResponse2012KeyInformation.
        Message in case of failed key 

        :return: The message of this InlineResponse2012KeyInformation.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse2012KeyInformation.
        Message in case of failed key 

        :param message: The message of this InlineResponse2012KeyInformation.
        :type: str
        """

        self._message = message

    @property
    def error_information(self):
        """
        Gets the error_information of this InlineResponse2012KeyInformation.

        :return: The error_information of this InlineResponse2012KeyInformation.
        :rtype: InlineResponse2012KeyInformationErrorInformation
        """
        return self._error_information

    @error_information.setter
    def error_information(self, error_information):
        """
        Sets the error_information of this InlineResponse2012KeyInformation.

        :param error_information: The error_information of this InlineResponse2012KeyInformation.
        :type: InlineResponse2012KeyInformationErrorInformation
        """

        self._error_information = error_information

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
        if not isinstance(other, InlineResponse2012KeyInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other