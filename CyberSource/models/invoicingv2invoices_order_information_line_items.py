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


class Invoicingv2invoicesOrderInformationLineItems(object):
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
        'product_sku': 'str',
        'product_name': 'str',
        'quantity': 'int',
        'unit_price': 'str',
        'discount_amount': 'str',
        'discount_rate': 'str',
        'tax_amount': 'str',
        'tax_rate': 'str',
        'total_amount': 'str'
    }

    attribute_map = {
        'product_sku': 'productSku',
        'product_name': 'productName',
        'quantity': 'quantity',
        'unit_price': 'unitPrice',
        'discount_amount': 'discountAmount',
        'discount_rate': 'discountRate',
        'tax_amount': 'taxAmount',
        'tax_rate': 'taxRate',
        'total_amount': 'totalAmount'
    }

    def __init__(self, product_sku=None, product_name=None, quantity=None, unit_price=None, discount_amount=None, discount_rate=None, tax_amount=None, tax_rate=None, total_amount=None):
        """
        Invoicingv2invoicesOrderInformationLineItems - a model defined in Swagger
        """

        self._product_sku = None
        self._product_name = None
        self._quantity = None
        self._unit_price = None
        self._discount_amount = None
        self._discount_rate = None
        self._tax_amount = None
        self._tax_rate = None
        self._total_amount = None

        if product_sku is not None:
          self.product_sku = product_sku
        if product_name is not None:
          self.product_name = product_name
        if quantity is not None:
          self.quantity = quantity
        if unit_price is not None:
          self.unit_price = unit_price
        if discount_amount is not None:
          self.discount_amount = discount_amount
        if discount_rate is not None:
          self.discount_rate = discount_rate
        if tax_amount is not None:
          self.tax_amount = tax_amount
        if tax_rate is not None:
          self.tax_rate = tax_rate
        if total_amount is not None:
          self.total_amount = total_amount

    @property
    def product_sku(self):
        """
        Gets the product_sku of this Invoicingv2invoicesOrderInformationLineItems.
        Product identifier code. Also known as the Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to **default** or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the values related to shipping and/or handling. 

        :return: The product_sku of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """
        Sets the product_sku of this Invoicingv2invoicesOrderInformationLineItems.
        Product identifier code. Also known as the Stock Keeping Unit (SKU) code for the product.  For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not set to **default** or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the values related to shipping and/or handling. 

        :param product_sku: The product_sku of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._product_sku = product_sku

    @property
    def product_name(self):
        """
        Gets the product_name of this Invoicingv2invoicesOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :return: The product_name of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this Invoicingv2invoicesOrderInformationLineItems.
        For an authorization or capture transaction (`processingOptions.capture` is `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values that are related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :param product_name: The product_name of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._product_name = product_name

    @property
    def quantity(self):
        """
        Gets the quantity of this Invoicingv2invoicesOrderInformationLineItems.
        Number of units for this order. Must be a non-negative integer.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :return: The quantity of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Invoicingv2invoicesOrderInformationLineItems.
        Number of units for this order. Must be a non-negative integer.  The default is `1`. For an authorization or capture transaction (`processingOptions.capture` is set to `true` or `false`), this field is required when `orderInformation.lineItems[].productCode` is not `default` or one of the other values related to shipping and/or handling.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. 

        :param quantity: The quantity of this Invoicingv2invoicesOrderInformationLineItems.
        :type: int
        """

        self._quantity = quantity

    @property
    def unit_price(self):
        """
        Gets the unit_price of this Invoicingv2invoicesOrderInformationLineItems.
        Per-item price of the product. This value for this field cannot be negative.  You must include either this field or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  You can include a decimal point (.), but you cannot include any other special characters. The value is truncated to the correct number of decimal places.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Tax Calculation Required field for U.S., Canadian, international and value added taxes.  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen.  #### Maximum Field Lengths For GPN and JCN Gateway: Decimal (10) All other processors: Decimal (15) 

        :return: The unit_price of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this Invoicingv2invoicesOrderInformationLineItems.
        Per-item price of the product. This value for this field cannot be negative.  You must include either this field or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  You can include a decimal point (.), but you cannot include any other special characters. The value is truncated to the correct number of decimal places.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either the 1st line item in the order and this field, or the request-level field `orderInformation.amountDetails.totalAmount` in your request.  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in the [Merchant Descriptors Using the SCMP API Guide.] (https://apps.cybersource.com/library/documentation/dev_guides/Merchant_Descriptors_SCMP_API/html/)  #### Tax Calculation Required field for U.S., Canadian, international and value added taxes.  #### Zero Amount Authorizations If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen.  #### Maximum Field Lengths For GPN and JCN Gateway: Decimal (10) All other processors: Decimal (15) 

        :param unit_price: The unit_price of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._unit_price = unit_price

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this Invoicingv2invoicesOrderInformationLineItems.
        Discount applied to the item.

        :return: The discount_amount of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this Invoicingv2invoicesOrderInformationLineItems.
        Discount applied to the item.

        :param discount_amount: The discount_amount of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._discount_amount = discount_amount

    @property
    def discount_rate(self):
        """
        Gets the discount_rate of this Invoicingv2invoicesOrderInformationLineItems.
        Rate the item is discounted. Maximum of 2 decimal places.  Example 5.25 (=5.25%) 

        :return: The discount_rate of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, discount_rate):
        """
        Sets the discount_rate of this Invoicingv2invoicesOrderInformationLineItems.
        Rate the item is discounted. Maximum of 2 decimal places.  Example 5.25 (=5.25%) 

        :param discount_rate: The discount_rate of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._discount_rate = discount_rate

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this Invoicingv2invoicesOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:   1. You include each line item in your request.  ..- 1st line item has amount=10.00, quantity=1, and taxAmount=0.80  ..- 2nd line item has amount=20.00, quantity=1, and taxAmount=1.60  2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  Optional field.  #### Airlines processing Tax portion of the order amount. This value cannot exceed 99999999999999 (fourteen 9s). Format: English characters only. Optional request field for a line item.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  Note if you send this field in your tax request, the value in the field will override the tax engine 

        :return: The tax_amount of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this Invoicingv2invoicesOrderInformationLineItems.
        Total tax to apply to the product. This value cannot be negative. The tax amount and the offer amount must be in the same currency. The tax amount field is additive.  The following example uses a two-exponent currency such as USD:   1. You include each line item in your request.  ..- 1st line item has amount=10.00, quantity=1, and taxAmount=0.80  ..- 2nd line item has amount=20.00, quantity=1, and taxAmount=1.60  2. The total amount authorized will be 32.40, not 30.00 with 2.40 of tax included.  Optional field.  #### Airlines processing Tax portion of the order amount. This value cannot exceed 99999999999999 (fourteen 9s). Format: English characters only. Optional request field for a line item.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes.  Note if you send this field in your tax request, the value in the field will override the tax engine 

        :param tax_amount: The tax_amount of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this Invoicingv2invoicesOrderInformationLineItems.
        Tax rate applied to the item.  For details, see `tax_rate` field description in the [Level II and Level III Processing Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/)  **Visa**: Valid range is 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated).  **Mastercard**: Valid range is 0.00001 to 0.99999 (0.001% to 99.999%). 

        :return: The tax_rate of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this Invoicingv2invoicesOrderInformationLineItems.
        Tax rate applied to the item.  For details, see `tax_rate` field description in the [Level II and Level III Processing Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html/)  **Visa**: Valid range is 0.01 to 0.99 (1% to 99%, with only whole percentage values accepted; values with additional decimal places will be truncated).  **Mastercard**: Valid range is 0.00001 to 0.99999 (0.001% to 99.999%). 

        :param tax_rate: The tax_rate of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._tax_rate = tax_rate

    @property
    def total_amount(self):
        """
        Gets the total_amount of this Invoicingv2invoicesOrderInformationLineItems.
        Total amount for the item. Normally calculated as the unit price times quantity.  When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the purchase amount total for prepaid gift cards in major units.  Example: 123.45 USD = 123 

        :return: The total_amount of this Invoicingv2invoicesOrderInformationLineItems.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this Invoicingv2invoicesOrderInformationLineItems.
        Total amount for the item. Normally calculated as the unit price times quantity.  When `orderInformation.lineItems[].productCode` is \"gift_card\", this is the purchase amount total for prepaid gift cards in major units.  Example: 123.45 USD = 123 

        :param total_amount: The total_amount of this Invoicingv2invoicesOrderInformationLineItems.
        :type: str
        """

        self._total_amount = total_amount

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
        if not isinstance(other, Invoicingv2invoicesOrderInformationLineItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
