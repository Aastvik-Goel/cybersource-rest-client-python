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


class Vasv2taxOrderInformationShippingDetails(object):
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
        'ship_from_locality': 'str',
        'ship_from_country': 'str',
        'ship_from_postal_code': 'str',
        'ship_from_administrative_area': 'str'
    }

    attribute_map = {
        'ship_from_locality': 'shipFromLocality',
        'ship_from_country': 'shipFromCountry',
        'ship_from_postal_code': 'shipFromPostalCode',
        'ship_from_administrative_area': 'shipFromAdministrativeArea'
    }

    def __init__(self, ship_from_locality=None, ship_from_country=None, ship_from_postal_code=None, ship_from_administrative_area=None):
        """
        Vasv2taxOrderInformationShippingDetails - a model defined in Swagger
        """

        self._ship_from_locality = None
        self._ship_from_country = None
        self._ship_from_postal_code = None
        self._ship_from_administrative_area = None

        if ship_from_locality is not None:
          self.ship_from_locality = ship_from_locality
        if ship_from_country is not None:
          self.ship_from_country = ship_from_country
        if ship_from_postal_code is not None:
          self.ship_from_postal_code = ship_from_postal_code
        if ship_from_administrative_area is not None:
          self.ship_from_administrative_area = ship_from_administrative_area

    @property
    def ship_from_locality(self):
        """
        Gets the ship_from_locality of this Vasv2taxOrderInformationShippingDetails.
        City where the product is shipped from. This field is used only when the `orderInformation.shipTo.administrativeArea` and `orderInformation.shipTo.country` fields are present.  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation This field is used to determine tax rules and/or rates applied to the transaction based on sourcing.  Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The ship_from_locality of this Vasv2taxOrderInformationShippingDetails.
        :rtype: str
        """
        return self._ship_from_locality

    @ship_from_locality.setter
    def ship_from_locality(self, ship_from_locality):
        """
        Sets the ship_from_locality of this Vasv2taxOrderInformationShippingDetails.
        City where the product is shipped from. This field is used only when the `orderInformation.shipTo.administrativeArea` and `orderInformation.shipTo.country` fields are present.  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation This field is used to determine tax rules and/or rates applied to the transaction based on sourcing.  Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param ship_from_locality: The ship_from_locality of this Vasv2taxOrderInformationShippingDetails.
        :type: str
        """

        self._ship_from_locality = ship_from_locality

    @property
    def ship_from_country(self):
        """
        Gets the ship_from_country of this Vasv2taxOrderInformationShippingDetails.
        Country from which the order is shipped. This field is used only when `orderInformation.shippingDetails.shipFromLocality` and `orderInformation.shippingDetails.shipFromAdministrativeArea` are present. Use the [ISO Standard Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation This field is used to determine tax rules and/ or rates applied to the transaction based on sourcing.  Optional for U.S., Canadian, international tax, and value added taxes. 

        :return: The ship_from_country of this Vasv2taxOrderInformationShippingDetails.
        :rtype: str
        """
        return self._ship_from_country

    @ship_from_country.setter
    def ship_from_country(self, ship_from_country):
        """
        Sets the ship_from_country of this Vasv2taxOrderInformationShippingDetails.
        Country from which the order is shipped. This field is used only when `orderInformation.shippingDetails.shipFromLocality` and `orderInformation.shippingDetails.shipFromAdministrativeArea` are present. Use the [ISO Standard Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation This field is used to determine tax rules and/ or rates applied to the transaction based on sourcing.  Optional for U.S., Canadian, international tax, and value added taxes. 

        :param ship_from_country: The ship_from_country of this Vasv2taxOrderInformationShippingDetails.
        :type: str
        """

        self._ship_from_country = ship_from_country

    @property
    def ship_from_postal_code(self):
        """
        Gets the ship_from_postal_code of this Vasv2taxOrderInformationShippingDetails.
        Postal code where the product is shipped from.  #### Tax Calculation This field is used to determine tax rules and/or rates applied to the transaction based on sourcing.  Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The ship_from_postal_code of this Vasv2taxOrderInformationShippingDetails.
        :rtype: str
        """
        return self._ship_from_postal_code

    @ship_from_postal_code.setter
    def ship_from_postal_code(self, ship_from_postal_code):
        """
        Sets the ship_from_postal_code of this Vasv2taxOrderInformationShippingDetails.
        Postal code where the product is shipped from.  #### Tax Calculation This field is used to determine tax rules and/or rates applied to the transaction based on sourcing.  Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param ship_from_postal_code: The ship_from_postal_code of this Vasv2taxOrderInformationShippingDetails.
        :type: str
        """

        self._ship_from_postal_code = ship_from_postal_code

    @property
    def ship_from_administrative_area(self):
        """
        Gets the ship_from_administrative_area of this Vasv2taxOrderInformationShippingDetails.
        State from which the order is shipped. This field is used only when `orderInformation.shippingDetails.shipFromLocality` and `orderInformation.shippingDetails.shipFromCountry` are present. Use the [State, Province, and Territory Codes for the United States and Canada](http://apps.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation This field is used to determine tax rules and/or rates applied to the transaction based on sourcing.  Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The ship_from_administrative_area of this Vasv2taxOrderInformationShippingDetails.
        :rtype: str
        """
        return self._ship_from_administrative_area

    @ship_from_administrative_area.setter
    def ship_from_administrative_area(self, ship_from_administrative_area):
        """
        Sets the ship_from_administrative_area of this Vasv2taxOrderInformationShippingDetails.
        State from which the order is shipped. This field is used only when `orderInformation.shippingDetails.shipFromLocality` and `orderInformation.shippingDetails.shipFromCountry` are present. Use the [State, Province, and Territory Codes for the United States and Canada](http://apps.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation This field is used to determine tax rules and/or rates applied to the transaction based on sourcing.  Optional for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param ship_from_administrative_area: The ship_from_administrative_area of this Vasv2taxOrderInformationShippingDetails.
        :type: str
        """

        self._ship_from_administrative_area = ship_from_administrative_area

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
        if not isinstance(other, Vasv2taxOrderInformationShippingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
