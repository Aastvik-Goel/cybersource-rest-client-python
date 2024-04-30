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


class PatchCustomerRequest(object):
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
        'links': 'Tmsv2customersLinks',
        'id': 'str',
        'object_information': 'Tmsv2customersObjectInformation',
        'buyer_information': 'Tmsv2customersBuyerInformation',
        'client_reference_information': 'Tmsv2customersClientReferenceInformation',
        'merchant_defined_information': 'list[Tmsv2customersMerchantDefinedInformation]',
        'default_payment_instrument': 'Tmsv2customersDefaultPaymentInstrument',
        'default_shipping_address': 'Tmsv2customersDefaultShippingAddress',
        'metadata': 'Tmsv2customersMetadata',
        'embedded': 'Tmsv2customersEmbedded'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'object_information': 'objectInformation',
        'buyer_information': 'buyerInformation',
        'client_reference_information': 'clientReferenceInformation',
        'merchant_defined_information': 'merchantDefinedInformation',
        'default_payment_instrument': 'defaultPaymentInstrument',
        'default_shipping_address': 'defaultShippingAddress',
        'metadata': 'metadata',
        'embedded': '_embedded'
    }

    def __init__(self, links=None, id=None, object_information=None, buyer_information=None, client_reference_information=None, merchant_defined_information=None, default_payment_instrument=None, default_shipping_address=None, metadata=None, embedded=None):
        """
        PatchCustomerRequest - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._object_information = None
        self._buyer_information = None
        self._client_reference_information = None
        self._merchant_defined_information = None
        self._default_payment_instrument = None
        self._default_shipping_address = None
        self._metadata = None
        self._embedded = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if object_information is not None:
          self.object_information = object_information
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if merchant_defined_information is not None:
          self.merchant_defined_information = merchant_defined_information
        if default_payment_instrument is not None:
          self.default_payment_instrument = default_payment_instrument
        if default_shipping_address is not None:
          self.default_shipping_address = default_shipping_address
        if metadata is not None:
          self.metadata = metadata
        if embedded is not None:
          self.embedded = embedded

    @property
    def links(self):
        """
        Gets the links of this PatchCustomerRequest.

        :return: The links of this PatchCustomerRequest.
        :rtype: Tmsv2customersLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PatchCustomerRequest.

        :param links: The links of this PatchCustomerRequest.
        :type: Tmsv2customersLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PatchCustomerRequest.
        The Id of the Customer Token.

        :return: The id of this PatchCustomerRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PatchCustomerRequest.
        The Id of the Customer Token.

        :param id: The id of this PatchCustomerRequest.
        :type: str
        """

        self._id = id

    @property
    def object_information(self):
        """
        Gets the object_information of this PatchCustomerRequest.

        :return: The object_information of this PatchCustomerRequest.
        :rtype: Tmsv2customersObjectInformation
        """
        return self._object_information

    @object_information.setter
    def object_information(self, object_information):
        """
        Sets the object_information of this PatchCustomerRequest.

        :param object_information: The object_information of this PatchCustomerRequest.
        :type: Tmsv2customersObjectInformation
        """

        self._object_information = object_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this PatchCustomerRequest.

        :return: The buyer_information of this PatchCustomerRequest.
        :rtype: Tmsv2customersBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this PatchCustomerRequest.

        :param buyer_information: The buyer_information of this PatchCustomerRequest.
        :type: Tmsv2customersBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this PatchCustomerRequest.

        :return: The client_reference_information of this PatchCustomerRequest.
        :rtype: Tmsv2customersClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this PatchCustomerRequest.

        :param client_reference_information: The client_reference_information of this PatchCustomerRequest.
        :type: Tmsv2customersClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def merchant_defined_information(self):
        """
        Gets the merchant_defined_information of this PatchCustomerRequest.
        Object containing the custom data that the merchant defines. 

        :return: The merchant_defined_information of this PatchCustomerRequest.
        :rtype: list[Tmsv2customersMerchantDefinedInformation]
        """
        return self._merchant_defined_information

    @merchant_defined_information.setter
    def merchant_defined_information(self, merchant_defined_information):
        """
        Sets the merchant_defined_information of this PatchCustomerRequest.
        Object containing the custom data that the merchant defines. 

        :param merchant_defined_information: The merchant_defined_information of this PatchCustomerRequest.
        :type: list[Tmsv2customersMerchantDefinedInformation]
        """

        self._merchant_defined_information = merchant_defined_information

    @property
    def default_payment_instrument(self):
        """
        Gets the default_payment_instrument of this PatchCustomerRequest.

        :return: The default_payment_instrument of this PatchCustomerRequest.
        :rtype: Tmsv2customersDefaultPaymentInstrument
        """
        return self._default_payment_instrument

    @default_payment_instrument.setter
    def default_payment_instrument(self, default_payment_instrument):
        """
        Sets the default_payment_instrument of this PatchCustomerRequest.

        :param default_payment_instrument: The default_payment_instrument of this PatchCustomerRequest.
        :type: Tmsv2customersDefaultPaymentInstrument
        """

        self._default_payment_instrument = default_payment_instrument

    @property
    def default_shipping_address(self):
        """
        Gets the default_shipping_address of this PatchCustomerRequest.

        :return: The default_shipping_address of this PatchCustomerRequest.
        :rtype: Tmsv2customersDefaultShippingAddress
        """
        return self._default_shipping_address

    @default_shipping_address.setter
    def default_shipping_address(self, default_shipping_address):
        """
        Sets the default_shipping_address of this PatchCustomerRequest.

        :param default_shipping_address: The default_shipping_address of this PatchCustomerRequest.
        :type: Tmsv2customersDefaultShippingAddress
        """

        self._default_shipping_address = default_shipping_address

    @property
    def metadata(self):
        """
        Gets the metadata of this PatchCustomerRequest.

        :return: The metadata of this PatchCustomerRequest.
        :rtype: Tmsv2customersMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this PatchCustomerRequest.

        :param metadata: The metadata of this PatchCustomerRequest.
        :type: Tmsv2customersMetadata
        """

        self._metadata = metadata

    @property
    def embedded(self):
        """
        Gets the embedded of this PatchCustomerRequest.

        :return: The embedded of this PatchCustomerRequest.
        :rtype: Tmsv2customersEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """
        Sets the embedded of this PatchCustomerRequest.

        :param embedded: The embedded of this PatchCustomerRequest.
        :type: Tmsv2customersEmbedded
        """

        self._embedded = embedded

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
        if not isinstance(other, PatchCustomerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
