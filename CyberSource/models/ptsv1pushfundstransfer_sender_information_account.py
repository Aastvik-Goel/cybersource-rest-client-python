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


class Ptsv1pushfundstransferSenderInformationAccount(object):
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
        'funds_source': 'str',
        'number': 'str'
    }

    attribute_map = {
        'funds_source': 'fundsSource',
        'number': 'number'
    }

    def __init__(self, funds_source=None, number=None):
        """
        Ptsv1pushfundstransferSenderInformationAccount - a model defined in Swagger
        """

        self._funds_source = None
        self._number = None

        if funds_source is not None:
          self.funds_source = funds_source
        if number is not None:
          self.number = number

    @property
    def funds_source(self):
        """
        Gets the funds_source of this Ptsv1pushfundstransferSenderInformationAccount.
        Source of funds. Possible values:  Chase Paymentech, FDC Compass, Visa Platform Connect:  - `01`: Credit card - `02`: Debit card - `03`: Prepaid card  Chase Paymentech, Visa Platform Connect:  - `04`: Cash - `05`: Debit or deposit account that is not linked to a Visa card. Includes checking accounts, savings accounts, and proprietary debit or ATM cards. - `06`: Credit account that is not linked to a Visa card. Includes credit cards and proprietary lines of credit.  FDC Compass: - `04`: Deposit Account  Funds Disbursement This value is most likely 05 to identify that the originator used a deposit account to fund the disbursement.  Credit Card Bill Payment This value must be 02, 03, 04, or 05. 

        :return: The funds_source of this Ptsv1pushfundstransferSenderInformationAccount.
        :rtype: str
        """
        return self._funds_source

    @funds_source.setter
    def funds_source(self, funds_source):
        """
        Sets the funds_source of this Ptsv1pushfundstransferSenderInformationAccount.
        Source of funds. Possible values:  Chase Paymentech, FDC Compass, Visa Platform Connect:  - `01`: Credit card - `02`: Debit card - `03`: Prepaid card  Chase Paymentech, Visa Platform Connect:  - `04`: Cash - `05`: Debit or deposit account that is not linked to a Visa card. Includes checking accounts, savings accounts, and proprietary debit or ATM cards. - `06`: Credit account that is not linked to a Visa card. Includes credit cards and proprietary lines of credit.  FDC Compass: - `04`: Deposit Account  Funds Disbursement This value is most likely 05 to identify that the originator used a deposit account to fund the disbursement.  Credit Card Bill Payment This value must be 02, 03, 04, or 05. 

        :param funds_source: The funds_source of this Ptsv1pushfundstransferSenderInformationAccount.
        :type: str
        """

        self._funds_source = funds_source

    @property
    def number(self):
        """
        Gets the number of this Ptsv1pushfundstransferSenderInformationAccount.
        The account number of the entity funding the transaction. It is the sender's account number. It can be a debit/credit card account number or bank account number.  Funds disbursements  This field is optional.  All other transactions  This field is required when the sender funds the transaction with a financial instrument, for example debit card. Length: 

        :return: The number of this Ptsv1pushfundstransferSenderInformationAccount.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Ptsv1pushfundstransferSenderInformationAccount.
        The account number of the entity funding the transaction. It is the sender's account number. It can be a debit/credit card account number or bank account number.  Funds disbursements  This field is optional.  All other transactions  This field is required when the sender funds the transaction with a financial instrument, for example debit card. Length: 

        :param number: The number of this Ptsv1pushfundstransferSenderInformationAccount.
        :type: str
        """

        self._number = number

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
        if not isinstance(other, Ptsv1pushfundstransferSenderInformationAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
