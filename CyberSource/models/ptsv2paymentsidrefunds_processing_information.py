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


class Ptsv2paymentsidrefundsProcessingInformation(object):
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
        'action_list': 'list[str]',
        'payment_solution': 'str',
        'reconciliation_id': 'str',
        'link_id': 'str',
        'report_group': 'str',
        'visa_checkout_id': 'str',
        'purchase_level': 'str',
        'recurring_options': 'Ptsv2paymentsidrefundsProcessingInformationRecurringOptions',
        'industry_data_type': 'str',
        'payment_type': 'str',
        'refund_options': 'Ptsv2paymentsidrefundsProcessingInformationRefundOptions'
    }

    attribute_map = {
        'action_list': 'actionList',
        'payment_solution': 'paymentSolution',
        'reconciliation_id': 'reconciliationId',
        'link_id': 'linkId',
        'report_group': 'reportGroup',
        'visa_checkout_id': 'visaCheckoutId',
        'purchase_level': 'purchaseLevel',
        'recurring_options': 'recurringOptions',
        'industry_data_type': 'industryDataType',
        'payment_type': 'paymentType',
        'refund_options': 'refundOptions'
    }

    def __init__(self, action_list=None, payment_solution=None, reconciliation_id=None, link_id=None, report_group=None, visa_checkout_id=None, purchase_level=None, recurring_options=None, industry_data_type=None, payment_type=None, refund_options=None):
        """
        Ptsv2paymentsidrefundsProcessingInformation - a model defined in Swagger
        """

        self._action_list = None
        self._payment_solution = None
        self._reconciliation_id = None
        self._link_id = None
        self._report_group = None
        self._visa_checkout_id = None
        self._purchase_level = None
        self._recurring_options = None
        self._industry_data_type = None
        self._payment_type = None
        self._refund_options = None

        if action_list is not None:
          self.action_list = action_list
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
        if purchase_level is not None:
          self.purchase_level = purchase_level
        if recurring_options is not None:
          self.recurring_options = recurring_options
        if industry_data_type is not None:
          self.industry_data_type = industry_data_type
        if payment_type is not None:
          self.payment_type = payment_type
        if refund_options is not None:
          self.refund_options = refund_options

    @property
    def action_list(self):
        """
        Gets the action_list of this Ptsv2paymentsidrefundsProcessingInformation.
        Array of actions (one or more) to be included in the payment to invoke bundled services along with payment status.  Possible values are one or more of follows:   - `AP_REFUND`: Use this when Alternative Payment Refund service is requested. 

        :return: The action_list of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: list[str]
        """
        return self._action_list

    @action_list.setter
    def action_list(self, action_list):
        """
        Sets the action_list of this Ptsv2paymentsidrefundsProcessingInformation.
        Array of actions (one or more) to be included in the payment to invoke bundled services along with payment status.  Possible values are one or more of follows:   - `AP_REFUND`: Use this when Alternative Payment Refund service is requested. 

        :param action_list: The action_list of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: list[str]
        """

        self._action_list = action_list

    @property
    def payment_solution(self):
        """
        Gets the payment_solution of this Ptsv2paymentsidrefundsProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the REST API.](https://developer.cybersource.com/content/dam/docs/cybs/en-us/apifields/reference/all/rest/api-fields.pdf)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct.   - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay.  - `013`: Cybersource P2PE Decryption  - `014`: Mastercard credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - `015`: Visa credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - `027`: Click to Pay. 

        :return: The payment_solution of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._payment_solution

    @payment_solution.setter
    def payment_solution(self, payment_solution):
        """
        Sets the payment_solution of this Ptsv2paymentsidrefundsProcessingInformation.
        Type of digital payment solution for the transaction. Possible Values:   - `visacheckout`: Visa Checkout. This value is required for Visa Checkout transactions. For details, see `payment_solution` field description in [Visa Checkout Using the REST API.](https://developer.cybersource.com/content/dam/docs/cybs/en-us/apifields/reference/all/rest/api-fields.pdf)  - `001`: Apple Pay.  - `004`: Cybersource In-App Solution.  - `005`: Masterpass. This value is required for Masterpass transactions on OmniPay Direct.   - `006`: Android Pay.  - `007`: Chase Pay.  - `008`: Samsung Pay.  - `012`: Google Pay.  - `013`: Cybersource P2PE Decryption  - `014`: Mastercard credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - `015`: Visa credential on file (COF) payment network token. Returned in authorizations that use a payment network token associated with a TMS token.  - `027`: Click to Pay. 

        :param payment_solution: The payment_solution of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._payment_solution = payment_solution

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv2paymentsidrefundsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :return: The reconciliation_id of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv2paymentsidrefundsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :param reconciliation_id: The reconciliation_id of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def link_id(self):
        """
        Gets the link_id of this Ptsv2paymentsidrefundsProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments 

        :return: The link_id of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """
        Sets the link_id of this Ptsv2paymentsidrefundsProcessingInformation.
        Value that links the current authorization request to the original authorization request. Set this value to the ID that was returned in the reply message from the original authorization request.  This value is used for:  - Partial authorizations - Split shipments 

        :param link_id: The link_id of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._link_id = link_id

    @property
    def report_group(self):
        """
        Gets the report_group of this Ptsv2paymentsidrefundsProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**. 

        :return: The report_group of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._report_group

    @report_group.setter
    def report_group(self, report_group):
        """
        Sets the report_group of this Ptsv2paymentsidrefundsProcessingInformation.
        Attribute that lets you define custom grouping for your processor reports. This field is supported only for **Worldpay VAP**. 

        :param report_group: The report_group of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._report_group = report_group

    @property
    def visa_checkout_id(self):
        """
        Gets the visa_checkout_id of this Ptsv2paymentsidrefundsProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field. 

        :return: The visa_checkout_id of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._visa_checkout_id

    @visa_checkout_id.setter
    def visa_checkout_id(self, visa_checkout_id):
        """
        Sets the visa_checkout_id of this Ptsv2paymentsidrefundsProcessingInformation.
        Identifier for the **Visa Checkout** order. Visa Checkout provides a unique order ID for every transaction in the Visa Checkout **callID** field. 

        :param visa_checkout_id: The visa_checkout_id of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._visa_checkout_id = visa_checkout_id

    @property
    def purchase_level(self):
        """
        Gets the purchase_level of this Ptsv2paymentsidrefundsProcessingInformation.
        Set this field to 3 to indicate that the request includes Level III data.

        :return: The purchase_level of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._purchase_level

    @purchase_level.setter
    def purchase_level(self, purchase_level):
        """
        Sets the purchase_level of this Ptsv2paymentsidrefundsProcessingInformation.
        Set this field to 3 to indicate that the request includes Level III data.

        :param purchase_level: The purchase_level of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._purchase_level = purchase_level

    @property
    def recurring_options(self):
        """
        Gets the recurring_options of this Ptsv2paymentsidrefundsProcessingInformation.

        :return: The recurring_options of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: Ptsv2paymentsidrefundsProcessingInformationRecurringOptions
        """
        return self._recurring_options

    @recurring_options.setter
    def recurring_options(self, recurring_options):
        """
        Sets the recurring_options of this Ptsv2paymentsidrefundsProcessingInformation.

        :param recurring_options: The recurring_options of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: Ptsv2paymentsidrefundsProcessingInformationRecurringOptions
        """

        self._recurring_options = recurring_options

    @property
    def industry_data_type(self):
        """
        Gets the industry_data_type of this Ptsv2paymentsidrefundsProcessingInformation.
        Indicates that the transaction includes industry-specific data.  Possible Values: - `airline` - `restaurant` - `lodging` - `auto_rental` - `transit` - `healthcare_medical` - `healthcare_transit` - `transit`  #### Card Present, Airlines and Auto Rental You must set this field to `airline` in order for airline data to be sent to the processor. For example, if this field is not set to `airline` or is not included in the request, no airline data is sent to the processor.  You must set this field to `restaurant` in order for restaurant data to be sent to the processor. When this field is not set to `restaurant` or is not included in the request, no restaurant data is sent to the processor.  You must set this field to `auto_rental` in order for auto rental data to be sent to the processor. For example, if this field is not set to `auto_rental` or is not included in the request, no auto rental data is sent to the processor.  Restaurant data is supported only on CyberSource through VisaNet. 

        :return: The industry_data_type of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._industry_data_type

    @industry_data_type.setter
    def industry_data_type(self, industry_data_type):
        """
        Sets the industry_data_type of this Ptsv2paymentsidrefundsProcessingInformation.
        Indicates that the transaction includes industry-specific data.  Possible Values: - `airline` - `restaurant` - `lodging` - `auto_rental` - `transit` - `healthcare_medical` - `healthcare_transit` - `transit`  #### Card Present, Airlines and Auto Rental You must set this field to `airline` in order for airline data to be sent to the processor. For example, if this field is not set to `airline` or is not included in the request, no airline data is sent to the processor.  You must set this field to `restaurant` in order for restaurant data to be sent to the processor. When this field is not set to `restaurant` or is not included in the request, no restaurant data is sent to the processor.  You must set this field to `auto_rental` in order for auto rental data to be sent to the processor. For example, if this field is not set to `auto_rental` or is not included in the request, no auto rental data is sent to the processor.  Restaurant data is supported only on CyberSource through VisaNet. 

        :param industry_data_type: The industry_data_type of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._industry_data_type = industry_data_type

    @property
    def payment_type(self):
        """
        Gets the payment_type of this Ptsv2paymentsidrefundsProcessingInformation.
        Identifier for the payment type

        :return: The payment_type of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """
        Sets the payment_type of this Ptsv2paymentsidrefundsProcessingInformation.
        Identifier for the payment type

        :param payment_type: The payment_type of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: str
        """

        self._payment_type = payment_type

    @property
    def refund_options(self):
        """
        Gets the refund_options of this Ptsv2paymentsidrefundsProcessingInformation.

        :return: The refund_options of this Ptsv2paymentsidrefundsProcessingInformation.
        :rtype: Ptsv2paymentsidrefundsProcessingInformationRefundOptions
        """
        return self._refund_options

    @refund_options.setter
    def refund_options(self, refund_options):
        """
        Sets the refund_options of this Ptsv2paymentsidrefundsProcessingInformation.

        :param refund_options: The refund_options of this Ptsv2paymentsidrefundsProcessingInformation.
        :type: Ptsv2paymentsidrefundsProcessingInformationRefundOptions
        """

        self._refund_options = refund_options

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
        if not isinstance(other, Ptsv2paymentsidrefundsProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
