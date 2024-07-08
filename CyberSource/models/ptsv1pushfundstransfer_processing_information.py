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


class Ptsv1pushfundstransferProcessingInformation(object):
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
        'business_application_id': 'str',
        'payouts_options': 'Ptsv1pushfundstransferProcessingInformationPayoutsOptions'
    }

    attribute_map = {
        'business_application_id': 'businessApplicationId',
        'payouts_options': 'payoutsOptions'
    }

    def __init__(self, business_application_id=None, payouts_options=None):
        """
        Ptsv1pushfundstransferProcessingInformation - a model defined in Swagger
        """

        self._business_application_id = None
        self._payouts_options = None

        if business_application_id is not None:
          self.business_application_id = business_application_id
        if payouts_options is not None:
          self.payouts_options = payouts_options

    @property
    def business_application_id(self):
        """
        Gets the business_application_id of this Ptsv1pushfundstransferProcessingInformation.
        Payouts transaction type.  Business Application ID: - `PP`: Person to person. - `FD`: Funds disbursement (general) 

        :return: The business_application_id of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: str
        """
        return self._business_application_id

    @business_application_id.setter
    def business_application_id(self, business_application_id):
        """
        Sets the business_application_id of this Ptsv1pushfundstransferProcessingInformation.
        Payouts transaction type.  Business Application ID: - `PP`: Person to person. - `FD`: Funds disbursement (general) 

        :param business_application_id: The business_application_id of this Ptsv1pushfundstransferProcessingInformation.
        :type: str
        """

        self._business_application_id = business_application_id

    @property
    def payouts_options(self):
        """
        Gets the payouts_options of this Ptsv1pushfundstransferProcessingInformation.

        :return: The payouts_options of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: Ptsv1pushfundstransferProcessingInformationPayoutsOptions
        """
        return self._payouts_options

    @payouts_options.setter
    def payouts_options(self, payouts_options):
        """
        Sets the payouts_options of this Ptsv1pushfundstransferProcessingInformation.

        :param payouts_options: The payouts_options of this Ptsv1pushfundstransferProcessingInformation.
        :type: Ptsv1pushfundstransferProcessingInformationPayoutsOptions
        """

        self._payouts_options = payouts_options

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
        if not isinstance(other, Ptsv1pushfundstransferProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
