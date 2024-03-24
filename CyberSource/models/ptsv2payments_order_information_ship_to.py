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


class Ptsv2paymentsOrderInformationShipTo(object):
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
        'title': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'address1': 'str',
        'address2': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'county': 'str',
        'country': 'str',
        'district': 'str',
        'building_number': 'str',
        'phone_number': 'str',
        'email': 'str',
        'company': 'str',
        'destination_types': 'str',
        'destination_code': 'int',
        'method': 'str'
    }

    attribute_map = {
        'title': 'title',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'address1': 'address1',
        'address2': 'address2',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'county': 'county',
        'country': 'country',
        'district': 'district',
        'building_number': 'buildingNumber',
        'phone_number': 'phoneNumber',
        'email': 'email',
        'company': 'company',
        'destination_types': 'destinationTypes',
        'destination_code': 'destinationCode',
        'method': 'method'
    }

    def __init__(self, title=None, first_name=None, middle_name=None, last_name=None, address1=None, address2=None, locality=None, administrative_area=None, postal_code=None, county=None, country=None, district=None, building_number=None, phone_number=None, email=None, company=None, destination_types=None, destination_code=None, method=None):
        """
        Ptsv2paymentsOrderInformationShipTo - a model defined in Swagger
        """

        self._title = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._address1 = None
        self._address2 = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._county = None
        self._country = None
        self._district = None
        self._building_number = None
        self._phone_number = None
        self._email = None
        self._company = None
        self._destination_types = None
        self._destination_code = None
        self._method = None

        if title is not None:
          self.title = title
        if first_name is not None:
          self.first_name = first_name
        if middle_name is not None:
          self.middle_name = middle_name
        if last_name is not None:
          self.last_name = last_name
        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if county is not None:
          self.county = county
        if country is not None:
          self.country = country
        if district is not None:
          self.district = district
        if building_number is not None:
          self.building_number = building_number
        if phone_number is not None:
          self.phone_number = phone_number
        if email is not None:
          self.email = email
        if company is not None:
          self.company = company
        if destination_types is not None:
          self.destination_types = destination_types
        if destination_code is not None:
          self.destination_code = destination_code
        if method is not None:
          self.method = method

    @property
    def title(self):
        """
        Gets the title of this Ptsv2paymentsOrderInformationShipTo.
        The title of the person receiving the product.

        :return: The title of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Ptsv2paymentsOrderInformationShipTo.
        The title of the person receiving the product.

        :param title: The title of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._title = title

    @property
    def first_name(self):
        """
        Gets the first_name of this Ptsv2paymentsOrderInformationShipTo.
        First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :return: The first_name of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Ptsv2paymentsOrderInformationShipTo.
        First name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :param first_name: The first_name of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this Ptsv2paymentsOrderInformationShipTo.
        Middle name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :return: The middle_name of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this Ptsv2paymentsOrderInformationShipTo.
        Middle name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :param middle_name: The middle_name of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Ptsv2paymentsOrderInformationShipTo.
        Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :return: The last_name of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Ptsv2paymentsOrderInformationShipTo.
        Last name of the recipient.  #### Litle Maximum length: 25  #### All other processors Maximum length: 60  Optional field. 

        :param last_name: The last_name of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._last_name = last_name

    @property
    def address1(self):
        """
        Gets the address1 of this Ptsv2paymentsOrderInformationShipTo.
        First line of the shipping address.  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The address1 of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Ptsv2paymentsOrderInformationShipTo.
        First line of the shipping address.  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param address1: The address1 of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Ptsv2paymentsOrderInformationShipTo.
        Second line of the shipping address.  Optional field.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The address2 of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Ptsv2paymentsOrderInformationShipTo.
        Second line of the shipping address.  Optional field.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param address2: The address2 of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._address2 = address2

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv2paymentsOrderInformationShipTo.
        City of the shipping address.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The locality of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv2paymentsOrderInformationShipTo.
        City of the shipping address.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param locality: The locality of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2paymentsOrderInformationShipTo.
        State or province of the shipping address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) (maximum length: 2)   Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The administrative_area of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2paymentsOrderInformationShipTo.
        State or province of the shipping address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) (maximum length: 2)   Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param administrative_area: The administrative_area of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2paymentsOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  #### American Express Direct Before sending the postal code to the processor, all nonalphanumeric characters are removed and, if the remaining value is longer than nine characters, the value is truncated starting from the right side. #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The postal_code of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2paymentsOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits.  Required field for authorization if any shipping address information is included in the request and shipping to the U.S. or Canada; otherwise, optional.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  Example 12345-6789  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  Example A1B 2C3  #### American Express Direct Before sending the postal code to the processor, all nonalphanumeric characters are removed and, if the remaining value is longer than nine characters, the value is truncated starting from the right side. #### Tax Calculation Optional field for U.S. and Canadian taxes. Not applicable to international and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param postal_code: The postal_code of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def county(self):
        """
        Gets the county of this Ptsv2paymentsOrderInformationShipTo.
        U.S. county if available.

        :return: The county of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this Ptsv2paymentsOrderInformationShipTo.
        U.S. county if available.

        :param county: The county of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._county = county

    @property
    def country(self):
        """
        Gets the country of this Ptsv2paymentsOrderInformationShipTo.
        Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :return: The country of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2paymentsOrderInformationShipTo.
        Country of the shipping address. Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf)  Required field for authorization if any shipping address information is included in the request; otherwise, optional.  #### Tax Calculation Optional field for U.S., Canadian, international tax, and value added taxes. Billing address objects will be used to determine the cardholder's location when shipTo objects are not present. 

        :param country: The country of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._country = country

    @property
    def district(self):
        """
        Gets the district of this Ptsv2paymentsOrderInformationShipTo.
        Neighborhood, community, or region within a city or municipality.

        :return: The district of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """
        Sets the district of this Ptsv2paymentsOrderInformationShipTo.
        Neighborhood, community, or region within a city or municipality.

        :param district: The district of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._district = district

    @property
    def building_number(self):
        """
        Gets the building_number of this Ptsv2paymentsOrderInformationShipTo.
        Building number in the street address. For example, the building number is 187 in the following address:  Rua da Quitanda 187 

        :return: The building_number of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """
        Sets the building_number of this Ptsv2paymentsOrderInformationShipTo.
        Building number in the street address. For example, the building number is 187 in the following address:  Rua da Quitanda 187 

        :param building_number: The building_number of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._building_number = building_number

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Ptsv2paymentsOrderInformationShipTo.
        Phone number associated with the shipping address.

        :return: The phone_number of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Ptsv2paymentsOrderInformationShipTo.
        Phone number associated with the shipping address.

        :param phone_number: The phone_number of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def email(self):
        """
        Gets the email of this Ptsv2paymentsOrderInformationShipTo.
        Email of the recipient. 

        :return: The email of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Ptsv2paymentsOrderInformationShipTo.
        Email of the recipient. 

        :param email: The email of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._email = email

    @property
    def company(self):
        """
        Gets the company of this Ptsv2paymentsOrderInformationShipTo.
        Name of the customer's company.  For processor-specific information, see the company_name field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The company of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Ptsv2paymentsOrderInformationShipTo.
        Name of the customer's company.  For processor-specific information, see the company_name field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param company: The company of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._company = company

    @property
    def destination_types(self):
        """
        Gets the destination_types of this Ptsv2paymentsOrderInformationShipTo.
        Shipping destination of item. Example: Commercial, Residential, Store 

        :return: The destination_types of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._destination_types

    @destination_types.setter
    def destination_types(self, destination_types):
        """
        Sets the destination_types of this Ptsv2paymentsOrderInformationShipTo.
        Shipping destination of item. Example: Commercial, Residential, Store 

        :param destination_types: The destination_types of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._destination_types = destination_types

    @property
    def destination_code(self):
        """
        Gets the destination_code of this Ptsv2paymentsOrderInformationShipTo.
        Indicates destination chosen for the transaction. Possible values: - 01- Ship to cardholder billing address - 02- Ship to another verified address on file with merchant - 03- Ship to address that is different than billing address - 04- Ship to store (store address should be populated on request) - 05- Digital goods - 06- Travel and event tickets, not shipped - 07- Other 

        :return: The destination_code of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: int
        """
        return self._destination_code

    @destination_code.setter
    def destination_code(self, destination_code):
        """
        Sets the destination_code of this Ptsv2paymentsOrderInformationShipTo.
        Indicates destination chosen for the transaction. Possible values: - 01- Ship to cardholder billing address - 02- Ship to another verified address on file with merchant - 03- Ship to address that is different than billing address - 04- Ship to store (store address should be populated on request) - 05- Digital goods - 06- Travel and event tickets, not shipped - 07- Other 

        :param destination_code: The destination_code of this Ptsv2paymentsOrderInformationShipTo.
        :type: int
        """

        self._destination_code = destination_code

    @property
    def method(self):
        """
        Gets the method of this Ptsv2paymentsOrderInformationShipTo.
        Shipping method for the product. Possible values: - lowcost: Lowest-cost service - sameday: Courier or same-day service - oneday: Next-day or overnight service - twoday: Two-day service - threeday: Three-day service - pickup: Store pick-up - other: Other shipping method - none: No shipping method because product is a service or subscription Required for American Express SafeKey (U.S.). 

        :return: The method of this Ptsv2paymentsOrderInformationShipTo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this Ptsv2paymentsOrderInformationShipTo.
        Shipping method for the product. Possible values: - lowcost: Lowest-cost service - sameday: Courier or same-day service - oneday: Next-day or overnight service - twoday: Two-day service - threeday: Three-day service - pickup: Store pick-up - other: Other shipping method - none: No shipping method because product is a service or subscription Required for American Express SafeKey (U.S.). 

        :param method: The method of this Ptsv2paymentsOrderInformationShipTo.
        :type: str
        """

        self._method = method

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
        if not isinstance(other, Ptsv2paymentsOrderInformationShipTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
