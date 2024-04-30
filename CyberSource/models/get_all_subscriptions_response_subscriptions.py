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


class GetAllSubscriptionsResponseSubscriptions(object):
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
        'links': 'GetAllSubscriptionsResponseLinks',
        'id': 'str',
        'plan_information': 'GetAllSubscriptionsResponsePlanInformation',
        'subscription_information': 'GetAllSubscriptionsResponseSubscriptionInformation',
        'payment_information': 'GetAllSubscriptionsResponsePaymentInformation',
        'order_information': 'GetAllSubscriptionsResponseOrderInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'plan_information': 'planInformation',
        'subscription_information': 'subscriptionInformation',
        'payment_information': 'paymentInformation',
        'order_information': 'orderInformation'
    }

    def __init__(self, links=None, id=None, plan_information=None, subscription_information=None, payment_information=None, order_information=None):
        """
        GetAllSubscriptionsResponseSubscriptions - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._plan_information = None
        self._subscription_information = None
        self._payment_information = None
        self._order_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if plan_information is not None:
          self.plan_information = plan_information
        if subscription_information is not None:
          self.subscription_information = subscription_information
        if payment_information is not None:
          self.payment_information = payment_information
        if order_information is not None:
          self.order_information = order_information

    @property
    def links(self):
        """
        Gets the links of this GetAllSubscriptionsResponseSubscriptions.

        :return: The links of this GetAllSubscriptionsResponseSubscriptions.
        :rtype: GetAllSubscriptionsResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this GetAllSubscriptionsResponseSubscriptions.

        :param links: The links of this GetAllSubscriptionsResponseSubscriptions.
        :type: GetAllSubscriptionsResponseLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this GetAllSubscriptionsResponseSubscriptions.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this GetAllSubscriptionsResponseSubscriptions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GetAllSubscriptionsResponseSubscriptions.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this GetAllSubscriptionsResponseSubscriptions.
        :type: str
        """

        self._id = id

    @property
    def plan_information(self):
        """
        Gets the plan_information of this GetAllSubscriptionsResponseSubscriptions.

        :return: The plan_information of this GetAllSubscriptionsResponseSubscriptions.
        :rtype: GetAllSubscriptionsResponsePlanInformation
        """
        return self._plan_information

    @plan_information.setter
    def plan_information(self, plan_information):
        """
        Sets the plan_information of this GetAllSubscriptionsResponseSubscriptions.

        :param plan_information: The plan_information of this GetAllSubscriptionsResponseSubscriptions.
        :type: GetAllSubscriptionsResponsePlanInformation
        """

        self._plan_information = plan_information

    @property
    def subscription_information(self):
        """
        Gets the subscription_information of this GetAllSubscriptionsResponseSubscriptions.

        :return: The subscription_information of this GetAllSubscriptionsResponseSubscriptions.
        :rtype: GetAllSubscriptionsResponseSubscriptionInformation
        """
        return self._subscription_information

    @subscription_information.setter
    def subscription_information(self, subscription_information):
        """
        Sets the subscription_information of this GetAllSubscriptionsResponseSubscriptions.

        :param subscription_information: The subscription_information of this GetAllSubscriptionsResponseSubscriptions.
        :type: GetAllSubscriptionsResponseSubscriptionInformation
        """

        self._subscription_information = subscription_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this GetAllSubscriptionsResponseSubscriptions.

        :return: The payment_information of this GetAllSubscriptionsResponseSubscriptions.
        :rtype: GetAllSubscriptionsResponsePaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this GetAllSubscriptionsResponseSubscriptions.

        :param payment_information: The payment_information of this GetAllSubscriptionsResponseSubscriptions.
        :type: GetAllSubscriptionsResponsePaymentInformation
        """

        self._payment_information = payment_information

    @property
    def order_information(self):
        """
        Gets the order_information of this GetAllSubscriptionsResponseSubscriptions.

        :return: The order_information of this GetAllSubscriptionsResponseSubscriptions.
        :rtype: GetAllSubscriptionsResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this GetAllSubscriptionsResponseSubscriptions.

        :param order_information: The order_information of this GetAllSubscriptionsResponseSubscriptions.
        :type: GetAllSubscriptionsResponseOrderInformation
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
        if not isinstance(other, GetAllSubscriptionsResponseSubscriptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
