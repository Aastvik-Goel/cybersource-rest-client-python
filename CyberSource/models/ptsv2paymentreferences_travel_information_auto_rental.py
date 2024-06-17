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


class Ptsv2paymentreferencesTravelInformationAutoRental(object):
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
        'company_name': 'str',
        'affiliate_name': 'str',
        'rental_address': 'Ptsv2paymentsTravelInformationAutoRentalRentalAddress',
        'return_address': 'Ptsv2paymentsTravelInformationAutoRentalReturnAddress',
        'return_date_time': 'str',
        'rental_date_time': 'str',
        'customer_name': 'str'
    }

    attribute_map = {
        'company_name': 'companyName',
        'affiliate_name': 'affiliateName',
        'rental_address': 'rentalAddress',
        'return_address': 'returnAddress',
        'return_date_time': 'returnDateTime',
        'rental_date_time': 'rentalDateTime',
        'customer_name': 'customerName'
    }

    def __init__(self, company_name=None, affiliate_name=None, rental_address=None, return_address=None, return_date_time=None, rental_date_time=None, customer_name=None):
        """
        Ptsv2paymentreferencesTravelInformationAutoRental - a model defined in Swagger
        """

        self._company_name = None
        self._affiliate_name = None
        self._rental_address = None
        self._return_address = None
        self._return_date_time = None
        self._rental_date_time = None
        self._customer_name = None

        if company_name is not None:
          self.company_name = company_name
        if affiliate_name is not None:
          self.affiliate_name = affiliate_name
        if rental_address is not None:
          self.rental_address = rental_address
        if return_address is not None:
          self.return_address = return_address
        if return_date_time is not None:
          self.return_date_time = return_date_time
        if rental_date_time is not None:
          self.rental_date_time = rental_date_time
        if customer_name is not None:
          self.customer_name = customer_name

    @property
    def company_name(self):
        """
        Gets the company_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Merchant to send their auto rental company name 

        :return: The company_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Merchant to send their auto rental company name 

        :param company_name: The company_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :type: str
        """



        self._company_name = company_name

    @property
    def affiliate_name(self):
        """
        Gets the affiliate_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        When merchant wants to send the affiliate name. 

        :return: The affiliate_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :rtype: str
        """
        return self._affiliate_name

    @affiliate_name.setter
    def affiliate_name(self, affiliate_name):
        """
        Sets the affiliate_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        When merchant wants to send the affiliate name. 

        :param affiliate_name: The affiliate_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :type: str
        """



        self._affiliate_name = affiliate_name

    @property
    def rental_address(self):
        """
        Gets the rental_address of this Ptsv2paymentreferencesTravelInformationAutoRental.

        :return: The rental_address of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :rtype: Ptsv2paymentsTravelInformationAutoRentalRentalAddress
        """
        return self._rental_address

    @rental_address.setter
    def rental_address(self, rental_address):
        """
        Sets the rental_address of this Ptsv2paymentreferencesTravelInformationAutoRental.

        :param rental_address: The rental_address of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :type: Ptsv2paymentsTravelInformationAutoRentalRentalAddress
        """



        self._rental_address = rental_address

    @property
    def return_address(self):
        """
        Gets the return_address of this Ptsv2paymentreferencesTravelInformationAutoRental.

        :return: The return_address of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :rtype: Ptsv2paymentsTravelInformationAutoRentalReturnAddress
        """
        return self._return_address

    @return_address.setter
    def return_address(self, return_address):
        """
        Sets the return_address of this Ptsv2paymentreferencesTravelInformationAutoRental.

        :param return_address: The return_address of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :type: Ptsv2paymentsTravelInformationAutoRentalReturnAddress
        """



        self._return_address = return_address

    @property
    def return_date_time(self):
        """
        Gets the return_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Date/time the auto was returned to the rental agency. Format: ``yyyy-MM-dd HH-mm-ss z`` This field is supported for Visa, MasterCard, and American Express. 

        :return: The return_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :rtype: str
        """
        return self._return_date_time

    @return_date_time.setter
    def return_date_time(self, return_date_time):
        """
        Sets the return_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Date/time the auto was returned to the rental agency. Format: ``yyyy-MM-dd HH-mm-ss z`` This field is supported for Visa, MasterCard, and American Express. 

        :param return_date_time: The return_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :type: str
        """



        self._return_date_time = return_date_time

    @property
    def rental_date_time(self):
        """
        Gets the rental_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Date/time the auto was picked up from the rental agency. Format: `yyyy-MM-dd HH-mm-ss z` This field is supported for Visa, MasterCard, and American Express. 

        :return: The rental_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :rtype: str
        """
        return self._rental_date_time

    @rental_date_time.setter
    def rental_date_time(self, rental_date_time):
        """
        Sets the rental_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Date/time the auto was picked up from the rental agency. Format: `yyyy-MM-dd HH-mm-ss z` This field is supported for Visa, MasterCard, and American Express. 

        :param rental_date_time: The rental_date_time of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :type: str
        """



        self._rental_date_time = rental_date_time

    @property
    def customer_name(self):
        """
        Gets the customer_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Name of the individual making the rental agreement.  Valid data lengths by card:  |Card Specific Validation|VISA|MasterCard|Discover|AMEX| |--- |--- |--- |--- | | Filed Length| 40| 40| 29| 26| | Field Type| AN| ANS| AN| AN| | M/O/C| O| M| M| M| 

        :return: The customer_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """
        Sets the customer_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        Name of the individual making the rental agreement.  Valid data lengths by card:  |Card Specific Validation|VISA|MasterCard|Discover|AMEX| |--- |--- |--- |--- | | Filed Length| 40| 40| 29| 26| | Field Type| AN| ANS| AN| AN| | M/O/C| O| M| M| M| 

        :param customer_name: The customer_name of this Ptsv2paymentreferencesTravelInformationAutoRental.
        :type: str
        """



        self._customer_name = customer_name

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
        if not isinstance(other, Ptsv2paymentreferencesTravelInformationAutoRental):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
