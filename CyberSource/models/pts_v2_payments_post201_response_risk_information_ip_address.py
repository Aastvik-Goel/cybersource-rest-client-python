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


class PtsV2PaymentsPost201ResponseRiskInformationIpAddress(object):
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
        'anonymizer_status': 'str',
        'locality': 'str',
        'country': 'str',
        'administrative_area': 'str',
        'routing_method': 'str',
        'carrier': 'str',
        'organization': 'str'
    }

    attribute_map = {
        'anonymizer_status': 'anonymizerStatus',
        'locality': 'locality',
        'country': 'country',
        'administrative_area': 'administrativeArea',
        'routing_method': 'routingMethod',
        'carrier': 'carrier',
        'organization': 'organization'
    }

    def __init__(self, anonymizer_status=None, locality=None, country=None, administrative_area=None, routing_method=None, carrier=None, organization=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationIpAddress - a model defined in Swagger
        """

        self._anonymizer_status = None
        self._locality = None
        self._country = None
        self._administrative_area = None
        self._routing_method = None
        self._carrier = None
        self._organization = None

        if anonymizer_status is not None:
          self.anonymizer_status = anonymizer_status
        if locality is not None:
          self.locality = locality
        if country is not None:
          self.country = country
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if routing_method is not None:
          self.routing_method = routing_method
        if carrier is not None:
          self.carrier = carrier
        if organization is not None:
          self.organization = organization

    @property
    def anonymizer_status(self):
        """
        Gets the anonymizer_status of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Indicates whether the transaction IP address is associated with a known anonymous proxy.  For all possible values, see the `score_ip_anonymizer_status` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The anonymizer_status of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._anonymizer_status

    @anonymizer_status.setter
    def anonymizer_status(self, anonymizer_status):
        """
        Sets the anonymizer_status of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Indicates whether the transaction IP address is associated with a known anonymous proxy.  For all possible values, see the `score_ip_anonymizer_status` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param anonymizer_status: The anonymizer_status of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :type: str
        """

        self._anonymizer_status = anonymizer_status

    @property
    def locality(self):
        """
        Gets the locality of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Name of the city decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_city` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The locality of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Name of the city decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_city` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param locality: The locality of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :type: str
        """

        self._locality = locality

    @property
    def country(self):
        """
        Gets the country of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Name of the country decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The country of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Name of the country decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param country: The country of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :type: str
        """

        self._country = country

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Name of the state decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_state` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The administrative_area of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Name of the state decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_state` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param administrative_area: The administrative_area of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def routing_method(self):
        """
        Gets the routing_method of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Routing method decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_routing_method` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The routing_method of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._routing_method

    @routing_method.setter
    def routing_method(self, routing_method):
        """
        Sets the routing_method of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Routing method decoded from the IP address used directly or indirectly by the customer to send the order.  For all possible values, see the `score_ip_routing_method` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param routing_method: The routing_method of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :type: str
        """

        self._routing_method = routing_method

    @property
    def carrier(self):
        """
        Gets the carrier of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Provides the name of the organization that owns the ASN. The carrier is responsible for the traffic carried on the network or set of networks designated as an Autonomous System (AS) and identified by the ASN. While there are more than 27,000 active ASNs, there are fewer carriers, because a single carrier often manages several ASNs. 

        :return: The carrier of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """
        Sets the carrier of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        Provides the name of the organization that owns the ASN. The carrier is responsible for the traffic carried on the network or set of networks designated as an Autonomous System (AS) and identified by the ASN. While there are more than 27,000 active ASNs, there are fewer carriers, because a single carrier often manages several ASNs. 

        :param carrier: The carrier of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :type: str
        """

        self._carrier = carrier

    @property
    def organization(self):
        """
        Gets the organization of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        The Registering Organization is the entity responsible for the actions and content associated with a given block of IP addresses. This is in contrast to the carrier, which is responsible for the routing of traffic for network blocks. Registering Organizations include many types of entities, including corporate, government, or educational entities, and ISPs managing the allocation and use of network blocks. 

        :return: The organization of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        The Registering Organization is the entity responsible for the actions and content associated with a given block of IP addresses. This is in contrast to the carrier, which is responsible for the routing of traffic for network blocks. Registering Organizations include many types of entities, including corporate, government, or educational entities, and ISPs managing the allocation and use of network blocks. 

        :param organization: The organization of this PtsV2PaymentsPost201ResponseRiskInformationIpAddress.
        :type: str
        """

        self._organization = organization

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationIpAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
