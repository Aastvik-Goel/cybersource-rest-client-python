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


class Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails(object):
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
        'type': 'str',
        'amount': 'str',
        'rate': 'str'
    }

    attribute_map = {
        'type': 'type',
        'amount': 'amount',
        'rate': 'rate'
    }

    def __init__(self, type=None, amount=None, rate=None):
        """
        Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails - a model defined in Swagger
        """

        self._type = None
        self._amount = None
        self._rate = None

        if type is not None:
          self.type = type
        if amount is not None:
          self.amount = amount
        if rate is not None:
          self.rate = rate

    @property
    def type(self):
        """
        Gets the type of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        Indicates the type of tax data for the _taxDetails_ object.  Possible values:  - `alternate` - `local` - `national` - `vat` - `other` - `green`  For processor-specific details, see the `alternate_tax_amount`, `local_tax`, `national_tax` or `vat_tax_amount` field descriptions in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/) 

        :return: The type of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        Indicates the type of tax data for the _taxDetails_ object.  Possible values:  - `alternate` - `local` - `national` - `vat` - `other` - `green`  For processor-specific details, see the `alternate_tax_amount`, `local_tax`, `national_tax` or `vat_tax_amount` field descriptions in [Level II and Level III Processing Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/) 

        :param type: The type of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        :type: str
        """



        self._type = type

    @property
    def amount(self):
        """
        Gets the amount of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        Indicates the amount of tax based on the `type` field as described in the table below:  | type      | type description | | ------------- |:-------------:| | `alternate` | Total amount of alternate tax for the order. | | `local`     | Sales tax for the order. | | `national`  | National tax for the order. | | `vat`       | Total amount of value added tax (VAT) included in the order. | | `other`     | Other tax. | | `green`     | Green tax amount for Korean Processing. | 

        :return: The amount of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        Indicates the amount of tax based on the `type` field as described in the table below:  | type      | type description | | ------------- |:-------------:| | `alternate` | Total amount of alternate tax for the order. | | `local`     | Sales tax for the order. | | `national`  | National tax for the order. | | `vat`       | Total amount of value added tax (VAT) included in the order. | | `other`     | Other tax. | | `green`     | Green tax amount for Korean Processing. | 

        :param amount: The amount of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        :type: str
        """



        self._amount = amount

    @property
    def rate(self):
        """
        Gets the rate of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        Rate of VAT or other tax for the order.  Example 0.040 (=4%)  Valid range: 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated)  For processor-specific details, see the `alternate_tax_amount`, `vat_rate`, `vat_tax_rate`, `local_tax`, `national_tax`, `vat_tax_amount` or `other_tax#_rate` field descriptions in the [Level II and Level III Processing Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/) 

        :return: The rate of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        Rate of VAT or other tax for the order.  Example 0.040 (=4%)  Valid range: 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated)  For processor-specific details, see the `alternate_tax_amount`, `vat_rate`, `vat_tax_rate`, `local_tax`, `national_tax`, `vat_tax_amount` or `other_tax#_rate` field descriptions in the [Level II and Level III Processing Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/) 

        :param rate: The rate of this Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails.
        :type: str
        """



        self._rate = rate

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
        if not isinstance(other, Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
