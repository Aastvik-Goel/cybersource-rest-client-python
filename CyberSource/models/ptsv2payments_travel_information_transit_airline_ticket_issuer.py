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


class Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer(object):
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
        'code': 'str',
        'name': 'str',
        'address': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'address': 'address',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, code=None, name=None, address=None, locality=None, administrative_area=None, postal_code=None, country=None):
        """
        Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer - a model defined in Swagger
        """

        self._code = None
        self._name = None
        self._address = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._country = None

        if code is not None:
          self.code = code
        if name is not None:
          self.name = name
        if address is not None:
          self.address = address
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if country is not None:
          self.country = country

    @property
    def code(self):
        """
        Gets the code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        IATA2 airline code. Format: English characters only. Required for Mastercard; optional for all other card types. 

        :return: The code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        IATA2 airline code. Format: English characters only. Required for Mastercard; optional for all other card types. 

        :param code: The code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :type: str
        """
        if code is not None and len(code) > 4:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `4`")

        self._code = code

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Name of the ticket issuer. If you do not include this field, CyberSource uses the value for your merchant name that is in the CyberSource merchant configuration database. 

        :return: The name of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Name of the ticket issuer. If you do not include this field, CyberSource uses the value for your merchant name that is in the CyberSource merchant configuration database. 

        :param name: The name of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :type: str
        """
        if name is not None and len(name) > 20:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `20`")

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Address of the company issuing the ticket. 

        :return: The address of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Address of the company issuing the ticket. 

        :param address: The address of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :type: str
        """
        if address is not None and len(address) > 16:
            raise ValueError("Invalid value for `address`, length must be less than or equal to `16`")

        self._address = address

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        City in which the transaction occurred. If the name of the city exceeds 18 characters, use meaningful abbreviations. Format: English characters only. Optional request field. 

        :return: The locality of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        City in which the transaction occurred. If the name of the city exceeds 18 characters, use meaningful abbreviations. Format: English characters only. Optional request field. 

        :param locality: The locality of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :type: str
        """
        if locality is not None and len(locality) > 18:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `18`")

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        State in which transaction occured. 

        :return: The administrative_area of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        State in which transaction occured. 

        :param administrative_area: The administrative_area of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 18:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `18`")

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Zip code of the city in which transaction occured. 

        :return: The postal_code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Zip code of the city in which transaction occured. 

        :param postal_code: The postal_code of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 15:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `15`")

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Country in which transaction occured. 

        :return: The country of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        Country in which transaction occured. 

        :param country: The country of this Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer.
        :type: str
        """
        if country is not None and len(country) > 18:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `18`")

        self._country = country

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
        if not isinstance(other, Ptsv2paymentsTravelInformationTransitAirlineTicketIssuer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other