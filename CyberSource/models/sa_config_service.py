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


class SAConfigService(object):
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
        'decision_manager_verbose_enabled': 'bool',
        'declined_retry_limit': 'float',
        'decision_manager_enabled': 'bool',
        'tokenization_enabled': 'bool',
        'reverse_auth_on_address_verification_system_failure': 'bool',
        'device_fingerprint_enabled': 'bool',
        'reverse_auth_on_card_verification_number_failure': 'bool'
    }

    attribute_map = {
        'decision_manager_verbose_enabled': 'decisionManagerVerboseEnabled',
        'declined_retry_limit': 'declinedRetryLimit',
        'decision_manager_enabled': 'decisionManagerEnabled',
        'tokenization_enabled': 'tokenizationEnabled',
        'reverse_auth_on_address_verification_system_failure': 'reverseAuthOnAddressVerificationSystemFailure',
        'device_fingerprint_enabled': 'deviceFingerprintEnabled',
        'reverse_auth_on_card_verification_number_failure': 'reverseAuthOnCardVerificationNumberFailure'
    }

    def __init__(self, decision_manager_verbose_enabled=None, declined_retry_limit=None, decision_manager_enabled=None, tokenization_enabled=None, reverse_auth_on_address_verification_system_failure=None, device_fingerprint_enabled=None, reverse_auth_on_card_verification_number_failure=None):
        """
        SAConfigService - a model defined in Swagger
        """

        self._decision_manager_verbose_enabled = None
        self._declined_retry_limit = None
        self._decision_manager_enabled = None
        self._tokenization_enabled = None
        self._reverse_auth_on_address_verification_system_failure = None
        self._device_fingerprint_enabled = None
        self._reverse_auth_on_card_verification_number_failure = None

        if decision_manager_verbose_enabled is not None:
          self.decision_manager_verbose_enabled = decision_manager_verbose_enabled
        if declined_retry_limit is not None:
          self.declined_retry_limit = declined_retry_limit
        if decision_manager_enabled is not None:
          self.decision_manager_enabled = decision_manager_enabled
        if tokenization_enabled is not None:
          self.tokenization_enabled = tokenization_enabled
        if reverse_auth_on_address_verification_system_failure is not None:
          self.reverse_auth_on_address_verification_system_failure = reverse_auth_on_address_verification_system_failure
        if device_fingerprint_enabled is not None:
          self.device_fingerprint_enabled = device_fingerprint_enabled
        if reverse_auth_on_card_verification_number_failure is not None:
          self.reverse_auth_on_card_verification_number_failure = reverse_auth_on_card_verification_number_failure

    @property
    def decision_manager_verbose_enabled(self):
        """
        Gets the decision_manager_verbose_enabled of this SAConfigService.
        Toggles whether verbose Decision Manager results should be present in the Secure Acceptance response. As this response passes through the browser, it is recommended to set this to \"false\" outside of debugging.

        :return: The decision_manager_verbose_enabled of this SAConfigService.
        :rtype: bool
        """
        return self._decision_manager_verbose_enabled

    @decision_manager_verbose_enabled.setter
    def decision_manager_verbose_enabled(self, decision_manager_verbose_enabled):
        """
        Sets the decision_manager_verbose_enabled of this SAConfigService.
        Toggles whether verbose Decision Manager results should be present in the Secure Acceptance response. As this response passes through the browser, it is recommended to set this to \"false\" outside of debugging.

        :param decision_manager_verbose_enabled: The decision_manager_verbose_enabled of this SAConfigService.
        :type: bool
        """



        self._decision_manager_verbose_enabled = decision_manager_verbose_enabled

    @property
    def declined_retry_limit(self):
        """
        Gets the declined_retry_limit of this SAConfigService.
        Defines the number of retries a payer is presented with on payment declines on Hosted Checkout. Valid values are between 0 and 5.

        :return: The declined_retry_limit of this SAConfigService.
        :rtype: float
        """
        return self._declined_retry_limit

    @declined_retry_limit.setter
    def declined_retry_limit(self, declined_retry_limit):
        """
        Sets the declined_retry_limit of this SAConfigService.
        Defines the number of retries a payer is presented with on payment declines on Hosted Checkout. Valid values are between 0 and 5.

        :param declined_retry_limit: The declined_retry_limit of this SAConfigService.
        :type: float
        """



        self._declined_retry_limit = declined_retry_limit

    @property
    def decision_manager_enabled(self):
        """
        Gets the decision_manager_enabled of this SAConfigService.
        Toggles whether Decision Manager is enabled or not for Secure Acceptance transactions. Requires the transacting MID to be enabled and configured for Decicion Manager.

        :return: The decision_manager_enabled of this SAConfigService.
        :rtype: bool
        """
        return self._decision_manager_enabled

    @decision_manager_enabled.setter
    def decision_manager_enabled(self, decision_manager_enabled):
        """
        Sets the decision_manager_enabled of this SAConfigService.
        Toggles whether Decision Manager is enabled or not for Secure Acceptance transactions. Requires the transacting MID to be enabled and configured for Decicion Manager.

        :param decision_manager_enabled: The decision_manager_enabled of this SAConfigService.
        :type: bool
        """



        self._decision_manager_enabled = decision_manager_enabled

    @property
    def tokenization_enabled(self):
        """
        Gets the tokenization_enabled of this SAConfigService.
        Toggles whether Tokenization is enabled or not for Secure Acceptance transactions. Requires the transacting MID to be enabled and configured for Tokenization.

        :return: The tokenization_enabled of this SAConfigService.
        :rtype: bool
        """
        return self._tokenization_enabled

    @tokenization_enabled.setter
    def tokenization_enabled(self, tokenization_enabled):
        """
        Sets the tokenization_enabled of this SAConfigService.
        Toggles whether Tokenization is enabled or not for Secure Acceptance transactions. Requires the transacting MID to be enabled and configured for Tokenization.

        :param tokenization_enabled: The tokenization_enabled of this SAConfigService.
        :type: bool
        """



        self._tokenization_enabled = tokenization_enabled

    @property
    def reverse_auth_on_address_verification_system_failure(self):
        """
        Gets the reverse_auth_on_address_verification_system_failure of this SAConfigService.
        Toggles whether or not an approved Authorization that fails AVS should be automatically reversed.

        :return: The reverse_auth_on_address_verification_system_failure of this SAConfigService.
        :rtype: bool
        """
        return self._reverse_auth_on_address_verification_system_failure

    @reverse_auth_on_address_verification_system_failure.setter
    def reverse_auth_on_address_verification_system_failure(self, reverse_auth_on_address_verification_system_failure):
        """
        Sets the reverse_auth_on_address_verification_system_failure of this SAConfigService.
        Toggles whether or not an approved Authorization that fails AVS should be automatically reversed.

        :param reverse_auth_on_address_verification_system_failure: The reverse_auth_on_address_verification_system_failure of this SAConfigService.
        :type: bool
        """



        self._reverse_auth_on_address_verification_system_failure = reverse_auth_on_address_verification_system_failure

    @property
    def device_fingerprint_enabled(self):
        """
        Gets the device_fingerprint_enabled of this SAConfigService.
        Toggles whether or not fraud Device Fingerprinting is enabled on the Hosted Checkout. This simplifies enablement for Decision Manager.

        :return: The device_fingerprint_enabled of this SAConfigService.
        :rtype: bool
        """
        return self._device_fingerprint_enabled

    @device_fingerprint_enabled.setter
    def device_fingerprint_enabled(self, device_fingerprint_enabled):
        """
        Sets the device_fingerprint_enabled of this SAConfigService.
        Toggles whether or not fraud Device Fingerprinting is enabled on the Hosted Checkout. This simplifies enablement for Decision Manager.

        :param device_fingerprint_enabled: The device_fingerprint_enabled of this SAConfigService.
        :type: bool
        """



        self._device_fingerprint_enabled = device_fingerprint_enabled

    @property
    def reverse_auth_on_card_verification_number_failure(self):
        """
        Gets the reverse_auth_on_card_verification_number_failure of this SAConfigService.
        Toggles whether or not an approved Authorization that fails CVN check that should be automatically reversed.

        :return: The reverse_auth_on_card_verification_number_failure of this SAConfigService.
        :rtype: bool
        """
        return self._reverse_auth_on_card_verification_number_failure

    @reverse_auth_on_card_verification_number_failure.setter
    def reverse_auth_on_card_verification_number_failure(self, reverse_auth_on_card_verification_number_failure):
        """
        Sets the reverse_auth_on_card_verification_number_failure of this SAConfigService.
        Toggles whether or not an approved Authorization that fails CVN check that should be automatically reversed.

        :param reverse_auth_on_card_verification_number_failure: The reverse_auth_on_card_verification_number_failure of this SAConfigService.
        :type: bool
        """



        self._reverse_auth_on_card_verification_number_failure = reverse_auth_on_card_verification_number_failure

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
        if not isinstance(other, SAConfigService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
