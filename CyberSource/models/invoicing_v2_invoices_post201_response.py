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


class InvoicingV2InvoicesPost201Response(object):
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
        'links': 'InvoicingV2InvoicesAllGet200ResponseLinks',
        'id': 'str',
        'submit_time_utc': 'str',
        'status': 'str',
        'customer_information': 'Invoicingv2invoicesCustomerInformation',
        'invoice_information': 'InvoicingV2InvoicesPost201ResponseInvoiceInformation',
        'order_information': 'InvoicingV2InvoicesPost201ResponseOrderInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'customer_information': 'customerInformation',
        'invoice_information': 'invoiceInformation',
        'order_information': 'orderInformation'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, status=None, customer_information=None, invoice_information=None, order_information=None):
        """
        InvoicingV2InvoicesPost201Response - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._customer_information = None
        self._invoice_information = None
        self._order_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if customer_information is not None:
          self.customer_information = customer_information
        if invoice_information is not None:
          self.invoice_information = invoice_information
        if order_information is not None:
          self.order_information = order_information

    @property
    def links(self):
        """
        Gets the links of this InvoicingV2InvoicesPost201Response.

        :return: The links of this InvoicingV2InvoicesPost201Response.
        :rtype: InvoicingV2InvoicesAllGet200ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InvoicingV2InvoicesPost201Response.

        :param links: The links of this InvoicingV2InvoicesPost201Response.
        :type: InvoicingV2InvoicesAllGet200ResponseLinks
        """



        self._links = links

    @property
    def id(self):
        """
        Gets the id of this InvoicingV2InvoicesPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this InvoicingV2InvoicesPost201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InvoicingV2InvoicesPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this InvoicingV2InvoicesPost201Response.
        :type: str
        """



        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this InvoicingV2InvoicesPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this InvoicingV2InvoicesPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this InvoicingV2InvoicesPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this InvoicingV2InvoicesPost201Response.
        :type: str
        """



        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this InvoicingV2InvoicesPost201Response.
        The status of the invoice.  Possible values: - DRAFT - CREATED - SENT - PARTIAL - PAID - CANCELED - PENDING 

        :return: The status of this InvoicingV2InvoicesPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this InvoicingV2InvoicesPost201Response.
        The status of the invoice.  Possible values: - DRAFT - CREATED - SENT - PARTIAL - PAID - CANCELED - PENDING 

        :param status: The status of this InvoicingV2InvoicesPost201Response.
        :type: str
        """



        self._status = status

    @property
    def customer_information(self):
        """
        Gets the customer_information of this InvoicingV2InvoicesPost201Response.

        :return: The customer_information of this InvoicingV2InvoicesPost201Response.
        :rtype: Invoicingv2invoicesCustomerInformation
        """
        return self._customer_information

    @customer_information.setter
    def customer_information(self, customer_information):
        """
        Sets the customer_information of this InvoicingV2InvoicesPost201Response.

        :param customer_information: The customer_information of this InvoicingV2InvoicesPost201Response.
        :type: Invoicingv2invoicesCustomerInformation
        """



        self._customer_information = customer_information

    @property
    def invoice_information(self):
        """
        Gets the invoice_information of this InvoicingV2InvoicesPost201Response.

        :return: The invoice_information of this InvoicingV2InvoicesPost201Response.
        :rtype: InvoicingV2InvoicesPost201ResponseInvoiceInformation
        """
        return self._invoice_information

    @invoice_information.setter
    def invoice_information(self, invoice_information):
        """
        Sets the invoice_information of this InvoicingV2InvoicesPost201Response.

        :param invoice_information: The invoice_information of this InvoicingV2InvoicesPost201Response.
        :type: InvoicingV2InvoicesPost201ResponseInvoiceInformation
        """



        self._invoice_information = invoice_information

    @property
    def order_information(self):
        """
        Gets the order_information of this InvoicingV2InvoicesPost201Response.

        :return: The order_information of this InvoicingV2InvoicesPost201Response.
        :rtype: InvoicingV2InvoicesPost201ResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this InvoicingV2InvoicesPost201Response.

        :param order_information: The order_information of this InvoicingV2InvoicesPost201Response.
        :type: InvoicingV2InvoicesPost201ResponseOrderInformation
        """



        self._order_information = order_information

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
        if not isinstance(other, InvoicingV2InvoicesPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
