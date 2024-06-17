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


class Invoicingv2invoicesInvoiceInformation(object):
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
        'invoice_number': 'str',
        'description': 'str',
        'due_date': 'date',
        'send_immediately': 'bool',
        'allow_partial_payments': 'bool',
        'delivery_mode': 'str'
    }

    attribute_map = {
        'invoice_number': 'invoiceNumber',
        'description': 'description',
        'due_date': 'dueDate',
        'send_immediately': 'sendImmediately',
        'allow_partial_payments': 'allowPartialPayments',
        'delivery_mode': 'deliveryMode'
    }

    def __init__(self, invoice_number=None, description=None, due_date=None, send_immediately=None, allow_partial_payments=None, delivery_mode=None):
        """
        Invoicingv2invoicesInvoiceInformation - a model defined in Swagger
        """

        self._invoice_number = None
        self._description = None
        self._due_date = None
        self._send_immediately = None
        self._allow_partial_payments = None
        self._delivery_mode = None

        if invoice_number is not None:
          self.invoice_number = invoice_number
        if description is not None:
          self.description = description
        if due_date is not None:
          self.due_date = due_date
        if send_immediately is not None:
          self.send_immediately = send_immediately
        if allow_partial_payments is not None:
          self.allow_partial_payments = allow_partial_payments
        if delivery_mode is not None:
          self.delivery_mode = delivery_mode

    @property
    def invoice_number(self):
        """
        Gets the invoice_number of this Invoicingv2invoicesInvoiceInformation.
        Invoice Number.

        :return: The invoice_number of this Invoicingv2invoicesInvoiceInformation.
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """
        Sets the invoice_number of this Invoicingv2invoicesInvoiceInformation.
        Invoice Number.

        :param invoice_number: The invoice_number of this Invoicingv2invoicesInvoiceInformation.
        :type: str
        """



        self._invoice_number = invoice_number

    @property
    def description(self):
        """
        Gets the description of this Invoicingv2invoicesInvoiceInformation.
        The description included in the invoice.

        :return: The description of this Invoicingv2invoicesInvoiceInformation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Invoicingv2invoicesInvoiceInformation.
        The description included in the invoice.

        :param description: The description of this Invoicingv2invoicesInvoiceInformation.
        :type: str
        """



        self._description = description

    @property
    def due_date(self):
        """
        Gets the due_date of this Invoicingv2invoicesInvoiceInformation.
        The invoice due date. This field is required for creating an invoice. Format: `YYYY-MM-DD`, where `YYYY` = year, `MM` = month, and `DD` = day 

        :return: The due_date of this Invoicingv2invoicesInvoiceInformation.
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """
        Sets the due_date of this Invoicingv2invoicesInvoiceInformation.
        The invoice due date. This field is required for creating an invoice. Format: `YYYY-MM-DD`, where `YYYY` = year, `MM` = month, and `DD` = day 

        :param due_date: The due_date of this Invoicingv2invoicesInvoiceInformation.
        :type: date
        """



        self._due_date = due_date

    @property
    def send_immediately(self):
        """
        Gets the send_immediately of this Invoicingv2invoicesInvoiceInformation.
        If set to `true`, we send the invoice immediately. If set to `false`, the invoice remains in draft mode.

        :return: The send_immediately of this Invoicingv2invoicesInvoiceInformation.
        :rtype: bool
        """
        return self._send_immediately

    @send_immediately.setter
    def send_immediately(self, send_immediately):
        """
        Sets the send_immediately of this Invoicingv2invoicesInvoiceInformation.
        If set to `true`, we send the invoice immediately. If set to `false`, the invoice remains in draft mode.

        :param send_immediately: The send_immediately of this Invoicingv2invoicesInvoiceInformation.
        :type: bool
        """



        self._send_immediately = send_immediately

    @property
    def allow_partial_payments(self):
        """
        Gets the allow_partial_payments of this Invoicingv2invoicesInvoiceInformation.
        If set to `true`, the payer can make a partial invoice payment.

        :return: The allow_partial_payments of this Invoicingv2invoicesInvoiceInformation.
        :rtype: bool
        """
        return self._allow_partial_payments

    @allow_partial_payments.setter
    def allow_partial_payments(self, allow_partial_payments):
        """
        Sets the allow_partial_payments of this Invoicingv2invoicesInvoiceInformation.
        If set to `true`, the payer can make a partial invoice payment.

        :param allow_partial_payments: The allow_partial_payments of this Invoicingv2invoicesInvoiceInformation.
        :type: bool
        """



        self._allow_partial_payments = allow_partial_payments

    @property
    def delivery_mode(self):
        """
        Gets the delivery_mode of this Invoicingv2invoicesInvoiceInformation.
        If set to `None`, the invoice is created, and its status is set to 'CREATED', but no email is sent.    Possible values:        - `None`   - `Email`  

        :return: The delivery_mode of this Invoicingv2invoicesInvoiceInformation.
        :rtype: str
        """
        return self._delivery_mode

    @delivery_mode.setter
    def delivery_mode(self, delivery_mode):
        """
        Sets the delivery_mode of this Invoicingv2invoicesInvoiceInformation.
        If set to `None`, the invoice is created, and its status is set to 'CREATED', but no email is sent.    Possible values:        - `None`   - `Email`  

        :param delivery_mode: The delivery_mode of this Invoicingv2invoicesInvoiceInformation.
        :type: str
        """



        self._delivery_mode = delivery_mode

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
        if not isinstance(other, Invoicingv2invoicesInvoiceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
