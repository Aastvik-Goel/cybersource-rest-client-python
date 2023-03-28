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


class InlineResponse20014ResponseRecordAdditionalUpdates(object):
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
        'customer_id': 'str',
        'payment_instrument_id': 'str',
        'creator': 'str',
        'state': 'str',
        'message': 'str'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'payment_instrument_id': 'paymentInstrumentId',
        'creator': 'creator',
        'state': 'state',
        'message': 'message'
    }

    def __init__(self, customer_id=None, payment_instrument_id=None, creator=None, state=None, message=None):
        """
        InlineResponse20014ResponseRecordAdditionalUpdates - a model defined in Swagger
        """

        self._customer_id = None
        self._payment_instrument_id = None
        self._creator = None
        self._state = None
        self._message = None

        if customer_id is not None:
          self.customer_id = customer_id
        if payment_instrument_id is not None:
          self.payment_instrument_id = payment_instrument_id
        if creator is not None:
          self.creator = creator
        if state is not None:
          self.state = state
        if message is not None:
          self.message = message

    @property
    def customer_id(self):
        """
        Gets the customer_id of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :return: The customer_id of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :param customer_id: The customer_id of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :type: str
        """

        self._customer_id = customer_id

    @property
    def payment_instrument_id(self):
        """
        Gets the payment_instrument_id of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :return: The payment_instrument_id of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :rtype: str
        """
        return self._payment_instrument_id

    @payment_instrument_id.setter
    def payment_instrument_id(self, payment_instrument_id):
        """
        Sets the payment_instrument_id of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :param payment_instrument_id: The payment_instrument_id of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :type: str
        """

        self._payment_instrument_id = payment_instrument_id

    @property
    def creator(self):
        """
        Gets the creator of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :return: The creator of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :param creator: The creator of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :type: str
        """

        self._creator = creator

    @property
    def state(self):
        """
        Gets the state of this InlineResponse20014ResponseRecordAdditionalUpdates.
        Valid Values:   * ACTIVE   * CLOSED 

        :return: The state of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this InlineResponse20014ResponseRecordAdditionalUpdates.
        Valid Values:   * ACTIVE   * CLOSED 

        :param state: The state of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :type: str
        """

        self._state = state

    @property
    def message(self):
        """
        Gets the message of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :return: The message of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this InlineResponse20014ResponseRecordAdditionalUpdates.

        :param message: The message of this InlineResponse20014ResponseRecordAdditionalUpdates.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, InlineResponse20014ResponseRecordAdditionalUpdates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
