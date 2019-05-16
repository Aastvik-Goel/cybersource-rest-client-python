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


class Ptsv2paymentsRecipientInformation(object):
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
        'account_id': 'str',
        'last_name': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'last_name': 'lastName',
        'postal_code': 'postalCode'
    }

    def __init__(self, account_id=None, last_name=None, postal_code=None):
        """
        Ptsv2paymentsRecipientInformation - a model defined in Swagger
        """

        self._account_id = None
        self._last_name = None
        self._postal_code = None

        if account_id is not None:
          self.account_id = account_id
        if last_name is not None:
          self.last_name = last_name
        if postal_code is not None:
          self.postal_code = postal_code

    @property
    def account_id(self):
        """
        Gets the account_id of this Ptsv2paymentsRecipientInformation.
        Identifier for the recipient’s account. Use the first six digits and last four digits of the recipient’s account number. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see \"Recipients,\" page 224. 

        :return: The account_id of this Ptsv2paymentsRecipientInformation.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this Ptsv2paymentsRecipientInformation.
        Identifier for the recipient’s account. Use the first six digits and last four digits of the recipient’s account number. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see \"Recipients,\" page 224. 

        :param account_id: The account_id of this Ptsv2paymentsRecipientInformation.
        :type: str
        """
        if account_id is not None and len(account_id) > 10:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `10`")

        self._account_id = account_id

    @property
    def last_name(self):
        """
        Gets the last_name of this Ptsv2paymentsRecipientInformation.
        Recipient’s last name. This field is a passthrough, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see \"Recipients,\" page 224. 

        :return: The last_name of this Ptsv2paymentsRecipientInformation.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Ptsv2paymentsRecipientInformation.
        Recipient’s last name. This field is a passthrough, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see \"Recipients,\" page 224. 

        :param last_name: The last_name of this Ptsv2paymentsRecipientInformation.
        :type: str
        """
        if last_name is not None and len(last_name) > 6:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `6`")

        self._last_name = last_name

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2paymentsRecipientInformation.
        Partial postal code for the recipient’s address. For example, if the postal code is **NN5 7SG**, the value for this  field should be the first part of the postal code: **NN5**. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see \"Recipients,\" page 224. 

        :return: The postal_code of this Ptsv2paymentsRecipientInformation.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2paymentsRecipientInformation.
        Partial postal code for the recipient’s address. For example, if the postal code is **NN5 7SG**, the value for this  field should be the first part of the postal code: **NN5**. This field is a pass-through, which means that CyberSource does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see \"Recipients,\" page 224. 

        :param postal_code: The postal_code of this Ptsv2paymentsRecipientInformation.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 6:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `6`")

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
        if not isinstance(other, Ptsv2paymentsRecipientInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other