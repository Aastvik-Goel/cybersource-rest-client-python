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


class PayerAuthConfigCardTypes(object):
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
        'verified_by_visa': 'PayerAuthConfigCardTypesVerifiedByVisa',
        'master_card_secure_code': 'PayerAuthConfigCardTypesVerifiedByVisa',
        'amex_safe_key': 'PayerAuthConfigCardTypesVerifiedByVisa',
        'j_cbj_secure': 'PayerAuthConfigCardTypesJCBJSecure',
        'diners_club_international_protect_buy': 'PayerAuthConfigCardTypesVerifiedByVisa',
        'elo': 'PayerAuthConfigCardTypesVerifiedByVisa',
        'upi': 'PayerAuthConfigCardTypesVerifiedByVisa',
        'cb': 'PayerAuthConfigCardTypesCB'
    }

    attribute_map = {
        'verified_by_visa': 'verifiedByVisa',
        'master_card_secure_code': 'masterCardSecureCode',
        'amex_safe_key': 'amexSafeKey',
        'j_cbj_secure': 'jCBJSecure',
        'diners_club_international_protect_buy': 'dinersClubInternationalProtectBuy',
        'elo': 'ELO',
        'upi': 'UPI',
        'cb': 'CB'
    }

    def __init__(self, verified_by_visa=None, master_card_secure_code=None, amex_safe_key=None, j_cbj_secure=None, diners_club_international_protect_buy=None, elo=None, upi=None, cb=None):
        """
        PayerAuthConfigCardTypes - a model defined in Swagger
        """

        self._verified_by_visa = None
        self._master_card_secure_code = None
        self._amex_safe_key = None
        self._j_cbj_secure = None
        self._diners_club_international_protect_buy = None
        self._elo = None
        self._upi = None
        self._cb = None

        if verified_by_visa is not None:
          self.verified_by_visa = verified_by_visa
        if master_card_secure_code is not None:
          self.master_card_secure_code = master_card_secure_code
        if amex_safe_key is not None:
          self.amex_safe_key = amex_safe_key
        if j_cbj_secure is not None:
          self.j_cbj_secure = j_cbj_secure
        if diners_club_international_protect_buy is not None:
          self.diners_club_international_protect_buy = diners_club_international_protect_buy
        if elo is not None:
          self.elo = elo
        if upi is not None:
          self.upi = upi
        if cb is not None:
          self.cb = cb

    @property
    def verified_by_visa(self):
        """
        Gets the verified_by_visa of this PayerAuthConfigCardTypes.

        :return: The verified_by_visa of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesVerifiedByVisa
        """
        return self._verified_by_visa

    @verified_by_visa.setter
    def verified_by_visa(self, verified_by_visa):
        """
        Sets the verified_by_visa of this PayerAuthConfigCardTypes.

        :param verified_by_visa: The verified_by_visa of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesVerifiedByVisa
        """

        self._verified_by_visa = verified_by_visa

    @property
    def master_card_secure_code(self):
        """
        Gets the master_card_secure_code of this PayerAuthConfigCardTypes.

        :return: The master_card_secure_code of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesVerifiedByVisa
        """
        return self._master_card_secure_code

    @master_card_secure_code.setter
    def master_card_secure_code(self, master_card_secure_code):
        """
        Sets the master_card_secure_code of this PayerAuthConfigCardTypes.

        :param master_card_secure_code: The master_card_secure_code of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesVerifiedByVisa
        """

        self._master_card_secure_code = master_card_secure_code

    @property
    def amex_safe_key(self):
        """
        Gets the amex_safe_key of this PayerAuthConfigCardTypes.

        :return: The amex_safe_key of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesVerifiedByVisa
        """
        return self._amex_safe_key

    @amex_safe_key.setter
    def amex_safe_key(self, amex_safe_key):
        """
        Sets the amex_safe_key of this PayerAuthConfigCardTypes.

        :param amex_safe_key: The amex_safe_key of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesVerifiedByVisa
        """

        self._amex_safe_key = amex_safe_key

    @property
    def j_cbj_secure(self):
        """
        Gets the j_cbj_secure of this PayerAuthConfigCardTypes.

        :return: The j_cbj_secure of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesJCBJSecure
        """
        return self._j_cbj_secure

    @j_cbj_secure.setter
    def j_cbj_secure(self, j_cbj_secure):
        """
        Sets the j_cbj_secure of this PayerAuthConfigCardTypes.

        :param j_cbj_secure: The j_cbj_secure of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesJCBJSecure
        """

        self._j_cbj_secure = j_cbj_secure

    @property
    def diners_club_international_protect_buy(self):
        """
        Gets the diners_club_international_protect_buy of this PayerAuthConfigCardTypes.

        :return: The diners_club_international_protect_buy of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesVerifiedByVisa
        """
        return self._diners_club_international_protect_buy

    @diners_club_international_protect_buy.setter
    def diners_club_international_protect_buy(self, diners_club_international_protect_buy):
        """
        Sets the diners_club_international_protect_buy of this PayerAuthConfigCardTypes.

        :param diners_club_international_protect_buy: The diners_club_international_protect_buy of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesVerifiedByVisa
        """

        self._diners_club_international_protect_buy = diners_club_international_protect_buy

    @property
    def elo(self):
        """
        Gets the elo of this PayerAuthConfigCardTypes.

        :return: The elo of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesVerifiedByVisa
        """
        return self._elo

    @elo.setter
    def elo(self, elo):
        """
        Sets the elo of this PayerAuthConfigCardTypes.

        :param elo: The elo of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesVerifiedByVisa
        """

        self._elo = elo

    @property
    def upi(self):
        """
        Gets the upi of this PayerAuthConfigCardTypes.

        :return: The upi of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesVerifiedByVisa
        """
        return self._upi

    @upi.setter
    def upi(self, upi):
        """
        Sets the upi of this PayerAuthConfigCardTypes.

        :param upi: The upi of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesVerifiedByVisa
        """

        self._upi = upi

    @property
    def cb(self):
        """
        Gets the cb of this PayerAuthConfigCardTypes.

        :return: The cb of this PayerAuthConfigCardTypes.
        :rtype: PayerAuthConfigCardTypesCB
        """
        return self._cb

    @cb.setter
    def cb(self, cb):
        """
        Sets the cb of this PayerAuthConfigCardTypes.

        :param cb: The cb of this PayerAuthConfigCardTypes.
        :type: PayerAuthConfigCardTypesCB
        """

        self._cb = cb

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
        if not isinstance(other, PayerAuthConfigCardTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
