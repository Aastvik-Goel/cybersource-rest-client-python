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


class Ptsv2paymentreferencesUserInterface(object):
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
        'border_radius': 'str',
        'theme': 'str',
        'color': 'Ptsv2paymentreferencesUserInterfaceColor'
    }

    attribute_map = {
        'border_radius': 'borderRadius',
        'theme': 'theme',
        'color': 'color'
    }

    def __init__(self, border_radius=None, theme=None, color=None):
        """
        Ptsv2paymentreferencesUserInterface - a model defined in Swagger
        """

        self._border_radius = None
        self._theme = None
        self._color = None

        if border_radius is not None:
          self.border_radius = border_radius
        if theme is not None:
          self.theme = theme
        if color is not None:
          self.color = color

    @property
    def border_radius(self):
        """
        Gets the border_radius of this Ptsv2paymentreferencesUserInterface.
        Border Radius, Allowed Values - Number, Chars, SPACE, Percentage(%), DOT(.), Example '25px 10px 25px 10px'; '2em 1em 0.5em 3em' 

        :return: The border_radius of this Ptsv2paymentreferencesUserInterface.
        :rtype: str
        """
        return self._border_radius

    @border_radius.setter
    def border_radius(self, border_radius):
        """
        Sets the border_radius of this Ptsv2paymentreferencesUserInterface.
        Border Radius, Allowed Values - Number, Chars, SPACE, Percentage(%), DOT(.), Example '25px 10px 25px 10px'; '2em 1em 0.5em 3em' 

        :param border_radius: The border_radius of this Ptsv2paymentreferencesUserInterface.
        :type: str
        """

        self._border_radius = border_radius

    @property
    def theme(self):
        """
        Gets the theme of this Ptsv2paymentreferencesUserInterface.
        UI Theme Name/Design Name - Allowed Chars: Alpha Numeric, Dot (.), Hyphen (-), Underscore (_) 

        :return: The theme of this Ptsv2paymentreferencesUserInterface.
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """
        Sets the theme of this Ptsv2paymentreferencesUserInterface.
        UI Theme Name/Design Name - Allowed Chars: Alpha Numeric, Dot (.), Hyphen (-), Underscore (_) 

        :param theme: The theme of this Ptsv2paymentreferencesUserInterface.
        :type: str
        """

        self._theme = theme

    @property
    def color(self):
        """
        Gets the color of this Ptsv2paymentreferencesUserInterface.

        :return: The color of this Ptsv2paymentreferencesUserInterface.
        :rtype: Ptsv2paymentreferencesUserInterfaceColor
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this Ptsv2paymentreferencesUserInterface.

        :param color: The color of this Ptsv2paymentreferencesUserInterface.
        :type: Ptsv2paymentreferencesUserInterfaceColor
        """

        self._color = color

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
        if not isinstance(other, Ptsv2paymentreferencesUserInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other