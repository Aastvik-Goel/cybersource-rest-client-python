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


class TssV2TransactionsGet200ResponsePointOfSaleInformation(object):
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
        'terminal_id': 'str',
        'entry_mode': 'str',
        'terminal_capability': 'int',
        'cardholder_verification_method_used': 'int',
        'emv': 'Ptsv2paymentsidreversalsPointOfSaleInformationEmv'
    }

    attribute_map = {
        'terminal_id': 'terminalId',
        'entry_mode': 'entryMode',
        'terminal_capability': 'terminalCapability',
        'cardholder_verification_method_used': 'cardholderVerificationMethodUsed',
        'emv': 'emv'
    }

    def __init__(self, terminal_id=None, entry_mode=None, terminal_capability=None, cardholder_verification_method_used=None, emv=None):
        """
        TssV2TransactionsGet200ResponsePointOfSaleInformation - a model defined in Swagger
        """

        self._terminal_id = None
        self._entry_mode = None
        self._terminal_capability = None
        self._cardholder_verification_method_used = None
        self._emv = None

        if terminal_id is not None:
          self.terminal_id = terminal_id
        if entry_mode is not None:
          self.entry_mode = entry_mode
        if terminal_capability is not None:
          self.terminal_capability = terminal_capability
        if cardholder_verification_method_used is not None:
          self.cardholder_verification_method_used = cardholder_verification_method_used
        if emv is not None:
          self.emv = emv

    @property
    def terminal_id(self):
        """
        Gets the terminal_id of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        Identifier for the terminal at your retail location. You can define this value yourself, but consult the processor for requirements.  #### CyberSource through VisaNet A list of all possible values is stored in your CyberSource account. If terminal ID validation is enabled for your CyberSource account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact CyberSource Customer Support.  When you do not include this field in a request, CyberSource uses the default value that is defined in your CyberSource account.  #### FDC Nashville Global To have your account configured to support this field, contact CyberSource Customer Support. This value must be a value that FDC Nashville Global issued to you.  #### For Payouts This field is applicable for CyberSource through VisaNet.  #### GPX Identifier for the terminal at your retail location. A list of all possible values is stored in your account. If terminal ID validation is enabled for your account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact customer support.  When you do not include this field in a request, the default value that is defined in your account is used.  Optional for authorizations.  #### Used by **Authorization** Optional for the following processors. When you do not include this field in a request, the default value that is defined in your account is used.   - American Express Direct   - Credit Mutuel-CIC   - FDC Nashville Global   - SIX - Chase Paymentech Solutions: Optional field. If you include this field in your request, you must also include `pointOfSaleInformation.catLevel`. - FDMS Nashville: The default value that is defined in your account is used. - GPX - OmniPay Direct: Optional field.  For the following processors, this field is not used. - GPN - JCN Gateway - RBS WorldPay Atlanta - TSYS Acquiring Solutions - Worldpay VAP  #### Card Present reply Terminal identifier assigned by the acquirer. This value must be printed on the receipt. 

        :return: The terminal_id of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """
        Sets the terminal_id of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        Identifier for the terminal at your retail location. You can define this value yourself, but consult the processor for requirements.  #### CyberSource through VisaNet A list of all possible values is stored in your CyberSource account. If terminal ID validation is enabled for your CyberSource account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact CyberSource Customer Support.  When you do not include this field in a request, CyberSource uses the default value that is defined in your CyberSource account.  #### FDC Nashville Global To have your account configured to support this field, contact CyberSource Customer Support. This value must be a value that FDC Nashville Global issued to you.  #### For Payouts This field is applicable for CyberSource through VisaNet.  #### GPX Identifier for the terminal at your retail location. A list of all possible values is stored in your account. If terminal ID validation is enabled for your account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact customer support.  When you do not include this field in a request, the default value that is defined in your account is used.  Optional for authorizations.  #### Used by **Authorization** Optional for the following processors. When you do not include this field in a request, the default value that is defined in your account is used.   - American Express Direct   - Credit Mutuel-CIC   - FDC Nashville Global   - SIX - Chase Paymentech Solutions: Optional field. If you include this field in your request, you must also include `pointOfSaleInformation.catLevel`. - FDMS Nashville: The default value that is defined in your account is used. - GPX - OmniPay Direct: Optional field.  For the following processors, this field is not used. - GPN - JCN Gateway - RBS WorldPay Atlanta - TSYS Acquiring Solutions - Worldpay VAP  #### Card Present reply Terminal identifier assigned by the acquirer. This value must be printed on the receipt. 

        :param terminal_id: The terminal_id of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :type: str
        """



        self._terminal_id = terminal_id

    @property
    def entry_mode(self):
        """
        Gets the entry_mode of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        Method of entering payment card information into the POS terminal. Possible values:   - `contact`: Read from direct contact with chip card.  - `contactless`: Read from a contactless interface using chip data.  - `keyed`: Manually keyed into POS terminal. This value is not supported on OmniPay Direct.  - `msd`: Read from a contactless interface using magnetic stripe data (MSD). This value is not supported on OmniPay Direct.  - `swiped`: Read from credit card magnetic stripe.  The `contact`, `contactless`, and `msd` values are supported only for EMV transactions.  #### Used by **Authorization** Required field.  #### Card Present Card present information about EMV applies only to credit card processing and PIN debit processing. All other card present information applies only to credit card processing.  #### PIN debit Required for a PIN debit purchase and a PIN debit credit request. 

        :return: The entry_mode of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :rtype: str
        """
        return self._entry_mode

    @entry_mode.setter
    def entry_mode(self, entry_mode):
        """
        Sets the entry_mode of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        Method of entering payment card information into the POS terminal. Possible values:   - `contact`: Read from direct contact with chip card.  - `contactless`: Read from a contactless interface using chip data.  - `keyed`: Manually keyed into POS terminal. This value is not supported on OmniPay Direct.  - `msd`: Read from a contactless interface using magnetic stripe data (MSD). This value is not supported on OmniPay Direct.  - `swiped`: Read from credit card magnetic stripe.  The `contact`, `contactless`, and `msd` values are supported only for EMV transactions.  #### Used by **Authorization** Required field.  #### Card Present Card present information about EMV applies only to credit card processing and PIN debit processing. All other card present information applies only to credit card processing.  #### PIN debit Required for a PIN debit purchase and a PIN debit credit request. 

        :param entry_mode: The entry_mode of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :type: str
        """



        self._entry_mode = entry_mode

    @property
    def terminal_capability(self):
        """
        Gets the terminal_capability of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        POS terminal's capability. Possible values:   - `1`: Terminal has a magnetic stripe reader only.  - `2`: Terminal has a magnetic stripe reader and manual entry capability.  - `3`: Terminal has manual entry capability only.  - `4`: Terminal can read chip cards.  - `5`: Terminal can read contactless chip cards; cannot use contact to read chip cards.  For an EMV transaction, the value of this field must be `4` or `5`.  #### PIN debit Required for PIN debit purchase and PIN debit credit request.  #### Used by **Authorization** Required for the following processors: - American Express Direct - Chase Paymentech Solutions - Credit Mutuel-CIC - FDC Nashville Global - FDMS Nashville - OmniPay Direct - SIX - Worldpay VAP  Optional for the following processors: - CyberSource through VisaNet - GPN - GPX - JCN Gateway - RBS WorldPay Atlanta - TSYS Acquiring Solutions 

        :return: The terminal_capability of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :rtype: int
        """
        return self._terminal_capability

    @terminal_capability.setter
    def terminal_capability(self, terminal_capability):
        """
        Sets the terminal_capability of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        POS terminal's capability. Possible values:   - `1`: Terminal has a magnetic stripe reader only.  - `2`: Terminal has a magnetic stripe reader and manual entry capability.  - `3`: Terminal has manual entry capability only.  - `4`: Terminal can read chip cards.  - `5`: Terminal can read contactless chip cards; cannot use contact to read chip cards.  For an EMV transaction, the value of this field must be `4` or `5`.  #### PIN debit Required for PIN debit purchase and PIN debit credit request.  #### Used by **Authorization** Required for the following processors: - American Express Direct - Chase Paymentech Solutions - Credit Mutuel-CIC - FDC Nashville Global - FDMS Nashville - OmniPay Direct - SIX - Worldpay VAP  Optional for the following processors: - CyberSource through VisaNet - GPN - GPX - JCN Gateway - RBS WorldPay Atlanta - TSYS Acquiring Solutions 

        :param terminal_capability: The terminal_capability of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :type: int
        """



        self._terminal_capability = terminal_capability

    @property
    def cardholder_verification_method_used(self):
        """
        Gets the cardholder_verification_method_used of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        Method that was used to verify the cardholder's identity. Possible values:    - `0`: No verification   - `1`: Signature   - `2`: PIN   - `3`: Cardholder device CVM 

        :return: The cardholder_verification_method_used of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :rtype: int
        """
        return self._cardholder_verification_method_used

    @cardholder_verification_method_used.setter
    def cardholder_verification_method_used(self, cardholder_verification_method_used):
        """
        Sets the cardholder_verification_method_used of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        Method that was used to verify the cardholder's identity. Possible values:    - `0`: No verification   - `1`: Signature   - `2`: PIN   - `3`: Cardholder device CVM 

        :param cardholder_verification_method_used: The cardholder_verification_method_used of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :type: int
        """



        self._cardholder_verification_method_used = cardholder_verification_method_used

    @property
    def emv(self):
        """
        Gets the emv of this TssV2TransactionsGet200ResponsePointOfSaleInformation.

        :return: The emv of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :rtype: Ptsv2paymentsidreversalsPointOfSaleInformationEmv
        """
        return self._emv

    @emv.setter
    def emv(self, emv):
        """
        Sets the emv of this TssV2TransactionsGet200ResponsePointOfSaleInformation.

        :param emv: The emv of this TssV2TransactionsGet200ResponsePointOfSaleInformation.
        :type: Ptsv2paymentsidreversalsPointOfSaleInformationEmv
        """



        self._emv = emv

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
        if not isinstance(other, TssV2TransactionsGet200ResponsePointOfSaleInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
