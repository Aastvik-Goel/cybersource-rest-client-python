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


class PostInstrumentIdentifierRequest(object):
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
        'links': 'TmsEmbeddedInstrumentIdentifierLinks',
        'id': 'str',
        'object': 'str',
        'state': 'str',
        'type': 'str',
        'token_provisioning_information': 'TmsEmbeddedInstrumentIdentifierTokenProvisioningInformation',
        'card': 'TmsEmbeddedInstrumentIdentifierCard',
        'bank_account': 'TmsEmbeddedInstrumentIdentifierBankAccount',
        'tokenized_card': 'TmsEmbeddedInstrumentIdentifierTokenizedCard',
        'issuer': 'TmsEmbeddedInstrumentIdentifierIssuer',
        'processing_information': 'TmsEmbeddedInstrumentIdentifierProcessingInformation',
        'bill_to': 'TmsEmbeddedInstrumentIdentifierBillTo',
        'metadata': 'TmsEmbeddedInstrumentIdentifierMetadata'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'object': 'object',
        'state': 'state',
        'type': 'type',
        'token_provisioning_information': 'tokenProvisioningInformation',
        'card': 'card',
        'bank_account': 'bankAccount',
        'tokenized_card': 'tokenizedCard',
        'issuer': 'issuer',
        'processing_information': 'processingInformation',
        'bill_to': 'billTo',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, id=None, object=None, state=None, type=None, token_provisioning_information=None, card=None, bank_account=None, tokenized_card=None, issuer=None, processing_information=None, bill_to=None, metadata=None):
        """
        PostInstrumentIdentifierRequest - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._object = None
        self._state = None
        self._type = None
        self._token_provisioning_information = None
        self._card = None
        self._bank_account = None
        self._tokenized_card = None
        self._issuer = None
        self._processing_information = None
        self._bill_to = None
        self._metadata = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if object is not None:
          self.object = object
        if state is not None:
          self.state = state
        if type is not None:
          self.type = type
        if token_provisioning_information is not None:
          self.token_provisioning_information = token_provisioning_information
        if card is not None:
          self.card = card
        if bank_account is not None:
          self.bank_account = bank_account
        if tokenized_card is not None:
          self.tokenized_card = tokenized_card
        if issuer is not None:
          self.issuer = issuer
        if processing_information is not None:
          self.processing_information = processing_information
        if bill_to is not None:
          self.bill_to = bill_to
        if metadata is not None:
          self.metadata = metadata

    @property
    def links(self):
        """
        Gets the links of this PostInstrumentIdentifierRequest.

        :return: The links of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PostInstrumentIdentifierRequest.

        :param links: The links of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierLinks
        """



        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PostInstrumentIdentifierRequest.
        The Id of the Instrument Identifier Token. 

        :return: The id of this PostInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PostInstrumentIdentifierRequest.
        The Id of the Instrument Identifier Token. 

        :param id: The id of this PostInstrumentIdentifierRequest.
        :type: str
        """



        self._id = id

    @property
    def object(self):
        """
        Gets the object of this PostInstrumentIdentifierRequest.
        The type.  Possible Values: - instrumentIdentifier 

        :return: The object of this PostInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this PostInstrumentIdentifierRequest.
        The type.  Possible Values: - instrumentIdentifier 

        :param object: The object of this PostInstrumentIdentifierRequest.
        :type: str
        """



        self._object = object

    @property
    def state(self):
        """
        Gets the state of this PostInstrumentIdentifierRequest.
        Issuers state for the card number. Possible Values: - ACTIVE - CLOSED : The account has been closed. 

        :return: The state of this PostInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PostInstrumentIdentifierRequest.
        Issuers state for the card number. Possible Values: - ACTIVE - CLOSED : The account has been closed. 

        :param state: The state of this PostInstrumentIdentifierRequest.
        :type: str
        """



        self._state = state

    @property
    def type(self):
        """
        Gets the type of this PostInstrumentIdentifierRequest.
        The type of Instrument Identifier. Possible Values: - enrollable card 

        :return: The type of this PostInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PostInstrumentIdentifierRequest.
        The type of Instrument Identifier. Possible Values: - enrollable card 

        :param type: The type of this PostInstrumentIdentifierRequest.
        :type: str
        """



        self._type = type

    @property
    def token_provisioning_information(self):
        """
        Gets the token_provisioning_information of this PostInstrumentIdentifierRequest.

        :return: The token_provisioning_information of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierTokenProvisioningInformation
        """
        return self._token_provisioning_information

    @token_provisioning_information.setter
    def token_provisioning_information(self, token_provisioning_information):
        """
        Sets the token_provisioning_information of this PostInstrumentIdentifierRequest.

        :param token_provisioning_information: The token_provisioning_information of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierTokenProvisioningInformation
        """



        self._token_provisioning_information = token_provisioning_information

    @property
    def card(self):
        """
        Gets the card of this PostInstrumentIdentifierRequest.

        :return: The card of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this PostInstrumentIdentifierRequest.

        :param card: The card of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierCard
        """



        self._card = card

    @property
    def bank_account(self):
        """
        Gets the bank_account of this PostInstrumentIdentifierRequest.

        :return: The bank_account of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this PostInstrumentIdentifierRequest.

        :param bank_account: The bank_account of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierBankAccount
        """



        self._bank_account = bank_account

    @property
    def tokenized_card(self):
        """
        Gets the tokenized_card of this PostInstrumentIdentifierRequest.

        :return: The tokenized_card of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierTokenizedCard
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """
        Sets the tokenized_card of this PostInstrumentIdentifierRequest.

        :param tokenized_card: The tokenized_card of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierTokenizedCard
        """



        self._tokenized_card = tokenized_card

    @property
    def issuer(self):
        """
        Gets the issuer of this PostInstrumentIdentifierRequest.

        :return: The issuer of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierIssuer
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this PostInstrumentIdentifierRequest.

        :param issuer: The issuer of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierIssuer
        """



        self._issuer = issuer

    @property
    def processing_information(self):
        """
        Gets the processing_information of this PostInstrumentIdentifierRequest.

        :return: The processing_information of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this PostInstrumentIdentifierRequest.

        :param processing_information: The processing_information of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierProcessingInformation
        """



        self._processing_information = processing_information

    @property
    def bill_to(self):
        """
        Gets the bill_to of this PostInstrumentIdentifierRequest.

        :return: The bill_to of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this PostInstrumentIdentifierRequest.

        :param bill_to: The bill_to of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierBillTo
        """



        self._bill_to = bill_to

    @property
    def metadata(self):
        """
        Gets the metadata of this PostInstrumentIdentifierRequest.

        :return: The metadata of this PostInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this PostInstrumentIdentifierRequest.

        :param metadata: The metadata of this PostInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierMetadata
        """



        self._metadata = metadata

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
        if not isinstance(other, PostInstrumentIdentifierRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
