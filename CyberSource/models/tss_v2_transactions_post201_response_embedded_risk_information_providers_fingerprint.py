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


class TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint(object):
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
        'true_ipaddress': 'str',
        'hash': 'str',
        'smart_id': 'str'
    }

    attribute_map = {
        'true_ipaddress': 'true_ipaddress',
        'hash': 'hash',
        'smart_id': 'smartId'
    }

    def __init__(self, true_ipaddress=None, hash=None, smart_id=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint - a model defined in Swagger
        """

        self._true_ipaddress = None
        self._hash = None
        self._smart_id = None

        if true_ipaddress is not None:
          self.true_ipaddress = true_ipaddress
        if hash is not None:
          self.hash = hash
        if smart_id is not None:
          self.smart_id = smart_id

    @property
    def true_ipaddress(self):
        """
        Gets the true_ipaddress of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        Customer's true IP address detected by the application.  For details, see the `true_ipaddress` field description in _Device Fingerprinting Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Device Fingerprinting Guide_ (PDF link). 

        :return: The true_ipaddress of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        :rtype: str
        """
        return self._true_ipaddress

    @true_ipaddress.setter
    def true_ipaddress(self, true_ipaddress):
        """
        Sets the true_ipaddress of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        Customer's true IP address detected by the application.  For details, see the `true_ipaddress` field description in _Device Fingerprinting Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Device Fingerprinting Guide_ (PDF link). 

        :param true_ipaddress: The true_ipaddress of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        :type: str
        """

        self._true_ipaddress = true_ipaddress

    @property
    def hash(self):
        """
        Gets the hash of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        The unique identifier of the device that is returned in the `riskInformation.providers.fingerprint.device_fingerprint_hash` API reply field. For more details about this field, see the `device_fingerprint_hash` field description in the _Device Fingerprinting Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Device Fingerprinting Guide_ (PDF link). 

        :return: The hash of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        The unique identifier of the device that is returned in the `riskInformation.providers.fingerprint.device_fingerprint_hash` API reply field. For more details about this field, see the `device_fingerprint_hash` field description in the _Device Fingerprinting Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Device Fingerprinting Guide_ (PDF link). 

        :param hash: The hash of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        :type: str
        """

        self._hash = hash

    @property
    def smart_id(self):
        """
        Gets the smart_id of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        The device identifier generated from attributes collected during profiling. Returned by a 3rd party when you use device fingerprinting.  For details, see the `device_fingerprint_smart_id` field description in [CyberSource Decision Manager Device Fingerprinting Guide.](https://www.cybersource.com/developers/documentation/fraud_management) 

        :return: The smart_id of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        :rtype: str
        """
        return self._smart_id

    @smart_id.setter
    def smart_id(self, smart_id):
        """
        Sets the smart_id of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        The device identifier generated from attributes collected during profiling. Returned by a 3rd party when you use device fingerprinting.  For details, see the `device_fingerprint_smart_id` field description in [CyberSource Decision Manager Device Fingerprinting Guide.](https://www.cybersource.com/developers/documentation/fraud_management) 

        :param smart_id: The smart_id of this TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint.
        :type: str
        """

        self._smart_id = smart_id

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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedRiskInformationProvidersFingerprint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
