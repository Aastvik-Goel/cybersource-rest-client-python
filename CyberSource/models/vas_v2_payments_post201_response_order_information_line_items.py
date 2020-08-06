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


class VasV2PaymentsPost201ResponseOrderInformationLineItems(object):
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
        'tax_details': 'list[VasV2PaymentsPost201ResponseOrderInformationTaxDetails]',
        'jurisdiction': 'list[VasV2PaymentsPost201ResponseOrderInformationJurisdiction]',
        'exempt_amount': 'str',
        'taxable_amount': 'str',
        'tax_amount': 'str'
    }

    attribute_map = {
        'tax_details': 'taxDetails',
        'jurisdiction': 'jurisdiction',
        'exempt_amount': 'exemptAmount',
        'taxable_amount': 'taxableAmount',
        'tax_amount': 'taxAmount'
    }

    def __init__(self, tax_details=None, jurisdiction=None, exempt_amount=None, taxable_amount=None, tax_amount=None):
        """
        VasV2PaymentsPost201ResponseOrderInformationLineItems - a model defined in Swagger
        """

        self._tax_details = None
        self._jurisdiction = None
        self._exempt_amount = None
        self._taxable_amount = None
        self._tax_amount = None

        if tax_details is not None:
          self.tax_details = tax_details
        if jurisdiction is not None:
          self.jurisdiction = jurisdiction
        if exempt_amount is not None:
          self.exempt_amount = exempt_amount
        if taxable_amount is not None:
          self.taxable_amount = taxable_amount
        if tax_amount is not None:
          self.tax_amount = tax_amount

    @property
    def tax_details(self):
        """
        Gets the tax_details of this VasV2PaymentsPost201ResponseOrderInformationLineItems.

        :return: The tax_details of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :rtype: list[VasV2PaymentsPost201ResponseOrderInformationTaxDetails]
        """
        return self._tax_details

    @tax_details.setter
    def tax_details(self, tax_details):
        """
        Sets the tax_details of this VasV2PaymentsPost201ResponseOrderInformationLineItems.

        :param tax_details: The tax_details of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :type: list[VasV2PaymentsPost201ResponseOrderInformationTaxDetails]
        """

        self._tax_details = tax_details

    @property
    def jurisdiction(self):
        """
        Gets the jurisdiction of this VasV2PaymentsPost201ResponseOrderInformationLineItems.

        :return: The jurisdiction of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :rtype: list[VasV2PaymentsPost201ResponseOrderInformationJurisdiction]
        """
        return self._jurisdiction

    @jurisdiction.setter
    def jurisdiction(self, jurisdiction):
        """
        Sets the jurisdiction of this VasV2PaymentsPost201ResponseOrderInformationLineItems.

        :param jurisdiction: The jurisdiction of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :type: list[VasV2PaymentsPost201ResponseOrderInformationJurisdiction]
        """

        self._jurisdiction = jurisdiction

    @property
    def exempt_amount(self):
        """
        Gets the exempt_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        Exempt amount for the lineItem. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :return: The exempt_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._exempt_amount

    @exempt_amount.setter
    def exempt_amount(self, exempt_amount):
        """
        Sets the exempt_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        Exempt amount for the lineItem. Returned only if the `taxInformation.showTaxPerLineItem` field is set to `Yes`. 

        :param exempt_amount: The exempt_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :type: str
        """
        if exempt_amount is not None and len(exempt_amount) > 15:
            raise ValueError("Invalid value for `exempt_amount`, length must be less than or equal to `15`")

        self._exempt_amount = exempt_amount

    @property
    def taxable_amount(self):
        """
        Gets the taxable_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        Portion of the item amount that is taxable. 

        :return: The taxable_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._taxable_amount

    @taxable_amount.setter
    def taxable_amount(self, taxable_amount):
        """
        Sets the taxable_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        Portion of the item amount that is taxable. 

        :param taxable_amount: The taxable_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :type: str
        """
        if taxable_amount is not None and len(taxable_amount) > 15:
            raise ValueError("Invalid value for `taxable_amount`, length must be less than or equal to `15`")

        self._taxable_amount = taxable_amount

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        Total tax for the item. This value is the sum of all taxes applied to the item. 

        :return: The tax_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        Total tax for the item. This value is the sum of all taxes applied to the item. 

        :param tax_amount: The tax_amount of this VasV2PaymentsPost201ResponseOrderInformationLineItems.
        :type: str
        """
        if tax_amount is not None and len(tax_amount) > 15:
            raise ValueError("Invalid value for `tax_amount`, length must be less than or equal to `15`")

        self._tax_amount = tax_amount

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
        if not isinstance(other, VasV2PaymentsPost201ResponseOrderInformationLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other