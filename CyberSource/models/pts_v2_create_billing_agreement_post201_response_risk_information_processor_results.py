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


class PtsV2CreateBillingAgreementPost201ResponseRiskInformationProcessorResults(object):
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
        'risk_score': 'str'
    }

    attribute_map = {
        'risk_score': 'riskScore'
    }

    def __init__(self, risk_score=None):
        """
        PtsV2CreateBillingAgreementPost201ResponseRiskInformationProcessorResults - a model defined in Swagger
        """

        self._risk_score = None

        if risk_score is not None:
          self.risk_score = risk_score

    @property
    def risk_score(self):
        """
        Gets the risk_score of this PtsV2CreateBillingAgreementPost201ResponseRiskInformationProcessorResults.
        Risk score returned by the processor. Possible values of 0-10. A value of 10 indicates a high risk. 

        :return: The risk_score of this PtsV2CreateBillingAgreementPost201ResponseRiskInformationProcessorResults.
        :rtype: str
        """
        return self._risk_score

    @risk_score.setter
    def risk_score(self, risk_score):
        """
        Sets the risk_score of this PtsV2CreateBillingAgreementPost201ResponseRiskInformationProcessorResults.
        Risk score returned by the processor. Possible values of 0-10. A value of 10 indicates a high risk. 

        :param risk_score: The risk_score of this PtsV2CreateBillingAgreementPost201ResponseRiskInformationProcessorResults.
        :type: str
        """

        self._risk_score = risk_score

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
        if not isinstance(other, PtsV2CreateBillingAgreementPost201ResponseRiskInformationProcessorResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
