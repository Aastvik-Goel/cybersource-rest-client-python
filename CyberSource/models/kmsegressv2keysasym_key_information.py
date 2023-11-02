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


class Kmsegressv2keysasymKeyInformation(object):
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
        'key_type': 'str',
        'organization_id': 'str',
        'pub': 'str',
        'key_id': 'str',
        'pvt': 'str',
        'status': 'str',
        'expiry_duration': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'tenant': 'tenant',
        'key_type': 'keyType',
        'organization_id': 'organizationId',
        'pub': 'pub',
        'key_id': 'keyId',
        'pvt': 'pvt',
        'status': 'status',
        'expiry_duration': 'expiryDuration'
    }

    def __init__(self, provider=None, tenant=None, key_type=None, organization_id=None, pub=None, key_id=None, pvt=None, status=None, expiry_duration=None):
        """
        Kmsegressv2keysasymKeyInformation - a model defined in Swagger
        """

        self._provider = None
        self._tenant = None
        self._key_type = None
        self._organization_id = None
        self._pub = None
        self._key_id = None
        self._pvt = None
        self._status = None
        self._expiry_duration = None

        if provider is not None:
          self.provider = provider
        if tenant is not None:
          self.tenant = tenant
        if key_type is not None:
          self.key_type = key_type
        if organization_id is not None:
          self.organization_id = organization_id
        if pub is not None:
          self.pub = pub
        if key_id is not None:
          self.key_id = key_id
        if pvt is not None:
          self.pvt = pvt
        if status is not None:
          self.status = status
        if expiry_duration is not None:
          self.expiry_duration = expiry_duration

    @property
    def provider(self):
        """
        Gets the provider of this Kmsegressv2keysasymKeyInformation.
        Provider name 

        :return: The provider of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this Kmsegressv2keysasymKeyInformation.
        Provider name 

        :param provider: The provider of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._provider = provider

    @property
    def tenant(self):
        """
        Gets the tenant of this Kmsegressv2keysasymKeyInformation.
        Tenant name 

        :return: The tenant of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of this Kmsegressv2keysasymKeyInformation.
        Tenant name 

        :param tenant: The tenant of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._tenant = tenant

    @property
    def key_type(self):
        """
        Gets the key_type of this Kmsegressv2keysasymKeyInformation.
        Type of the key 

        :return: The key_type of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """
        Sets the key_type of this Kmsegressv2keysasymKeyInformation.
        Type of the key 

        :param key_type: The key_type of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._key_type = key_type

    @property
    def organization_id(self):
        """
        Gets the organization_id of this Kmsegressv2keysasymKeyInformation.
        Organization Id 

        :return: The organization_id of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this Kmsegressv2keysasymKeyInformation.
        Organization Id 

        :param organization_id: The organization_id of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def pub(self):
        """
        Gets the pub of this Kmsegressv2keysasymKeyInformation.
        Public certificate with only base64 encoded payload and not the header (BEGIN CERTIFICATE) and footer (END CERTIFICATE) 

        :return: The pub of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._pub

    @pub.setter
    def pub(self, pub):
        """
        Sets the pub of this Kmsegressv2keysasymKeyInformation.
        Public certificate with only base64 encoded payload and not the header (BEGIN CERTIFICATE) and footer (END CERTIFICATE) 

        :param pub: The pub of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._pub = pub

    @property
    def key_id(self):
        """
        Gets the key_id of this Kmsegressv2keysasymKeyInformation.
        Key Serial Number 

        :return: The key_id of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this Kmsegressv2keysasymKeyInformation.
        Key Serial Number 

        :param key_id: The key_id of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._key_id = key_id

    @property
    def pvt(self):
        """
        Gets the pvt of this Kmsegressv2keysasymKeyInformation.
        Private certificate with only base64 encoded payload and not header (BEGIN CERTIFICATE) and footer (END CERTIFICATE) 

        :return: The pvt of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._pvt

    @pvt.setter
    def pvt(self, pvt):
        """
        Sets the pvt of this Kmsegressv2keysasymKeyInformation.
        Private certificate with only base64 encoded payload and not header (BEGIN CERTIFICATE) and footer (END CERTIFICATE) 

        :param pvt: The pvt of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._pvt = pvt

    @property
    def status(self):
        """
        Gets the status of this Kmsegressv2keysasymKeyInformation.
        The status of the key 

        :return: The status of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Kmsegressv2keysasymKeyInformation.
        The status of the key 

        :param status: The status of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._status = status

    @property
    def expiry_duration(self):
        """
        Gets the expiry_duration of this Kmsegressv2keysasymKeyInformation.
        Key expiry duration in days 

        :return: The expiry_duration of this Kmsegressv2keysasymKeyInformation.
        :rtype: str
        """
        return self._expiry_duration

    @expiry_duration.setter
    def expiry_duration(self, expiry_duration):
        """
        Sets the expiry_duration of this Kmsegressv2keysasymKeyInformation.
        Key expiry duration in days 

        :param expiry_duration: The expiry_duration of this Kmsegressv2keysasymKeyInformation.
        :type: str
        """

        self._expiry_duration = expiry_duration

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
        if not isinstance(other, Kmsegressv2keysasymKeyInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
