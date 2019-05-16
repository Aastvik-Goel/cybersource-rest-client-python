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


class Ptsv2paymentsidcapturesOrderInformationShippingDetails(object):
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
        'ship_from_postal_code': 'str'
    }

    attribute_map = {
        'ship_from_postal_code': 'shipFromPostalCode'
    }

    def __init__(self, ship_from_postal_code=None):
        """
        Ptsv2paymentsidcapturesOrderInformationShippingDetails - a model defined in Swagger
        """

        self._ship_from_postal_code = None

        if ship_from_postal_code is not None:
          self.ship_from_postal_code = ship_from_postal_code

    @property
    def ship_from_postal_code(self):
        """
        Gets the ship_from_postal_code of this Ptsv2paymentsidcapturesOrderInformationShippingDetails.
        Postal code for the address from which the goods are shipped, which is used to establish nexus. The default is the postal code associated with your CyberSource account.  The postal code must consist of 5 to 9 digits. When the billing country is the U.S., the 9-digit postal code must follow this format:  `[5 digits][dash][4 digits]`  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format:  `[alpha][numeric][alpha][space] [numeric][alpha][numeric]`  Example A1B 2C3  This field is frequently used for Level II and Level III transactions. 

        :return: The ship_from_postal_code of this Ptsv2paymentsidcapturesOrderInformationShippingDetails.
        :rtype: str
        """
        return self._ship_from_postal_code

    @ship_from_postal_code.setter
    def ship_from_postal_code(self, ship_from_postal_code):
        """
        Sets the ship_from_postal_code of this Ptsv2paymentsidcapturesOrderInformationShippingDetails.
        Postal code for the address from which the goods are shipped, which is used to establish nexus. The default is the postal code associated with your CyberSource account.  The postal code must consist of 5 to 9 digits. When the billing country is the U.S., the 9-digit postal code must follow this format:  `[5 digits][dash][4 digits]`  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format:  `[alpha][numeric][alpha][space] [numeric][alpha][numeric]`  Example A1B 2C3  This field is frequently used for Level II and Level III transactions. 

        :param ship_from_postal_code: The ship_from_postal_code of this Ptsv2paymentsidcapturesOrderInformationShippingDetails.
        :type: str
        """
        if ship_from_postal_code is not None and len(ship_from_postal_code) > 10:
            raise ValueError("Invalid value for `ship_from_postal_code`, length must be less than or equal to `10`")

        self._ship_from_postal_code = ship_from_postal_code

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
        if not isinstance(other, Ptsv2paymentsidcapturesOrderInformationShippingDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other