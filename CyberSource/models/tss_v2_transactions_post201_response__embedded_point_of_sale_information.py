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


class TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation(object):
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
        'terminal_serial_number': 'str',
        'device_id': 'str',
        'partner': 'TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner',
        'emv': 'Ptsv2paymentsidreversalsPointOfSaleInformationEmv'
    }

    attribute_map = {
        'terminal_id': 'terminalId',
        'terminal_serial_number': 'terminalSerialNumber',
        'device_id': 'deviceId',
        'partner': 'partner',
        'emv': 'emv'
    }

    def __init__(self, terminal_id=None, terminal_serial_number=None, device_id=None, partner=None, emv=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation - a model defined in Swagger
        """

        self._terminal_id = None
        self._terminal_serial_number = None
        self._device_id = None
        self._partner = None
        self._emv = None

        if terminal_id is not None:
          self.terminal_id = terminal_id
        if terminal_serial_number is not None:
          self.terminal_serial_number = terminal_serial_number
        if device_id is not None:
          self.device_id = device_id
        if partner is not None:
          self.partner = partner
        if emv is not None:
          self.emv = emv

    @property
    def terminal_id(self):
        """
        Gets the terminal_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        Identifier for the terminal at your retail location. You can define this value yourself, but consult the processor for requirements.  #### CyberSource through VisaNet A list of all possible values is stored in your CyberSource account. If terminal ID validation is enabled for your CyberSource account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact CyberSource Customer Support.  When you do not include this field in a request, CyberSource uses the default value that is defined in your CyberSource account.  #### FDC Nashville Global To have your account configured to support this field, contact CyberSource Customer Support. This value must be a value that FDC Nashville Global issued to you.  #### For Payouts This field is applicable for CyberSource through VisaNet.  #### GPX Identifier for the terminal at your retail location. A list of all possible values is stored in your account. If terminal ID validation is enabled for your account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact customer support.  When you do not include this field in a request, the default value that is defined in your account is used.  Optional for authorizations.  #### Used by **Authorization** Optional for the following processors. When you do not include this field in a request, the default value that is defined in your account is used.   - American Express Direct   - Credit Mutuel-CIC   - FDC Nashville Global   - SIX - Chase Paymentech Solutions: Optional field. If you include this field in your request, you must also include `pointOfSaleInformation.catLevel`. - FDMS Nashville: The default value that is defined in your account is used. - GPX - OmniPay Direct: Optional field.  For the following processors, this field is not used. - GPN - JCN Gateway - RBS WorldPay Atlanta - TSYS Acquiring Solutions - Worldpay VAP  #### Card Present reply Terminal identifier assigned by the acquirer. This value must be printed on the receipt. 

        :return: The terminal_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """
        Sets the terminal_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        Identifier for the terminal at your retail location. You can define this value yourself, but consult the processor for requirements.  #### CyberSource through VisaNet A list of all possible values is stored in your CyberSource account. If terminal ID validation is enabled for your CyberSource account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact CyberSource Customer Support.  When you do not include this field in a request, CyberSource uses the default value that is defined in your CyberSource account.  #### FDC Nashville Global To have your account configured to support this field, contact CyberSource Customer Support. This value must be a value that FDC Nashville Global issued to you.  #### For Payouts This field is applicable for CyberSource through VisaNet.  #### GPX Identifier for the terminal at your retail location. A list of all possible values is stored in your account. If terminal ID validation is enabled for your account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact customer support.  When you do not include this field in a request, the default value that is defined in your account is used.  Optional for authorizations.  #### Used by **Authorization** Optional for the following processors. When you do not include this field in a request, the default value that is defined in your account is used.   - American Express Direct   - Credit Mutuel-CIC   - FDC Nashville Global   - SIX - Chase Paymentech Solutions: Optional field. If you include this field in your request, you must also include `pointOfSaleInformation.catLevel`. - FDMS Nashville: The default value that is defined in your account is used. - GPX - OmniPay Direct: Optional field.  For the following processors, this field is not used. - GPN - JCN Gateway - RBS WorldPay Atlanta - TSYS Acquiring Solutions - Worldpay VAP  #### Card Present reply Terminal identifier assigned by the acquirer. This value must be printed on the receipt. 

        :param terminal_id: The terminal_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :type: str
        """

        self._terminal_id = terminal_id

    @property
    def terminal_serial_number(self):
        """
        Gets the terminal_serial_number of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        Terminal serial number assigned by the hardware manufacturer. This value is provided by the client software that is installed on the POS terminal.  This value is not forwarded to the processor. Instead, the value is forwarded to the reporting functionality.  #### Used by **Authorization and Credit** Optional. This field is supported only by client software that is installed on your POS terminals for the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX 

        :return: The terminal_serial_number of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :rtype: str
        """
        return self._terminal_serial_number

    @terminal_serial_number.setter
    def terminal_serial_number(self, terminal_serial_number):
        """
        Sets the terminal_serial_number of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        Terminal serial number assigned by the hardware manufacturer. This value is provided by the client software that is installed on the POS terminal.  This value is not forwarded to the processor. Instead, the value is forwarded to the reporting functionality.  #### Used by **Authorization and Credit** Optional. This field is supported only by client software that is installed on your POS terminals for the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX 

        :param terminal_serial_number: The terminal_serial_number of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :type: str
        """

        self._terminal_serial_number = terminal_serial_number

    @property
    def device_id(self):
        """
        Gets the device_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        Value created by the client software that uniquely identifies the POS device. CyberSource does not forward this value to the processor. Instead, the value is forwarded to the CyberSource reporting functionality.  This field is supported only for authorizations and credits on these processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  Optional field. String (32) 

        :return: The device_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        Value created by the client software that uniquely identifies the POS device. CyberSource does not forward this value to the processor. Instead, the value is forwarded to the CyberSource reporting functionality.  This field is supported only for authorizations and credits on these processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  Optional field. String (32) 

        :param device_id: The device_id of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :type: str
        """

        self._device_id = device_id

    @property
    def partner(self):
        """
        Gets the partner of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.

        :return: The partner of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :rtype: TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """
        Sets the partner of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.

        :param partner: The partner of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :type: TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformationPartner
        """

        self._partner = partner

    @property
    def emv(self):
        """
        Gets the emv of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.

        :return: The emv of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
        :rtype: Ptsv2paymentsidreversalsPointOfSaleInformationEmv
        """
        return self._emv

    @emv.setter
    def emv(self, emv):
        """
        Sets the emv of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.

        :param emv: The emv of this TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation.
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
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedPointOfSaleInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
