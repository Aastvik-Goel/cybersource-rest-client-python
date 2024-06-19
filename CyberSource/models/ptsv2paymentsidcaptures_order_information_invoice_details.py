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


class Ptsv2paymentsidcapturesOrderInformationInvoiceDetails(object):
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
        'purchase_order_number': 'str',
        'purchase_order_date': 'str',
        'purchase_contact_name': 'str',
        'taxable': 'bool',
        'vat_invoice_reference_number': 'str',
        'commodity_code': 'str',
        'transaction_advice_addendum': 'list[Ptsv2paymentsOrderInformationInvoiceDetailsTransactionAdviceAddendum]'
    }

    attribute_map = {
        'purchase_order_number': 'purchaseOrderNumber',
        'purchase_order_date': 'purchaseOrderDate',
        'purchase_contact_name': 'purchaseContactName',
        'taxable': 'taxable',
        'vat_invoice_reference_number': 'vatInvoiceReferenceNumber',
        'commodity_code': 'commodityCode',
        'transaction_advice_addendum': 'transactionAdviceAddendum'
    }

    def __init__(self, purchase_order_number=None, purchase_order_date=None, purchase_contact_name=None, taxable=None, vat_invoice_reference_number=None, commodity_code=None, transaction_advice_addendum=None):
        """
        Ptsv2paymentsidcapturesOrderInformationInvoiceDetails - a model defined in Swagger
        """

        self._purchase_order_number = None
        self._purchase_order_date = None
        self._purchase_contact_name = None
        self._taxable = None
        self._vat_invoice_reference_number = None
        self._commodity_code = None
        self._transaction_advice_addendum = None

        if purchase_order_number is not None:
          self.purchase_order_number = purchase_order_number
        if purchase_order_date is not None:
          self.purchase_order_date = purchase_order_date
        if purchase_contact_name is not None:
          self.purchase_contact_name = purchase_contact_name
        if taxable is not None:
          self.taxable = taxable
        if vat_invoice_reference_number is not None:
          self.vat_invoice_reference_number = vat_invoice_reference_number
        if commodity_code is not None:
          self.commodity_code = commodity_code
        if transaction_advice_addendum is not None:
          self.transaction_advice_addendum = transaction_advice_addendum

    @property
    def purchase_order_number(self):
        """
        Gets the purchase_order_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        Value used by your customer to identify the order. This value is typically a purchase order number. CyberSource recommends that you do not populate the field with all zeros or nines.  For processor-specific information, see the `user_po` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The purchase_order_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :rtype: str
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """
        Sets the purchase_order_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        Value used by your customer to identify the order. This value is typically a purchase order number. CyberSource recommends that you do not populate the field with all zeros or nines.  For processor-specific information, see the `user_po` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param purchase_order_number: The purchase_order_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :type: str
        """

        self._purchase_order_number = purchase_order_number

    @property
    def purchase_order_date(self):
        """
        Gets the purchase_order_date of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        Date the order was processed. `Format: YYYY-MM-DD`.  For processor-specific information, see the `purchaser_order_date` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The purchase_order_date of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :rtype: str
        """
        return self._purchase_order_date

    @purchase_order_date.setter
    def purchase_order_date(self, purchase_order_date):
        """
        Sets the purchase_order_date of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        Date the order was processed. `Format: YYYY-MM-DD`.  For processor-specific information, see the `purchaser_order_date` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param purchase_order_date: The purchase_order_date of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :type: str
        """

        self._purchase_order_date = purchase_order_date

    @property
    def purchase_contact_name(self):
        """
        Gets the purchase_contact_name of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        The name of the individual or the company contacted for company authorized purchases.  For processor-specific information, see the `authorized_contact_name` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The purchase_contact_name of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :rtype: str
        """
        return self._purchase_contact_name

    @purchase_contact_name.setter
    def purchase_contact_name(self, purchase_contact_name):
        """
        Sets the purchase_contact_name of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        The name of the individual or the company contacted for company authorized purchases.  For processor-specific information, see the `authorized_contact_name` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param purchase_contact_name: The purchase_contact_name of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :type: str
        """

        self._purchase_contact_name = purchase_contact_name

    @property
    def taxable(self):
        """
        Gets the taxable of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        Flag that indicates whether an order is taxable. This value must be true if the sum of all _lineItems[].taxAmount_ values > 0.  If you do not include any `lineItems[].taxAmount` values in your request, CyberSource does not include `invoiceDetails.taxable` in the data it sends to the processor.  For processor-specific information, see the `tax_indicator` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html)  Possible values:  - **true**  - **false** 

        :return: The taxable of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :rtype: bool
        """
        return self._taxable

    @taxable.setter
    def taxable(self, taxable):
        """
        Sets the taxable of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        Flag that indicates whether an order is taxable. This value must be true if the sum of all _lineItems[].taxAmount_ values > 0.  If you do not include any `lineItems[].taxAmount` values in your request, CyberSource does not include `invoiceDetails.taxable` in the data it sends to the processor.  For processor-specific information, see the `tax_indicator` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html)  Possible values:  - **true**  - **false** 

        :param taxable: The taxable of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :type: bool
        """

        self._taxable = taxable

    @property
    def vat_invoice_reference_number(self):
        """
        Gets the vat_invoice_reference_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        VAT invoice number associated with the transaction.  For processor-specific information, see the `vat_invoice_ref_number` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The vat_invoice_reference_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :rtype: str
        """
        return self._vat_invoice_reference_number

    @vat_invoice_reference_number.setter
    def vat_invoice_reference_number(self, vat_invoice_reference_number):
        """
        Sets the vat_invoice_reference_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        VAT invoice number associated with the transaction.  For processor-specific information, see the `vat_invoice_ref_number` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param vat_invoice_reference_number: The vat_invoice_reference_number of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :type: str
        """

        self._vat_invoice_reference_number = vat_invoice_reference_number

    @property
    def commodity_code(self):
        """
        Gets the commodity_code of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        International description code of the overall order's goods or services or the Categorizes purchases for VAT reporting. Contact your acquirer for a list of codes.  For processor-specific information, see the `summary_commodity_code` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The commodity_code of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :rtype: str
        """
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, commodity_code):
        """
        Sets the commodity_code of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        International description code of the overall order's goods or services or the Categorizes purchases for VAT reporting. Contact your acquirer for a list of codes.  For processor-specific information, see the `summary_commodity_code` field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param commodity_code: The commodity_code of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :type: str
        """

        self._commodity_code = commodity_code

    @property
    def transaction_advice_addendum(self):
        """
        Gets the transaction_advice_addendum of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.

        :return: The transaction_advice_addendum of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :rtype: list[Ptsv2paymentsOrderInformationInvoiceDetailsTransactionAdviceAddendum]
        """
        return self._transaction_advice_addendum

    @transaction_advice_addendum.setter
    def transaction_advice_addendum(self, transaction_advice_addendum):
        """
        Sets the transaction_advice_addendum of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.

        :param transaction_advice_addendum: The transaction_advice_addendum of this Ptsv2paymentsidcapturesOrderInformationInvoiceDetails.
        :type: list[Ptsv2paymentsOrderInformationInvoiceDetailsTransactionAdviceAddendum]
        """

        self._transaction_advice_addendum = transaction_advice_addendum

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
        if not isinstance(other, Ptsv2paymentsidcapturesOrderInformationInvoiceDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
