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


class Vasv2taxTaxInformation(object):
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
        'reporting_date': 'str',
        'date_override_reason': 'str',
        'nexus': 'list[str]',
        'no_nexus': 'list[str]',
        'show_tax_per_line_item': 'str',
        'commit_indicator': 'bool',
        'refund_indicator': 'bool'
    }

    attribute_map = {
        'reporting_date': 'reportingDate',
        'date_override_reason': 'dateOverrideReason',
        'nexus': 'nexus',
        'no_nexus': 'noNexus',
        'show_tax_per_line_item': 'showTaxPerLineItem',
        'commit_indicator': 'commitIndicator',
        'refund_indicator': 'refundIndicator'
    }

    def __init__(self, reporting_date=None, date_override_reason=None, nexus=None, no_nexus=None, show_tax_per_line_item=None, commit_indicator=None, refund_indicator=None):
        """
        Vasv2taxTaxInformation - a model defined in Swagger
        """

        self._reporting_date = None
        self._date_override_reason = None
        self._nexus = None
        self._no_nexus = None
        self._show_tax_per_line_item = None
        self._commit_indicator = None
        self._refund_indicator = None

        if reporting_date is not None:
          self.reporting_date = reporting_date
        if date_override_reason is not None:
          self.date_override_reason = date_override_reason
        if nexus is not None:
          self.nexus = nexus
        if no_nexus is not None:
          self.no_nexus = no_nexus
        if show_tax_per_line_item is not None:
          self.show_tax_per_line_item = show_tax_per_line_item
        if commit_indicator is not None:
          self.commit_indicator = commit_indicator
        if refund_indicator is not None:
          self.refund_indicator = refund_indicator

    @property
    def reporting_date(self):
        """
        Gets the reporting_date of this Vasv2taxTaxInformation.
        Reporting date of transaction. Format: YYYYMMDD. Defaults to current date if not specified. Optional for U.S., Canadian, international tax, and value added taxes. 

        :return: The reporting_date of this Vasv2taxTaxInformation.
        :rtype: str
        """
        return self._reporting_date

    @reporting_date.setter
    def reporting_date(self, reporting_date):
        """
        Sets the reporting_date of this Vasv2taxTaxInformation.
        Reporting date of transaction. Format: YYYYMMDD. Defaults to current date if not specified. Optional for U.S., Canadian, international tax, and value added taxes. 

        :param reporting_date: The reporting_date of this Vasv2taxTaxInformation.
        :type: str
        """



        self._reporting_date = reporting_date

    @property
    def date_override_reason(self):
        """
        Gets the date_override_reason of this Vasv2taxTaxInformation.
        If a past or future date is specified in `orderInformation.invoiceDetails.invoiceDate`, then provide the reason for that for audit purposes. Typical reasons include: 'Return', 'Layaway', 'Imported'.  Optional for U.S., Canadian, international tax, and value added taxes. 

        :return: The date_override_reason of this Vasv2taxTaxInformation.
        :rtype: str
        """
        return self._date_override_reason

    @date_override_reason.setter
    def date_override_reason(self, date_override_reason):
        """
        Sets the date_override_reason of this Vasv2taxTaxInformation.
        If a past or future date is specified in `orderInformation.invoiceDetails.invoiceDate`, then provide the reason for that for audit purposes. Typical reasons include: 'Return', 'Layaway', 'Imported'.  Optional for U.S., Canadian, international tax, and value added taxes. 

        :param date_override_reason: The date_override_reason of this Vasv2taxTaxInformation.
        :type: str
        """



        self._date_override_reason = date_override_reason

    @property
    def nexus(self):
        """
        Gets the nexus of this Vasv2taxTaxInformation.
        Comma-separated list of states or provinces in which merchandise is taxable. Note merchandise may be still be non-taxable or tax exempt depending on the product taxability. Indicate the type of product you are selling in the product code field for product-level taxability rules to be applied. Do not use both the `taxInformation.nexus` and `taxInformation.noNexus` fields in your request. If you do not include this field in a tax calculation service request, the tax system makes its calculations as if you have nexus in every US state or Canadian province. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  If you indicate you do not have nexus in the destination state, jurisdiction level fields are left blank in the Tax Detail Report.  Optional field for U.S. and Canadian taxes only. Either this field or `taxInformation.noNexus` is required if you do not have nexus in every state or province.  Not applicable for international and value added taxes. 

        :return: The nexus of this Vasv2taxTaxInformation.
        :rtype: list[str]
        """
        return self._nexus

    @nexus.setter
    def nexus(self, nexus):
        """
        Sets the nexus of this Vasv2taxTaxInformation.
        Comma-separated list of states or provinces in which merchandise is taxable. Note merchandise may be still be non-taxable or tax exempt depending on the product taxability. Indicate the type of product you are selling in the product code field for product-level taxability rules to be applied. Do not use both the `taxInformation.nexus` and `taxInformation.noNexus` fields in your request. If you do not include this field in a tax calculation service request, the tax system makes its calculations as if you have nexus in every US state or Canadian province. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  If you indicate you do not have nexus in the destination state, jurisdiction level fields are left blank in the Tax Detail Report.  Optional field for U.S. and Canadian taxes only. Either this field or `taxInformation.noNexus` is required if you do not have nexus in every state or province.  Not applicable for international and value added taxes. 

        :param nexus: The nexus of this Vasv2taxTaxInformation.
        :type: list[str]
        """



        self._nexus = nexus

    @property
    def no_nexus(self):
        """
        Gets the no_nexus of this Vasv2taxTaxInformation.
        Comma-separated list of states or provinces where you do not have nexus. Check with a tax advisor to determine where your business has nexus. Do not use both the `taxInformation.nexus` and `taxInformation.noNexus` fields in your request. If you do not include this field in a tax calculation service request, the tax system makes its calculations as if you have nexus in every US state or Canadian province. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  If you indicate you do not have nexus in the destination state, jurisdiction level fields are left blank in the Tax Detail Report.  Optional field for U.S. and Canadian taxes only. Either this field or `taxInformation.nexus` is required if you do not have nexus in every state or province.  Not applicable for international and value added taxes. 

        :return: The no_nexus of this Vasv2taxTaxInformation.
        :rtype: list[str]
        """
        return self._no_nexus

    @no_nexus.setter
    def no_nexus(self, no_nexus):
        """
        Sets the no_nexus of this Vasv2taxTaxInformation.
        Comma-separated list of states or provinces where you do not have nexus. Check with a tax advisor to determine where your business has nexus. Do not use both the `taxInformation.nexus` and `taxInformation.noNexus` fields in your request. If you do not include this field in a tax calculation service request, the tax system makes its calculations as if you have nexus in every US state or Canadian province. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  If you indicate you do not have nexus in the destination state, jurisdiction level fields are left blank in the Tax Detail Report.  Optional field for U.S. and Canadian taxes only. Either this field or `taxInformation.nexus` is required if you do not have nexus in every state or province.  Not applicable for international and value added taxes. 

        :param no_nexus: The no_nexus of this Vasv2taxTaxInformation.
        :type: list[str]
        """



        self._no_nexus = no_nexus

    @property
    def show_tax_per_line_item(self):
        """
        Gets the show_tax_per_line_item of this Vasv2taxTaxInformation.
        Whether or not to display tax amounts for each line item. This field can contain one of the following values: - `Yes` - Display tax amounts for each line item - `No` (default) - Do not display tax amounts for each line item  Optional for U.S., Canadian, international tax, and value added taxes. 

        :return: The show_tax_per_line_item of this Vasv2taxTaxInformation.
        :rtype: str
        """
        return self._show_tax_per_line_item

    @show_tax_per_line_item.setter
    def show_tax_per_line_item(self, show_tax_per_line_item):
        """
        Sets the show_tax_per_line_item of this Vasv2taxTaxInformation.
        Whether or not to display tax amounts for each line item. This field can contain one of the following values: - `Yes` - Display tax amounts for each line item - `No` (default) - Do not display tax amounts for each line item  Optional for U.S., Canadian, international tax, and value added taxes. 

        :param show_tax_per_line_item: The show_tax_per_line_item of this Vasv2taxTaxInformation.
        :type: str
        """



        self._show_tax_per_line_item = show_tax_per_line_item

    @property
    def commit_indicator(self):
        """
        Gets the commit_indicator of this Vasv2taxTaxInformation.
        Indicates whether this is a committed tax transaction. For a committed tax transaction, the status in the Tax Detail Report is \"Committed.\" For an uncommitted tax transaction, the status in the Tax Detail Report is \"Uncommitted.\" Possible values: - `true`: This is a committed tax transaction. - `false` (default): This is not a committed tax transaction.  A committed tax request is a tax service request that sets the status field in the Tax Detail Report to committed. The committed status indicates that the amount calculated by the tax service is included in the amount of a capture or credit.  Use a void service request to cancel a committed tax request or a committed refund tax request. The void transaction is included as a separate entry in the Tax Detail Report. The value of the status field is cancelled. The value of the link ID is the request ID of the committed tax request or refund tax request that was voided. You can use the value of the link ID to reconcile your orders.  Optional for U.S., Canadian, international tax, and value added taxes. For more information on Tax Detail Report features refer the [Tax Service Guide](https://developer.cybersource.com/docs/cybs/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview.html). 

        :return: The commit_indicator of this Vasv2taxTaxInformation.
        :rtype: bool
        """
        return self._commit_indicator

    @commit_indicator.setter
    def commit_indicator(self, commit_indicator):
        """
        Sets the commit_indicator of this Vasv2taxTaxInformation.
        Indicates whether this is a committed tax transaction. For a committed tax transaction, the status in the Tax Detail Report is \"Committed.\" For an uncommitted tax transaction, the status in the Tax Detail Report is \"Uncommitted.\" Possible values: - `true`: This is a committed tax transaction. - `false` (default): This is not a committed tax transaction.  A committed tax request is a tax service request that sets the status field in the Tax Detail Report to committed. The committed status indicates that the amount calculated by the tax service is included in the amount of a capture or credit.  Use a void service request to cancel a committed tax request or a committed refund tax request. The void transaction is included as a separate entry in the Tax Detail Report. The value of the status field is cancelled. The value of the link ID is the request ID of the committed tax request or refund tax request that was voided. You can use the value of the link ID to reconcile your orders.  Optional for U.S., Canadian, international tax, and value added taxes. For more information on Tax Detail Report features refer the [Tax Service Guide](https://developer.cybersource.com/docs/cybs/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview.html). 

        :param commit_indicator: The commit_indicator of this Vasv2taxTaxInformation.
        :type: bool
        """



        self._commit_indicator = commit_indicator

    @property
    def refund_indicator(self):
        """
        Gets the refund_indicator of this Vasv2taxTaxInformation.
        Indicates whether this is a refund tax transaction. For a refund tax transaction, amounts in the Tax Detail Report will be negative. Possible values: - `true`: This is a refund tax transaction. - `false` (default): This is not a refund tax transaction.  A refund tax request is a tax service request that sets the transaction type field in the Tax Detail Report to refunded and makes the reported amount negative. Tax amounts are returned as positive amounts in reply messages, but they are saved in reports as negative amounts which enables the reporting software to accurately calculate the aggregate amounts.  Optional for U.S., Canadian, international tax, and value added taxes. For more information on Tax Detail Report features refer the [Tax Service Guide](https://developer.cybersource.com/docs/cybs/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview.html). 

        :return: The refund_indicator of this Vasv2taxTaxInformation.
        :rtype: bool
        """
        return self._refund_indicator

    @refund_indicator.setter
    def refund_indicator(self, refund_indicator):
        """
        Sets the refund_indicator of this Vasv2taxTaxInformation.
        Indicates whether this is a refund tax transaction. For a refund tax transaction, amounts in the Tax Detail Report will be negative. Possible values: - `true`: This is a refund tax transaction. - `false` (default): This is not a refund tax transaction.  A refund tax request is a tax service request that sets the transaction type field in the Tax Detail Report to refunded and makes the reported amount negative. Tax amounts are returned as positive amounts in reply messages, but they are saved in reports as negative amounts which enables the reporting software to accurately calculate the aggregate amounts.  Optional for U.S., Canadian, international tax, and value added taxes. For more information on Tax Detail Report features refer the [Tax Service Guide](https://developer.cybersource.com/docs/cybs/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview.html). 

        :param refund_indicator: The refund_indicator of this Vasv2taxTaxInformation.
        :type: bool
        """



        self._refund_indicator = refund_indicator

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
        if not isinstance(other, Vasv2taxTaxInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
