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


class Vasv2taxOrderInformationOrderAcceptance(object):
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
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'country': 'country'
    }

    def __init__(self, locality=None, administrative_area=None, postal_code=None, country=None):
        """
        Vasv2taxOrderInformationOrderAcceptance - a model defined in Swagger
        """

        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._country = None

        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if country is not None:
          self.country = country

    @property
    def locality(self):
        """
        Gets the locality of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance city. This field is not used unless the `orderInformation.orderAcceptance.administrativeArea` and `orderInformation.orderAcceptance.country` fields are present.  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The locality of this Vasv2taxOrderInformationOrderAcceptance.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance city. This field is not used unless the `orderInformation.orderAcceptance.administrativeArea` and `orderInformation.orderAcceptance.country` fields are present.  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param locality: The locality of this Vasv2taxOrderInformationOrderAcceptance.
        :type: str
        """

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance state. This field is not used unless the `orderInformation.orderAcceptance.locality` and `orderInformation.orderAcceptance.country` fields are present. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The administrative_area of this Vasv2taxOrderInformationOrderAcceptance.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance state. This field is not used unless the `orderInformation.orderAcceptance.locality` and `orderInformation.orderAcceptance.country` fields are present. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param administrative_area: The administrative_area of this Vasv2taxOrderInformationOrderAcceptance.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance postal code. This field is not used unless the `orderInformation.orderAcceptance.locality`, `orderInformation.orderAcceptance.administrativeArea`, and `orderInformation.orderAcceptance.country` fields are present. Must be sent at the line or offer level to be surfaced in the Tax Detail Report.  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The postal_code of this Vasv2taxOrderInformationOrderAcceptance.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance postal code. This field is not used unless the `orderInformation.orderAcceptance.locality`, `orderInformation.orderAcceptance.administrativeArea`, and `orderInformation.orderAcceptance.country` fields are present. Must be sent at the line or offer level to be surfaced in the Tax Detail Report.  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param postal_code: The postal_code of this Vasv2taxOrderInformationOrderAcceptance.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance country. This field is not used unless the `orderInformation.orderAcceptance.administrativeArea` and `orderInformation.orderAcceptance.locality` fields are present. Use the [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :return: The country of this Vasv2taxOrderInformationOrderAcceptance.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Vasv2taxOrderInformationOrderAcceptance.
        Order acceptance country. This field is not used unless the `orderInformation.orderAcceptance.administrativeArea` and `orderInformation.orderAcceptance.locality` fields are present. Use the [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  **NOTE** If this field appears in a `lineItems` object, then the value of this field in the `lineItems` object overrides the value of the corresponding field at the request-level or order-level object.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. 

        :param country: The country of this Vasv2taxOrderInformationOrderAcceptance.
        :type: str
        """

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
        if not isinstance(other, Vasv2taxOrderInformationOrderAcceptance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
