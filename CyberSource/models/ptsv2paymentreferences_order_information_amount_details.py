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


class Ptsv2paymentreferencesOrderInformationAmountDetails(object):
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
        'total_amount': 'str',
        'currency': 'str',
        'discount_amount': 'str',
        'tax_amount': 'str',
        'duty_amount': 'str',
        'exchange_rate': 'str',
        'exchange_rate_time_stamp': 'str',
        'settlement_currency': 'str',
        'giftwrap_amount': 'str',
        'handling_amount': 'str',
        'shipping_amount': 'str',
        'shipping_discount_amount': 'str',
        'insurance_amount': 'str'
    }

    attribute_map = {
        'total_amount': 'totalAmount',
        'currency': 'currency',
        'discount_amount': 'discountAmount',
        'tax_amount': 'taxAmount',
        'duty_amount': 'dutyAmount',
        'exchange_rate': 'exchangeRate',
        'exchange_rate_time_stamp': 'exchangeRateTimeStamp',
        'settlement_currency': 'settlementCurrency',
        'giftwrap_amount': 'giftwrapAmount',
        'handling_amount': 'handlingAmount',
        'shipping_amount': 'shippingAmount',
        'shipping_discount_amount': 'shippingDiscountAmount',
        'insurance_amount': 'insuranceAmount'
    }

    def __init__(self, total_amount=None, currency=None, discount_amount=None, tax_amount=None, duty_amount=None, exchange_rate=None, exchange_rate_time_stamp=None, settlement_currency=None, giftwrap_amount=None, handling_amount=None, shipping_amount=None, shipping_discount_amount=None, insurance_amount=None):
        """
        Ptsv2paymentreferencesOrderInformationAmountDetails - a model defined in Swagger
        """

        self._total_amount = None
        self._currency = None
        self._discount_amount = None
        self._tax_amount = None
        self._duty_amount = None
        self._exchange_rate = None
        self._exchange_rate_time_stamp = None
        self._settlement_currency = None
        self._giftwrap_amount = None
        self._handling_amount = None
        self._shipping_amount = None
        self._shipping_discount_amount = None
        self._insurance_amount = None

        if total_amount is not None:
          self.total_amount = total_amount
        if currency is not None:
          self.currency = currency
        if discount_amount is not None:
          self.discount_amount = discount_amount
        if tax_amount is not None:
          self.tax_amount = tax_amount
        if duty_amount is not None:
          self.duty_amount = duty_amount
        if exchange_rate is not None:
          self.exchange_rate = exchange_rate
        if exchange_rate_time_stamp is not None:
          self.exchange_rate_time_stamp = exchange_rate_time_stamp
        if settlement_currency is not None:
          self.settlement_currency = settlement_currency
        if giftwrap_amount is not None:
          self.giftwrap_amount = giftwrap_amount
        if handling_amount is not None:
          self.handling_amount = handling_amount
        if shipping_amount is not None:
          self.shipping_amount = shipping_amount
        if shipping_discount_amount is not None:
          self.shipping_discount_amount = shipping_discount_amount
        if insurance_amount is not None:
          self.insurance_amount = insurance_amount

    @property
    def total_amount(self):
        """
        Gets the total_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. For details, see: - \"Authorization Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Capture Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Credit Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. For details, see \"Zero Amount Authorizations,\" \"Credit Information for Specific Processors\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Card Present Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.  #### Invoicing Required for creating a new invoice.  #### PIN Debit Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. For details, see `grand_total_amount` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in \"Authorization Information for Specific Processors\" of the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC for First Data Not used. 

        :return: The total_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  **Note** For CTV, FDCCompass, Paymentech processors, the maximum length for this field is 12.  **Important** Some processors have specific requirements and limitations, such as maximum amounts and maximum field lengths. For details, see: - \"Authorization Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Capture Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/). - \"Credit Information for Specific Processors\" in the [Credit Card Services Using the SCMP API Guide](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/).  If your processor supports zero amount authorizations, you can set this field to 0 for the authorization to check if the card is lost or stolen. For details, see \"Zero Amount Authorizations,\" \"Credit Information for Specific Processors\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### Card Present Required to include either this field or `orderInformation.lineItems[].unitPrice` for the order.  #### Invoicing Required for creating a new invoice.  #### PIN Debit Amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount.  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit; however, for all other processors, these fields are required.  #### DCC with a Third-Party Provider Set this field to the converted amount that was returned by the DCC provider. You must include either this field or the 1st line item in the order and the specific line-order amount in your request. For details, see `grand_total_amount` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### FDMS South If you accept IDR or CLP currencies, see the entry for FDMS South in \"Authorization Information for Specific Processors\" of the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### DCC for First Data Not used. 

        :param total_amount: The total_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._total_amount = total_amount

    @property
    def currency(self):
        """
        Gets the currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :return: The currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Currency used for the order. Use the three-character [ISO Standard Currency Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf)  #### Used by **Authorization** Required field.  **Authorization Reversal** For an authorization reversal (`reversalInformation`) or a capture (`processingOptions.capture` is set to `true`), you must use the same currency that you used in your payment authorization request.  #### PIN Debit Currency for the amount you requested for the PIN debit purchase. This value is returned for partial authorizations. The issuing bank can approve a partial amount if the balance on the debit card is less than the requested transaction amount. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf). Returned by PIN debit purchase.  For PIN debit reversal requests, you must use the same currency that was used for the PIN debit purchase or PIN debit credit that you are reversing. For the possible values, see the [ISO Standard Currency Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/currencies.pdf).  Required field for PIN Debit purchase and PIN Debit credit requests. Optional field for PIN Debit reversal requests.  #### GPX This field is optional for reversing an authorization or credit.  #### DCC for First Data Your local currency. For details, see the `currency` field description in [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf).  #### Tax Calculation Required for international tax and value added tax only. Optional for U.S. and Canadian taxes. Your local currency. 

        :param currency: The currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._currency = currency

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Total discount amount applied to the order. 

        :return: The discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Total discount amount applied to the order. 

        :param discount_amount: The discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._discount_amount = discount_amount

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Total tax amount for all the items in the order. 

        :return: The tax_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Total tax amount for all the items in the order. 

        :param tax_amount: The tax_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._tax_amount = tax_amount

    @property
    def duty_amount(self):
        """
        Gets the duty_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Total charges for any import or export duties included in the order. 

        :return: The duty_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._duty_amount

    @duty_amount.setter
    def duty_amount(self, duty_amount):
        """
        Sets the duty_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Total charges for any import or export duties included in the order. 

        :param duty_amount: The duty_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._duty_amount = duty_amount

    @property
    def exchange_rate(self):
        """
        Gets the exchange_rate of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Exchange rate returned by the DCC service. Includes a decimal point and a maximum of 4 decimal places.  For details, see `exchange_rate` request-level field description in the [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf) 

        :return: The exchange_rate of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """
        Sets the exchange_rate of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Exchange rate returned by the DCC service. Includes a decimal point and a maximum of 4 decimal places.  For details, see `exchange_rate` request-level field description in the [Dynamic Currency Conversion For First Data Using the SCMP API](http://apps.cybersource.com/library/documentation/dev_guides/DCC_FirstData_SCMP/DCC_FirstData_SCMP_API.pdf) 

        :param exchange_rate: The exchange_rate of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._exchange_rate = exchange_rate

    @property
    def exchange_rate_time_stamp(self):
        """
        Gets the exchange_rate_time_stamp of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Time stamp for the exchange rate. This value is returned by the DCC service.  Format: `YYYYMMDD~HH:MM`  where ~ denotes a space. 

        :return: The exchange_rate_time_stamp of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._exchange_rate_time_stamp

    @exchange_rate_time_stamp.setter
    def exchange_rate_time_stamp(self, exchange_rate_time_stamp):
        """
        Sets the exchange_rate_time_stamp of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        Time stamp for the exchange rate. This value is returned by the DCC service.  Format: `YYYYMMDD~HH:MM`  where ~ denotes a space. 

        :param exchange_rate_time_stamp: The exchange_rate_time_stamp of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._exchange_rate_time_stamp = exchange_rate_time_stamp

    @property
    def settlement_currency(self):
        """
        Gets the settlement_currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. This field is returned for OCT transactions. 

        :return: The settlement_currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """
        Sets the settlement_currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        This is a multicurrency-only field. It contains a 3-digit numeric code that identifies the currency used by the issuer to bill the cardholder's account. This field is returned for OCT transactions. 

        :param settlement_currency: The settlement_currency of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._settlement_currency = settlement_currency

    @property
    def giftwrap_amount(self):
        """
        Gets the giftwrap_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        giftwrap amount (RFU).

        :return: The giftwrap_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._giftwrap_amount

    @giftwrap_amount.setter
    def giftwrap_amount(self, giftwrap_amount):
        """
        Sets the giftwrap_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        giftwrap amount (RFU).

        :param giftwrap_amount: The giftwrap_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._giftwrap_amount = giftwrap_amount

    @property
    def handling_amount(self):
        """
        Gets the handling_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        handling amount (RFU)

        :return: The handling_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._handling_amount

    @handling_amount.setter
    def handling_amount(self, handling_amount):
        """
        Sets the handling_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        handling amount (RFU)

        :param handling_amount: The handling_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._handling_amount = handling_amount

    @property
    def shipping_amount(self):
        """
        Gets the shipping_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        shipping amount (RFU)

        :return: The shipping_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._shipping_amount

    @shipping_amount.setter
    def shipping_amount(self, shipping_amount):
        """
        Sets the shipping_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        shipping amount (RFU)

        :param shipping_amount: The shipping_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._shipping_amount = shipping_amount

    @property
    def shipping_discount_amount(self):
        """
        Gets the shipping_discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        shipping discount amount (RFU)

        :return: The shipping_discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._shipping_discount_amount

    @shipping_discount_amount.setter
    def shipping_discount_amount(self, shipping_discount_amount):
        """
        Sets the shipping_discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        shipping discount amount (RFU)

        :param shipping_discount_amount: The shipping_discount_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._shipping_discount_amount = shipping_discount_amount

    @property
    def insurance_amount(self):
        """
        Gets the insurance_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        insurance amount (RFU)

        :return: The insurance_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :rtype: str
        """
        return self._insurance_amount

    @insurance_amount.setter
    def insurance_amount(self, insurance_amount):
        """
        Sets the insurance_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        insurance amount (RFU)

        :param insurance_amount: The insurance_amount of this Ptsv2paymentreferencesOrderInformationAmountDetails.
        :type: str
        """



        self._insurance_amount = insurance_amount

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
        if not isinstance(other, Ptsv2paymentreferencesOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
