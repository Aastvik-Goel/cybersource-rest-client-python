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


class RiskV1DecisionsPost201ResponsePaymentInformation(object):
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
        'bin_country': 'str',
        'account_type': 'str',
        'issuer': 'str',
        'scheme': 'str',
        'bin': 'str'
    }

    attribute_map = {
        'bin_country': 'binCountry',
        'account_type': 'accountType',
        'issuer': 'issuer',
        'scheme': 'scheme',
        'bin': 'bin'
    }

    def __init__(self, bin_country=None, account_type=None, issuer=None, scheme=None, bin=None):
        """
        RiskV1DecisionsPost201ResponsePaymentInformation - a model defined in Swagger
        """

        self._bin_country = None
        self._account_type = None
        self._issuer = None
        self._scheme = None
        self._bin = None

        if bin_country is not None:
          self.bin_country = bin_country
        if account_type is not None:
          self.account_type = account_type
        if issuer is not None:
          self.issuer = issuer
        if scheme is not None:
          self.scheme = scheme
        if bin is not None:
          self.bin = bin

    @property
    def bin_country(self):
        """
        Gets the bin_country of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Country (two-digit country code) associated with the BIN of the customer's card used for the payment. Returned if the information is available. Use this field for additional information when reviewing orders. This information is also displayed in the details page of the CyberSource Business Center.  For all possible values, see the `bin_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The bin_country of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._bin_country

    @bin_country.setter
    def bin_country(self, bin_country):
        """
        Sets the bin_country of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Country (two-digit country code) associated with the BIN of the customer's card used for the payment. Returned if the information is available. Use this field for additional information when reviewing orders. This information is also displayed in the details page of the CyberSource Business Center.  For all possible values, see the `bin_country` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param bin_country: The bin_country of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :type: str
        """



        self._bin_country = bin_country

    @property
    def account_type(self):
        """
        Gets the account_type of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Type of payment card account. This field can refer to a credit card, debit card, or prepaid card account type.  For all possible values, see the `score_card_account_type` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The account_type of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Type of payment card account. This field can refer to a credit card, debit card, or prepaid card account type.  For all possible values, see the `score_card_account_type` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param account_type: The account_type of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :type: str
        """



        self._account_type = account_type

    @property
    def issuer(self):
        """
        Gets the issuer of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Name of the bank or entity that issued the card account.  For all possible values, see the `score_card_issuer` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The issuer of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Name of the bank or entity that issued the card account.  For all possible values, see the `score_card_issuer` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param issuer: The issuer of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :type: str
        """



        self._issuer = issuer

    @property
    def scheme(self):
        """
        Gets the scheme of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Subtype of card account. This field can contain one of the following values: - Maestro International - Maestro UK Domestic - MasterCard Credit - MasterCard Debit - Visa Credit - Visa Debit - Visa Electron  **Note** Additional values may be present.  For all possible values, see the `score_card_scheme` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The scheme of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """
        Sets the scheme of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Subtype of card account. This field can contain one of the following values: - Maestro International - Maestro UK Domestic - MasterCard Credit - MasterCard Debit - Visa Credit - Visa Debit - Visa Electron  **Note** Additional values may be present.  For all possible values, see the `score_card_scheme` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param scheme: The scheme of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :type: str
        """



        self._scheme = scheme

    @property
    def bin(self):
        """
        Gets the bin of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Credit card BIN (the first six digits of the credit card).Derived either from the `cc_bin` request field or from the first six characters of the `customer_cc_num` field.  For all possible values, see the `score_cc_bin` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The bin of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin):
        """
        Sets the bin of this RiskV1DecisionsPost201ResponsePaymentInformation.
        Credit card BIN (the first six digits of the credit card).Derived either from the `cc_bin` request field or from the first six characters of the `customer_cc_num` field.  For all possible values, see the `score_cc_bin` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param bin: The bin of this RiskV1DecisionsPost201ResponsePaymentInformation.
        :type: str
        """



        self._bin = bin

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
        if not isinstance(other, RiskV1DecisionsPost201ResponsePaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
