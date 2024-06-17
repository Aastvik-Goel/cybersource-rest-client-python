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


class Invoicingv2invoicesidInvoiceInformation(object):
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
        'description': 'str',
        'due_date': 'date',
        'allow_partial_payments': 'bool',
        'delivery_mode': 'str'
    }

    attribute_map = {
        'description': 'description',
        'due_date': 'dueDate',
        'allow_partial_payments': 'allowPartialPayments',
        'delivery_mode': 'deliveryMode'
    }

    def __init__(self, description=None, due_date=None, allow_partial_payments=None, delivery_mode=None):
        """
        Invoicingv2invoicesidInvoiceInformation - a model defined in Swagger
        """

        self._description = None
        self._due_date = None
        self._allow_partial_payments = None
        self._delivery_mode = None

        if description is not None:
          self.description = description
        if due_date is not None:
          self.due_date = due_date
        if allow_partial_payments is not None:
          self.allow_partial_payments = allow_partial_payments
        if delivery_mode is not None:
          self.delivery_mode = delivery_mode

    @property
    def description(self):
        """
        Gets the description of this Invoicingv2invoicesidInvoiceInformation.
        The description included in the invoice.

        :return: The description of this Invoicingv2invoicesidInvoiceInformation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Invoicingv2invoicesidInvoiceInformation.
        The description included in the invoice.

        :param description: The description of this Invoicingv2invoicesidInvoiceInformation.
        :type: str
        """



        self._description = description

    @property
    def due_date(self):
        """
        Gets the due_date of this Invoicingv2invoicesidInvoiceInformation.
        The invoice due date. This field is required for creating an invoice. Format: `YYYY-MM-DD`, where `YYYY` = year, `MM` = month, and `DD` = day 

        :return: The due_date of this Invoicingv2invoicesidInvoiceInformation.
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """
        Sets the due_date of this Invoicingv2invoicesidInvoiceInformation.
        The invoice due date. This field is required for creating an invoice. Format: `YYYY-MM-DD`, where `YYYY` = year, `MM` = month, and `DD` = day 

        :param due_date: The due_date of this Invoicingv2invoicesidInvoiceInformation.
        :type: date
        """



        self._due_date = due_date

    @property
    def allow_partial_payments(self):
        """
        Gets the allow_partial_payments of this Invoicingv2invoicesidInvoiceInformation.
        If set to `true`, the payer can make a partial invoice payment.

        :return: The allow_partial_payments of this Invoicingv2invoicesidInvoiceInformation.
        :rtype: bool
        """
        return self._allow_partial_payments

    @allow_partial_payments.setter
    def allow_partial_payments(self, allow_partial_payments):
        """
        Sets the allow_partial_payments of this Invoicingv2invoicesidInvoiceInformation.
        If set to `true`, the payer can make a partial invoice payment.

        :param allow_partial_payments: The allow_partial_payments of this Invoicingv2invoicesidInvoiceInformation.
        :type: bool
        """



        self._allow_partial_payments = allow_partial_payments

    @property
    def delivery_mode(self):
        """
        Gets the delivery_mode of this Invoicingv2invoicesidInvoiceInformation.
        If set to `None`, the invoice is created, and its status is set to 'CREATED', but no email is sent.    Possible values:        - `None`   - `Email`  

        :return: The delivery_mode of this Invoicingv2invoicesidInvoiceInformation.
        :rtype: str
        """
        return self._delivery_mode

    @delivery_mode.setter
    def delivery_mode(self, delivery_mode):
        """
        Sets the delivery_mode of this Invoicingv2invoicesidInvoiceInformation.
        If set to `None`, the invoice is created, and its status is set to 'CREATED', but no email is sent.    Possible values:        - `None`   - `Email`  

        :param delivery_mode: The delivery_mode of this Invoicingv2invoicesidInvoiceInformation.
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
        if not isinstance(other, Invoicingv2invoicesidInvoiceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
