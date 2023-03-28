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


class Tmsv2customersEmbeddedDefaultPaymentInstrument(object):
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
        'links': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentLinks',
        'id': 'str',
        'object': 'str',
        'default': 'bool',
        'state': 'str',
        'type': 'str',
        'bank_account': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentBankAccount',
        'card': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentCard',
        'buyer_information': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformation',
        'bill_to': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo',
        'processing_information': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformation',
        'merchant_information': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentMerchantInformation',
        'instrument_identifier': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentInstrumentIdentifier',
        'metadata': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentMetadata',
        'embedded': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbedded'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'object': 'object',
        'default': 'default',
        'state': 'state',
        'type': 'type',
        'bank_account': 'bankAccount',
        'card': 'card',
        'buyer_information': 'buyerInformation',
        'bill_to': 'billTo',
        'processing_information': 'processingInformation',
        'merchant_information': 'merchantInformation',
        'instrument_identifier': 'instrumentIdentifier',
        'metadata': 'metadata',
        'embedded': '_embedded'
    }

    def __init__(self, links=None, id=None, object=None, default=None, state=None, type=None, bank_account=None, card=None, buyer_information=None, bill_to=None, processing_information=None, merchant_information=None, instrument_identifier=None, metadata=None, embedded=None):
        """
        Tmsv2customersEmbeddedDefaultPaymentInstrument - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._object = None
        self._default = None
        self._state = None
        self._type = None
        self._bank_account = None
        self._card = None
        self._buyer_information = None
        self._bill_to = None
        self._processing_information = None
        self._merchant_information = None
        self._instrument_identifier = None
        self._metadata = None
        self._embedded = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if object is not None:
          self.object = object
        if default is not None:
          self.default = default
        if state is not None:
          self.state = state
        if type is not None:
          self.type = type
        if bank_account is not None:
          self.bank_account = bank_account
        if card is not None:
          self.card = card
        if buyer_information is not None:
          self.buyer_information = buyer_information
        if bill_to is not None:
          self.bill_to = bill_to
        if processing_information is not None:
          self.processing_information = processing_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier
        if metadata is not None:
          self.metadata = metadata
        if embedded is not None:
          self.embedded = embedded

    @property
    def links(self):
        """
        Gets the links of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The links of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param links: The links of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        The Id of the Payment Instrument Token.

        :return: The id of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        The Id of the Payment Instrument Token.

        :param id: The id of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """
        Gets the object of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        The type.  Possible Values: - paymentInstrument 

        :return: The object of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        The type.  Possible Values: - paymentInstrument 

        :param object: The object of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: str
        """

        self._object = object

    @property
    def default(self):
        """
        Gets the default of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        Flag that indicates whether customer payment instrument is the dafault. Possible Values:  - `true`: Payment instrument is customer's default.  - `false`: Payment instrument is not customer's default. 

        :return: The default of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        Flag that indicates whether customer payment instrument is the dafault. Possible Values:  - `true`: Payment instrument is customer's default.  - `false`: Payment instrument is not customer's default. 

        :param default: The default of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: bool
        """

        self._default = default

    @property
    def state(self):
        """
        Gets the state of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        Issuers state for the card number. Possible Values: - ACTIVE - CLOSED : The account has been closed. 

        :return: The state of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        Issuers state for the card number. Possible Values: - ACTIVE - CLOSED : The account has been closed. 

        :param state: The state of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: str
        """

        self._state = state

    @property
    def type(self):
        """
        Gets the type of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        The type of Payment Instrument. Possible Values: - cardHash 

        :return: The type of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        The type of Payment Instrument. Possible Values: - cardHash 

        :param type: The type of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: str
        """

        self._type = type

    @property
    def bank_account(self):
        """
        Gets the bank_account of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The bank_account of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param bank_account: The bank_account of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentBankAccount
        """

        self._bank_account = bank_account

    @property
    def card(self):
        """
        Gets the card of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The card of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param card: The card of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentCard
        """

        self._card = card

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The buyer_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param buyer_information: The buyer_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentBuyerInformation
        """

        self._buyer_information = buyer_information

    @property
    def bill_to(self):
        """
        Gets the bill_to of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The bill_to of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param bill_to: The bill_to of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentBillTo
        """

        self._bill_to = bill_to

    @property
    def processing_information(self):
        """
        Gets the processing_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The processing_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param processing_information: The processing_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The merchant_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param merchant_information: The merchant_information of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The instrument_identifier of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentInstrumentIdentifier
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param instrument_identifier: The instrument_identifier of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentInstrumentIdentifier
        """

        self._instrument_identifier = instrument_identifier

    @property
    def metadata(self):
        """
        Gets the metadata of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The metadata of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param metadata: The metadata of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentMetadata
        """

        self._metadata = metadata

    @property
    def embedded(self):
        """
        Gets the embedded of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :return: The embedded of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """
        Sets the embedded of this Tmsv2customersEmbeddedDefaultPaymentInstrument.

        :param embedded: The embedded of this Tmsv2customersEmbeddedDefaultPaymentInstrument.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbedded
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
        if not isinstance(other, Tmsv2customersEmbeddedDefaultPaymentInstrument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
