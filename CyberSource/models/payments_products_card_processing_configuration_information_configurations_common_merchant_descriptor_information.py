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


class PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation(object):
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
        'name': 'str',
        'city': 'str',
        'country': 'str',
        'phone': 'str',
        'state': 'str',
        'street': 'str',
        'zip': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'city': 'city',
        'country': 'country',
        'phone': 'phone',
        'state': 'state',
        'street': 'street',
        'zip': 'zip',
        'url': 'url'
    }

    def __init__(self, name=None, city=None, country=None, phone=None, state=None, street=None, zip=None, url=None):
        """
        PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation - a model defined in Swagger
        """

        self._name = None
        self._city = None
        self._country = None
        self._phone = None
        self._state = None
        self._street = None
        self._zip = None
        self._url = None

        if name is not None:
          self.name = name
        if city is not None:
          self.city = city
        if country is not None:
          self.country = country
        if phone is not None:
          self.phone = phone
        if state is not None:
          self.state = state
        if street is not None:
          self.street = street
        if zip is not None:
          self.zip = zip
        if url is not None:
          self.url = url

    @property
    def name(self):
        """
        Gets the name of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for TSYS (tsys), RUPAY, American Express Direct (amexdirect) and Elavon Americas (elavonamericas) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>38</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :return: The name of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for TSYS (tsys), RUPAY, American Express Direct (amexdirect) and Elavon Americas (elavonamericas) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>38</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :param name: The name of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._name = name

    @property
    def city(self):
        """
        Gets the city of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for American Express Direct (amexdirect), TSYS (tsys), RUPAY and Elavon Americas (elavonamericas) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>21</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :return: The city of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for American Express Direct (amexdirect), TSYS (tsys), RUPAY and Elavon Americas (elavonamericas) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>21</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :param city: The city of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """
        Gets the country of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for Six (six), Elavon Americas (elavonamericas), TSYS (tsys) and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>3</td><td>3</td><td>^[A-Z]+$</td></tr> </table> 

        :return: The country of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for Six (six), Elavon Americas (elavonamericas), TSYS (tsys) and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>3</td><td>3</td><td>^[A-Z]+$</td></tr> </table> 

        :param country: The country of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """
        Gets the phone of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for RUPAY, Elavon Americas (elavonamericas), American Express Direct (amexdirect) and TSYS (tsys) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>20</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :return: The phone of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for RUPAY, Elavon Americas (elavonamericas), American Express Direct (amexdirect) and TSYS (tsys) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>20</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :param phone: The phone of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._phone = phone

    @property
    def state(self):
        """
        Gets the state of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for RUPAY, TSYS (tsys), Elavon Americas (elavonamericas) and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>No</td><td>1</td><td>3</td><td>^[A-Z]+$</td></tr> </table> 

        :return: The state of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for RUPAY, TSYS (tsys), Elavon Americas (elavonamericas) and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>No</td><td>1</td><td>3</td><td>^[A-Z]+$</td></tr> </table> 

        :param state: The state of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._state = state

    @property
    def street(self):
        """
        Gets the street of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for American Express Direct (amexdirect), TSYS (tsys) and Elavon Americas (elavonamericas) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>38</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :return: The street of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for American Express Direct (amexdirect), TSYS (tsys) and Elavon Americas (elavonamericas) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>38</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :param street: The street of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._street = street

    @property
    def zip(self):
        """
        Gets the zip of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for Elavon Americas (elavonamericas), RUPAY, American Express Direct (amexdirect) and TSYS (tsys) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>15</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :return: The zip of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for Elavon Americas (elavonamericas), RUPAY, American Express Direct (amexdirect) and TSYS (tsys) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, cp, hybrid</td><td>Yes</td><td>1</td><td>15</td><td>^[0-9a-zA-Z\\s]+$</td></tr> </table> 

        :param zip: The zip of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._zip = zip

    @property
    def url(self):
        """
        Gets the url of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for RUPAY and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, hybrid</td><td>Yes</td><td>1</td><td>40</td><td>URL</td></tr> <tr><td>American Express Direct</td><td>cp</td><td>No</td><td>1</td><td>40</td><td>URL</td></tr> </table> 

        :return: The url of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        Applicable for RUPAY and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Min. Length</th><th>Max. Length</th><th>Regex</th></tr></thead> <tr><td>American Express Direct</td><td>cnp, hybrid</td><td>Yes</td><td>1</td><td>40</td><td>URL</td></tr> <tr><td>American Express Direct</td><td>cp</td><td>No</td><td>1</td><td>40</td><td>URL</td></tr> </table> 

        :param url: The url of this PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, PaymentsProductsCardProcessingConfigurationInformationConfigurationsCommonMerchantDescriptorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other