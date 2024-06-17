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


class CardProcessingConfigFeaturesCardNotPresentInstallment(object):
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
        'enable_installment': 'bool',
        'installment_plan': 'str'
    }

    attribute_map = {
        'enable_installment': 'enableInstallment',
        'installment_plan': 'installmentPlan'
    }

    def __init__(self, enable_installment=None, installment_plan=None):
        """
        CardProcessingConfigFeaturesCardNotPresentInstallment - a model defined in Swagger
        """

        self._enable_installment = None
        self._installment_plan = None

        if enable_installment is not None:
          self.enable_installment = enable_installment
        if installment_plan is not None:
          self.installment_plan = installment_plan

    @property
    def enable_installment(self):
        """
        Gets the enable_installment of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        This flag is to enable for installment plan programs. Applicable for Fiserv (fiserv), Vero (vero) and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Default Value</th></tr></thead> <tr><td>American Express Direct</td><td>cnp</td><td>No</td><td>No</td></tr> </table> 

        :return: The enable_installment of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        :rtype: bool
        """
        return self._enable_installment

    @enable_installment.setter
    def enable_installment(self, enable_installment):
        """
        Sets the enable_installment of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        This flag is to enable for installment plan programs. Applicable for Fiserv (fiserv), Vero (vero) and American Express Direct (amexdirect) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th><th>Default Value</th></tr></thead> <tr><td>American Express Direct</td><td>cnp</td><td>No</td><td>No</td></tr> </table> 

        :param enable_installment: The enable_installment of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        :type: bool
        """



        self._enable_installment = enable_installment

    @property
    def installment_plan(self):
        """
        Gets the installment_plan of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        This indicates the type of funding for the installment plan associated with the payment.  Valid values: \"merchant\" - Merchant-funded installment plan \"issuer\" - Issuer-funded installment plan  Applicable for Fiserv (fiserv), American Express Direct (amexdirect) and Vero (vero) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th></tr></thead> <tr><td>American Express Direct</td><td>cnp</td><td>No</td></tr> </table> 

        :return: The installment_plan of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        :rtype: str
        """
        return self._installment_plan

    @installment_plan.setter
    def installment_plan(self, installment_plan):
        """
        Sets the installment_plan of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        This indicates the type of funding for the installment plan associated with the payment.  Valid values: \"merchant\" - Merchant-funded installment plan \"issuer\" - Issuer-funded installment plan  Applicable for Fiserv (fiserv), American Express Direct (amexdirect) and Vero (vero) processors.  Validation details (for selected processors)...  <table> <thead><tr><th>Processor</th><th>Acceptance Type</th><th>Required</th></tr></thead> <tr><td>American Express Direct</td><td>cnp</td><td>No</td></tr> </table> 

        :param installment_plan: The installment_plan of this CardProcessingConfigFeaturesCardNotPresentInstallment.
        :type: str
        """



        self._installment_plan = installment_plan

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
        if not isinstance(other, CardProcessingConfigFeaturesCardNotPresentInstallment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
