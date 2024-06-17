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


class Ptsv2paymentsPaymentInformationCard(object):
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
        'number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'type': 'str',
        'use_as': 'str',
        'source_account_type': 'str',
        'source_account_type_details': 'str',
        'security_code': 'str',
        'security_code_indicator': 'str',
        'account_encoder_id': 'str',
        'issue_number': 'str',
        'start_month': 'str',
        'start_year': 'str',
        'product_name': 'str',
        'type_selection_indicator': 'str'
    }

    attribute_map = {
        'number': 'number',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'type': 'type',
        'use_as': 'useAs',
        'source_account_type': 'sourceAccountType',
        'source_account_type_details': 'sourceAccountTypeDetails',
        'security_code': 'securityCode',
        'security_code_indicator': 'securityCodeIndicator',
        'account_encoder_id': 'accountEncoderId',
        'issue_number': 'issueNumber',
        'start_month': 'startMonth',
        'start_year': 'startYear',
        'product_name': 'productName',
        'type_selection_indicator': 'typeSelectionIndicator'
    }

    def __init__(self, number=None, expiration_month=None, expiration_year=None, type=None, use_as=None, source_account_type=None, source_account_type_details=None, security_code=None, security_code_indicator=None, account_encoder_id=None, issue_number=None, start_month=None, start_year=None, product_name=None, type_selection_indicator=None):
        """
        Ptsv2paymentsPaymentInformationCard - a model defined in Swagger
        """

        self._number = None
        self._expiration_month = None
        self._expiration_year = None
        self._type = None
        self._use_as = None
        self._source_account_type = None
        self._source_account_type_details = None
        self._security_code = None
        self._security_code_indicator = None
        self._account_encoder_id = None
        self._issue_number = None
        self._start_month = None
        self._start_year = None
        self._product_name = None
        self._type_selection_indicator = None

        if number is not None:
          self.number = number
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if type is not None:
          self.type = type
        if use_as is not None:
          self.use_as = use_as
        if source_account_type is not None:
          self.source_account_type = source_account_type
        if source_account_type_details is not None:
          self.source_account_type_details = source_account_type_details
        if security_code is not None:
          self.security_code = security_code
        if security_code_indicator is not None:
          self.security_code_indicator = security_code_indicator
        if account_encoder_id is not None:
          self.account_encoder_id = account_encoder_id
        if issue_number is not None:
          self.issue_number = issue_number
        if start_month is not None:
          self.start_month = start_month
        if start_year is not None:
          self.start_year = start_year
        if product_name is not None:
          self.product_name = product_name
        if type_selection_indicator is not None:
          self.type_selection_indicator = type_selection_indicator

    @property
    def number(self):
        """
        Gets the number of this Ptsv2paymentsPaymentInformationCard.
        The customer's payment card number, also known as the Primary Account Number (PAN). You can also use this field for encoded account numbers.  #### FDMS Nashville Required. String (19)  #### GPX Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :return: The number of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Ptsv2paymentsPaymentInformationCard.
        The customer's payment card number, also known as the Primary Account Number (PAN). You can also use this field for encoded account numbers.  #### FDMS Nashville Required. String (19)  #### GPX Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :param number: The number of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._number = number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this Ptsv2paymentsPaymentInformationCard.
        Two-digit month in which the payment card expires.  Format: `MM`.  Valid values: `01` through `12`. Leading 0 is required.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (_type_=039), if there is no expiration date on the card, use `12`.  #### FDMS Nashville Required field.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :return: The expiration_month of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this Ptsv2paymentsPaymentInformationCard.
        Two-digit month in which the payment card expires.  Format: `MM`.  Valid values: `01` through `12`. Leading 0 is required.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (_type_=039), if there is no expiration date on the card, use `12`.  #### FDMS Nashville Required field.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :param expiration_month: The expiration_month of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this Ptsv2paymentsPaymentInformationCard.
        Four-digit year in which the payment card expires.  Format: `YYYY`.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`1900` through `3000`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (**_type_**`=039`), if there is no expiration date on the card, use `2021`.  #### FDMS Nashville Required field.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. If you send in 2 digits, they must be the last 2 digits of the year.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :return: The expiration_year of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this Ptsv2paymentsPaymentInformationCard.
        Four-digit year in which the payment card expires.  Format: `YYYY`.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`1900` through `3000`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (**_type_**`=039`), if there is no expiration date on the card, use `2021`.  #### FDMS Nashville Required field.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. If you send in 2 digits, they must be the last 2 digits of the year.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :param expiration_year: The expiration_year of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._expiration_year = expiration_year

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsPaymentInformationCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. For card-present transactions on all processors except SIX, the Visa Electron card type is processed the same way that the Visa debit card is processed. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `031`: Delta[^1]: Use this value only for Ingenico ePayments. For other processors, use `001` for all Visa card types. - `033`: Visa Electron[^1]. Use this value only for Ingenico ePayments and SIX. For other processors, use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1,4] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay - '070': EFTPOS  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. [^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :return: The type of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsPaymentInformationCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. For card-present transactions on all processors except SIX, the Visa Electron card type is processed the same way that the Visa debit card is processed. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `031`: Delta[^1]: Use this value only for Ingenico ePayments. For other processors, use `001` for all Visa card types. - `033`: Visa Electron[^1]. Use this value only for Ingenico ePayments and SIX. For other processors, use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1,4] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay - '070': EFTPOS  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. [^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :param type: The type of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._type = type

    @property
    def use_as(self):
        """
        Gets the use_as of this Ptsv2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card.  This field is available only for China UnionPay, Cielo, Comercio Latino and Visa Platform Connect. The cardholder provides this information during the payment process.  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet.  **China UnionPayCard Transactions on China UnionPay:** Possible values:  - C: Domestic credit card  - D: Domestic debit card  - F: International credit card  - I: International debit card  When the value is D, the e-commerce indicator and CAVV fields must be included in the authorization request. When the value is C, F or I the card verification number, expiration month and expiration year fields must in included in the authorization request.  **Cielo and Comercio Latino Credit Card Transactions:** On these processors, this field is supported only for authorizations.  Possible values:  - CR: Credit card  - DB: Debit card       **Visa Platform Connect Credit Card Transactions:** This field is supported for all card types on Visa Platform Connect. For combo **card present** transactions with Mastercard on Brazilian-issued cards, possible values:  - CR: Credit card  - DB: Debit Card  For combo **card not present** transactions with Mastercard on Brazilian-issued cards, possible values:  - C: Credit card  - D: Debit card  A value of CR or DB in the useAs field takes precedence over any value in the Source Account Type field. 

        :return: The use_as of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._use_as

    @use_as.setter
    def use_as(self, use_as):
        """
        Sets the use_as of this Ptsv2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card.  This field is available only for China UnionPay, Cielo, Comercio Latino and Visa Platform Connect. The cardholder provides this information during the payment process.  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet.  **China UnionPayCard Transactions on China UnionPay:** Possible values:  - C: Domestic credit card  - D: Domestic debit card  - F: International credit card  - I: International debit card  When the value is D, the e-commerce indicator and CAVV fields must be included in the authorization request. When the value is C, F or I the card verification number, expiration month and expiration year fields must in included in the authorization request.  **Cielo and Comercio Latino Credit Card Transactions:** On these processors, this field is supported only for authorizations.  Possible values:  - CR: Credit card  - DB: Debit card       **Visa Platform Connect Credit Card Transactions:** This field is supported for all card types on Visa Platform Connect. For combo **card present** transactions with Mastercard on Brazilian-issued cards, possible values:  - CR: Credit card  - DB: Debit Card  For combo **card not present** transactions with Mastercard on Brazilian-issued cards, possible values:  - C: Credit card  - D: Debit card  A value of CR or DB in the useAs field takes precedence over any value in the Source Account Type field. 

        :param use_as: The use_as of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._use_as = use_as

    @property
    def source_account_type(self):
        """
        Gets the source_account_type of this Ptsv2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card.  The cardholder provides this information during the payment process.  This field is required in the following cases:   - Debit transactions on Cielo and Comercio Latino.   - Transactions with Brazilian-issued cards on CyberSource through VisaNet.   - Applicable only for CyberSource through VisaNet (CtV).  **Note** Combo cards in Brazil contain credit and debit functionality in a single card. Visa systems use a credit bank identification number (BIN) for this type of card. Using the BIN to determine whether a card is debit or credit can cause transactions with these cards to be processed incorrectly. CyberSource strongly recommends that you include this field for combo card transactions.  Possible values include the following.   - `CH`: Checking account  - `CR`: Credit card account  - `SA`: Saving account  - `LI`: Line of credit or credit portion of combo card  - `PP`: Prepaid card account or prepaid portion of combo card  - `UA`: Universal account  If useAs is set to credit/debit and there is a value in SourceAccountType, the value in the SourceAccountType field will take precedence. If useAs is set to CR/DB and there is a value in SourceAccountType, the value in the useAs field will take precedence. 

        :return: The source_account_type of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._source_account_type

    @source_account_type.setter
    def source_account_type(self, source_account_type):
        """
        Sets the source_account_type of this Ptsv2paymentsPaymentInformationCard.
        Flag that specifies the type of account associated with the card.  The cardholder provides this information during the payment process.  This field is required in the following cases:   - Debit transactions on Cielo and Comercio Latino.   - Transactions with Brazilian-issued cards on CyberSource through VisaNet.   - Applicable only for CyberSource through VisaNet (CtV).  **Note** Combo cards in Brazil contain credit and debit functionality in a single card. Visa systems use a credit bank identification number (BIN) for this type of card. Using the BIN to determine whether a card is debit or credit can cause transactions with these cards to be processed incorrectly. CyberSource strongly recommends that you include this field for combo card transactions.  Possible values include the following.   - `CH`: Checking account  - `CR`: Credit card account  - `SA`: Saving account  - `LI`: Line of credit or credit portion of combo card  - `PP`: Prepaid card account or prepaid portion of combo card  - `UA`: Universal account  If useAs is set to credit/debit and there is a value in SourceAccountType, the value in the SourceAccountType field will take precedence. If useAs is set to CR/DB and there is a value in SourceAccountType, the value in the useAs field will take precedence. 

        :param source_account_type: The source_account_type of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._source_account_type = source_account_type

    @property
    def source_account_type_details(self):
        """
        Gets the source_account_type_details of this Ptsv2paymentsPaymentInformationCard.
        Type of account that is being used when the value for the override_payment_method field is line of credit (LI) or prepaid card (PP). Possible values for line of credit: - `AGRC`: Visa Agro Custeio - `AGRE`: Visa Agro Electron - `AGRI`: Visa Agro Investimento - `AGRO`: Visa Agro Possible values for prepaid card: - `VVA`: Visa Vale Alimentacao - `VVF`: Visa Vale Flex - `VVR`: Visa Vale Refeicao This field is supported only for combo card transactions in Brazil on CyberSource through VisaNet. 

        :return: The source_account_type_details of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._source_account_type_details

    @source_account_type_details.setter
    def source_account_type_details(self, source_account_type_details):
        """
        Sets the source_account_type_details of this Ptsv2paymentsPaymentInformationCard.
        Type of account that is being used when the value for the override_payment_method field is line of credit (LI) or prepaid card (PP). Possible values for line of credit: - `AGRC`: Visa Agro Custeio - `AGRE`: Visa Agro Electron - `AGRI`: Visa Agro Investimento - `AGRO`: Visa Agro Possible values for prepaid card: - `VVA`: Visa Vale Alimentacao - `VVF`: Visa Vale Flex - `VVR`: Visa Vale Refeicao This field is supported only for combo card transactions in Brazil on CyberSource through VisaNet. 

        :param source_account_type_details: The source_account_type_details of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._source_account_type_details = source_account_type_details

    @property
    def security_code(self):
        """
        Gets the security_code of this Ptsv2paymentsPaymentInformationCard.
        Card Verification Number.  #### FDMS Nashville Required for American Express or if swiped; otherwise, optional.  #### Ingenico ePayments Do not include this field when `commerceIndicator=recurring`. **Note** Ingenico ePayments was previously called _Global Collect_.  #### TSYS Acquiring Solutions Optional if pointOfSaleInformation.entryMode=keyed; otherwise, not used.  #### GPX Optional.  #### All other processors: Optional. 

        :return: The security_code of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """
        Sets the security_code of this Ptsv2paymentsPaymentInformationCard.
        Card Verification Number.  #### FDMS Nashville Required for American Express or if swiped; otherwise, optional.  #### Ingenico ePayments Do not include this field when `commerceIndicator=recurring`. **Note** Ingenico ePayments was previously called _Global Collect_.  #### TSYS Acquiring Solutions Optional if pointOfSaleInformation.entryMode=keyed; otherwise, not used.  #### GPX Optional.  #### All other processors: Optional. 

        :param security_code: The security_code of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._security_code = security_code

    @property
    def security_code_indicator(self):
        """
        Gets the security_code_indicator of this Ptsv2paymentsPaymentInformationCard.
        Indicates whether a CVN code was sent. Possible values:   - `0` (default): CVN service not requested. This default value is used when you do not include      `securityCode` field in the request.  - `1` (default): CVN service requested and supported. This default value is used when you include      `securityCode` field in the request.  - `2`: CVN on credit card is illegible.  - `9`: CVN was not imprinted on credit card.  #### FDMS Nashville Required for American Express cards; otherwise, optional.  #### TSYS Acquiring Solutions Optional if `pointOfSaleInformation.entryMode=keyed`; otherwise, not used.  #### All other processors Optional. 

        :return: The security_code_indicator of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._security_code_indicator

    @security_code_indicator.setter
    def security_code_indicator(self, security_code_indicator):
        """
        Sets the security_code_indicator of this Ptsv2paymentsPaymentInformationCard.
        Indicates whether a CVN code was sent. Possible values:   - `0` (default): CVN service not requested. This default value is used when you do not include      `securityCode` field in the request.  - `1` (default): CVN service requested and supported. This default value is used when you include      `securityCode` field in the request.  - `2`: CVN on credit card is illegible.  - `9`: CVN was not imprinted on credit card.  #### FDMS Nashville Required for American Express cards; otherwise, optional.  #### TSYS Acquiring Solutions Optional if `pointOfSaleInformation.entryMode=keyed`; otherwise, not used.  #### All other processors Optional. 

        :param security_code_indicator: The security_code_indicator of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._security_code_indicator = security_code_indicator

    @property
    def account_encoder_id(self):
        """
        Gets the account_encoder_id of this Ptsv2paymentsPaymentInformationCard.
        Identifier for the issuing bank that provided the customer's encoded account number. Contact your processor for the bank's ID. 

        :return: The account_encoder_id of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._account_encoder_id

    @account_encoder_id.setter
    def account_encoder_id(self, account_encoder_id):
        """
        Sets the account_encoder_id of this Ptsv2paymentsPaymentInformationCard.
        Identifier for the issuing bank that provided the customer's encoded account number. Contact your processor for the bank's ID. 

        :param account_encoder_id: The account_encoder_id of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._account_encoder_id = account_encoder_id

    @property
    def issue_number(self):
        """
        Gets the issue_number of this Ptsv2paymentsPaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  **Note** The issue number is not required for Maestro (UK Domestic) transactions. 

        :return: The issue_number of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """
        Sets the issue_number of this Ptsv2paymentsPaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  **Note** The issue number is not required for Maestro (UK Domestic) transactions. 

        :param issue_number: The issue_number of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._issue_number = issue_number

    @property
    def start_month(self):
        """
        Gets the start_month of this Ptsv2paymentsPaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_month of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """
        Sets the start_month of this Ptsv2paymentsPaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_month: The start_month of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._start_month = start_month

    @property
    def start_year(self):
        """
        Gets the start_year of this Ptsv2paymentsPaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_year of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this Ptsv2paymentsPaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_year: The start_year of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._start_year = start_year

    @property
    def product_name(self):
        """
        Gets the product_name of this Ptsv2paymentsPaymentInformationCard.
        Name of the card product.  Possible value: - BNDES  This field is supported only for BNDES transactions on CyberSource through VisaNet.  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR4 - Position: 115-120 - Field: Brazil Country Data 

        :return: The product_name of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this Ptsv2paymentsPaymentInformationCard.
        Name of the card product.  Possible value: - BNDES  This field is supported only for BNDES transactions on CyberSource through VisaNet.  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR4 - Position: 115-120 - Field: Brazil Country Data 

        :param product_name: The product_name of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._product_name = product_name

    @property
    def type_selection_indicator(self):
        """
        Gets the type_selection_indicator of this Ptsv2paymentsPaymentInformationCard.
        Flag that identifies how the card type was selected.  Possible values: - 0: Card type was selected based on default acquirer settings. - 1: Customer selected the card type. 

        :return: The type_selection_indicator of this Ptsv2paymentsPaymentInformationCard.
        :rtype: str
        """
        return self._type_selection_indicator

    @type_selection_indicator.setter
    def type_selection_indicator(self, type_selection_indicator):
        """
        Sets the type_selection_indicator of this Ptsv2paymentsPaymentInformationCard.
        Flag that identifies how the card type was selected.  Possible values: - 0: Card type was selected based on default acquirer settings. - 1: Customer selected the card type. 

        :param type_selection_indicator: The type_selection_indicator of this Ptsv2paymentsPaymentInformationCard.
        :type: str
        """



        self._type_selection_indicator = type_selection_indicator

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
        if not isinstance(other, Ptsv2paymentsPaymentInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
