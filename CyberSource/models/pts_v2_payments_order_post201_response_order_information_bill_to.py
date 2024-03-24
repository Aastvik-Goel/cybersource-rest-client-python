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


class PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo(object):
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
        'name_suffix': 'str',
        'address1': 'str',
        'address2': 'str',
        'locality': 'str',
        'postal_code': 'str',
        'administrative_area': 'str',
        'country': 'str',
        'email': 'str',
        'phone_number': 'str',
        'verification_status': 'str'
    }

    attribute_map = {
        'title': 'title',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'name_suffix': 'nameSuffix',
        'address1': 'address1',
        'address2': 'address2',
        'locality': 'locality',
        'postal_code': 'postalCode',
        'administrative_area': 'administrativeArea',
        'country': 'country',
        'email': 'email',
        'phone_number': 'phoneNumber',
        'verification_status': 'verificationStatus'
    }

    def __init__(self, title=None, first_name=None, middle_name=None, last_name=None, name_suffix=None, address1=None, address2=None, locality=None, postal_code=None, administrative_area=None, country=None, email=None, phone_number=None, verification_status=None):
        """
        PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo - a model defined in Swagger
        """

        self._title = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._name_suffix = None
        self._address1 = None
        self._address2 = None
        self._locality = None
        self._postal_code = None
        self._administrative_area = None
        self._country = None
        self._email = None
        self._phone_number = None
        self._verification_status = None

        if title is not None:
          self.title = title
        if first_name is not None:
          self.first_name = first_name
        if middle_name is not None:
          self.middle_name = middle_name
        if last_name is not None:
          self.last_name = last_name
        if name_suffix is not None:
          self.name_suffix = name_suffix
        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if locality is not None:
          self.locality = locality
        if postal_code is not None:
          self.postal_code = postal_code
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if country is not None:
          self.country = country
        if email is not None:
          self.email = email
        if phone_number is not None:
          self.phone_number = phone_number
        if verification_status is not None:
          self.verification_status = verification_status

    @property
    def title(self):
        """
        Gets the title of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Title. 

        :return: The title of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Title. 

        :param title: The title of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._title = title

    @property
    def first_name(self):
        """
        Gets the first_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's first name. This name must be the same as the name on the card.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### SEPA Required for Create Mandate and Import Mandate #### BACS Required for Import Mandate  #### CyberSource Latin American Processing **Important** For an authorization request, CyberSource Latin American Processing concatenates `orderInformation.billTo.firstName` and `orderInformation.billTo.lastName`. If the concatenated value exceeds 30 characters, CyberSource Latin American Processing declines the authorization request.\\ **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called _CyberSource Latin American Processing_. It is not for any other Latin American processors that CyberSource supports.  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :return: The first_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's first name. This name must be the same as the name on the card.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### SEPA Required for Create Mandate and Import Mandate #### BACS Required for Import Mandate  #### CyberSource Latin American Processing **Important** For an authorization request, CyberSource Latin American Processing concatenates `orderInformation.billTo.firstName` and `orderInformation.billTo.lastName`. If the concatenated value exceeds 30 characters, CyberSource Latin American Processing declines the authorization request.\\ **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called _CyberSource Latin American Processing_. It is not for any other Latin American processors that CyberSource supports.  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :param first_name: The first_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's middle name. 

        :return: The middle_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's middle name. 

        :param middle_name: The middle_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's last name. This name must be the same as the name on the card.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### SEPA Required for Create Mandate and Import Mandate #### BACS Required for Import Mandate #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### CyberSource Latin American Processing **Important** For an authorization request, CyberSource Latin American Processing concatenates `orderInformation.billTo.firstName` and `orderInformation.billTo.lastName`. If the concatenated value exceeds 30 characters, CyberSource Latin American Processing declines the authorization request.\\ **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### OmniPay Direct Optional field.  #### RBS WorldPay Atlanta Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :return: The last_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's last name. This name must be the same as the name on the card.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### SEPA Required for Create Mandate and Import Mandate #### BACS Required for Import Mandate #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### CyberSource Latin American Processing **Important** For an authorization request, CyberSource Latin American Processing concatenates `orderInformation.billTo.firstName` and `orderInformation.billTo.lastName`. If the concatenated value exceeds 30 characters, CyberSource Latin American Processing declines the authorization request.\\ **Note** CyberSource Latin American Processing is the name of a specific processing connection that CyberSource supports. In the CyberSource API documentation, CyberSource Latin American Processing does not refer to the general topic of processing in Latin America. The information in this field description is for the specific processing connection called CyberSource Latin American Processing. It is not for any other Latin American processors that CyberSource supports.  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### OmniPay Direct Optional field.  #### RBS WorldPay Atlanta Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :param last_name: The last_name of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._last_name = last_name

    @property
    def name_suffix(self):
        """
        Gets the name_suffix of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's name suffix. 

        :return: The name_suffix of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._name_suffix

    @name_suffix.setter
    def name_suffix(self, name_suffix):
        """
        Sets the name_suffix of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's name suffix. 

        :param name_suffix: The name_suffix of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._name_suffix = name_suffix

    @property
    def address1(self):
        """
        Gets the address1 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        First line of the billing street address. 

        :return: The address1 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        First line of the billing street address. 

        :param address1: The address1 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Second line of the billing street address. 

        :return: The address2 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Second line of the billing street address. 

        :param address2: The address2 of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._address2 = address2

    @property
    def locality(self):
        """
        Gets the locality of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        City of the billing address. 

        :return: The locality of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        City of the billing address. 

        :param locality: The locality of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._locality = locality

    @property
    def postal_code(self):
        """
        Gets the postal_code of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits. When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits] Example: 12345-6789 When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric] Example: A1B 2C3 

        :return: The postal_code of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits. When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits] Example: 12345-6789 When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric] Example: A1B 2C3 

        :param postal_code: The postal_code of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        State or province of the billing address. Use the State, Province, and Territory Codes for the United States and Canada. 

        :return: The administrative_area of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        State or province of the billing address. Use the State, Province, and Territory Codes for the United States and Canada. 

        :param administrative_area: The administrative_area of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def country(self):
        """
        Gets the country of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Country of the billing address. Use the two-character ISO Standard Country Codes. 

        :return: The country of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Country of the billing address. Use the two-character ISO Standard Country Codes. 

        :param country: The country of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """
        Gets the email of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's email address. 

        :return: The email of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's email address. 

        :param email: The email of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's phone number.  It is recommended that you include the country code when the order is from outside the U.S.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Optional field.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :return: The phone_number of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Customer's phone number.  It is recommended that you include the country code when the order is from outside the U.S.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Optional field.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :param phone_number: The phone_number of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def verification_status(self):
        """
        Gets the verification_status of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Whether buyer has verified their identity. Used in case of PayPal transactions.  Possible Values: * VERIFIED * UNVERIFIED 

        :return: The verification_status of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :rtype: str
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        """
        Sets the verification_status of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        Whether buyer has verified their identity. Used in case of PayPal transactions.  Possible Values: * VERIFIED * UNVERIFIED 

        :param verification_status: The verification_status of this PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo.
        :type: str
        """

        self._verification_status = verification_status

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
        if not isinstance(other, PtsV2PaymentsOrderPost201ResponseOrderInformationBillTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
