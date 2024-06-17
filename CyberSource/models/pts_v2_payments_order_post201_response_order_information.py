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


class PtsV2PaymentsOrderPost201ResponseOrderInformation(object):
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
        'bill_to': 'PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo',
        'ship_to': 'PtsV2PaymentsOrderPost201ResponseOrderInformationShipTo',
        'amount_details': 'PtsV2PaymentsOrderPost201ResponseOrderInformationAmountDetails',
        'shipping_details': 'PtsV2PaymentsOrderPost201ResponseOrderInformationShippingDetails'
    }

    attribute_map = {
        'bill_to': 'billTo',
        'ship_to': 'shipTo',
        'amount_details': 'amountDetails',
        'shipping_details': 'shippingDetails'
    }

    def __init__(self, bill_to=None, ship_to=None, amount_details=None, shipping_details=None):
        """
        PtsV2PaymentsOrderPost201ResponseOrderInformation - a model defined in Swagger
        """

        self._bill_to = None
        self._ship_to = None
        self._amount_details = None
        self._shipping_details = None

        if bill_to is not None:
          self.bill_to = bill_to
        if ship_to is not None:
          self.ship_to = ship_to
        if amount_details is not None:
          self.amount_details = amount_details
        if shipping_details is not None:
          self.shipping_details = shipping_details

    @property
    def bill_to(self):
        """
        Gets the bill_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :return: The bill_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :rtype: PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :param bill_to: The bill_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :type: PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo
        """



        self._bill_to = bill_to

    @property
    def ship_to(self):
        """
        Gets the ship_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :return: The ship_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :rtype: PtsV2PaymentsOrderPost201ResponseOrderInformationShipTo
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """
        Sets the ship_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :param ship_to: The ship_to of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :type: PtsV2PaymentsOrderPost201ResponseOrderInformationShipTo
        """



        self._ship_to = ship_to

    @property
    def amount_details(self):
        """
        Gets the amount_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :return: The amount_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :rtype: PtsV2PaymentsOrderPost201ResponseOrderInformationAmountDetails
        """
        return self._amount_details

    @amount_details.setter
    def amount_details(self, amount_details):
        """
        Sets the amount_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :param amount_details: The amount_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :type: PtsV2PaymentsOrderPost201ResponseOrderInformationAmountDetails
        """



        self._amount_details = amount_details

    @property
    def shipping_details(self):
        """
        Gets the shipping_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :return: The shipping_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :rtype: PtsV2PaymentsOrderPost201ResponseOrderInformationShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """
        Sets the shipping_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.

        :param shipping_details: The shipping_details of this PtsV2PaymentsOrderPost201ResponseOrderInformation.
        :type: PtsV2PaymentsOrderPost201ResponseOrderInformationShippingDetails
        """



        self._shipping_details = shipping_details

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
        if not isinstance(other, PtsV2PaymentsOrderPost201ResponseOrderInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
