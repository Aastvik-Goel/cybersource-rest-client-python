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


class Ptsv2paymentsidrefundsClientReferenceInformation(object):
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
        'code': 'str',
        'reconciliation_id': 'str',
        'return_reconciliation_id': 'str',
        'paused_request_id': 'str',
        'transaction_id': 'str',
        'comments': 'str',
        'partner': 'Ptsv2paymentsClientReferenceInformationPartner',
        'application_name': 'str',
        'application_version': 'str',
        'application_user': 'str'
    }

    attribute_map = {
        'code': 'code',
        'reconciliation_id': 'reconciliationId',
        'return_reconciliation_id': 'returnReconciliationId',
        'paused_request_id': 'pausedRequestId',
        'transaction_id': 'transactionId',
        'comments': 'comments',
        'partner': 'partner',
        'application_name': 'applicationName',
        'application_version': 'applicationVersion',
        'application_user': 'applicationUser'
    }

    def __init__(self, code=None, reconciliation_id=None, return_reconciliation_id=None, paused_request_id=None, transaction_id=None, comments=None, partner=None, application_name=None, application_version=None, application_user=None):
        """
        Ptsv2paymentsidrefundsClientReferenceInformation - a model defined in Swagger
        """

        self._code = None
        self._reconciliation_id = None
        self._return_reconciliation_id = None
        self._paused_request_id = None
        self._transaction_id = None
        self._comments = None
        self._partner = None
        self._application_name = None
        self._application_version = None
        self._application_user = None

        if code is not None:
          self.code = code
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if return_reconciliation_id is not None:
          self.return_reconciliation_id = return_reconciliation_id
        if paused_request_id is not None:
          self.paused_request_id = paused_request_id
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if comments is not None:
          self.comments = comments
        if partner is not None:
          self.partner = partner
        if application_name is not None:
          self.application_name = application_name
        if application_version is not None:
          self.application_version = application_version
        if application_user is not None:
          self.application_user = application_user

    @property
    def code(self):
        """
        Gets the code of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  #### Used by **Authorization** Required field.  #### PIN Debit Requests for PIN debit reversals need to use the same merchant reference number that was used in the transaction that is being reversed.  Required field for all PIN Debit requests (purchase, credit, and reversal).  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports. 

        :return: The code of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Merchant-generated order reference or tracking number. It is recommended that you send a unique value for each transaction so that you can perform meaningful searches for the transaction.  #### Used by **Authorization** Required field.  #### PIN Debit Requests for PIN debit reversals need to use the same merchant reference number that was used in the transaction that is being reversed.  Required field for all PIN Debit requests (purchase, credit, and reversal).  #### FDC Nashville Global Certain circumstances can cause the processor to truncate this value to 15 or 17 characters for Level II and Level III processing, which can cause a discrepancy between the value you submit and the value included in some processor reports. 

        :param code: The code of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._code = code

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :return: The reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :param reconciliation_id: The reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def return_reconciliation_id(self):
        """
        Gets the return_reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        A new ID which is created for refund

        :return: The return_reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._return_reconciliation_id

    @return_reconciliation_id.setter
    def return_reconciliation_id(self, return_reconciliation_id):
        """
        Sets the return_reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        A new ID which is created for refund

        :param return_reconciliation_id: The return_reconciliation_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._return_reconciliation_id = return_reconciliation_id

    @property
    def paused_request_id(self):
        """
        Gets the paused_request_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Used to resume a transaction that was paused for an order modification rule to allow for payer authentication to complete. To resume and continue with the authorization/decision service flow, call the services and include the request id from the prior decision call. 

        :return: The paused_request_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._paused_request_id

    @paused_request_id.setter
    def paused_request_id(self, paused_request_id):
        """
        Sets the paused_request_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Used to resume a transaction that was paused for an order modification rule to allow for payer authentication to complete. To resume and continue with the authorization/decision service flow, call the services and include the request id from the prior decision call. 

        :param paused_request_id: The paused_request_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._paused_request_id = paused_request_id

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Identifier that you assign to the transaction. Normally generated by a client server to identify a unique API request.  **Note** Use this field only if you want to support merchant-initiated reversal and void operations.  #### Used by **Authorization, Authorization Reversal, Capture, Credit, and Void** Optional field.  #### PIN Debit For a PIN debit reversal, your request must include a request ID or a merchant transaction identifier. Optional field for PIN debit purchase or credit requests. 

        :return: The transaction_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Identifier that you assign to the transaction. Normally generated by a client server to identify a unique API request.  **Note** Use this field only if you want to support merchant-initiated reversal and void operations.  #### Used by **Authorization, Authorization Reversal, Capture, Credit, and Void** Optional field.  #### PIN Debit For a PIN debit reversal, your request must include a request ID or a merchant transaction identifier. Optional field for PIN debit purchase or credit requests. 

        :param transaction_id: The transaction_id of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def comments(self):
        """
        Gets the comments of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Comments

        :return: The comments of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Comments

        :param comments: The comments of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._comments = comments

    @property
    def partner(self):
        """
        Gets the partner of this Ptsv2paymentsidrefundsClientReferenceInformation.

        :return: The partner of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: Ptsv2paymentsClientReferenceInformationPartner
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """
        Sets the partner of this Ptsv2paymentsidrefundsClientReferenceInformation.

        :param partner: The partner of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: Ptsv2paymentsClientReferenceInformationPartner
        """

        self._partner = partner

    @property
    def application_name(self):
        """
        Gets the application_name of this Ptsv2paymentsidrefundsClientReferenceInformation.
        The name of the Connection Method client (such as Virtual Terminal or SOAP Toolkit API) that the merchant uses to send a transaction request to CyberSource. 

        :return: The application_name of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this Ptsv2paymentsidrefundsClientReferenceInformation.
        The name of the Connection Method client (such as Virtual Terminal or SOAP Toolkit API) that the merchant uses to send a transaction request to CyberSource. 

        :param application_name: The application_name of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._application_name = application_name

    @property
    def application_version(self):
        """
        Gets the application_version of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Version of the CyberSource application or integration used for a transaction. 

        :return: The application_version of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this Ptsv2paymentsidrefundsClientReferenceInformation.
        Version of the CyberSource application or integration used for a transaction. 

        :param application_version: The application_version of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._application_version = application_version

    @property
    def application_user(self):
        """
        Gets the application_user of this Ptsv2paymentsidrefundsClientReferenceInformation.
        The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method. 

        :return: The application_user of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :rtype: str
        """
        return self._application_user

    @application_user.setter
    def application_user(self, application_user):
        """
        Sets the application_user of this Ptsv2paymentsidrefundsClientReferenceInformation.
        The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method. 

        :param application_user: The application_user of this Ptsv2paymentsidrefundsClientReferenceInformation.
        :type: str
        """

        self._application_user = application_user

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
        if not isinstance(other, Ptsv2paymentsidrefundsClientReferenceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other