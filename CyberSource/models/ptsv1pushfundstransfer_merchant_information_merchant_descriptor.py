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


class Ptsv1pushfundstransferMerchantInformationMerchantDescriptor(object):
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
        'administrative_area': 'str',
        'contact': 'str',
        'country': 'str',
        'locality': 'str',
        'name': 'str',
        'store_id': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'administrative_area': 'administrativeArea',
        'contact': 'contact',
        'country': 'country',
        'locality': 'locality',
        'name': 'name',
        'store_id': 'storeId',
        'postal_code': 'postalCode'
    }

    def __init__(self, administrative_area=None, contact=None, country=None, locality=None, name=None, store_id=None, postal_code=None):
        """
        Ptsv1pushfundstransferMerchantInformationMerchantDescriptor - a model defined in Swagger
        """

        self._administrative_area = None
        self._contact = None
        self._country = None
        self._locality = None
        self._name = None
        self._store_id = None
        self._postal_code = None

        if administrative_area is not None:
          self.administrative_area = administrative_area
        if contact is not None:
          self.contact = contact
        if country is not None:
          self.country = country
        if locality is not None:
          self.locality = locality
        if name is not None:
          self.name = name
        if store_id is not None:
          self.store_id = store_id
        if postal_code is not None:
          self.postal_code = postal_code

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        The state where the merchant is located.  See https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf  Note This field is supported only for businesses located in the U.S. or Canada. 

        :return: The administrative_area of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        The state where the merchant is located.  See https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf  Note This field is supported only for businesses located in the U.S. or Canada. 

        :param administrative_area: The administrative_area of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._administrative_area = administrative_area

    @property
    def contact(self):
        """
        Gets the contact of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see merchant_descriptor_contact field description in Credit Card Services Using the SCMP API.--> Contact information for the merchant.  Note These are the maximum data lengths for the following payment processors:  FDC Compass (13) Chase Paymentech (13). 

        :return: The contact of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see merchant_descriptor_contact field description in Credit Card Services Using the SCMP API.--> Contact information for the merchant.  Note These are the maximum data lengths for the following payment processors:  FDC Compass (13) Chase Paymentech (13). 

        :param contact: The contact of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._contact = contact

    @property
    def country(self):
        """
        Gets the country of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's country.  Country code for your business location. Use the ISO Standard Alpha Country Codes This value might be displayed on the cardholder's statement.  See https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf  Note If your business is located in the U.S. or Canada and you include this field in a request, you must also include merchantInformation.merchantDescriptor.administrativeArea. 

        :return: The country of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's country.  Country code for your business location. Use the ISO Standard Alpha Country Codes This value might be displayed on the cardholder's statement.  See https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf  Note If your business is located in the U.S. or Canada and you include this field in a request, you must also include merchantInformation.merchantDescriptor.administrativeArea. 

        :param country: The country of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._country = country

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's City.  City for your business location. This value might be displayed on the cardholder's statement. 

        :return: The locality of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's City.  City for your business location. This value might be displayed on the cardholder's statement. 

        :param locality: The locality of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._locality = locality

    @property
    def name(self):
        """
        Gets the name of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's business name. This name is displayed on the cardholder's statement.  Chase Paymentech, Visa Platform Connect: length 22 

        :return: The name of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's business name. This name is displayed on the cardholder's statement.  Chase Paymentech, Visa Platform Connect: length 22 

        :param name: The name of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._name = name

    @property
    def store_id(self):
        """
        Gets the store_id of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        The unique id of the merchant's shop which assigned by the merchant. 

        :return: The store_id of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """
        Sets the store_id of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        The unique id of the merchant's shop which assigned by the merchant. 

        :param store_id: The store_id of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._store_id = store_id

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's postal code. This value might be displayed on the cardholder's statement.  If your business is domiciled in the U.S., you can use a 5-digit or 9-digit postal code. A 9-digit postal code must follow this format: [5 digits][dash][4 digits] Example: 12345-6789  If your business is domiciled in Canada, you can use a 6-digit or 9-digit postal code. A 6-digit postal code must follow this format: [alpha][numeric][alpha][space] [numeric][alpha][numeric] Example: A1B 2C3 

        :return: The postal_code of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        Merchant's postal code. This value might be displayed on the cardholder's statement.  If your business is domiciled in the U.S., you can use a 5-digit or 9-digit postal code. A 9-digit postal code must follow this format: [5 digits][dash][4 digits] Example: 12345-6789  If your business is domiciled in Canada, you can use a 6-digit or 9-digit postal code. A 6-digit postal code must follow this format: [alpha][numeric][alpha][space] [numeric][alpha][numeric] Example: A1B 2C3 

        :param postal_code: The postal_code of this Ptsv1pushfundstransferMerchantInformationMerchantDescriptor.
        :type: str
        """



        self._postal_code = postal_code

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
        if not isinstance(other, Ptsv1pushfundstransferMerchantInformationMerchantDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
