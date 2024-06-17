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


class GetPlanResponse(object):
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
        'links': 'PtsV2IncrementalAuthorizationPatch201ResponseLinks',
        'id': 'str',
        'submit_time_utc': 'str',
        'plan_information': 'GetAllPlansResponsePlanInformation',
        'order_information': 'GetAllPlansResponseOrderInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'plan_information': 'planInformation',
        'order_information': 'orderInformation'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, plan_information=None, order_information=None):
        """
        GetPlanResponse - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._plan_information = None
        self._order_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if plan_information is not None:
          self.plan_information = plan_information
        if order_information is not None:
          self.order_information = order_information

    @property
    def links(self):
        """
        Gets the links of this GetPlanResponse.

        :return: The links of this GetPlanResponse.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this GetPlanResponse.

        :param links: The links of this GetPlanResponse.
        :type: PtsV2IncrementalAuthorizationPatch201ResponseLinks
        """



        self._links = links

    @property
    def id(self):
        """
        Gets the id of this GetPlanResponse.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this GetPlanResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetPlanResponse.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this GetPlanResponse.
        :type: str
        """



        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this GetPlanResponse.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this GetPlanResponse.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this GetPlanResponse.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this GetPlanResponse.
        :type: str
        """



        self._submit_time_utc = submit_time_utc

    @property
    def plan_information(self):
        """
        Gets the plan_information of this GetPlanResponse.

        :return: The plan_information of this GetPlanResponse.
        :rtype: GetAllPlansResponsePlanInformation
        """
        return self._plan_information

    @plan_information.setter
    def plan_information(self, plan_information):
        """
        Sets the plan_information of this GetPlanResponse.

        :param plan_information: The plan_information of this GetPlanResponse.
        :type: GetAllPlansResponsePlanInformation
        """



        self._plan_information = plan_information

    @property
    def order_information(self):
        """
        Gets the order_information of this GetPlanResponse.

        :return: The order_information of this GetPlanResponse.
        :rtype: GetAllPlansResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this GetPlanResponse.

        :param order_information: The order_information of this GetPlanResponse.
        :type: GetAllPlansResponseOrderInformation
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
        if not isinstance(other, GetPlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
