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


class Boardingv1registrationsOrganizationInformationKYC(object):
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
        'when_is_customer_charged': 'str',
        'when_is_customer_charged_description': 'str',
        'offer_subscriptions': 'bool',
        'monthly_subscription_percent': 'float',
        'quarterly_subscription_percent': 'float',
        'semi_annual_subscription_percent': 'float',
        'annual_subscription_percent': 'float',
        'time_to_product_delivery': 'str',
        'estimated_monthly_sales': 'float',
        'average_order_amount': 'float',
        'largest_expected_order_amount': 'float',
        'deposit_bank_account': 'Boardingv1registrationsOrganizationInformationKYCDepositBankAccount'
    }

    attribute_map = {
        'when_is_customer_charged': 'whenIsCustomerCharged',
        'when_is_customer_charged_description': 'whenIsCustomerChargedDescription',
        'offer_subscriptions': 'offerSubscriptions',
        'monthly_subscription_percent': 'monthlySubscriptionPercent',
        'quarterly_subscription_percent': 'quarterlySubscriptionPercent',
        'semi_annual_subscription_percent': 'semiAnnualSubscriptionPercent',
        'annual_subscription_percent': 'annualSubscriptionPercent',
        'time_to_product_delivery': 'timeToProductDelivery',
        'estimated_monthly_sales': 'estimatedMonthlySales',
        'average_order_amount': 'averageOrderAmount',
        'largest_expected_order_amount': 'largestExpectedOrderAmount',
        'deposit_bank_account': 'depositBankAccount'
    }

    def __init__(self, when_is_customer_charged=None, when_is_customer_charged_description=None, offer_subscriptions=None, monthly_subscription_percent=None, quarterly_subscription_percent=None, semi_annual_subscription_percent=None, annual_subscription_percent=None, time_to_product_delivery=None, estimated_monthly_sales=None, average_order_amount=None, largest_expected_order_amount=None, deposit_bank_account=None):
        """
        Boardingv1registrationsOrganizationInformationKYC - a model defined in Swagger
        """

        self._when_is_customer_charged = None
        self._when_is_customer_charged_description = None
        self._offer_subscriptions = None
        self._monthly_subscription_percent = None
        self._quarterly_subscription_percent = None
        self._semi_annual_subscription_percent = None
        self._annual_subscription_percent = None
        self._time_to_product_delivery = None
        self._estimated_monthly_sales = None
        self._average_order_amount = None
        self._largest_expected_order_amount = None
        self._deposit_bank_account = None

        self.when_is_customer_charged = when_is_customer_charged
        if when_is_customer_charged_description is not None:
          self.when_is_customer_charged_description = when_is_customer_charged_description
        self.offer_subscriptions = offer_subscriptions
        if monthly_subscription_percent is not None:
          self.monthly_subscription_percent = monthly_subscription_percent
        if quarterly_subscription_percent is not None:
          self.quarterly_subscription_percent = quarterly_subscription_percent
        if semi_annual_subscription_percent is not None:
          self.semi_annual_subscription_percent = semi_annual_subscription_percent
        if annual_subscription_percent is not None:
          self.annual_subscription_percent = annual_subscription_percent
        self.time_to_product_delivery = time_to_product_delivery
        self.estimated_monthly_sales = estimated_monthly_sales
        self.average_order_amount = average_order_amount
        self.largest_expected_order_amount = largest_expected_order_amount
        if deposit_bank_account is not None:
          self.deposit_bank_account = deposit_bank_account

    @property
    def when_is_customer_charged(self):
        """
        Gets the when_is_customer_charged of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The when_is_customer_charged of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: str
        """
        return self._when_is_customer_charged

    @when_is_customer_charged.setter
    def when_is_customer_charged(self, when_is_customer_charged):
        """
        Sets the when_is_customer_charged of this Boardingv1registrationsOrganizationInformationKYC.

        :param when_is_customer_charged: The when_is_customer_charged of this Boardingv1registrationsOrganizationInformationKYC.
        :type: str
        """
        allowed_values = ["ONETIMEBEFORE", "ONETIMEAFTER", "OTHER"]
        if when_is_customer_charged not in allowed_values:
            raise ValueError(
                "Invalid value for `when_is_customer_charged` ({0}), must be one of {1}"
                .format(when_is_customer_charged, allowed_values)
            )

        self._when_is_customer_charged = when_is_customer_charged

    @property
    def when_is_customer_charged_description(self):
        """
        Gets the when_is_customer_charged_description of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The when_is_customer_charged_description of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: str
        """
        return self._when_is_customer_charged_description

    @when_is_customer_charged_description.setter
    def when_is_customer_charged_description(self, when_is_customer_charged_description):
        """
        Sets the when_is_customer_charged_description of this Boardingv1registrationsOrganizationInformationKYC.

        :param when_is_customer_charged_description: The when_is_customer_charged_description of this Boardingv1registrationsOrganizationInformationKYC.
        :type: str
        """

        self._when_is_customer_charged_description = when_is_customer_charged_description

    @property
    def offer_subscriptions(self):
        """
        Gets the offer_subscriptions of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The offer_subscriptions of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: bool
        """
        return self._offer_subscriptions

    @offer_subscriptions.setter
    def offer_subscriptions(self, offer_subscriptions):
        """
        Sets the offer_subscriptions of this Boardingv1registrationsOrganizationInformationKYC.

        :param offer_subscriptions: The offer_subscriptions of this Boardingv1registrationsOrganizationInformationKYC.
        :type: bool
        """

        self._offer_subscriptions = offer_subscriptions

    @property
    def monthly_subscription_percent(self):
        """
        Gets the monthly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The monthly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: float
        """
        return self._monthly_subscription_percent

    @monthly_subscription_percent.setter
    def monthly_subscription_percent(self, monthly_subscription_percent):
        """
        Sets the monthly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :param monthly_subscription_percent: The monthly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :type: float
        """

        self._monthly_subscription_percent = monthly_subscription_percent

    @property
    def quarterly_subscription_percent(self):
        """
        Gets the quarterly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The quarterly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: float
        """
        return self._quarterly_subscription_percent

    @quarterly_subscription_percent.setter
    def quarterly_subscription_percent(self, quarterly_subscription_percent):
        """
        Sets the quarterly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :param quarterly_subscription_percent: The quarterly_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :type: float
        """

        self._quarterly_subscription_percent = quarterly_subscription_percent

    @property
    def semi_annual_subscription_percent(self):
        """
        Gets the semi_annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The semi_annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: float
        """
        return self._semi_annual_subscription_percent

    @semi_annual_subscription_percent.setter
    def semi_annual_subscription_percent(self, semi_annual_subscription_percent):
        """
        Sets the semi_annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :param semi_annual_subscription_percent: The semi_annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :type: float
        """

        self._semi_annual_subscription_percent = semi_annual_subscription_percent

    @property
    def annual_subscription_percent(self):
        """
        Gets the annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: float
        """
        return self._annual_subscription_percent

    @annual_subscription_percent.setter
    def annual_subscription_percent(self, annual_subscription_percent):
        """
        Sets the annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.

        :param annual_subscription_percent: The annual_subscription_percent of this Boardingv1registrationsOrganizationInformationKYC.
        :type: float
        """

        self._annual_subscription_percent = annual_subscription_percent

    @property
    def time_to_product_delivery(self):
        """
        Gets the time_to_product_delivery of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The time_to_product_delivery of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: str
        """
        return self._time_to_product_delivery

    @time_to_product_delivery.setter
    def time_to_product_delivery(self, time_to_product_delivery):
        """
        Sets the time_to_product_delivery of this Boardingv1registrationsOrganizationInformationKYC.

        :param time_to_product_delivery: The time_to_product_delivery of this Boardingv1registrationsOrganizationInformationKYC.
        :type: str
        """
        allowed_values = ["INSTANT", "UPTO2", "UPTO5", "UPTO10", "GREATERTHAN10"]
        if time_to_product_delivery not in allowed_values:
            raise ValueError(
                "Invalid value for `time_to_product_delivery` ({0}), must be one of {1}"
                .format(time_to_product_delivery, allowed_values)
            )

        self._time_to_product_delivery = time_to_product_delivery

    @property
    def estimated_monthly_sales(self):
        """
        Gets the estimated_monthly_sales of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The estimated_monthly_sales of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: float
        """
        return self._estimated_monthly_sales

    @estimated_monthly_sales.setter
    def estimated_monthly_sales(self, estimated_monthly_sales):
        """
        Sets the estimated_monthly_sales of this Boardingv1registrationsOrganizationInformationKYC.

        :param estimated_monthly_sales: The estimated_monthly_sales of this Boardingv1registrationsOrganizationInformationKYC.
        :type: float
        """

        self._estimated_monthly_sales = estimated_monthly_sales

    @property
    def average_order_amount(self):
        """
        Gets the average_order_amount of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The average_order_amount of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: float
        """
        return self._average_order_amount

    @average_order_amount.setter
    def average_order_amount(self, average_order_amount):
        """
        Sets the average_order_amount of this Boardingv1registrationsOrganizationInformationKYC.

        :param average_order_amount: The average_order_amount of this Boardingv1registrationsOrganizationInformationKYC.
        :type: float
        """

        self._average_order_amount = average_order_amount

    @property
    def largest_expected_order_amount(self):
        """
        Gets the largest_expected_order_amount of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The largest_expected_order_amount of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: float
        """
        return self._largest_expected_order_amount

    @largest_expected_order_amount.setter
    def largest_expected_order_amount(self, largest_expected_order_amount):
        """
        Sets the largest_expected_order_amount of this Boardingv1registrationsOrganizationInformationKYC.

        :param largest_expected_order_amount: The largest_expected_order_amount of this Boardingv1registrationsOrganizationInformationKYC.
        :type: float
        """

        self._largest_expected_order_amount = largest_expected_order_amount

    @property
    def deposit_bank_account(self):
        """
        Gets the deposit_bank_account of this Boardingv1registrationsOrganizationInformationKYC.

        :return: The deposit_bank_account of this Boardingv1registrationsOrganizationInformationKYC.
        :rtype: Boardingv1registrationsOrganizationInformationKYCDepositBankAccount
        """
        return self._deposit_bank_account

    @deposit_bank_account.setter
    def deposit_bank_account(self, deposit_bank_account):
        """
        Sets the deposit_bank_account of this Boardingv1registrationsOrganizationInformationKYC.

        :param deposit_bank_account: The deposit_bank_account of this Boardingv1registrationsOrganizationInformationKYC.
        :type: Boardingv1registrationsOrganizationInformationKYCDepositBankAccount
        """

        self._deposit_bank_account = deposit_bank_account

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
        if not isinstance(other, Boardingv1registrationsOrganizationInformationKYC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
