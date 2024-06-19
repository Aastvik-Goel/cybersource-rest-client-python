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


class InlineResponse202(object):
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
        'links': 'InlineResponse202Links',
        'batch_id': 'str',
        'batch_item_count': 'int'
    }

    attribute_map = {
        'links': '_links',
        'batch_id': 'batchId',
        'batch_item_count': 'batchItemCount'
    }

    def __init__(self, links=None, batch_id=None, batch_item_count=None):
        """
        InlineResponse202 - a model defined in Swagger
        """

        self._links = None
        self._batch_id = None
        self._batch_item_count = None

        if links is not None:
          self.links = links
        if batch_id is not None:
          self.batch_id = batch_id
        if batch_item_count is not None:
          self.batch_item_count = batch_item_count

    @property
    def links(self):
        """
        Gets the links of this InlineResponse202.

        :return: The links of this InlineResponse202.
        :rtype: InlineResponse202Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this InlineResponse202.

        :param links: The links of this InlineResponse202.
        :type: InlineResponse202Links
        """

        self._links = links

    @property
    def batch_id(self):
        """
        Gets the batch_id of this InlineResponse202.
        Unique identification number assigned to the submitted request.

        :return: The batch_id of this InlineResponse202.
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """
        Sets the batch_id of this InlineResponse202.
        Unique identification number assigned to the submitted request.

        :param batch_id: The batch_id of this InlineResponse202.
        :type: str
        """

        self._batch_id = batch_id

    @property
    def batch_item_count(self):
        """
        Gets the batch_item_count of this InlineResponse202.

        :return: The batch_item_count of this InlineResponse202.
        :rtype: int
        """
        return self._batch_item_count

    @batch_item_count.setter
    def batch_item_count(self, batch_item_count):
        """
        Sets the batch_item_count of this InlineResponse202.

        :param batch_item_count: The batch_item_count of this InlineResponse202.
        :type: int
        """

        self._batch_item_count = batch_item_count

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
        if not isinstance(other, InlineResponse202):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
