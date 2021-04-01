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


class Ptsv2paymentsidreversalsProcessingInformation(object):
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
        'payment_solution': 'str',
        'reconciliation_id': 'str',
        'link_id': 'str',
        'report_group': 'str',
        'visa_checkout_id': 'str',
        'issuer': 'Ptsv2paymentsIssuerInformation'
    }

    attribute_map = {
        'payment_solution': 'paymentSolution',
        'reconciliation_id': 'reconciliationId',
        'link_id': 'linkId',
        'report_group': 'reportGroup',
        'visa_checkout_id': 'visaCheckoutId',
        'issuer': 'issuer'
    }

    def __init__(self, payment_solution=None, reconciliation_id=None, link_id=None, report_group=None, visa_checkout_id=None, issuer=None):
        """
        Ptsv2paymentsidreversalsProcessingInformation - a model defined in Swagger
        """

        self._payment_solution = None
        self._reconciliation_id = None
        self._link_id = None
        self._report_group = None
        self._visa_checkout_id = None
        self._issuer = None

        if payment_solution is not None:
          self.payment_solution = payment_solution
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if link_id is not None:
          self.link_id = link_id
        if report_group is not None:
          self.report_group = report_group
        if visa_checkout_id is not None:
          self.visa_checkout_id = visa_checkout_id
        if issuer is not None:
          self.issuer = issuer

    @property
    def payment_solution(self):
        """
        Gets the payment_solution of this Ptsv2paymentsidreversalsProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay.  - `014`: Mastercard credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - `015`: Visa credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token. 

        :return: The payment_solution of this Ptsv2paymentsidreversalsProcessingInformation.
        :rtype: str
        """
        return self._payment_solution

    @payment_solution.setter
    def payment_solution(self, payment_solution):
        """
        Sets the payment_solution of this Ptsv2paymentsidreversalsProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/VCO_SCMP_API/html/)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct. For details, see \"Masterpass\" in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay.  - `014`: Mastercard credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - `015`: Visa credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token. 

        :param payment_solution: The payment_solution of this Ptsv2paymentsidreversalsProcessingInformation.
        :type: str
        """

        self._payment_solution = payment_solution

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv2paymentsidreversalsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :return: The reconciliation_id of this Ptsv2paymentsidreversalsProcessingInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv2paymentsidreversalsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :param reconciliation_id: The reconciliation_id of this Ptsv2paymentsidreversalsProcessingInformation.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def link_id(self):
        """
        Gets the link_id of this Ptsv2paymentsidreversalsProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments  For details, see `link_to_request` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The link_id of this Ptsv2paymentsidreversalsProcessingInformation.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """
        Sets the link_id of this Ptsv2paymentsidreversalsProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments  For details, see `link_to_request` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param link_id: The link_id of this Ptsv2paymentsidreversalsProcessingInformation.
        :type: str
        """

        self._link_id = link_id

    @property
    def report_group(self):
        """
        Gets the report_group of this Ptsv2paymentsidreversalsProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**.  For details, see `report_group` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The report_group of this Ptsv2paymentsidreversalsProcessingInformation.
        :rtype: str
        """
        return self._report_group

    @report_group.setter
    def report_group(self, report_group):
        """
        Sets the report_group of this Ptsv2paymentsidreversalsProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**.  For details, see `report_group` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param report_group: The report_group of this Ptsv2paymentsidreversalsProcessingInformation.
        :type: str
        """

        self._report_group = report_group

    @property
    def visa_checkout_id(self):
        """
        Gets the visa_checkout_id of this Ptsv2paymentsidreversalsProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field. 

        :return: The visa_checkout_id of this Ptsv2paymentsidreversalsProcessingInformation.
        :rtype: str
        """
        return self._visa_checkout_id

    @visa_checkout_id.setter
    def visa_checkout_id(self, visa_checkout_id):
        """
        Sets the visa_checkout_id of this Ptsv2paymentsidreversalsProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field. 

        :param visa_checkout_id: The visa_checkout_id of this Ptsv2paymentsidreversalsProcessingInformation.
        :type: str
        """

        self._visa_checkout_id = visa_checkout_id

    @property
    def issuer(self):
        """
        Gets the issuer of this Ptsv2paymentsidreversalsProcessingInformation.

        :return: The issuer of this Ptsv2paymentsidreversalsProcessingInformation.
        :rtype: Ptsv2paymentsIssuerInformation
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this Ptsv2paymentsidreversalsProcessingInformation.

        :param issuer: The issuer of this Ptsv2paymentsidreversalsProcessingInformation.
        :type: Ptsv2paymentsIssuerInformation
        """

        self._issuer = issuer

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
        if not isinstance(other, Ptsv2paymentsidreversalsProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
