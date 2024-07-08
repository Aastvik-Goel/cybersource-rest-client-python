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


class ECheckConfigUnderwriting(object):
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
        'standard_entry_class_codes': 'str',
        'enable_hold': 'bool',
        'monthly_total_transaction_amount_limit': 'float',
        'holding_days': 'float',
        'enable_credits': 'bool',
        'transaction_amount_limit': 'float',
        'risk_reserve_method': 'str',
        'risk_reserve_rate': 'float',
        'risk_reserve_target_amount': 'float',
        'solution_organization_id': 'str'
    }

    attribute_map = {
        'standard_entry_class_codes': 'standardEntryClassCodes',
        'enable_hold': 'enableHold',
        'monthly_total_transaction_amount_limit': 'monthlyTotalTransactionAmountLimit',
        'holding_days': 'holdingDays',
        'enable_credits': 'enableCredits',
        'transaction_amount_limit': 'transactionAmountLimit',
        'risk_reserve_method': 'riskReserveMethod',
        'risk_reserve_rate': 'riskReserveRate',
        'risk_reserve_target_amount': 'riskReserveTargetAmount',
        'solution_organization_id': 'solutionOrganizationId'
    }

    def __init__(self, standard_entry_class_codes='CCD,PPD,TEL,WEB', enable_hold=True, monthly_total_transaction_amount_limit=None, holding_days=None, enable_credits=None, transaction_amount_limit=None, risk_reserve_method=None, risk_reserve_rate=None, risk_reserve_target_amount=None, solution_organization_id=None):
        """
        ECheckConfigUnderwriting - a model defined in Swagger
        """

        self._standard_entry_class_codes = None
        self._enable_hold = None
        self._monthly_total_transaction_amount_limit = None
        self._holding_days = None
        self._enable_credits = None
        self._transaction_amount_limit = None
        self._risk_reserve_method = None
        self._risk_reserve_rate = None
        self._risk_reserve_target_amount = None
        self._solution_organization_id = None

        self.standard_entry_class_codes = standard_entry_class_codes
        self.enable_hold = enable_hold
        self.monthly_total_transaction_amount_limit = monthly_total_transaction_amount_limit
        self.holding_days = holding_days
        if enable_credits is not None:
          self.enable_credits = enable_credits
        self.transaction_amount_limit = transaction_amount_limit
        self.risk_reserve_method = risk_reserve_method
        self.risk_reserve_rate = risk_reserve_rate
        self.risk_reserve_target_amount = risk_reserve_target_amount
        if solution_organization_id is not None:
          self.solution_organization_id = solution_organization_id

    @property
    def standard_entry_class_codes(self):
        """
        Gets the standard_entry_class_codes of this ECheckConfigUnderwriting.
        Mandatory  Free-text (csv)  Possible values (combination):  CCD — Cash Concentration or Disbursement, or CCD, is a charge or refund against a business checking account. One-time or recurring CCD transactions are fund transfers to or from a corporate entity. A standing authorization is required for recurring transactions. PPD — Prearranged Payment and Deposit Entry, or PPD, is a charge or refund against a customer's checking or savings account. PPD entries can only be originated when payment and deposit terms between the merchant and the customer are prearranged. A written authorization from the customer is required for one-time transactions and a written standing authorization is required for recurring transactions. TEL — Telephone-Initiated Entry, or TEL, is a one-time charge against a customer's checking or savings account. TEL transactions can only be originated when a business relationship between the merchant and the customer already exists; or if a relationship does not exist, then only when the customer initiates the telephone call to the merchant. Payment authorization is obtained from the customer by telephone. WEB — Internet-Initiated Entry or WEB is a charge against a customer's checking or savings account. One-time or recurring WEB transactions are originated through the Internet. Payment authorization is also obtained from the customer through the Internet. 

        :return: The standard_entry_class_codes of this ECheckConfigUnderwriting.
        :rtype: str
        """
        return self._standard_entry_class_codes

    @standard_entry_class_codes.setter
    def standard_entry_class_codes(self, standard_entry_class_codes):
        """
        Sets the standard_entry_class_codes of this ECheckConfigUnderwriting.
        Mandatory  Free-text (csv)  Possible values (combination):  CCD — Cash Concentration or Disbursement, or CCD, is a charge or refund against a business checking account. One-time or recurring CCD transactions are fund transfers to or from a corporate entity. A standing authorization is required for recurring transactions. PPD — Prearranged Payment and Deposit Entry, or PPD, is a charge or refund against a customer's checking or savings account. PPD entries can only be originated when payment and deposit terms between the merchant and the customer are prearranged. A written authorization from the customer is required for one-time transactions and a written standing authorization is required for recurring transactions. TEL — Telephone-Initiated Entry, or TEL, is a one-time charge against a customer's checking or savings account. TEL transactions can only be originated when a business relationship between the merchant and the customer already exists; or if a relationship does not exist, then only when the customer initiates the telephone call to the merchant. Payment authorization is obtained from the customer by telephone. WEB — Internet-Initiated Entry or WEB is a charge against a customer's checking or savings account. One-time or recurring WEB transactions are originated through the Internet. Payment authorization is also obtained from the customer through the Internet. 

        :param standard_entry_class_codes: The standard_entry_class_codes of this ECheckConfigUnderwriting.
        :type: str
        """

        self._standard_entry_class_codes = standard_entry_class_codes

    @property
    def enable_hold(self):
        """
        Gets the enable_hold of this ECheckConfigUnderwriting.
        Mandatory  Determines whether CYBS has placed the merchant on a funding hold This will often be set to True for new merchants until the risk team has completed additional verification of their first transaction. It will be switched to \"false\" once underwriting review is completed and we are ready to start funding the merchant. 

        :return: The enable_hold of this ECheckConfigUnderwriting.
        :rtype: bool
        """
        return self._enable_hold

    @enable_hold.setter
    def enable_hold(self, enable_hold):
        """
        Sets the enable_hold of this ECheckConfigUnderwriting.
        Mandatory  Determines whether CYBS has placed the merchant on a funding hold This will often be set to True for new merchants until the risk team has completed additional verification of their first transaction. It will be switched to \"false\" once underwriting review is completed and we are ready to start funding the merchant. 

        :param enable_hold: The enable_hold of this ECheckConfigUnderwriting.
        :type: bool
        """

        self._enable_hold = enable_hold

    @property
    def monthly_total_transaction_amount_limit(self):
        """
        Gets the monthly_total_transaction_amount_limit of this ECheckConfigUnderwriting.
        Mandatory  Monthly Maximum total Transaction Amount 12 digit including decimal 

        :return: The monthly_total_transaction_amount_limit of this ECheckConfigUnderwriting.
        :rtype: float
        """
        return self._monthly_total_transaction_amount_limit

    @monthly_total_transaction_amount_limit.setter
    def monthly_total_transaction_amount_limit(self, monthly_total_transaction_amount_limit):
        """
        Sets the monthly_total_transaction_amount_limit of this ECheckConfigUnderwriting.
        Mandatory  Monthly Maximum total Transaction Amount 12 digit including decimal 

        :param monthly_total_transaction_amount_limit: The monthly_total_transaction_amount_limit of this ECheckConfigUnderwriting.
        :type: float
        """

        self._monthly_total_transaction_amount_limit = monthly_total_transaction_amount_limit

    @property
    def holding_days(self):
        """
        Gets the holding_days of this ECheckConfigUnderwriting.
        Mandatory  Funds Hold Days (Number of days funds will be held before it will be deposited into merchant account) 3 digits 

        :return: The holding_days of this ECheckConfigUnderwriting.
        :rtype: float
        """
        return self._holding_days

    @holding_days.setter
    def holding_days(self, holding_days):
        """
        Sets the holding_days of this ECheckConfigUnderwriting.
        Mandatory  Funds Hold Days (Number of days funds will be held before it will be deposited into merchant account) 3 digits 

        :param holding_days: The holding_days of this ECheckConfigUnderwriting.
        :type: float
        """

        self._holding_days = holding_days

    @property
    def enable_credits(self):
        """
        Gets the enable_credits of this ECheckConfigUnderwriting.
        Optional  Allow Credits (True/False) 

        :return: The enable_credits of this ECheckConfigUnderwriting.
        :rtype: bool
        """
        return self._enable_credits

    @enable_credits.setter
    def enable_credits(self, enable_credits):
        """
        Sets the enable_credits of this ECheckConfigUnderwriting.
        Optional  Allow Credits (True/False) 

        :param enable_credits: The enable_credits of this ECheckConfigUnderwriting.
        :type: bool
        """

        self._enable_credits = enable_credits

    @property
    def transaction_amount_limit(self):
        """
        Gets the transaction_amount_limit of this ECheckConfigUnderwriting.
        Mandatory  Maximum total Transaction Amount This is a per transaction limit. For example, the merchant is limited to processing transactions under $100 12 digits (including decimal - USD only) 

        :return: The transaction_amount_limit of this ECheckConfigUnderwriting.
        :rtype: float
        """
        return self._transaction_amount_limit

    @transaction_amount_limit.setter
    def transaction_amount_limit(self, transaction_amount_limit):
        """
        Sets the transaction_amount_limit of this ECheckConfigUnderwriting.
        Mandatory  Maximum total Transaction Amount This is a per transaction limit. For example, the merchant is limited to processing transactions under $100 12 digits (including decimal - USD only) 

        :param transaction_amount_limit: The transaction_amount_limit of this ECheckConfigUnderwriting.
        :type: float
        """

        self._transaction_amount_limit = transaction_amount_limit

    @property
    def risk_reserve_method(self):
        """
        Gets the risk_reserve_method of this ECheckConfigUnderwriting.
        Mandatory Reserve Method  Possible value: - fixed - none Most merchants do not have a reserve attached to their account so the default value would be \"none.\"   For a Fixed Reserve, the reserve balance is established by either, (1) a receipt of a lump sum deposit from a merchant, or (2) withholding funds at a Reserve Rate established for the account from each batch settlement until the reserve balance is equal to a set Reserve Target. A Fixed Reserve may also be established by a combination of lump sum deposit and withholding of settlement funds.  A Rolling Reserve balance is established by withholding from a merchant's available settlement funds at a Reserve Rate (percentage) and no Reserve Target is specified. Rather, each amount withheld is retained for a specified number of Reserve Holding Days and then released back to the merchant. 

        :return: The risk_reserve_method of this ECheckConfigUnderwriting.
        :rtype: str
        """
        return self._risk_reserve_method

    @risk_reserve_method.setter
    def risk_reserve_method(self, risk_reserve_method):
        """
        Sets the risk_reserve_method of this ECheckConfigUnderwriting.
        Mandatory Reserve Method  Possible value: - fixed - none Most merchants do not have a reserve attached to their account so the default value would be \"none.\"   For a Fixed Reserve, the reserve balance is established by either, (1) a receipt of a lump sum deposit from a merchant, or (2) withholding funds at a Reserve Rate established for the account from each batch settlement until the reserve balance is equal to a set Reserve Target. A Fixed Reserve may also be established by a combination of lump sum deposit and withholding of settlement funds.  A Rolling Reserve balance is established by withholding from a merchant's available settlement funds at a Reserve Rate (percentage) and no Reserve Target is specified. Rather, each amount withheld is retained for a specified number of Reserve Holding Days and then released back to the merchant. 

        :param risk_reserve_method: The risk_reserve_method of this ECheckConfigUnderwriting.
        :type: str
        """

        self._risk_reserve_method = risk_reserve_method

    @property
    def risk_reserve_rate(self):
        """
        Gets the risk_reserve_rate of this ECheckConfigUnderwriting.
        Mandatory  Reserve Rate (% of TPV)=> Relevant for Rolling Reserve and Fixed Reserve The percentage rate at which risk funds are withheld from each eCheck.Net batch settlement. 

        :return: The risk_reserve_rate of this ECheckConfigUnderwriting.
        :rtype: float
        """
        return self._risk_reserve_rate

    @risk_reserve_rate.setter
    def risk_reserve_rate(self, risk_reserve_rate):
        """
        Sets the risk_reserve_rate of this ECheckConfigUnderwriting.
        Mandatory  Reserve Rate (% of TPV)=> Relevant for Rolling Reserve and Fixed Reserve The percentage rate at which risk funds are withheld from each eCheck.Net batch settlement. 

        :param risk_reserve_rate: The risk_reserve_rate of this ECheckConfigUnderwriting.
        :type: float
        """

        self._risk_reserve_rate = risk_reserve_rate

    @property
    def risk_reserve_target_amount(self):
        """
        Gets the risk_reserve_target_amount of this ECheckConfigUnderwriting.
        Mandatory  Reserve Target (fixed $ amount)=> Relevant for Fixed Reserve ONLY  The maximum dollar amount that can be held in Risk Reserve for a fixed reserve. Once risk withholdings reach the Reserve Target established for the eCheck.Net account, a portion of available funds will be deposited to the merchant's bank account 12 digit including decimal 

        :return: The risk_reserve_target_amount of this ECheckConfigUnderwriting.
        :rtype: float
        """
        return self._risk_reserve_target_amount

    @risk_reserve_target_amount.setter
    def risk_reserve_target_amount(self, risk_reserve_target_amount):
        """
        Sets the risk_reserve_target_amount of this ECheckConfigUnderwriting.
        Mandatory  Reserve Target (fixed $ amount)=> Relevant for Fixed Reserve ONLY  The maximum dollar amount that can be held in Risk Reserve for a fixed reserve. Once risk withholdings reach the Reserve Target established for the eCheck.Net account, a portion of available funds will be deposited to the merchant's bank account 12 digit including decimal 

        :param risk_reserve_target_amount: The risk_reserve_target_amount of this ECheckConfigUnderwriting.
        :type: float
        """

        self._risk_reserve_target_amount = risk_reserve_target_amount

    @property
    def solution_organization_id(self):
        """
        Gets the solution_organization_id of this ECheckConfigUnderwriting.
        Solution organization id

        :return: The solution_organization_id of this ECheckConfigUnderwriting.
        :rtype: str
        """
        return self._solution_organization_id

    @solution_organization_id.setter
    def solution_organization_id(self, solution_organization_id):
        """
        Sets the solution_organization_id of this ECheckConfigUnderwriting.
        Solution organization id

        :param solution_organization_id: The solution_organization_id of this ECheckConfigUnderwriting.
        :type: str
        """

        self._solution_organization_id = solution_organization_id

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
        if not isinstance(other, ECheckConfigUnderwriting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
