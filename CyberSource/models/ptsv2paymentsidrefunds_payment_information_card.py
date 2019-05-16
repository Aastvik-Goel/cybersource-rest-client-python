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


class Ptsv2paymentsidrefundsPaymentInformationCard(object):
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
        'number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'account_encoder_id': 'str',
        'issue_number': 'str',
        'start_month': 'str',
        'start_year': 'str'
    }

    attribute_map = {
        'number': 'number',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'account_encoder_id': 'accountEncoderId',
        'issue_number': 'issueNumber',
        'start_month': 'startMonth',
        'start_year': 'startYear'
    }

    def __init__(self, number=None, expiration_month=None, expiration_year=None, type=None, account_encoder_id=None, issue_number=None, start_month=None, start_year=None):
        """
        Ptsv2paymentsidrefundsPaymentInformationCard - a model defined in Swagger
        """

        self._number = None
        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._account_encoder_id = None
        self._issue_number = None
        self._start_month = None
        self._start_year = None

        if number is not None:
          self.number = number
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if type is not None:
          self.type = type
        if account_encoder_id is not None:
          self.account_encoder_id = account_encoder_id
        if issue_number is not None:
          self.issue_number = issue_number
        if start_month is not None:
          self.start_month = start_month
        if start_year is not None:
          self.start_year = start_year

    @property
    def number(self):
        """
        Gets the number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        The customer’s payment card number, also knows as the Primary Account Nunmber (PAN). You can also use this field for encoded account numbers.  For processor-specific information, see the `customer_cc_number` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        The customer’s payment card number, also knows as the Primary Account Nunmber (PAN). You can also use this field for encoded account numbers.  For processor-specific information, see the `customer_cc_number` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param number: The number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """
        if number is not None and len(number) > 20:
            raise ValueError("Invalid value for `number`, length must be less than or equal to `20`")

        self._number = number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Two-digit month in which the payment card expires.  Format: `MM`.  Valid values: `01` through `12`.  **Barclays and Streamline**\\ For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  **Encoded Account Numbers**\\ For encoded account numbers (_type_=039), if there is no expiration date on the card, use `12`.  For processor-specific information, see the `customer_cc_expmo` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Two-digit month in which the payment card expires.  Format: `MM`.  Valid values: `01` through `12`.  **Barclays and Streamline**\\ For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  **Encoded Account Numbers**\\ For encoded account numbers (_type_=039), if there is no expiration date on the card, use `12`.  For processor-specific information, see the `customer_cc_expmo` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_month: The expiration_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """
        if expiration_month is not None and len(expiration_month) > 2:
            raise ValueError("Invalid value for `expiration_month`, length must be less than or equal to `2`")

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Four-digit year in which the credit card expires.  Format: `YYYY`.   **Barclays and Streamline**\\ For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`1900` through `3000`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  **FDC Nashville Global and FDMS South**\\ You can send in 2 digits or 4 digits. If you send in 2 digits, they must be the last 2 digits of the year.  **Encoded Account Numbers**\\ For encoded account numbers (_type_=039), if there is no expiration date on the card, use `2021`.  For processor-specific information, see the `customer_cc_expyr` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The expiration_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Four-digit year in which the credit card expires.  Format: `YYYY`.   **Barclays and Streamline**\\ For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`1900` through `3000`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  **FDC Nashville Global and FDMS South**\\ You can send in 2 digits or 4 digits. If you send in 2 digits, they must be the last 2 digits of the year.  **Encoded Account Numbers**\\ For encoded account numbers (_type_=039), if there is no expiration date on the card, use `2021`.  For processor-specific information, see the `customer_cc_expyr` field in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param expiration_year: The expiration_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """
        if expiration_year is not None and len(expiration_year) > 4:
            raise ValueError("Invalid value for `expiration_year`, length must be less than or equal to `4`")

        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover - 005: Diners Club - 007: JCB - 024: Maestro (UK Domestic) - 039 Encoded account number - 042: Maestro (International) 

        :return: The type of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover - 005: Diners Club - 007: JCB - 024: Maestro (UK Domestic) - 039 Encoded account number - 042: Maestro (International) 

        :param type: The type of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """

        self._type = type

    @property
    def account_encoder_id(self):
        """
        Gets the account_encoder_id of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Identifier for the issuing bank that provided the customer’s encoded account number. Contact your processor for the bank’s ID. 

        :return: The account_encoder_id of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._account_encoder_id

    @account_encoder_id.setter
    def account_encoder_id(self, account_encoder_id):
        """
        Sets the account_encoder_id of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Identifier for the issuing bank that provided the customer’s encoded account number. Contact your processor for the bank’s ID. 

        :param account_encoder_id: The account_encoder_id of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """
        if account_encoder_id is not None and len(account_encoder_id) > 3:
            raise ValueError("Invalid value for `account_encoder_id`, length must be less than or equal to `3`")

        self._account_encoder_id = account_encoder_id

    @property
    def issue_number(self):
        """
        Gets the issue_number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  **Note** The issue number is not required for Maestro (UK Domestic) transactions. 

        :return: The issue_number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """
        Sets the issue_number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  **Note** The issue number is not required for Maestro (UK Domestic) transactions. 

        :param issue_number: The issue_number of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """
        if issue_number is not None and len(issue_number) > 5:
            raise ValueError("Invalid value for `issue_number`, length must be less than or equal to `5`")

        self._issue_number = issue_number

    @property
    def start_month(self):
        """
        Gets the start_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """
        Sets the start_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_month: The start_month of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """
        if start_month is not None and len(start_month) > 2:
            raise ValueError("Invalid value for `start_month`, length must be less than or equal to `2`")

        self._start_month = start_month

    @property
    def start_year(self):
        """
        Gets the start_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_year: The start_year of this Ptsv2paymentsidrefundsPaymentInformationCard.
        :type: str
        """
        if start_year is not None and len(start_year) > 4:
            raise ValueError("Invalid value for `start_year`, length must be less than or equal to `4`")

        self._start_year = start_year

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
        if not isinstance(other, Ptsv2paymentsidrefundsPaymentInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other