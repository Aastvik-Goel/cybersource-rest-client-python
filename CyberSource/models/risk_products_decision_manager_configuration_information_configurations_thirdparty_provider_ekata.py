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


class RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata(object):
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
        'enabled': 'bool',
        'enable_real_time': 'bool',
        'use_cybs_credentials': 'bool',
        'credentials': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkataCredentials'
    }

    attribute_map = {
        'enabled': 'enabled',
        'enable_real_time': 'enableRealTime',
        'use_cybs_credentials': 'useCybsCredentials',
        'credentials': 'credentials'
    }

    def __init__(self, enabled=None, enable_real_time=None, use_cybs_credentials=None, credentials=None):
        """
        RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata - a model defined in Swagger
        """

        self._enabled = None
        self._enable_real_time = None
        self._use_cybs_credentials = None
        self._credentials = None

        if enabled is not None:
          self.enabled = enabled
        if enable_real_time is not None:
          self.enable_real_time = enable_real_time
        if use_cybs_credentials is not None:
          self.use_cybs_credentials = use_cybs_credentials
        if credentials is not None:
          self.credentials = credentials

    @property
    def enabled(self):
        """
        Gets the enabled of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :return: The enabled of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :param enabled: The enabled of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :type: bool
        """

        self._enabled = enabled

    @property
    def enable_real_time(self):
        """
        Gets the enable_real_time of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :return: The enable_real_time of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :rtype: bool
        """
        return self._enable_real_time

    @enable_real_time.setter
    def enable_real_time(self, enable_real_time):
        """
        Sets the enable_real_time of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :param enable_real_time: The enable_real_time of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :type: bool
        """

        self._enable_real_time = enable_real_time

    @property
    def use_cybs_credentials(self):
        """
        Gets the use_cybs_credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :return: The use_cybs_credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :rtype: bool
        """
        return self._use_cybs_credentials

    @use_cybs_credentials.setter
    def use_cybs_credentials(self, use_cybs_credentials):
        """
        Sets the use_cybs_credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :param use_cybs_credentials: The use_cybs_credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :type: bool
        """

        self._use_cybs_credentials = use_cybs_credentials

    @property
    def credentials(self):
        """
        Gets the credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :return: The credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkataCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.

        :param credentials: The credentials of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkataCredentials
        """

        self._credentials = credentials

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
        if not isinstance(other, RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
